# Generated by Django 5.0.6 on 2024-05-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], max_length=5),
        ),
    ]
