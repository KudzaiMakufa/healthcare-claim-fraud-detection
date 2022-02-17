# Generated by Django 3.1.7 on 2022-02-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_library_is_fraudulent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.CharField(default=None, max_length=100)),
                ('potential_fraud', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CVE_Scan',
        ),
    ]
