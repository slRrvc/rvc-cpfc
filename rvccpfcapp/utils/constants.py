
class Constants():
    DECIMAL_PLACES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    THEMES = (
        ('Thema padrão', 'Thema padrão'),
        ('themes/cerulean', 'Cerulean'),
        ('themes/cyborg', 'Cyborg'),
        ('themes/readable', 'Readable'),
        ('themes/simplex', 'Simplex'),
        ('themes/spruce', 'Spruce'),
        ('themes/superhero', 'SuperHero'),
        ('themes/united', 'United'),
    )

    LANGUAGE = (
        ('pt-br', 'Portugues Brasil - (pt-br)'),
        ('en-us', 'Inglês (Estados Unidos) - (en-us)'),
    )

    MONETARY_SYMBOL = (
        ('R$', 'Real Brasil - (R$)'),
        ('$', 'Dollar - ($)'),
        ('€', 'Euro - (€)'),
    )

    THOUSAND_SEPARATOR = (
        (',', 'Virgula - (,)'),
        ('.', 'Ponto - (.)'),
    )

    DECIMAL_SEPARATOR = (
        (',', 'Virgula - (,)'),
        ('.', 'Ponto - (.)'),
    )

    DATE_SAPARATOR = (
        ('/', 'Barra (/)'),
        ('-', 'Ifên (-)'),
        ('*', 'Asterisco (*)'),
    )

    DATE_FORMAT = (
        ('%d %m %Y', 'Alemanha (dd/mm/aaaa)'),
        ('%d %m %Y', 'Brasil (DD/MM/AAAA)'),
        ('%Y %m %d', 'China (aaaa/mm/dd)'),
        ('%d %m %Y', 'França (dd/mm/aaaa)'),
        ('%d %m %Y', 'França (dd/mm/aaaa)'),
        ('%m %d %Y', 'Inglês (mm/dd/aaaa)'),
        ('%d %m %Y', 'Espanha (dd/mm/aaaa)'),
    )

    EXTENDED_DATE_FORMAT = (
        ('%d, de %B de %Y', 'Dia, de mês de ano'),
        ('%B, %d de %Y', 'Mês, dia de ano'),
        ('%Y, %d de %B', 'Ano, dia de mês'),
    )

    TIME_FORMAT = (
        ('%H:%M:%S', '24 Horas (H:M:S)'),
        ('%I:%M:%S %p', 'AM/PM (H:M:S)'),
        ('%H:%M', '24 Horas (H:M)'),
        ('%I:%M %p', 'AM/PM (H:M)'),
    )

    FILE_EXTENSION = (
        ('.docx', '.docx'),
        ('.PDF', '.PDF'),
        ('.rvc', '.rvc'),
    )
