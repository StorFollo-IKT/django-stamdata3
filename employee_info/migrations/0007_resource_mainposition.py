# Generated by Django 3.1.5 on 2021-02-05 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_info', '0006_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='mainPosition',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resource2', to='employee_info.employment'),
        ),
    ]
