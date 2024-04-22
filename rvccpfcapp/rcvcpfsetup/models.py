from django.db import models


class configuracoes(models.Model):
    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    theme = models.CharField(
        max_length=50,
        verbose_name='Thema'
    )

    thousandSeparator = models.CharField(
        max_length=50, verbose_name='Themas'
    )  # Separador de Milhares

    decimalSeparator = models.CharField(
        max_length=1,
        default=',',
        verbose_name='Separador Decimal'
    )  # Ponto Decimal

    shortDateFormat = models.CharField(
        max_length=10,
        verbose_name='Formato Data'
    )  # Formato de Data

    shortTimeFormat = models.CharField(
        max_length=8,
        verbose_name='Separador Horas'
    )  # Formato de Horas

    dateSeparator = models.CharField(
        max_length=1,
        default='/',
        verbose_name='Separador Data'
    )  # Separador de Data

    timeSeparator = models.CharField(
        max_length=1,
        default=':',
        verbose_name='Separador Horas'
    )  # Separador de Horas

    currencyString = models.CharField(
        max_length=3,
        verbose_name='Símbolo Monetário'
    )  # Símbolo de Valor Monetário

    currencyFormat = models.IntegerField(
        default=0,
        verbose_name='Valor Positivo'
    )  # Formato de Valor Positivo (0 = "R$1,00")

    negCurrFormat = models.IntegerField(
        default=1,
        verbose_name='Valor Negativo'
    )  # Formato de Valor Negativo (2 = "-R$1,00")

    currencyDecimals = models.IntegerField(
        default=2,
        verbose_name='Casas Decimais'
    )  # Número de Casas Decimais

    def __str__(self):
        return self.theme
