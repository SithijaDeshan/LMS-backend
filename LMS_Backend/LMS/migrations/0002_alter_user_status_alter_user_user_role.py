# Generated by Django 4.2.9 on 2024-01-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, default='none', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(default='user', max_length=10),
        ),
    ]