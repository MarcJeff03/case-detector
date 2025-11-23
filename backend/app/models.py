"""
Definition of models.
"""

from django.db import models
import app.utils.pdf_extract as BERT
from app.constants import app_constants
from app.ra_keywords import RA_KEYWORDS, STOP_WORDS
import json
from django.core.files import File
import os
import re

class Config(models.Model):

    year = models.IntegerField()
    day = models.IntegerField()
    month = models.IntegerField()




class Person(models.Model):

    first_name = models.CharField(max_length=255, null = False)
    middle_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = False)
    contact_number = models.CharField(max_length=255, null = True)
    address = models.TextField(null = False)
    

class Credibility(models.Model):

    serial_number = models.CharField(max_length=50, null=True, blank=True, default=None)
    title = models.TextField(null=False, default="No Title")
    description = models.TextField(null=True, default="No Description / (N/A)")
    file_location = models.FileField(upload_to="reviewed_papers", null = True)
    plagiarism_level = models.FloatField(default=0.00)
    is_plagirized = models.BooleanField(default = False)
    is_pdf = models.BooleanField(default = True)
    remarks = models.TextField(default=None)
    non_pdf_text = models.TextField(default = None, null = True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null = True, default = None)
    complaint_id = models.IntegerField(null = True, default = None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )  # Execute inherited default.

        self.analyze_saved_file()

    def analyze_saved_file(self):
        try:
            saved_text = self.get_saved_contents()
            self.get_paper_contents(saved_text)
        except Exception as e:
            print(e)
        self_instance = Credibility.objects.get(id=int(self.pk))
        
        # Only assign person if complaint_id is valid
        if self_instance.complaint_id:
            try:
                self_instance.person = Person.objects.get(id=self_instance.complaint_id)
            except Person.DoesNotExist:
                print(f"Warning: Person with id {self_instance.complaint_id} does not exist")
                self_instance.person = None

        if self_instance.is_pdf:
            pdf_path = self_instance.file_location.path
            text = BERT.extract_text_from_pdf(pdf_path)

            # Only update person if we have a valid complaint_id
            update_data = {}
            if self_instance.complaint_id:
                try:
                    update_data['person'] = Person.objects.get(id=self_instance.complaint_id)
                except Person.DoesNotExist:
                    print(f"Warning: Person with id {self_instance.complaint_id} does not exist")
            
            if update_data:
                Credibility.objects.filter(pk=self_instance.pk).update(**update_data)

        else:
            # generate pdf and immediately open it when saving
            final_path = BERT.create_pdf_from_text(self_instance.non_pdf_text)
            print(self_instance.person)
            with open(final_path, "rb") as f:
                filename = os.path.basename(final_path)

                # store the file manually
                self_instance.file_location.save(filename, File(f), save=False)
                
                # persist using update(), avoids triggering save() again
                Credibility.objects.filter(pk=self_instance.pk).update(
                    file_location=self_instance.file_location.name,
                    person = Person.objects.get(id=self_instance.complaint_id)
                )
                
            text = BERT.extract_text_from_pdf(final_path)

        return text
  
        
    def get_paper_contents(self, text_contents: str) -> None:
        """Do a select query and join all so no CPU intensive will be done."""

        # Use imported RA_KEYWORDS from ra_keywords.py

        bert_instance = BERT.BERTAlgorithm()
        messages = []
        research_papers = Research.objects.all()
        
        total_mean = 0
        papers = 0
        
        # Convert complaint text to lowercase for keyword matching
        text_lower = text_contents.lower()
        
        if len(research_papers) > 0:

            for each_papers in research_papers:

                paper_contents = self.join_paper_contents(each_papers.pk)
                
                # Skip if no paper contents (not analyzed yet)
                if not paper_contents:
                    print(f"Skipping {each_papers.title} - no datasets found")
                    continue
                
                # Check for keyword matches
                keyword_boost = 0
                matched_keywords = []
                has_keyword_match = False
                
                for ra_num, keywords in RA_KEYWORDS.items():
                    if ra_num in each_papers.title.upper():
                        # Count how many keywords match, ignoring stop words
                        for keyword in keywords:
                            if keyword in text_lower and keyword not in STOP_WORDS:
                                matched_keywords.append(keyword)
                        
                        if matched_keywords:
                            has_keyword_match = True
                            # Boost score based on keyword matches (max 0.3 boost)
                            keyword_boost = min(len(matched_keywords) * 0.05, 0.3)
                            print(f"  → Keyword boost for {each_papers.title}: +{keyword_boost:.2f} (matched: {matched_keywords[:5]})")
                        else:
                            print(f"  ✗ No keywords matched for {each_papers.title}")
                        break
                
                # Skip if no keyword match found - ONLY show PDFs with relevant keywords
                if not has_keyword_match:
                    print(f"Skipping {each_papers.title} - no relevant keywords found in complaint")
                    continue
                    
                calculated_cosine = bert_instance.calculate_cosine(text_contents, paper_contents)
                
                # Apply keyword boost
                final_score = min(calculated_cosine + keyword_boost, 1.0)
                
                print(f"Comparing with {each_papers.title}: BERT={calculated_cosine:.4f}, Keywords=+{keyword_boost:.2f}, Final={final_score:.4f}")
         
                # Now check if final score meets threshold
                if final_score >= app_constants.ACCEPTABLE_PLAGIARISM_SENTENCES:
                   
                    messages.append({
                        "title": each_papers.title,
                        "location": str(each_papers.file_location),
                        "probability": round(final_score * 100, 2),  # Convert to percentage
                        "confidence": final_score,
                        "keywords_matched": len(matched_keywords)
                    })

                    total_mean = total_mean + final_score # ONLY INCLUDE CALCULATION IF MATCHED
                    papers = papers + 1 # Increment paper FOR RELATED ELSE SKIP
                    print(f"✓ MATCH FOUND: {each_papers.title} (final score: {final_score:.4f})")
                else:
                    print(f"  ✗ Score too low for {each_papers.title} ({final_score:.4f} < {app_constants.ACCEPTABLE_PLAGIARISM_SENTENCES})")

            # Sort messages by probability (highest first)
            messages.sort(key=lambda x: x['confidence'], reverse=True)
            
            # Calculate average AFTER all papers
            if papers > 0:
                total_mean = total_mean / papers
                total_mean = round(total_mean, 2)
                print(f"Average similarity across {papers} matching papers: {total_mean}")
                
                # Show ranked matches
                print("\n📊 RANKED MATCHES (by probability):")
                for idx, msg in enumerate(messages, 1):
                    print(f"  {idx}. {msg['title']}: {msg['probability']}% confidence")
            else:
                total_mean = 0
                print("No matches found above threshold")

        plagiarized = False

        if total_mean >= app_constants.ACCEPTABLE_PLAGIARISM_LEVEL:
            plagiarized = True

        print(f"Final result - Plagiarism level: {total_mean}, Is plagiarized: {plagiarized}")
        print(f"Matched papers: {len(messages)}")
        
        Credibility.objects.all().filter(id = self.pk).update(
            plagiarism_level = total_mean, is_plagirized = plagiarized,
            remarks = json.dumps(messages)
        )

        print("Plagiarism level was updated.")
                

    def join_paper_contents(self, id: int) -> str:
        """
        Join all paper contents by research paper.
        args:
            id : primary key of research paper.

        returns:
            "" : if not found
        """

        placeholder = ""
        each_sentences = Datasets.objects.all().filter(title_id=int(id))

        if isinstance(id, int) == False or len(each_sentences) < 1:
            return ""

        if len(each_sentences) > 0:

            for sentence in each_sentences:
                placeholder = placeholder + sentence.phrase + " "
            else:
                placeholder = placeholder[0 : len(placeholder) - 1]

            return placeholder

    def get_saved_contents(self):
        """
        Returns the saved text contents for this Credibility instance.
        If PDF, tries to extract text from the file; otherwise, returns non_pdf_text.
        """
        if self.is_pdf and self.file_location:
            try:
                # Try to extract text from the PDF file
                return BERT.extract_text_from_pdf(self.file_location.path)
            except Exception as e:
                print(f"Error extracting text from PDF: {e}")
                return ""
        else:
            # If not a PDF, return the non_pdf_text field if it exists
            return self.non_pdf_text or ""

class Research(models.Model):

    title = models.TextField(null=False, default="No Title")
    description = models.TextField(null=True, default="No Description / (N/A)")
    file_location = models.FileField(upload_to="papers")
    reviewed = models.BooleanField(default=False)


class Datasets(models.Model):

    title_id = models.ForeignKey(Research, on_delete=models.CASCADE)
    phrase = models.TextField(null=True)
    similar_sample = models.TextField(null=True)
    plagiarized = models.BooleanField(default=False)
