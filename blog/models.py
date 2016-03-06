from django.db import models
from django.utils import timezone

class Post(models.Model): #функцией class задаём объект Post (имя можно менять), про который указываем, что это модель Django
	author = models.ForeignKey('auth.User') #Ссылка на другую модель
	title = models.CharField(max_length=200) #models.CharField - текстовое поле с ограниченным количеством знаков
	text = models.TextField() #текстовое поле без ограничения знаков
	create_date = models.DateTimeField( #дата и время
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	
	def publish(self): #создаем метод - publish; self - это он обращается сам к себе
		self.published_date = timezone.now()
		self.save()
	def __str__(self): #метод для вызывания строки
		return self.title


