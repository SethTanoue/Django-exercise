# greetings/urls.py
from django.urls import path
from .import views

app_name = 'greetings'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]

class UpdateView(generic.edit.UpdateView):
    template_name = 'greetings/update.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index')
    
class DeleteView(generic.edit.DeleteView):
    template_name = 'greetings/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Greeting
    success_url = reverse_lazy('greetings:index')