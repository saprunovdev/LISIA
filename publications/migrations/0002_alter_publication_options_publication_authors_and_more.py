# Generated by Django 4.1.2 on 2022-10-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'publication', 'verbose_name_plural': 'publications'},
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='publication',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='published_where',
            field=models.EmailField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='publication',
            name='title',
            field=models.EmailField(blank=True, max_length=400),
        ),
    ]
