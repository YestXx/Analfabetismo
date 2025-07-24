# forms.py
from django import forms
from .models import Usuario, Perfil, Cargo, Avaliacao, Aula, Exercicio, Resultado, Progresso, Mensagem, Notificacao, Trilha

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'idade', 'cidade', 'escolaridade', 'foto_perfil']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'escolaridade': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['descricao_perfil']
        widgets = {'descricao_perfil': forms.TextInput(attrs={'class': 'form-control'})}

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nome_cargo', 'descricao_cargo']
        widgets = {'nome_cargo': forms.TextInput(attrs={'class': 'form-control'}), 'descricao_cargo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})}

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nivel_inicial']
        widgets = {'nivel_inicial': forms.TextInput(attrs={'class': 'form-control'})}

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['titulo', 'conteudo', 'midia', 'tipo_atividade']
        widgets = {'titulo': forms.TextInput(attrs={'class': 'form-control'}), 'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), 'midia': forms.ClearableFileInput(attrs={'class': 'form-control-file'}), 'tipo_atividade': forms.TextInput(attrs={'class': 'form-control'})}

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['aula', 'texto', 'audio', 'tipo_exercicio', 'nivel']
        widgets = {'aula': forms.Select(attrs={'class': 'form-select'}), 'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), 'audio': forms.ClearableFileInput(attrs={'class': 'form-control-file'}), 'tipo_exercicio': forms.TextInput(attrs={'class': 'form-control'}), 'nivel': forms.TextInput(attrs={'class': 'form-control'})}

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['exercicio', 'acerto', 'tempo_resposta']
        widgets = {'exercicio': forms.Select(attrs={'class': 'form-select'}), 'acerto': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 'tempo_resposta': forms.NumberInput(attrs={'class': 'form-control'})}

class ProgressoForm(forms.ModelForm):
    class Meta:
        model = Progresso
        fields = ['nivel_atual', 'percentual_conclusao']
        widgets = {'nivel_atual': forms.TextInput(attrs={'class': 'form-control'}), 'percentual_conclusao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})}

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['destinatario', 'mensagem']
        widgets = {'destinatario': forms.Select(attrs={'class': 'form-select'}), 'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})}

class NotificacaoForm(forms.ModelForm):
    class Meta:
        model = Notificacao
        fields = ['tipo', 'mensagem']
        widgets = {'tipo': forms.TextInput(attrs={'class': 'form-control'}), 'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})}

class TrilhaForm(forms.ModelForm):
    class Meta:
        model = Trilha
        fields = ['nome', 'nivel', 'descricao']
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'}), 'nivel': forms.TextInput(attrs={'class': 'form-control'}), 'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})}
