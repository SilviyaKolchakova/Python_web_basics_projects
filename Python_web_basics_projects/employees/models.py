from django.db import models

from Python_web_basics_projects import employees


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract=True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
    )
    third_name = models.CharField(
        max_length=30,
    )

    identity_card = models.CharField(
        max_length=10,
    )

    job_title = models.IntegerField(
        choices=(
            (1, 'Software Developer'),
            (2, 'DevOps Specialists'),
            (3, 'QA Engineer'),
        )
    )
    #ManytoOne(many employees to one department)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('first_name',)



class Project(models.Model):
    name = models.CharField(
        max_length=20,
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employee
    )

class User(models.Model):
    email = models.EmailField()

    #OneToOneField
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    #когато правим OneToOneField има логика да сменим primary_key

