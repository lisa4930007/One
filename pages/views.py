from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'

class BlessingPageView(TemplateView):
	template_name = 'blessing.html'