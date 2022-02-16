# Generated by Django 3.1.3 on 2020-11-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0002_mainmenu_has_submenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
                ('url', models.CharField(default='', max_length=25)),
                ('permissions', models.CharField(default='', max_length=25)),
                ('icon_class', models.CharField(default='', max_length=25)),
            ],
        ),
    ]
