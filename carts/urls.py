from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CartView

urlpatterns = [
    path('<user>/cart/', CartView.as_view()),
]

