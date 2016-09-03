from __future__ import unicode_literals

# Create your models here.

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify




CATEGORIES = (
	('WDP', 'Wordpress'),
	('DJO', 'Django'),
	('BLG', 'Blogging'),
	('AFF', 'Affiliate Marketing'),
	('LSY', 'Lifestyle'),
	('TVL', 'Travel'),
	('RCS', 'Resources'),
	)

class Post(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	category    = models.CharField(max_length=3, choices=CATEGORIES, default='BLG',)
	text = models.TextField()
	cover_image = models.ImageField(upload_to='documents/%Y/%m/%d')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	published = models.BooleanField(default=False, verbose_name='Publish this post')
	slug = models.SlugField(max_length=200, unique=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

