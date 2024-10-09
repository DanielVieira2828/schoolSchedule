from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        exclude = ['horas_atuais', 'cursos']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-white placeholder-gray-400',
                'placeholder': 'Ex: Carlos Alberto De Nobrega'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-white placeholder-gray-400',
                'placeholder': 'Ex: carlos.nobrega@fatec.sp.gov.br'
            }),
            'ra': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-white placeholder-gray-400',
                'placeholder': 'Ex: 42345-342'
            }),
            'disciplina': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-white placeholder-gray-400',
            }),
            'max_horas': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-white placeholder-gray-400',
            }),
            # 'disciplina': forms.Select(attrs={
            #     'class': 'w-full p-2 border border-gray-300 rounded-lg bg-transparent text-white',
            # }),
        }

class ProfessorEditarForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'ra', 'max_horas', 'horas_atuais', 'materias']
        exclude = ['horas_atuais']
        widgets = {
            'materias': forms.CheckboxSelectMultiple(),  # Exibe as matérias como checkboxes
        }