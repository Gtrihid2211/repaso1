from django import forms
from django.core.exceptions import ValidationError


class FechasForm(forms.Form):
    fecha_inicio = forms.DateField(input_formats=['%d/%m/%Y'],help_text='Formato: dd/mm/yyyy')
    fecha_fin = forms.DateField(input_formats=['%d/%m/%Y'],help_text='Formato: dd/mm/yyyy')

    dias_semana = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miercoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sabado'),
        ('domingo', 'Domingo'),
    ]
    dias = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     choices=dias_semana,
                                     help_text='Selecciona los días de la semana')
    email = forms.EmailField(help_text='Introduce tu dirección de correo electrónico')

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        dias = cleaned_data.get('dias')
        email = cleaned_data.get('email')

        # Validación 1: fecha final es igual o superior a la fecha de inicio
        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise ValidationError('La fecha de inicio debe ser anterior a la fecha de fin.')

        # Validación 2: al menos un día de la semana debe ser seleccionado
        if not dias:
            raise ValidationError('Selecciona al menos un día de la semana.')

        # Validación 3: no se han seleccionado más de tres días
        if len(dias) > 3:
            raise ValidationError('Selecciona como máximo tres días de la semana.')

        # Validación 4: el correo electrónico pertenece a la organización @iesmartinezm.es
        if email and not email.endswith('@iesmartinezm.es'):
            raise ValidationError('El correo electrónico debe ser del dominio "iesmartinezm.es".')

        return cleaned_data






