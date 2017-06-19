from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_lengh=30)
	address = models.CharField(max_lengh=50)
	city = model.CharField(max_lengh=60)
	state_province = models.CharField(max_lengh=30)
	country = models.CharField(max_lengh=50)
	website = models.URLField()

class Author(models.Model):
	first_name = models.CharField(max_lengh=30)
	last_name = models.CharField(max_lengh=40)
	email = models.EmailField()

class Book(models.Model):
	title = models.CharField(max_lengh=100)
	authors = models.ManyToMany(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()






