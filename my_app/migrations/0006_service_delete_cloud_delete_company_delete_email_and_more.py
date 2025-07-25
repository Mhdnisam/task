# Generated by Django 5.2.4 on 2025-07-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_cloud_company_findlocalinstallers_hardware_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('email', 'Email & Collaboration'), ('software', 'Software Brands'), ('hardware', 'Hardware'), ('security', 'Security & Backup'), ('cloud', 'Cloud'), ('ondemand', 'On Demand Services'), ('installers', 'Find Local Installers'), ('company', 'Company')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cloud',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Findlocalinstallers',
        ),
        migrations.DeleteModel(
            name='Hardware',
        ),
        migrations.DeleteModel(
            name='Ondemandservices',
        ),
        migrations.DeleteModel(
            name='Security',
        ),
        migrations.DeleteModel(
            name='softwarebrands',
        ),
    ]
