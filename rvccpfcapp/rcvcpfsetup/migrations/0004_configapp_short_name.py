# Generated by Django 5.0.3 on 2024-04-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcvcpfsetup', '0003_alter_configapp_application_alter_configapp_nameapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='configapp',
            name='short_name',
            field=models.CharField(default='RVC - C. P. Florestal', max_length=50, verbose_name='Nome do Aplicativo'),
        ),
    ]