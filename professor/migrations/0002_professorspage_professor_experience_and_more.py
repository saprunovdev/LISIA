# Generated by Django 4.1.2 on 2022-10-24 09:01

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professorspage',
            name='professor_experience',
            field=wagtail.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='professorspage',
            name='professor_personal',
            field=wagtail.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='professorspage',
            name='professor_professional',
            field=wagtail.fields.RichTextField(default=''),
        ),
    ]
