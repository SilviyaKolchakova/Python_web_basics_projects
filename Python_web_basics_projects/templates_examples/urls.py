from django.urls import path

from Python_web_basics_projects.templates_examples.views import index

urlpatterns = (
    path('', index, name='templates index'),

)