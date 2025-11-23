# This file marks the utils directory as a Python package.
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
from nltk.tokenize import sent_tokenize
import re
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random
from torch.utils.data import Dataset  # Only keep Dataset for class inheritance

from io import BytesIO
from django.core.files.base import ContentFile
from fpdf import FPDF
from django.core.files.base import ContentFile
from io import BytesIO
from datetime import datetime

# Initialize NLTK components
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

from PyPDF2 import PdfReader
# Configure Tesseract path for Windows

# from transformers import pipeline

# pipeline("automatic-speech-recognition", model="openai/whisper-small")
# print(pipeline, "RUNNING PIPELINE")

lemmatizer = WordNetLemmatizer()

def create_pdf_from_text(text, filename="generated.pdf"):
	"""
	Create a PDF from text and return a ContentFile suitable for FileField,
	without saving the file temporarily to the disk.
	"""
	pdf = FPDF()

	# Add a page
	pdf.add_page()

	# Set the border color to white (RGB: 255, 255, 255) to make it "transparent"
	pdf.set_draw_color(255, 255, 255)

	# Set font: Arial, regular, 12pt
	pdf.set_font("Arial", "", 12)

	# The multi_cell method will automatically handle new pages
	pdf.multi_cell(w=0, h=10, txt=text, border=1, align='L')

	# Auto-generate filename with current timestamp
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"generated_{timestamp}.pdf"
	final_file_name = "media/reviewed_papers/" + filename
	pdf.output(final_file_name)

	# Get PDF content as bytes and return a ContentFile
	# 'dest="S"' returns the document as a string.
	# pdf_bytes = pdf.output(dest="S").encode('latin-1')

	# ContentFile takes the bytes and a filename to create a file-like object
	return final_file_name

def extract_text_from_pdf(pdf_path):
	"""Extract texts from PDF with OCR support for image-based PDFs."""
	try:
		# First, try traditional text extraction
		reader = PdfReader(pdf_path)
		text = ""
		for page in reader.pages:
			page_text = page.extract_text()
			if page_text:
				text += page_text
        
		# If we got substantial text, return it
		if len(text.strip()) > 100:
			print(f"Extracted {len(text)} characters using standard PDF text extraction")
			return text
        
		# If text extraction failed or returned minimal text, use OCR
		print("Standard text extraction failed. Using OCR for image-based PDF...")
		text = extract_text_with_ocr(pdf_path)
		print(f"Extracted {len(text)} characters using OCR")
		return text
        
	except Exception as e:
		print(f"Error extracting text from PDF: {e}")
		# Fallback to OCR if standard extraction fails
		try:
			print("Falling back to OCR...")
			text = extract_text_with_ocr(pdf_path)
			return text
		except Exception as ocr_error:
			print(f"OCR also failed: {ocr_error}")
			return ""

def extract_text_with_ocr(pdf_path):
	"""Extract text from image-based PDF using OCR (Tesseract)."""
	try:
		# Convert PDF to images with Poppler path specified
		print("Converting PDF pages to images...")
		poppler_path = r'C:\Program Files\poppler\Library\bin'
		images = convert_from_path(pdf_path, dpi=300, fmt='jpeg', poppler_path=poppler_path)
        
		text = ""
		total_pages = len(images)
        
		# Process each page
		for i, image in enumerate(images, 1):
			print(f"Processing page {i}/{total_pages} with OCR...")
            
			# Use Tesseract to extract text from image
			page_text = pytesseract.image_to_string(image, lang='eng')
			text += page_text + "\n"
        
		print(f"OCR completed. Extracted {len(text)} characters from {total_pages} pages")
		return text
        
	except Exception as e:
		print(f"OCR extraction error: {e}")
		raise e

def extract_valid_phrases(text):
    from transformers import pipeline
    sentences = sent_tokenize(text)
    classifier = pipeline(
        "text-classification", model="bert-base-uncased", return_all_scores=True
    )
    valid_phrases = []
    for sentence in sentences:
        if re.match(r"^[A-Za-z][^\.:]*[\.:]$", sentence):
            scores = classifier(sentence)
            sentence_is_valid = scores[0][1]["score"] > 0.1
            if sentence_is_valid == True:
                if (
                    len(re.findall(r"\w+", sentence)) > 2
                ):
                    if sentence not in valid_phrases:
                        valid_phrases.append(sentence)
    return valid_phrases

def preprocess(text):
	tokens = word_tokenize(text)
	tokens = [
		lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalnum()
	]
	return tokens

def generate_paraphrases(text):
	tokens = preprocess(text)
	stop_words = set(stopwords.words("english"))
	paraphrases = []

	for i, token in enumerate(tokens):
		if token.lower() in stop_words or not token.isalpha():
			continue

		synonyms = set()
		for syn in wordnet.synsets(token):
			for lemma in syn.lemmas():
				synonym = lemma.name().replace("_", " ")
				if synonym.lower() != token.lower():
					synonyms.add(synonym)

		for synonym in synonyms:
			new_tokens = tokens.copy()
			new_tokens[i] = synonym
			paraphrases.append(" ".join(new_tokens))
	return paraphrases

def score_paraphrases(original_text, paraphrases):
	pass

def paraphrase(text):
	paraphrases = generate_paraphrases(text)
	return paraphrases

def get_texts_and_synonyms(valid_phrases):
	"""Returns an interable dictionary that can be used to compare words."""
	__objects = []
	for phrase in valid_phrases:
		old_sentence = phrase.replace("\n", " ")
		options = paraphrase(old_sentence)
		new = ""
		if len(options) > 0:

			print(options[0])
			new = options[0]
			generated_index = random.randint(0, len(options) - 1)
			new = options[generated_index]

			__objects.append({"original_sentence": old_sentence, "new_sentence": new})

	return __objects

class TextPairDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_length):
        self.data = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        import torch
        text1 = str(self.data.iloc[idx, 0])
        text2 = str(self.data.iloc[idx, 1])
        label = self.data.iloc[idx, 2]
        inputs = self.tokenizer(
            text1,
            text2,
            truncation=True,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt",
        )
        inputs = {key: val.squeeze(0) for key, val in inputs.items()}
        inputs["labels"] = torch.tensor(label, dtype=torch.long)
        return inputs

class BERTAlgorithm:
    def __init__(self):
        from transformers import BertTokenizer, BertModel
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def calculate_cosine(self, text_1, text_2):
        import torch
        from sklearn.metrics.pairwise import cosine_similarity
        print("CALCULATING COSINE")
        inputs1 = self.tokenizer(text_1, return_tensors='pt', padding=True, truncation=True)
        inputs2 = self.tokenizer(text_2, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs1 = self.model(**inputs1)
            outputs2 = self.model(**inputs2)
        embeddings1 = outputs1.last_hidden_state.mean(dim=1)
        embeddings2 = outputs2.last_hidden_state.mean(dim=1)
        similarity_score = cosine_similarity(embeddings1, embeddings2)[0][0]
        return similarity_score
# This file marks the utils directory as a Python package.
