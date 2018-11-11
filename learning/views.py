from django.shortcuts import render
from .models import LearnTable
# Create your views here.
class Learning(object):
	"""docstring for Learning"""
	@staticmethod
	def list_learn_table(request):
		tables = LearnTable.objects.all()
		context = {
			"title":"Learn Tables",
			"tables":tables
		}
		return render(request,"learning/templates/learn_tables.html", context)
	
	@staticmethod
	def learn_table(request,id):
		learn_table = LearnTable.objects.get(id=id);
		date_colums = [*set([mark.mark_date for mark in learn_table.get_marks.all()])]
		schl_class = learn_table.for_class 
		date_colums.sort()
		
		 
		context = {
			'title':'Learn Table',
			'date_colums':date_colums,
			'learn_table':learn_table,
			'schl_class':schl_class
		}
		return render(request,"learning/templates/learn_table.html", context)

