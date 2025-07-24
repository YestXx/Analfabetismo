from django.contrib import admin
from .models import Usuario, Perfil, Cargo, Avaliacao, Aula, Exercicio, Resultado, Progresso, Mensagem, Notificacao, Trilha

class ExercicioInline(admin.TabularInline):
    model = Exercicio
    extra = 1

class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_atividade')
    search_fields = ('titulo', 'conteudo')
    inlines = [ExercicioInline]

class ResultadoInline(admin.TabularInline):
    model = Resultado
    extra = 1

class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('aula', 'tipo_exercicio', 'nivel')
    search_fields = ('texto',)
    inlines = [ResultadoInline]

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class ProgressoInline(admin.TabularInline):
    model = Progresso
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'idade', 'cidade', 'escolaridade')
    search_fields = ('username', 'email', 'cidade')
    inlines = [AvaliacaoInline, ProgressoInline]

class MensagemAdmin(admin.ModelAdmin):
    list_display = ('remetente', 'destinatario', 'timestamp')
    search_fields = ('mensagem',)
    list_filter = ('timestamp',)

class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'data_hora')
    search_fields = ('mensagem',)
    list_filter = ('tipo', 'data_hora')

class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    search_fields = ('nome', 'nivel')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('descricao_perfil',)
    search_fields = ('descricao_perfil',)

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'descricao_cargo')
    search_fields = ('nome_cargo',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Avaliacao)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Exercicio, ExercicioAdmin)
admin.site.register(Resultado)
admin.site.register(Progresso)
admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(Notificacao, NotificacaoAdmin)
admin.site.register(Trilha, TrilhaAdmin)
