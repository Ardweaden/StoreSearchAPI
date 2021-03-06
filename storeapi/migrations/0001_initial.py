# Generated by Django 2.1.4 on 2018-12-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('context', models.CharField(default='', max_length=100)),
                ('version', models.CharField(default='', max_length=100)),
                ('provider', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='', max_length=100)),
                ('tags', models.TextField(default='')),
                ('apiDefinition', models.TextField(default='')),
                ('endpointURLs', models.TextField(default='')),
                ('businessInformation', models.TextField(default='')),
                ('keywords', models.TextField(default='')),
            ],
        ),
    ]
