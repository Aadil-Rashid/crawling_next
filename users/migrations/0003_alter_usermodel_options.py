# Generated by Django 3.2.7 on 2021-10-05 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210921_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'permissions': [('can_fly', 'Can fly in the air'), ('can_sing', 'Can sing the song very loud')], 'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
    ]
