from django.contrib import admin
from polls.models import AnswerList, Question

# Register your models here.
admin.site.register(AnswerList)
admin.site.register(Question)