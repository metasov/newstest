from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from django.core import validators

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_("email address"), blank=False, unique=True,
		help_text=_('Required'))
	username = models.CharField(_('username'), max_length=30, unique=True,
		help_text=_('30 characters or fewer. Letters, digits and '
					'@/./+/-/_ only.'),
		validators=[
			validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
		])
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into this admin '
					'site.'))
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as '
					'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email], **kwargs)


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