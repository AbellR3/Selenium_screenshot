# Generated by Django 4.0.3 on 2022-03-22 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=600)),
                ('pge_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selector', models.CharField(choices=[('id', 'id'), ('class name', 'class name'), ('XPATH', 'XPATH'), ('tag name', 'tag name')], max_length=50)),
                ('setted_image', models.CharField(default=None, max_length=300)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.page')),
            ],
        ),
    ]
