

# from django.shortcuts import render
# # from django.template.loader import get_template
# from django.http import Http404, HttpResponse
# # from django.template import Template, Context
# import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail, get_connection


def hello(request):
	return HttpResponse("Welcome the Page at %s  %s  %s  %s." % (request.path,request.get_host(), request.get_full_path(), request.is_secure() ) )

# def hi(request):
# 	try:
# 		ua = request.META['HTTP_USER_AGENT']
# 	except KeyError:
# 		ua = 'unknown'
# 	return HttpResponse("Your browser is %s" % ua)


# def hi(request):
# 	ua = request.META.get('HTTP_USER_AGENT', 'unknown')
# 	return HttpResponse("Your browser is %s" % ua)

def hi(request):
	values = request.META
	html = []
	for k in sorted(values):
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
	return HttpResponse("<table>%s</table>" % '\n'.join(html))


# def hello(request):
# 	return render(request,"Hello World!")

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	html = "<html><body>It is now %s</body></html>" % now
# 	return HttpResponse(html)

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	t = Template("<html><body>It is now {{ current_date }}.</body></html>")
# 	html = t.render(Context({'current_date': now}))
# 	return HttpResponse(html)

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	t = get_template('current_datetime.html')
# 	html = t.render({'current_date': now})
# 	return HttpResponse(html)

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	return render(request, 'current_datetime.html', {'current_date': now })

def current_datetime(request):
	current_date = datetime.datetime.now()
	return render(request, 'current_datetime.html', locals())



# def hours_ahead(request, offset):
# 	try:
# 		offset = int(offset)
# 	except ValueError:
# 		raise Http404()
# 	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
# 	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
# 	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		hour_offset = int(offset)
	except ValueError:
		raise Http404()
	next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
	return render(request, 'hours_ahead.html', locals())

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'jasper.wj@foxmail.com'),
				['jasper.wang@163.com'],
				connection=con
			)
			# return HttpResponse('ABC')
			return HttpResponseRedirect('/contact/thanks')
	else:
		form = ContactForm()
	return render(request, 'contact_form.html', {'form': form})


def thanks(request):
	return HttpResponse("I don't know!")


# def display_meta(request):
# 	values = request.META
# 	html = []
# 	for k in sorted(values):
# 		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
# 	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def display_meta(request):
	values = request.META.items()
	# v = values
	#  v = sorted(values, reverse = False)
	v = sorted(values, key=lambda values:values[0])
	return render(request, 'display_meta.html', {'values': v})



