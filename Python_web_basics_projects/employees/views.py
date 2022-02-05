from django.http import HttpResponse
from django.shortcuts import render

from Python_web_basics_projects.employees.models import Department, Employee


def home(request):
    return HttpResponse('This is home')


def list_departments(request):
    # department = Department(
    #     name='NewDepartment'
    # )
    # department.save()

    context = {
        'departments': Department.objects.all(),
        'employees': Employee.objects.all()
    }
    return render(request, 'list_departments.html', context)


def department_details(request):
    return HttpResponse('Details for the departments')
