from django.db import models


class Service(models.Model):
    '''
    docstring
    '''
    id = models.PositiveIntegerField(
        primary_key=True,
        auto_created=True,
        blank=False,
        unique=True
    )

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название услуги',
        blank=False,
    )
    description = models.TextField(
        max_length=350,
        verbose_name='Описание'
    )

    equipment_used = models.ManyToManyField(
        to='Equipment',
        blank=True,
        verbose_name='Используемое оборудование'

    )
    illustration = models.ImageField(
        blank=True,
        verbose_name='Иллюстрация'

    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Contract(models.Model):
    '''
    docstring
    '''
    id = models.AutoField(
        primary_key=True,
        auto_created=True,
        unique=True,
        blank=False
    )
    number = models.CharField(
        unique=True,
        blank=True,
        verbose_name='Номер контракта'

    )

    client = models.ForeignKey(
        to='Client',
        blank=False,
        on_delete = models.DO_NOTHING,
        verbose_name='Клиент'
    )

    service = models.ForeignKey(
        to='Service',
        on_delete=models.DO_NOTHING,
        verbose_name='Услуга'
    )

    signed_date = models.DateField(
        verbose_name='Дата подписания'
    )

    completed = models.BooleanField(
        verbose_name='Закончен?',
        blank=False,
    )
    completed_date = models.DateField(
        verbose_name='Дата завершения',
        blank=True,
        null=True,
    )

    equipment_required = models.ForeignKey(
        to='Equipment',
        on_delete=models.DO_NOTHING,
        verbose_name='Необходимое оборудование'
    )

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return self.number


class Equipment(models.Model):
    '''
    docstring
    '''
    id = models.PositiveIntegerField(
        primary_key=True,
        auto_created=True,
        blank=False,
        unique=True
    )

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название оборудования',
        blank=False,
    )

    description = models.TextField(
        max_length=350,
        verbose_name='Описание'
    )

    class EquipmentState(models.TextChoices):
        READY = 'Ready_to_use'
        BUSY = 'Used_in_another_contract'
        BROKEN = 'Need_to_be_repair'

    is_free = models.CharField(
        choices=EquipmentState,
        blank=False,
        verbose_name='Свободно для использования'
    )

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.name


class Client(models.Model):
    '''
    docstring
    '''
    organization_name = models.CharField(
        max_length=150,
        verbose_name='Наименование организации',
        blank=False
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        verbose_name='Email'
    )

    contact_number = models.CharField(
        max_length=12,
        verbose_name='Контактный номер телефона',
        blank=False
    )

    inn = models.PositiveIntegerField(
        #max_length=10,
        verbose_name='ИНН',
        blank=True,
        null=True
    )

    bik = models.PositiveIntegerField(
        #max_length=9,
        verbose_name='БИК',
        blank=True,
        null=True
    )

    kpp = models.PositiveIntegerField(
        #max_length=9,
        verbose_name='КПП',
        blank=True,
        null=True
    )

    correspondent_account = models.PositiveIntegerField(
        #max_length=20,
        verbose_name='Корреспондентский счет',
        blank=True,
        null=True
    )

    checking_account = models.PositiveIntegerField(
        #max_length=20,
        verbose_name='Расчетный счет',
        blank=True,
        null=True
    )

    bank = models.CharField(
        max_length=200,
        verbose_name='Банк получателя',
        blank=True,
        null=True
    )

    address_country = models.CharField(
        max_length=50,
        verbose_name='Страна',
        blank=True,
        null=True
    )

    post_index = models.PositiveIntegerField(
        #max_length=6,
        verbose_name='Почтовый индекс',
        blank=True,
        null=True
    )

    address_city = models.CharField(
        max_length=50,
        verbose_name='Населенный пункт',
        blank=True,
        null=True
    )

    address_street = models.CharField(
        max_length=50,
        verbose_name='Улица',
        blank=True,
        null=True
    )

    address_building = models.PositiveIntegerField(
        #max_length=10,
        verbose_name='Номер здания',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.organization_name