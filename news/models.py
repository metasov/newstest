from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
	title = models.CharField("Title", max_length=120)
	description = models.TextField("Description")
	creation_date = models.DateField("Creation Date", default=date.today)
	publication_date = models.DateField("Publication Date", default=date.today)
	order = models.IntegerField("Order", default=1)
	class Meta:
		ordering = ('order', )

class DeletedNews(models.Model):
	user = models.ForeignKey(User, related_name="deleted_news")
	news = models.ForeignKey(News, related_name="users_deleted")
