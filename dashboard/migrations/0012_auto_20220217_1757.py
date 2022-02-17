# Generated by Django 3.1.7 on 2022-02-17 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_physician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='physician_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.physician'),
        ),
    ]
