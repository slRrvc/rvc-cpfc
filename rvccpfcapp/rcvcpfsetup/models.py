from django.db import models
from utils.constants import Constants
from utils.model_validators import velidate_png
from utils.images import resize_image


class ConfigApp(models.Model):
    class Meta:
        verbose_name = 'Configuração do App'
        verbose_name_plural = 'Configurações do App'

    application = models.CharField(
        max_length=30,
        default='rvccpf',
        verbose_name='Aplicativo'
    )

    nameapp = models.CharField(
        max_length=50,
        default='RVC - Controle de Produção Florestal',
        verbose_name='Nome do Aplicativo'
    )

    short_name = models.CharField(
        max_length=50,
        default='CP - Florestal',
        verbose_name='Nome abreviado'
    )

    title = models.CharField(
        max_length=50,
        default='RVC (CP - Florestal)',
        verbose_name='Titulo da Aplicativo'
    )

    description = models.TextField(
        max_length=254,
        verbose_name='Descrição do Aplicativo'
    )

    language = models.CharField(
        max_length=5,
        default='pt-BR',
        choices=Constants.LANGUAGE,
        verbose_name='Idioma'
    )  # Idioma = pt-br

    monetary_symbol = models.CharField(
        max_length=2,
        default='R$',
        choices=Constants.MONETARY_SYMBOL,
        verbose_name='Simbolo monetário'
    )  # Simbolo Monetário = r$

    thousand_separator = models.CharField(
        max_length=1,
        choices=Constants.THOUSAND_SEPARATOR,
        default='.',
        verbose_name='Separador de milhar'
    )  # Separador de Milhar = .

    decimal_separator = models.CharField(
        max_length=1,
        default=',',
        choices=Constants.DECIMAL_SEPARATOR,
        verbose_name='Separador de decimal'
    )  # Separador de decimal = ,

    date_separator = models.CharField(
        max_length=1,
        default='/',
        choices=Constants.DATE_SAPARATOR,
        verbose_name='Separador de data'
    )  # Separador de data = /

    date_format = models.CharField(
        max_length=8,
        default='%d %m %Y',
        choices=Constants.DATE_FORMAT,
        verbose_name='Formato de data'
    )  # Separador de hora = dd/mm/yyyy

    extended_date_format = models.CharField(
        max_length=15,
        default='%d, de %B de %Y',
        choices=Constants.EXTENDED_DATE_FORMAT,
        verbose_name='Data por extenso'
    )  # Data por extenso = dd "de" mmmm "de" yyyy

    time_format = models.CharField(
        max_length=11,
        default='%H:%M:%S',
        choices=Constants.TIME_FORMAT,
        verbose_name='Formato da hora'
    )  # Separador de hora = hh:mm:ss

    decimal_places_ha = models.CharField(
        max_length=1,
        default='2',
        choices=Constants.DECIMAL_PLACES,
        verbose_name='Casas Decimais (HA)'
    )  # Número de Casas Decimais=4

    decimal_places_mdc = models.CharField(
        max_length=1,
        default='2',
        choices=Constants.DECIMAL_PLACES,
        verbose_name='Casas Decimais (MDC)'
    )  # Número de Casas Decimais MDC=3

    decimal_places_m3 = models.CharField(
        max_length=1,
        default='2',
        choices=Constants.DECIMAL_PLACES,
        verbose_name='Casas Decimais (M³)'
    )  # Número de Casas Decimais cubico=3

    decimal_places_valor = models.CharField(
        max_length=1,
        default='2',
        choices=Constants.DECIMAL_PLACES,
        verbose_name='Casas Decimais (Valor)'
    )  # Número de Casas Decimais valor=2

    decimal_places_peso = models.CharField(
        max_length=1,
        default='2',
        choices=Constants.DECIMAL_PLACES,
        verbose_name='Casas Decimais (Peso)'
    )  # Número de Casas Decimais peso=3

    decimal_places_porcentagem = models.CharField(
        max_length=1,
        default='2',
        choices=Constants.DECIMAL_PLACES,
        verbose_name='Casas Decimais',
    )  # Número de Casas Decimais percentagem=2

    themes = models.CharField(
        max_length=30,
        default='Thema padrão',
        choices=Constants.THEMES,
        verbose_name='Tema do sistema',
    )  # Seleção de thema do sistema = themes/cyborg

    email_sistema = models.CharField(
        max_length=50,
        default='rvcsoftware@rvcsoftware.com.br',
        verbose_name='E-mail do Sistema',
    )  # Seleção de thema do sistema = rvcsoftware@rvcsoftware.com.br

    file_extension = models.CharField(
        max_length=5,
        default='.rvc',
        choices=Constants.FILE_EXTENSION,
        verbose_name='Extensão de arquivos',
    )  # Seleção de thema do sistema = .docx

    show_header = models.BooleanField(
        default=True,
        verbose_name='Mostrar cabeçalho'
    )

    show_search = models.BooleanField(
        default=True,
        verbose_name='Mostrar pesquisa'
    )

    show_menu = models.BooleanField(
        default=True,
        verbose_name='Mostrar menu'
    )

    show_description = models.BooleanField(
        default=True,
        verbose_name='Mostrar descrição'
    )

    show_pagination = models.BooleanField(
        default=True,
        verbose_name='Mostrar paginação'
    )

    show_footer = models.BooleanField(
        default=True,
        verbose_name='Mostrar rodapé'
    )

    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[velidate_png],
    )

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)

        super().save(*args, **kwargs)

        favicon_changed = False
        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.application
