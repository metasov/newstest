from __future__ import unicode_literals
from django.contrib import admin
from news.models import News, DeletedNews, User
from news.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class NewsUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'password1', 'password2'),
		}),
	)
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('username', 'email', 'is_staff')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
	search_fields = ('username', 'email')
	ordering = ('email',)
	filter_horizontal = ('groups', 'user_permissions',)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'creation_date', 'publication_date')
	search_fields = ('title', )

# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(DeletedNews)
admin.site.register(User, NewsUserAdmin)