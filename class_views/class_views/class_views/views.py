from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateAnimalForm
from .models import Animal, Publisher, Book, Author

variable_global = "Esto es un string global"

class MyView(View):
    necesita_self = "Esto es un string en la clase"
    variable_en_clase = "Este contenido no saldrá en la respuesta"
    def get(self, request):
        no_necesita_self = "Esto es un string en el método"
        return HttpResponse(f"{variable_global}. {self.necesita_self}. {no_necesita_self}. {self.variable_en_clase}.")

class SubClaseView(MyView):
    variable_en_clase = "String desde subclase"
    def get(self, request):
        return HttpResponse(f"Hola desde subclase.")
    
# Ejemplo con animales y perros y gatos
class AnimalListView(generic.ListView):
    model = Animal
    template_name = 'animal.html'
    context_object_name = 'animals'
    def get_queryset(self):
        """Retornamos los Animales de la bbdd"""
        return Animal.objects.all().values()
    
class AnimalView(View):
    animal = "Animal"
    sonido = "Sonido del animal"
    def get(self, request):
        return HttpResponse(f"{self.animal}: {self.sonido}")

class Perro(AnimalView):
    animal = "Perro"
    sonido = "Guau"

class Gato(AnimalView):
    animal = "Gato"
    sonido = "Miau"
        
# TODO: personalizar msg pasando param / args
class SuccessView(View):
    template_name = 'success.html'
    msg = "Formulario enviado correctamente."
    def get(self, request):
        return render(request, self.template_name, {'msg': self.msg})
# TODO: personalizar msg pasando param / args -> considerar si fusionar estas dos clases en una sola
class ErrorView(View):
    template_name = 'error.html'
    error = "Error al enviar el formulario. Vuelve a intertarlo."
    def get(self, request):
        return render(request, self.template_name, {'error': self.error})   
    
class CreateAnimalFormView(View):
    form_class = CreateAnimalForm
    initial = {'name': 'Thor'}
    template_name = 'create_animal.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('class_views:success'))
        else:
            return HttpResponseRedirect(reverse('class_views:error'))
        #return render(request, self.template_name, {'form': form})

# Ejemplo #3 con libros y autores y editoriales
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/

# Vista de listado de Publishers
class PublisherListView(ListView):
    model = Publisher
    template_name = 'publishers.html'
    context_object_name = 'publishers'

# Vista de detalle de un Publisher
class PublisherDetailView(DetailView):

    model = Publisher
    template_name = 'publisher.html'
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all() # TODO: filtrar por publisher
        return context