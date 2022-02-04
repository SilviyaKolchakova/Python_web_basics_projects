from django.http import HttpResponse



def home(request):
    return HttpResponse('This is home')


def list_departments(request):
    return HttpResponse('This is a list of departments')


def department_details(request):
    return HttpResponse('Details for the departments')
