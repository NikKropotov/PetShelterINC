from datetime import datetime

from django.utils.timezone import now
from django.utils import timezone
from django.db import models
from django.urls import reverse


# Таблица с контактами.
class Contact(models.Model):
    idcontact = models.AutoField('Id Контакта', primary_key=True)
    contact_name = models.CharField('Имя', max_length=45)
    contact_phone = models.CharField('Номер телефона', max_length=20)
    contact_email = models.CharField('Email', max_length=45, blank=True, default=None)
    contact_two_name = models.CharField('Запасное Имя', max_length=45, blank=True, default=None)
    contact_two_phone = models.CharField('Запасной номер телефона', max_length=20, blank=True, default=None)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        db_table = "contact"

    def __str__(self):
        return self.contact_name


class Shelters(models.Model):
    idshelter = models.AutoField('Id Приюта', primary_key=True)
    Places = (
        ('Муниципальный приют', 'Муниципальный приют'),
        ('Частный приют', 'Частный приют'),
    )
    shelter_place = models.CharField('Тип приюта', max_length=45, choices=Places, blank=True, default=None)
    shelter_name = models.CharField('Название приюта', max_length=45, blank=True, default=None)
    shelter_region = models.CharField('Регион', max_length=60, blank=True, default=None)
    shelter_city = models.CharField('Город', max_length=60)

    class Meta:
        verbose_name = 'Приюты'
        verbose_name_plural = 'Приюты'
        db_table = "shelter"

    def __str__(self):
        return self.shelter_name


# Таблица с породами.
class PetsBreed(models.Model):
    idpet_breed = models.AutoField('Id Породы', primary_key=True)
    breed = models.CharField('Порода', max_length=45)

    class Meta:
        ordering = ["idpet_breed"]
        verbose_name = 'Породы животных'
        verbose_name_plural = 'Породы животных'
        db_table = "pet_breed"

    def __str__(self):
        return self.breed


# Таблица с животными.
class Pets(models.Model):
    idpet = models.AutoField('Id Животного', primary_key=True)
    pet_name = models.CharField('Имя животного', max_length=100)
    Status = (
        ('Ищет дом', 'Ищет дом'),
        ('Нашел дом', 'Нашел дом'),
    )
    pet_status = models.CharField('Статус животного', max_length=15, choices=Status)
    Gender = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    pet_gender = models.CharField('Пол', max_length=10, choices=Gender)
    pet_age = models.CharField('Возраст', max_length=20)
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
    pet_toilet = models.CharField('Приучен к туалету', max_length=25, blank=True, default=None)
    Size = (
        ('Крошечный', 'Крошечный'),
        ('Небольшой', 'Небольшой'),
        ('Средний', 'Средний'),
        ('Крупный', 'Крупный'),
    )
    pet_size = models.CharField('Размер', max_length=15, choices=Size)
    pet_type = models.CharField('Тип', max_length=100)
    pet_breed = models.CharField('Порода', max_length=60)
    wool_length = (
        ('Короткая', 'Короткая'),
        ('Средняя', 'Средняя'),
        ('Длинная', 'Длинная'),
    )
    pet_wool_length = models.CharField('Длина шерсти', max_length=10, choices=wool_length)
    pet_wool_color = models.CharField('Цвет шерсти', max_length=50)
    pet_wool_color_extra = models.CharField('Дополнительный цвет шерсти', max_length=50, blank=True, default=None,
                                            null=True)
    pet_weight = models.CharField('Вес', max_length=25)
    pet_health = models.CharField('Здоровье', max_length=100)
    pet_privicies = models.TextField('Особенности', max_length=150, blank=True, default=None)
    pet_temperament = models.CharField('Темперамент', max_length=30)
    pet_human_centred = models.CharField('Ориентированность на людей', max_length=30, blank=True, default=None)
    pet_attitude_children = models.CharField('Ориентированность на детей', max_length=30, blank=True, default=None)
    pet_attitude_cat = models.CharField('Ориентированность на котов', max_length=30, blank=True)
    pet_attitude_other_pets = models.CharField('Ориентированность на других собак', max_length=30, blank=True,
                                               default=None)
    pet_keeping = models.CharField('Содержание', max_length=50, blank=True, default=None)
    pet_live_in_apartment = models.CharField('Приучен к жизни в квартире', max_length=20, blank=True, default=None)
    pet_accustomed_to_a_leash = models.CharField('Приучен к поводку', max_length=20, blank=True, default=None)
    pet_training = models.CharField('Приучен к дрессировкам', max_length=20, blank=True, default=None)
    pet_location = models.CharField('Место нахождения', max_length=45)
    contact_idcontact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    shelter_idshelter = models.ForeignKey(Shelters, on_delete=models.CASCADE)
    pet_breed_idpet_breed = models.ForeignKey(PetsBreed, on_delete=models.CASCADE)
    petImagePath = models.ImageField('Фото животного', upload_to='Pets_images')

    def get_absolute_url(self):
        return reverse('pets_detail', kwargs={'idpet': self.idpet})

    class Meta:
        verbose_name = 'Животные'
        verbose_name_plural = 'Животные'
        db_table = "pet"


