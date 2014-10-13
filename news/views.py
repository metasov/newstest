from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, \
								logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from news.models import News, DeletedNews, User
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

PAGE_NEWS_COUNT = 5
ADJ_PAGES = 2

def login(request):
	form = AuthenticationForm(request = request,
							  data = request.POST or None)
	next = request.GET.get("next", "/")
	if request.user.is_authenticated():
		return HttpResponseRedirect(next)
	if form.is_valid():	
		user = form.get_user()
		auth_login(request, user)
		return HttpResponseRedirect(next)
	request.session.set_test_cookie()
	return render_to_response("login.html", RequestContext(request, {
		"form": form
	}))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

# Create your views here.
@login_required
def feed(request, page_num=None):
	page_num = page_num and int(page_num) or 1
	news = News.objects.all()
	p = Paginator(news, PAGE_NEWS_COUNT)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(p.num_pages)

	min_page = max(1, page_num - ADJ_PAGES)
	max_page = min(p.num_pages, page_num + ADJ_PAGES)
	pages_range = range(min_page, max_page + 1)

	return render_to_response("feed.html", RequestContext(request, {
		"page": page,
		"pages_range": pages_range
	}))

