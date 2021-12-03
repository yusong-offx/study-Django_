from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import *

# Create your views here.
class BooksModelView(TemplateView):
	template_name = 'book/index.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['model_list'] = ['Book', 'Author', 'Publisher']
		return context