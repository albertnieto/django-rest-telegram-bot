import os
from django.contrib import admin
from django.urls import path
from dotenv import load_dotenv, find_dotenv
from django_rest_telegram.api.views import webhookView

load_dotenv(find_dotenv())

urlpatterns = [
    path("admin/", admin.site.urls),
    path(os.getenv("WH_ROUTE"), webhookView)
]
