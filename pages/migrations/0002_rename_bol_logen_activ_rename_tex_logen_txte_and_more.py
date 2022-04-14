# Generated by Django 4.0.4 on 2022-04-14 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logen',
            old_name='bol',
            new_name='activ',
        ),
        migrations.RenameField(
            model_name='logen',
            old_name='tex',
            new_name='txte',
        ),
        migrations.RenameField(
            model_name='logen',
            old_name='name',
            new_name='usernam',
        ),
        migrations.AlterField(
            model_name='show',
            name='facebook',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='gmail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='twitter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
