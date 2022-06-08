from django.views import generic
from django.urls import reverse_lazy
from .models import Greeting

class IndexView(generic.ListView):
    template_name = 'greetings/index.html'
    context_object_name = 'greeting_list'

    def get_queryset(self):
        """Return the all greetings."""
        return Greeting.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'greetings/create.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index') 