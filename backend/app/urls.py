"""
Definition of urls for app.
"""

from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView as DjangoTemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from app.views import TemplateView
from app.static_views import StaticHTMLView, StaticPartialView, StaticConstantView
from .api import *
import app.constants.url_constants as URLConstants
from app.constants import app_constants
from django.conf.urls.static import static
from . import settings
from app.api import AnalyzePaper
from app.defined_api.audio_transcribe import Transcribe

MainView = TemplateView()

# Create static HTML view instances
class LoginStaticView(StaticHTMLView):
    html_file = 'login.html'

class HomeStaticView(StaticHTMLView):
    html_file = 'home.html'

class DatasetsStaticView(StaticHTMLView):
    html_file = 'datasets.html'

class LibraryStaticView(StaticHTMLView):
    html_file = 'library.html'

class CredibilityStaticView(StaticHTMLView):
    html_file = 'credibility.html'

class ComplaintsStaticView(StaticHTMLView):
    html_file = 'complaints.html'

class HeyStaticView(StaticHTMLView):
    html_file = 'hey.html'

# Partial views
class NavbarPartialView(StaticPartialView):
    html_file = 'navbar.html'

class SidebarPartialView(StaticPartialView):
    html_file = 'sidebar.html'

class FooterPartialView(StaticPartialView):
    html_file = 'footer.html'

# Config.js view
class ConfigJsView(StaticHTMLView):
    html_file = 'config.js'
    content_type = 'application/javascript'

# Constant views  
class ErrorConstantView(StaticConstantView):
    html_file = 'error.html'

class ExpiredConstantView(StaticConstantView):
    html_file = 'expired.html'

class ComplaintTableConstantView(StaticConstantView):
    html_file = 'complaint_table.html'

list_create_patterns = URLConstants.GenericAPI.list_create_patterns
get_update_destroy_patterns = URLConstants.GenericAPI.retrieve_update_delete_patterns

api_patterns = [
    path("api/", include((list_create_patterns, app_constants.APP_NAME))),
    path("api/", include((get_update_destroy_patterns, app_constants.APP_NAME))),
]

predefined_patterns = [path("api/analyze-paper/<str:id>/", AnalyzePaper.as_view()),
                       path("api/transcribe-audio/", Transcribe.as_view(), name = "transcribe-audio")]

# CSRF token endpoint
@ensure_csrf_cookie
def get_csrf_token(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['Access-Control-Allow-Origin'] = 'https://case-detector.vercel.app'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response

# Health check endpoint for Render
def health_check(request):
    return JsonResponse({'status': 'healthy'})

# Root redirect
from django.views.generic import RedirectView

# Authentication patterns
auth_patterns = [
    path("", RedirectView.as_view(url='/login.html', permanent=False), name="root"),
    path("health/", health_check, name="health"),
    path("csrf/", get_csrf_token, name="csrf"),
    path("authenticate_user/", MainView.authenticate_user, name="authenticate_user"),
    path("logout/", MainView.user_logout, name="logout"),
]

# Static HTML patterns (for pure static HTML files)
static_html_patterns = [
    path("login.html", LoginStaticView.as_view(), name="login"),
    path("home.html", HomeStaticView.as_view(), name="home"),
    path("datasets.html", DatasetsStaticView.as_view(), name="datasets"),
    path("library.html", LibraryStaticView.as_view(), name="library"),
    path("credibility.html", CredibilityStaticView.as_view(), name="credibility"),
    path("complaints.html", ComplaintsStaticView.as_view(), name="complaints"),
    path("hey.html", HeyStaticView.as_view(), name="hey"),
    # Config.js
    path("config.js", ConfigJsView.as_view(), name="config_js"),
    # Partials
    path("partials/navbar.html", NavbarPartialView.as_view(), name="partial_navbar"),
    path("partials/sidebar.html", SidebarPartialView.as_view(), name="partial_sidebar"),
    path("partials/footer.html", FooterPartialView.as_view(), name="partial_footer"),
    # Constants
    path("static/constants/error.html", ErrorConstantView.as_view(), name="constant_error"),
    path("static/constants/expired.html", ExpiredConstantView.as_view(), name="constant_expired"),
    path("static/constants/complaint_table.html", ComplaintTableConstantView.as_view(), name="constant_complaint_table"),
]

urlpatterns = [
    *auth_patterns,
    *static_html_patterns,
    *api_patterns,
    *predefined_patterns,
]

# Serve media files (works in both development and production)
# In production, consider using cloud storage (S3, Cloudinary) for better performance
from django.views.static import serve as static_serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]

# Serve static files during development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
