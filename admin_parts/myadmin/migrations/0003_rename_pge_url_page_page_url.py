# Generated by Django 4.0.3 on 2022-03-22 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_element_selector_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='pge_url',
            new_name='page_url',
        ),
    ]
