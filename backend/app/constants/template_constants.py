from app.builder.template_builder import Builder
from app.constants import app_constants
from app.models import *

# NOTE: Do not query the database at import time!
# Provide context values from your view instead.
HOME = (
    Builder()
    .addPage("app/home.html")
    .addTitle("home")
    .addContext({
        "title": "Home - Page",
        "obj_name": "home",
        "research": 0,  # Set in view
        "credibility": 0,  # Set in view
        "datasets": 0,  # Set in view
        "plagiarism": 0,  # Set in view
    })
)
HOME.build()

DATASETS = (
	Builder()
	.addPage("app/datasets.html")
	.addTitle("datasets")
)

DATASETS.build()

COMPLAINTS = (
	Builder()
	.addPage("app/complaints.html")
	.addTitle("complaints")
)

COMPLAINTS.build()

LIBRARY = (
	Builder()
	.addPage("app/library.html")
	.addTitle("library")
)

LIBRARY.build()

CREDIBILITY = (
	Builder()
	.addPage("app/credibility.html")
	.addTitle("credibility")
)

CREDIBILITY.build()

LOGIN = (
	Builder()
	.addPage("app/login.html")
	.addTitle("login")
	.addContext(
		{
			"title": "Login - Page",
			"obj_name": "login",
			"app_name": app_constants.SOFTWARE_NAME,
			"app_desc": app_constants.SOFTWARE_DESCRIPTION
		}
	)
)
LOGIN.build()