from django.urls import path
from .views import HomePageView, BlessingPageView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('blessing/', BlessingPageView.as_view(), name='blessing'),
]