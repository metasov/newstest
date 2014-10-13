from __future__ import unicode_literals
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, \
								logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from news.models import News, DeletedNews, User
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from simplejson import dumps

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
	news = news.exclude(users_deleted__user=request.user)
	p = Paginator(news, PAGE_NEWS_COUNT)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(p.num_pages)

	min_page = max(1, page_num - ADJ_PAGES)
	max_page = min(p.num_pages, page_num + ADJ_PAGES)
	pages_range = range(min_page, max_page + 1)

	if request.is_ajax():
		response = {
			"news": [],
			"pagination": ""
		}
		tmpl = loader.get_template("news_li.html")
		cntx = RequestContext(request, {
			"page": page,
			"pages_range": pages_range,
			"news": None,
		})
		for news in page.object_list:
			cntx["news"] = news
			response["news"].append(tmpl.render(cntx))
		tmpl = loader.get_template("pagination.html")
		response["pagination"] = tmpl.render(cntx)
		return HttpResponse(dumps(response), content_type="application/json")
	else:
		return render_to_response("feed.html", RequestContext(request, {
			"page": page,
			"pages_range": pages_range
		}))


@login_required
def news_page(request, news_id):
	news = get_object_or_404(News, id=news_id)
	back = request.GET.get("back", "/")
	return render_to_response("news.html", RequestContext(request, {
		"news": news,
		"back": back
	}))

@login_required
def remove(request, news_id):
	news = get_object_or_404(News, id=news_id)
	next = request.GET.get("next", "/")
	if not request.is_ajax():
		if not request.method == "POST":
			return render_to_response("remove_form.html", RequestContext(request, {
				"news": news,
				"next": next
			}))

		if request.POST.get("submit", "No") != "Yes":
			return HttpResponseRedirect(next)
	try:
		dn = DeletedNews.objects.get(user = request.user,
									 news = news)
	except DeletedNews.DoesNotExist:
		DeletedNews(user = request.user, news = news).save()
	if not request.is_ajax():
		return HttpResponseRedirect(next)
	else:
		return HttpResponse(dumps({'success': True}))
		