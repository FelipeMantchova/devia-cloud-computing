from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World! Felipe com Docker! Trabalho 1")