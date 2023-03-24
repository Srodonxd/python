# Generated by Django 4.1.7 on 2023-03-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='rezyser',
        ),
        migrations.RemoveField(
            model_name='film',
            name='tytul',
        ),
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AddField(
            model_name='film',
            name='name',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.DeleteModel(
            name='Rezyser',
        ),
    ]
