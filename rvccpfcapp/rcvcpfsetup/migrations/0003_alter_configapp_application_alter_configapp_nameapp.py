# Generated by Django 5.0.3 on 2024-04-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcvcpfsetup', '0002_configapp_delete_configuracoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configapp',
            name='application',
            field=models.CharField(default='rvccpf', max_length=30, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='configapp',
            name='nameapp',
            field=models.CharField(default='RVC - Controle de Produção Floresta', max_length=50, verbose_name='Nome do Aplicativo'),
        ),
    ]