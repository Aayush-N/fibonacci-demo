from django.urls import path

from callhub_demo.main.apis import FibonacciAPIView

app_name = "api"

urlpatterns = [
    path("fibonacci/", FibonacciAPIView.as_view(), name="fibonacci"),
]
