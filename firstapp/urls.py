from django.contrib import admin
from django.urls import path
from django.urls import include
from . import view

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("/", (view.home)),
    path("about/", (view.about)),
]
