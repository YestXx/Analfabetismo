from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import (
    Usuario, Perfil, Cargo, Avaliacao, Aula, Exercicio,
    Resultado, Progresso, Mensagem, Notificacao, Trilha
)

# Inlines para relacionamentos
class ExercicioInline(admin.TabularInline):
    model = Exercicio
    extra = 1

class ResultadoInline(admin.TabularInline):
    model = Resultado
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class ProgressoInline(admin.TabularInline):
    model = Progresso
    extra = 1

# Admin para o seu Usuario customizado
@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    # Campos exibidos na listagem
    list_display = ('username', 'email', 'idade', 'cidade', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Campos de busca
    search_fields = ('username', 'email', 'cidade')

    # Inlines para avaliações e progresso
    inlines = [AvaliacaoInline, ProgressoInline]

    # Agrupadores de campos nas páginas Add/Edit
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'idade', 'cidade', 'escolaridade', 'foto_perfil')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (  # para a página de criação de usuário
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

# Desregistre o Group se não quiser gerenciá-lo separado:
admin.site.unregister(Group)

# Registre os demais modelos com seus admins próprios
@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_atividade')
    search_fields = ('titulo', 'conteudo')
    inlines = [ExercicioInline]

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('aula', 'tipo_exercicio', 'nivel')
    search_fields = ('texto',)
    inlines = [ResultadoInline]

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('remetente', 'destinatario', 'timestamp')
    search_fields = ('mensagem',)
    list_filter = ('timestamp',)

@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'data_hora')
    search_fields = ('mensagem',)
    list_filter = ('tipo', 'data_hora')

@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    search_fields = ('nome', 'nivel')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('descricao_perfil',)
    search_fields = ('descricao_perfil',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'descricao_cargo')
    search_fields = ('nome_cargo',)

# Modelos sem customização extra
admin.site.register(Resultado)
admin.site.register(Avaliacao)
admin.site.register(Progresso)
