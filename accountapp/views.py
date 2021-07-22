from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request): #인증과정 해주기 / 로그인 한사람만
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))




class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #완료하고나서 어디로 돌아 갈 것인지
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_User'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

