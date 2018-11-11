from django.contrib import admin
from django.urls import path
from .views import Learning

urlpatterns = [
    path('learn_tables/',Learning.list_learn_table, name = "list-learn-tables" ),
    path('learn_tables/<int:id>/', Learning.learn_table, name = "learn-table" ),
]