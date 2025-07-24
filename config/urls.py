from django.contrib import admin
from django.urls import path
from app.views import DashboardView, TrilhasView, AulasView, EditarAulaView, ExerciciosView, ResultadoView, ProgressoView, MensagensView, NotificacoesView, PerfisView, CargosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('trilhas/', TrilhasView.as_view(), name='trilhas'),
    path('aulas/', AulasView.as_view(), name='aulas'),
    path('aulas/<int:pk>/editar/', EditarAulaView.as_view(), name='editar_aula'),
    path('exercicios/', ExerciciosView.as_view(), name='exercicios'),
    path('resultados/', ResultadoView.as_view(), name='resultados'),
    path('progresso/', ProgressoView.as_view(), name='progresso'),
    path('mensagens/', MensagensView.as_view(), name='mensagens'),
    path('notificacoes/', NotificacoesView.as_view(), name='notificacoes'),
    path('perfis/', PerfisView.as_view(), name='perfis'),
    path('cargos/', CargosView.as_view(), name='cargos'),
]