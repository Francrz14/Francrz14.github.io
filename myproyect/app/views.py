from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Devuelva las cinco últimas preguntas publicadas."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'
    def get_queryset(self):
        """
        Excluye las preguntas que aún no se han publicado.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Vuelve a mostrar el formulario de votación de preguntas.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "No seleccionaste una opción.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devuelve un HttpResponseRedirect después de tratar con éxito
        # con datos POST. Esto evita que los datos se publiquen dos veces si un
        # usuario pulsa el botón Atrás.
        return HttpResponseRedirect(reverse('app:results', args=(question.id,)))   
    #return HttpResponse("Va a votar sobre la pregunta %s." % question_id)
