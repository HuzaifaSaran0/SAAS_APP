from django.shortcuts import render, HttpResponse
from visits.models import Page_Visit


def home_page_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Home Page</h1>")
    return about_page_view(request, *args, **kwargs)


def about_page_view(request, *args, **kwargs):
    queryset = Page_Visit.objects.all()
    my_title = "Home Page"
    page_qs = Page_Visit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() / queryset.count()) * 100
    except:
        percent = 0
    html_template = "home.html"
    my_context = {
        "title":my_title,   
        "percent":percent,
        "page_visit_count":page_qs.count(),
        "total_visit_count":queryset.count(),

    }

    Page_Visit.objects.create(path=request.path)
    
    return render(request, html_template, my_context)


def base_page_view(request):
    return render(request, 'base.html', {})