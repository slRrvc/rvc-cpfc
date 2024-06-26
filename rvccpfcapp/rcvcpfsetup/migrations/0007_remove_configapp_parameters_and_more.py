# Generated by Django 5.0.3 on 2024-04-29 18:44

import utils.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcvcpfsetup', '0006_parameters_sitesetup_remove_configapp_date_format_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configapp',
            name='parameters',
        ),
        migrations.RemoveField(
            model_name='configapp',
            name='site_setup',
        ),
        migrations.AddField(
            model_name='configapp',
            name='date_format',
            field=models.CharField(choices=[('%d %m %Y', 'Alemanha (dd/mm/aaaa)'), ('%d %m %Y', 'Brasil (DD/MM/AAAA)'), ('%Y %m %d', 'China (aaaa/mm/dd)'), ('%d %m %Y', 'França (dd/mm/aaaa)'), ('%d %m %Y', 'França (dd/mm/aaaa)'), ('%m %d %Y', 'Inglês (mm/dd/aaaa)'), ('%d %m %Y', 'Espanha (dd/mm/aaaa)')], default='%d %m %Y', max_length=8, verbose_name='Formato de data'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='date_separator',
            field=models.CharField(choices=[('/', 'Barra (/)'), ('-', 'Ifên (-)'), ('*', 'Asterisco (*)')], default='/', max_length=1, verbose_name='Separador de data'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_places_ha',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Casas Decimais (HA)'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_places_m3',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Casas Decimais (M³)'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_places_mdc',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Casas Decimais (MDC)'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_places_peso',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Casas Decimais (Peso)'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_places_porcentagem',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Casas Decimais'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_places_valor',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=1, verbose_name='Casas Decimais (Valor)'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='decimal_separator',
            field=models.CharField(choices=[(',', 'Virgula - (,)'), ('.', 'Ponto - (.)')], default=',', max_length=1, verbose_name='Separador de decimal'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='email_sistema',
            field=models.CharField(default='rvcsoftware@rvcsoftware.com.br', max_length=50, verbose_name='E-mail do Sistema'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='extended_date_format',
            field=models.CharField(choices=[('%d, de %B de %Y', 'Dia, de mês de ano'), ('%B, %d de %Y', 'Mês, dia de ano'), ('%Y, %d de %B', 'Ano, dia de mês')], default='%d, de %B de %Y', max_length=15, verbose_name='Data por extenso'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.model_validators.velidate_png]),
        ),
        migrations.AddField(
            model_name='configapp',
            name='file_extension',
            field=models.CharField(choices=[('.docx', '.docx'), ('.PDF', '.PDF'), ('.rvc', '.rvc')], default='.rvc', max_length=5, verbose_name='Extensão de arquivos'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='language',
            field=models.CharField(choices=[('pt-br', 'Portugues Brasil - (pt-br)'), ('en-us', 'Inglês (Estados Unidos) - (en-us)')], default='pt-BR', max_length=5, verbose_name='Idioma'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='monetary_symbol',
            field=models.CharField(choices=[('R$', 'Real Brasil - (R$)'), ('$', 'Dollar - ($)'), ('€', 'Euro - (€)')], default='R$', max_length=2, verbose_name='Simbolo monetário'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='show_description',
            field=models.BooleanField(default=True, verbose_name='Mostrar descrição'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='show_footer',
            field=models.BooleanField(default=True, verbose_name='Mostrar rodapé'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='show_header',
            field=models.BooleanField(default=True, verbose_name='Mostrar cabeçalho'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='show_menu',
            field=models.BooleanField(default=True, verbose_name='Mostrar menu'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='show_pagination',
            field=models.BooleanField(default=True, verbose_name='Mostrar paginação'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='show_search',
            field=models.BooleanField(default=True, verbose_name='Mostrar pesquisa'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='themes',
            field=models.CharField(choices=[('Thema padrão', 'Thema padrão'), ('themes/cerulean', 'Cerulean'), ('themes/cyborg', 'Cyborg'), ('themes/readable', 'Readable'), ('themes/simplex', 'Simplex'), ('themes/spruce', 'Spruce'), ('themes/superhero', 'SuperHero'), ('themes/united', 'United')], default='Thema padrão', max_length=30, verbose_name='Tema do sistema'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='thousand_separator',
            field=models.CharField(choices=[(',', 'Virgula - (,)'), ('.', 'Ponto - (.)')], default='.', max_length=1, verbose_name='Separador de milhar'),
        ),
        migrations.AddField(
            model_name='configapp',
            name='time_format',
            field=models.CharField(choices=[('%H:%M:%S', '24 Horas (H:M:S)'), ('%I:%M:%S %p', 'AM/PM (H:M:S)'), ('%H:%M', '24 Horas (H:M)'), ('%I:%M %p', 'AM/PM (H:M)')], default='%H:%M:%S', max_length=11, verbose_name='Formato da hora'),
        ),
        migrations.DeleteModel(
            name='Parameters',
        ),
        migrations.DeleteModel(
            name='SiteSetup',
        ),
    ]
