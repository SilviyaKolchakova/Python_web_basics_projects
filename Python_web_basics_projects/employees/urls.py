from django.urls import path

from Python_web_basics_projects.employees.views import list_departments, department_details

urlpatterns = (
    path('list', list_departments),
    path('details/', department_details),

)