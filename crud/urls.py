from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('add_new_employee', view=views.add_new_employee, name='add_new_employee'),
    path('show_all_employees/', view=views.show_all_employees, name='show_all_employees'),
    path('edit_employee/<str:id>/', view=views.edit_employee, name='edit_employee'),
    path('edit_employee_save', view=views.edit_employee_save, name='edit_employee_save'),
    path('delete_employee/<str:id>/', view=views.delete_employee, name='delete_employee'),
]
