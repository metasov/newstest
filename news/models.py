from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
from django.conf import settings

# Create your models here.
class News(models.Model):
	title = models.CharField("Title", max_length=120)
	description = models.TextField("Description")
	creation_date = models.DateField("Creation Date", default=date.today)
	publication_date = models.DateField("Publication Date", default=date.today)
	order = models.IntegerField("Order", default=1)
	class Meta:
		ordering = ('order', )
		verbose_name = "News"
		verbose_name_plural = "News"

	def __unicode__(self):
		return self.title

class DeletedNews(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="deleted_news")
	news = models.ForeignKey(News, related_name="users_deleted")
	class Meta:
		verbose_name = "Deleted News"
		verbose_name_plural = "Deleted News"
	def __unicode__(self):
		return "%s <--> %s" % (self.user.email, self.news.title)