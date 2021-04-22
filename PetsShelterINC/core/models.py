from django.db import connections
from django.db import models


# Таблица с животными.
class Pets(models.Model):
    idpet = models.AutoField('Id_pet', primary_key=True)
    pet_name = models.CharField('Имя животного', max_length=100)
    Status = (
        ('Ищет дом', 'Ищет дом'),
        ('Нашел дом', 'Нашел дом'),
    )
    pet_status = models.CharField('Статус животного', max_length=45, choices=Status)
    Gender = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    pet_gender = models.CharField('Пол', max_length=10, choices=Gender)
    pet_age = models.CharField('Возраст', max_length=100)
    Vac = (
        ('Да', 'Да'),
        ('Частично', 'Частично'),
        ('Нет', 'Нет'),
    )
    pet_vaccination = models.CharField('Вакцинация', max_length=10, choices=Vac)
    Ste = (
        ('Да', 'Да'),
        ('Частично', 'Частично'),
        ('Нет', 'Нет'),
    )
    pet_sterilization = models.CharField('Стерилизация', max_length=10, choices=Ste)
    pet_toilet = models.CharField('Приучен к туалету', max_length=25, blank=True)
    Size = (
        ('Крошечный', 'Крошечный'),
        ('Небольшой', 'Небольшой'),
        ('Средний', 'Средний'),
        ('Крупный', 'Крупный'),
    )
    pet_size = models.CharField('Размер', max_length=15, choices=Size)
    pet_type = models.CharField('Тип', max_length=100)
    pet_breed = models.CharField('Порода', max_length=100)
    wool_length = (
        ('Короткая', 'Короткая'),
        ('Средняя', 'Средняя'),
        ('Длинная', 'Длинная'),
    )
    pet_wool_length = models.CharField('Длина шерсти', max_length=100, choices=wool_length)
    pet_wool_color = models.CharField('Цвет шерсти', max_length=100)
    pet_weight = models.CharField('Вес', max_length=50)
    pet_health = models.CharField('Здоровье', max_length=100)
    pet_privicies = models.CharField('Особенности', max_length=100, blank=True)
    pet_temperament = models.CharField('Темперамент', max_length=30)
    pet_human_centred = models.CharField('Ориентированность на людей', max_length=30, blank=True)
    pet_attitude_chlidren = models.CharField('Ориентированность на детей', max_length=30, blank=True)
    pet_attitude_cat = models.CharField('Ориентированность на котов', max_length=30, blank=True)
    pet_attitude_other_pets = models.CharField('Ориентированность на других собак', max_length=30, blank=True)
    pet_keeping = models.CharField('Содержание', max_length=50, blank=True)
    pet_live_in_apartment = models.CharField('Приучен к жизни в квартире', max_length=20, blank=True)
    pet_accustomed_to_a_leash = models.CharField('Приучен к поводку', max_length=20, blank=True)
    pet_training = models.CharField('Приучен к дрессировкам', max_length=20, blank=True)
    pet_location = models.CharField('Место нахождения', max_length=45)
    contact_idcontact = models.IntegerField('Контакты')
    shelter_idshelter = models.IntegerField('Номер приюта')
    petImagePath = models.ImageField('Фото животного', upload_to='Pets_images')

    class Meta:
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'
        db_table = "pet"


# Таблица с контактами.
class Contact(models.Model):
    idcontact = models.AutoField('Id_contact', primary_key=True)
    contact_mane = models.CharField('Имя', max_length=45)
    contact_phone = models.CharField('Номер телефона', max_length=45)
    contact_email = models.CharField('Email', max_length=45, blank=True)
    contact_two_name = models.CharField('Запасное Имя', max_length=45, blank=True)
    contact_two_phone = models.CharField('Запасной номер телефона', max_length=45, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        db_table = "contact"
