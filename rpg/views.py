from django.views.generic import CreateView

#busca a rota da url pelo name dela
from django.views import reverse_lazy

#from .models import # aí tu coloca as classes aqui, tipo Jogador, Campus, etc

#exemplo de class
'''
class CampusCreate(CreateView):
    model = Campus
    fields = ['nome']
    template_name = 'campeonato/form.html'(ainda n tem o html)
    success_url = reverse_lazy('index(pagina inicial)')
'''