# Generated by Django 4.1 on 2022-10-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_coursemodel_teacher_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='coursemodel',
            name='teacher_image',
        ),
        migrations.RemoveField(
            model_name='coursemodel',
            name='teacher_level',
        ),
    ]