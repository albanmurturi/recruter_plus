# Generated by Django 4.2.9 on 2024-02-16 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_interview_learend_quesions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='learend_quesions',
            new_name='learend_quesitons',
        ),
    ]
