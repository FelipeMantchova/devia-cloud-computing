from django.http import HttpResponse

def home(request):
    return HttpResponse("Nome: Felipe Mantovanelli Barros. Disciplina: Cloud Computing & Site Reliability Engineering")