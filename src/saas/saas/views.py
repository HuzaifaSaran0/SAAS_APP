from django.shortcuts import render, HttpResponse
from visits.models import Page_Visit


def home_page_view(request):
    # return HttpResponse("<h1>Home Page</h1>")
    queryset = Page_Visit.objects.all()
    my_title = "Home Page"
    my_context = {
        "title":my_title,
        "queryset":queryset
    }

    Page_Visit.objects.create()
    
    return render(request, 'home.html', my_context)


def base_page_view(request):
    return render(request, 'base.html', {})