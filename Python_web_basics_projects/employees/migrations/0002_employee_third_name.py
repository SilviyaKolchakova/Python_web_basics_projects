# Generated by Django 3.2.12 on 2022-02-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='third_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]