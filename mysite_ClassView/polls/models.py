from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class AnswerList(models.Model):
	answer_list = models.ForeignKey(Question, on_delete=models.CASCADE)
	answers_options = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self) -> str:
		return self.answer_list