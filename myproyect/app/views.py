from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("index.html")
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request,))

def test(request):
    return HttpResponse("Ësto es un test")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")    
    return render(request, 'app/detail.html', {'question': question})   
    #return HttpResponse("Estás viendo la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Va a votar sobre la pregunta %s." % question_id)
