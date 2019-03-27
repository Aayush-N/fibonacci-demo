from django.urls import path

from .views import FibonacciEntryView, DisplayFibonacciView

app_name = "main"
urlpatterns = [
    path("", view=FibonacciEntryView.as_view(), name="home"),
    path("display/", view=DisplayFibonacciView.as_view(), name="display")
]
