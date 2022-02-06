from django.shortcuts import render

from Python_web_basics_projects.employees.models import Employee


def index(request):
    context = {
        'title': 'Employees list',
        'employees': Employee.objects.all(),
    }
    return render(request, 'templates_examples/index.html', context)
