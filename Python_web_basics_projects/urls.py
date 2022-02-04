
from django.contrib import admin
from django.urls import path, include


from Python_web_basics_projects.employees.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    path('departments/', include('Python_web_basics_projects.employees.urls'))
]
