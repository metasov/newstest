from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import News, DeletedNews, User
from django.core.paginator import Paginator, EmptyPage

PAGE_NEWS_COUNT = 5

# Create your views here.
@login_required
def feed(request, page_num=None):
	page_num = page_num or 1
	news = News.objects.all()
	p = Paginator(news, PAGE_NEWS_COUNT)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(p.num_pages)

	result = "<br/>\n".join([ "%(title)s(%(description)s)" % page.object_list])

	return HttpResponse(result)
