# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    idade = models.PositiveIntegerField(verbose_name="Idade", null=True, blank=True)
    cidade = models.CharField(max_length=100, verbose_name="Cidade", null=True, blank=True)
    escolaridade = models.CharField(max_length=100, verbose_name="Escolaridade", null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='perfil/', verbose_name="Foto de Perfil", null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='grupos',
        blank=True,
        related_name='usuarios_custom',
        related_query_name='usuario_custom'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='permissões do usuário',
        blank=True,
        related_name='usuarios_custom_perms',
        related_query_name='usuario_custom_perms'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Perfil(models.Model):
    descricao_perfil = models.CharField(max_length=50, verbose_name="Descrição do perfil")

    def __str__(self):
        return self.descricao_perfil

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=50, verbose_name="Nome do cargo")
    descricao_cargo = models.TextField(verbose_name="Descrição do cargo")

    def __str__(self):
        return self.nome_cargo

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nivel_inicial = models.CharField(max_length=50, verbose_name="Nível inicial")
    data = models.DateField(auto_now_add=True, verbose_name="Data da avaliação")

    def __str__(self):
        return f"Avaliação de {self.usuario} - {self.nivel_inicial}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Aula(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título da aula")
    conteudo = models.TextField(verbose_name="Conteúdo da aula")
    midia = models.FileField(upload_to='aulas/', verbose_name="Mídia da aula", null=True, blank=True)
    tipo_atividade = models.CharField(max_length=50, verbose_name="Tipo de atividade")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"

class Exercicio(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, verbose_name="Aula")
    texto = models.TextField(verbose_name="Texto do exercício")
    audio = models.FileField(upload_to='exercicios/audio/', verbose_name="Áudio do exercício", null=True, blank=True)
    tipo_exercicio = models.CharField(max_length=50, verbose_name="Tipo de exercício")
    nivel = models.CharField(max_length=50, verbose_name="Nível do exercício")

    def __str__(self):
        return f"Exercício {self.id} - {self.aula.titulo}"

    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"

class Resultado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, verbose_name="Exercício")
    acerto = models.BooleanField(verbose_name="Acertou?")
    tempo_resposta = models.IntegerField(verbose_name="Tempo de resposta (segundos)")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data do resultado")

    def __str__(self):
        return f"Resultado de {self.usuario} - {self.exercicio}"

    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"

class Progresso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nivel_atual = models.CharField(max_length=50, verbose_name="Nível atual")
    percentual_conclusao = models.FloatField(verbose_name="Percentual de conclusão")
    data_ultima_atividade = models.DateTimeField(auto_now=True, verbose_name="Última atividade")

    def __str__(self):
        return f"Progresso de {self.usuario}"

    class Meta:
        verbose_name = "Progresso"
        verbose_name_plural = "Progressos"

class Mensagem(models.Model):
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mensagens_enviadas", verbose_name="Remetente")
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mensagens_recebidas", verbose_name="Destinatário")
    mensagem = models.TextField(verbose_name="Mensagem")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora")

    def __str__(self):
        return f"{self.remetente} -> {self.destinatario}: {self.mensagem[:20]}..."

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    tipo = models.CharField(max_length=50, verbose_name="Tipo de notificação")
    mensagem = models.TextField(verbose_name="Mensagem da notificação")
    data_hora = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora")

    def __str__(self):
        return f"Notificação para {self.usuario} - {self.tipo}"

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"

class Trilha(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da trilha")
    nivel = models.CharField(max_length=50, verbose_name="Nível da trilha")
    descricao = models.TextField(verbose_name="Descrição da trilha")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Trilha"
        verbose_name_plural = "Trilhas"