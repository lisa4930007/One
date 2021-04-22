from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	# TODO: 直接帶登入資訊到 home 不用到登入頁面
	template_name = 'registration/signup.html'

# TODO:Lisa 已登入的user 轉址登入頁面到首頁