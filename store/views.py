from django.db import models
from django.http import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,TemplateView, ListView, DetailView
from .models import Debt
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class Home(TemplateView):
    template_name = 'store/home.html'

class DebtList(LoginRequiredMixin, ListView):
    model = Debt
    template_name = 'store/debt_list.html'
    context_object_name = 'debts'

class DebtCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Debt
    fields = ['name', 'amount', 'paid', 'balance', 'date']
    success_message = "successfully created"

    def form_valid(self, form):
        form.instance.keeper = self.request.user
        return super().form_valid(form)

class DebtDetail(LoginRequiredMixin, DetailView):
    model = Debt

class DebtUpdate(LoginRequiredMixin, UserPassesTestMixin ,SuccessMessageMixin, UpdateView):
     model = Debt
     fields = ['name', 'amount', 'paid', 'balance', 'date']
     success_message = "successfully updated"

     def form_valid(self, form):
        form.instance.keeper = self.request.user
        return super().form_valid(form)

     def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.keeper:
            return True
        return False

class DebtDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin, DeleteView):
    model = Debt
    success_url = '/'
    success_message = "successfully deleted"

    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.keeper:
            return True
        return False




    

    
    