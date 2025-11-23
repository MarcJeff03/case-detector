"""
Custom views for serving static HTML files
"""
from django.http import HttpResponse
from django.views import View
import os
from django.conf import settings


class StaticHTMLView(View):
    """
    Serve pure static HTML files without Django template processing
    """
    html_file = None
    subdirectory = ''  # For partials, constants, etc.
    content_type = 'text/html'  # Default content type
    
    def get(self, request):
        if not self.html_file:
            return HttpResponse("HTML file not specified", status=500)
        
        # Build the full path to the HTML file
        if self.subdirectory:
            file_path = os.path.join(settings.BASE_DIR, '..', 'frontend', 'public', self.subdirectory, self.html_file)
        else:
            file_path = os.path.join(settings.BASE_DIR, '..', 'frontend', 'public', self.html_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            return HttpResponse(html_content, content_type=self.content_type)
        except FileNotFoundError:
            return HttpResponse(f"File not found: {self.html_file}", status=404)
        except Exception as e:
            return HttpResponse(f"Error loading file: {str(e)}", status=500)


class StaticPartialView(StaticHTMLView):
    """
    Serve partial HTML files (navbar, sidebar, footer, etc.)
    """
    subdirectory = 'partials'


class StaticConstantView(StaticHTMLView):
    """
    Serve constant HTML files (error, expired, etc.)
    """
    subdirectory = 'constants'
