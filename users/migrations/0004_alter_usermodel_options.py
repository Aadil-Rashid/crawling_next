# Generated by Django 3.2.7 on 2021-10-06 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
    ]
