# Generated by Django 3.1.7 on 2022-02-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20220217_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physician_id', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]