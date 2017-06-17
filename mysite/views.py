

from django.shortcuts import render
# from django.template.loader import get_template
# from django.http import Http404, HttpResponse
# from django.template import Template, Context
import datetime



# def hello(request):
# 	return HttpResponse("Hello World!")

def hello(request):
	return render(request,"Hello World!")

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



