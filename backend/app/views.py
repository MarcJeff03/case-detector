from django.shortcuts import redirect
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import app.constants.template_constants as Templates
from django.contrib.auth import logout, authenticate, login


class TemplateView:
    """Built in Template Renderer View Level"""

    def __init__(self):
        pass

    def complaints(self, request):
        """  Renders the complaint's profile. """

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.COMPLAINTS.render_page(request)

    def home(self, request):
        """Renders the home page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.HOME.render_page(request)

    def datasets(self, request):
        """Renders the datasets page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")
        
        return Templates.DATASETS.render_page(request)

    def library(self, request):
        """Renders the library page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.LIBRARY.render_page(request)

    def credibility(self, request):
        """Renders the credibility page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.CREDIBILITY.render_page(request)

    def login(self, request):
        assert isinstance(request, HttpRequest)

        if request.user.is_authenticated == False:
            return Templates.LOGIN.render_page(request)

        return redirect("home") #Change the home to your index page.

    @csrf_exempt
    def authenticate_user(self, request):
        try:
            if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)  # Library level not instance.
                    # Return JSON response for cross-origin requests
                    return JsonResponse({
                        'success': True,
                        'redirect': '/home.html'
                    })
                else:
                    return JsonResponse({
                        'success': False,
                        'error': 'Invalid credentials'
                    }, status=401)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)

        return JsonResponse({
            'success': False,
            'error': 'Invalid request method'
        }, status=400)

    def user_logout(self, request):
        from django.contrib.auth import logout
        from django.shortcuts import redirect
        logout(request)
        return redirect("login")

