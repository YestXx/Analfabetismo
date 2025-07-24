from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import (
    Usuario, Perfil, Cargo, Avaliacao, Aula,
    Exercicio, Resultado, Progresso,
    Mensagem, Notificacao, Trilha
)
from .forms import (
    UsuarioForm, PerfilForm, CargoForm, AvaliacaoForm,
    AulaForm, ExercicioForm, ResultadoForm, ProgressoForm,
    MensagemForm, NotificacaoForm, TrilhaForm
)


# ====================================================
# Dashboard / Home: mostra resumo de Trilhas e Progresso
# ====================================================
class DashboardView(View):
    def get(self, request):
        trilhas = Trilha.objects.all()
        if request.user.is_authenticated:
            progresso = Progresso.objects.filter(usuario=request.user).first()
        else:
            progresso = None
        return render(request, 'dashboard.html', {
            'trilhas': trilhas,
            'progresso': progresso
        })


# ============================
# CRUD de Trilhas de Aprendiz.
# ============================
class TrilhasView(View):
    template = 'trilhas.html'

    def get(self, request):
        trilhas = Trilha.objects.all()
        form = TrilhaForm()
        return render(request, self.template, {'trilhas': trilhas, 'form': form})

    def post(self, request):
        form = TrilhaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trilha criada com sucesso!')
        else:
            messages.error(request, 'Erro ao criar trilha.')
        return redirect('trilhas')


# ======================
# CRUD de Aulas
# ======================
class AulasView(View):
    template = 'aulas.html'

    def get(self, request):
        aulas = Aula.objects.all()
        form = AulaForm()
        return render(request, self.template, {'aulas': aulas, 'form': form})

    def post(self, request):
        form = AulaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aula salva com sucesso!')
        else:
            messages.error(request, 'Corrija os erros antes de salvar.')
        return redirect('aulas')


class EditarAulaView(View):
    template = 'editar_aula.html'

    def get(self, request, pk):
        aula = get_object_or_404(Aula, pk=pk)
        form = AulaForm(instance=aula)
        return render(request, self.template, {'aula': aula, 'form': form})

    def post(self, request, pk):
        aula = get_object_or_404(Aula, pk=pk)
        form = AulaForm(request.POST, request.FILES, instance=aula)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aula atualizada!')
            return redirect('editar_aula', pk=pk)
        messages.error(request, 'Corrija os erros no formulário.')
        return render(request, self.template, {'aula': aula, 'form': form})


# ======================
# CRUD de Exercícios
# ======================
class ExerciciosView(View):
    template = 'exercicios.html'

    def get(self, request):
        exercicios = Exercicio.objects.select_related('aula').all()
        form = ExercicioForm()
        return render(request, self.template, {'exercicios': exercicios, 'form': form})

    def post(self, request):
        form = ExercicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercício criado com sucesso!')
        else:
            messages.error(request, 'Corrija os erros antes de criar.')
        return redirect('exercicios')


# ================================
# Registrar Resultado de Exercício
# ================================
class ResultadoView(View):
    template = 'resultados.html'

    def get(self, request):
        resultados = Resultado.objects.filter(usuario=request.user)
        form = ResultadoForm(initial={'usuario': request.user})
        return render(request, self.template, {'resultados': resultados, 'form': form})

    def post(self, request):
        form = ResultadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resultado registrado!')
        else:
            messages.error(request, 'Erro ao registrar resultado.')
        return redirect('resultados')


# ================================
# Progresso do Usuário
# ================================
class ProgressoView(View):
    template = 'progresso.html'

    def get(self, request):
        progresso = get_object_or_404(Progresso, usuario=request.user)
        return render(request, self.template, {'progresso': progresso})


# ================================
# Mensagens (Chat) com Educadores
# ================================
class MensagensView(View):
    template = 'mensagens.html'

    def get(self, request):
        mensagens = Mensagem.objects.filter(
            destinatario=request.user
        ).select_related('remetente')
        form = MensagemForm(initial={'remetente': request.user})
        return render(request, self.template, {'mensagens': mensagens, 'form': form})

    def post(self, request):
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada!')
        else:
            messages.error(request, 'Erro ao enviar mensagem.')
        return redirect('mensagens')


# ======================================
# Notificações Motivacionais
# ======================================
class NotificacoesView(View):
    template = 'notificacoes.html'

    def get(self, request):
        notifs = Notificacao.objects.filter(usuario=request.user)
        return render(request, self.template, {'notificacoes': notifs})


# ======================================
# Perfil e Cargo (somente CRUD admin-like)
# ======================================
class PerfisView(View):
    template = 'perfis.html'

    def get(self, request):
        perfis = Perfil.objects.all()
        form = PerfilForm()
        return render(request, self.template, {'perfis': perfis, 'form': form})

    def post(self, request):
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil criado!')
        else:
            messages.error(request, 'Erro ao criar perfil.')
        return redirect('perfis')


class CargosView(View):
    template = 'cargos.html'

    def get(self, request):
        cargos = Cargo.objects.all()
        form = CargoForm()
        return render(request, self.template, {'cargos': cargos, 'form': form})

    def post(self, request):
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo criado!')
        else:
            messages.error(request, 'Erro ao criar cargo.')
        return redirect('cargos')
