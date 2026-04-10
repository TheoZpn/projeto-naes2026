from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

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

'''
class CampusUpdate(UdateView):
    model = Campus
    fields = ['nome']
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('index')
    extra_content ={
        'titulo': "editar dados do campus"
        'botao': "atualizar campus"
    }
'''

'''
class CampusDelete(DeleteView):
    model = Campus
    fields = ['nome']
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('index')
    extra_content ={
        'titulo': "deletar um campus"
        'botao': "sim, excluir"
    }
'''

'''
class CampusList(ListView):
    model = Campus
    template_name = 'campeonato/list.html'
'''

'''
class CampusDetail(DetailView):
    model = Campus
    template_name = 'campeonato/detail.html'
'''