class FoundPets(models.Model):
    idfound_pet = models.AutoField('Id Найденного животного', primary_key=True)
    found_pet_name = models.CharField('Кличка', max_length=45, default=None, blank=True)
    Status = (
        ('Найдена', 'Найдена'),
        ('Дома', 'Дома'),
    )
    found_pet_status = models.CharField('Статус животного', max_length=15, choices=Status, blank=True,
                                        default="Найдена")
    found_pet_color = models.CharField('Цвет шерсти', max_length=45, default=None)
    found_pet_breed = models.CharField('Порода', max_length=60, default=None, blank=True)
    found_pet_age = models.CharField('Примерный возраст', max_length=25, default=None, blank=True)
    Gender = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    found_pet_gender = models.CharField('Пол', max_length=10, default=None, blank=True, choices=Gender)
    Size = (
        ('Крошечный', 'Крошечный'),
        ('Небольшой', 'Небольшой'),
        ('Средний', 'Средний'),
        ('Крупный', 'Крупный'),
    )
    found_pet_size = models.CharField('Размер', max_length=15, choices=Size)
    found_pet_health = models.CharField('Состояние здоровья', max_length=70, default=None, blank=True)
    found_pet_found_datetime = models.DateTimeField('Дата и время нахождения', default=datetime.now)
    found_pet_found_location = models.CharField('Город', max_length=100, default=None)
    found_pet_description = models.TextField('Дополнительное описание', default=None, blank=True)
    found_contact_name = models.CharField('Имя', max_length=45, default=None)
    found_contact_phone = models.CharField('Номер телефона', max_length=20)
    found_contact_email = models.CharField('Email', max_length=45, blank=True, default=None)
    found_petImagePath = models.ImageField('Фото животного', upload_to='Found_Pets_images')

    def get_absolute_url(self):
        return reverse('found_pets_detail', kwargs={'idfound_pet': self.idfound_pet})

    class Meta:
        verbose_name = 'Найденные животные'
        verbose_name_plural = 'Найденные животные'
        db_table = "found_pet"


class LostPets(models.Model):
    idlost_pet = models.AutoField('Id Потерянного животного', primary_key=True)
    Status = (
        ('Пропала', 'Пропала'),
        ('Дома', 'Дома'),
    )
    lost_pet_status = models.CharField('Статус животного', max_length=15, choices=Status)
    lost_pet_name = models.CharField('Кличка', max_length=45, default=None)
    lost_pet_breed = models.CharField('Порода', max_length=60, default=None)
    Gender = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    lost_pet_gender = models.CharField('Пол', max_length=10, default=None, choices=Gender)
    lost_pet_age = models.CharField('Возраст', max_length=25, default=None)
    lost_pet_color = models.CharField('Цвет шерсти', max_length=45, default=None)
    Size = (
        ('Крошечный', 'Крошечный'),
        ('Небольшой', 'Небольшой'),
        ('Средний', 'Средний'),
        ('Крупный', 'Крупный'),
    )
    lost_pet_size = models.CharField('Размер', max_length=15, default=None, choices=Size)
    lost_pet_description = models.TextField('Описание', default=None, blank=True)
    lost_pet_lost_datetime = models.DateTimeField('Дата и время потери', default=datetime.now)
    lost_pet_lost_location = models.CharField('Место потери', max_length=80, default=None)
    lost_contact_name = models.CharField('Имя', max_length=45, default=None)
    lost_contact_phone = models.CharField('Номер телефона', max_length=20)
    lost_contact_email = models.CharField('Email', max_length=45, blank=True, default=None)
    lost_petImagePath = models.ImageField('Фото животного', upload_to='Lost_Pets_images')

    class Meta:
        verbose_name = 'Потерянные животные'
        verbose_name_plural = 'Потерянные животные'
        db_table = "lost_pet"


class Events(models.Model):
    idevent = models.AutoField('Id Мероприятия', primary_key=True)
    event_title = models.CharField('Название', max_length=45, default=None)
    event_datetime = models.DateTimeField('Дата и время мероприятия', default=None)
    event_location = models.CharField('Место мероприятия', max_length=80, default=None)
    event_person_count = models.CharField('Число человек', max_length=45, default=None, blank=True)
    event_director_full_name = models.CharField('ФИО Организатора', max_length=45, default=None)
    event_director_phone = models.CharField('Телефон Организатора', max_length=45, default=None)
    event_director_email = models.CharField('Email Организатора', max_length=45, default=None, blank=True)
    event_description = models.TextField('Дополнительное описание', max_length=400, default=None)

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'
        db_table = "event"
