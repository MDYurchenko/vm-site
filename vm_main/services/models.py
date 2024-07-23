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
        max_length=350
    )
    equipment_used = models.ManyToManyField(
        to='Equipment',
        blank=True

    )
    illustration = models.ImageField(
        blank=True

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
    id = models.PositiveIntegerField(
        primary_key=True,
        unique=True,
        blank=False
    )
    number = models.CharField(
        unique=True,
        blank=True
    )

    client = models.ForeignKey(
        to='Client',
        blank=False,
        on_delete = models.DO_NOTHING
    )

    service = models.ForeignKey(
        to='Service',
        on_delete=models.DO_NOTHING
    )
    signed_date = models.DateField(
        verbose_name='Дата подписания'
    )

    completed = models.BooleanField(
        verbose_name='Закончен?',
        blank=False,
    )
    completed_date = models.DateField(
        verbose_name='Дата завершения'
    )

    equipment_required = models.ForeignKey(
        to='Equipment',
        on_delete=models.DO_NOTHING
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
        max_length=150
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        verbose_name='Email'
    )

    contact_number = models.CharField(
        max_length=12
    )


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.organization_name