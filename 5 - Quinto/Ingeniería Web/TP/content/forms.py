from .models import Content, Section, LISTS_SECTION_NAME, Tag
from django import forms
from django.forms import TextInput, Textarea, Select, CheckboxInput, SelectMultiple

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            label='Título',
                            widget=TextInput(attrs={'class': 'form-control'}),
                            error_messages={'required': 'Debes ingresar un título.',},
                            required=True)

    section = forms.ModelChoiceField(queryset=Section.objects.exclude(name=LISTS_SECTION_NAME),
                                      empty_label=None,
                                      label='Sección',
                                      required=True,
                                      widget=Select(attrs={'class':'form-control'}),
                                      error_messages={ 'required': 'Debes elegir una sección.' })

    published = forms.BooleanField(required=False,
                                   widget=CheckboxInput(),
                                   label='Publicado',
                                   help_text='<br><small>Nota: si no se selecciona esta opción, el post será guardado, pero no visible para los demás usuarios.</small>')

    tags = forms.CharField(label='Tags',
                           widget=SelectMultiple(attrs={'class': 'form-control',
                                                        'id': 'tagsinput'},),
                           help_text='<small>Nota: utilizá la tecla "enter" para confirmar los tags. Podés ingresar hasta 10.</small>',
                           required=False)

    items = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'items-list'}, ),
                            required=False)

    item_input = forms.CharField(label='Contenido Relacionado',
                                 widget=TextInput(attrs={'class': 'form-control itemInput'}, ),
                                 help_text='<small>Nota: comenzá a escribir el nombre de la película o serie y seleccioná la que desees para añadirla a la lista.</small>',
                                 required=False)

    class Meta:
        model = Content
        fields = ['title', 'section', 'description', 'published', 'tags',]
        widgets = {
            'description': Textarea(attrs={'id': 'summernote'}),
        }

        labels = {
            'description': 'Contenido',
        }

        error_messages = {
            'description': {
                'required': 'Debes ingresar contenido.',
            },
        }

    def clean_tags(self):
        data = ','.join([tag.replace(',', '') for tag in self.data.getlist('tags')])

        return data

class CommentForm(forms.ModelForm):
    response_to_id = forms.IntegerField(widget=forms.HiddenInput(),
                                        required=False)

    class Meta:
        model = Content
        fields = ['description',]
        widgets = {
            'description': Textarea(attrs={'id': 'summernote'}),
        }

        labels = {
            'description': 'Comentario',
        }

        error_messages = {
            'description': {
                'required': 'Debes ingresar un comentario. No rompas los huevos, si no.',
            },
        }

class ListForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            label='Título',
                            widget=TextInput(attrs={'class': 'form-control'}),
                            error_messages={'required': 'Debes ingresar un título.',},
                            required=True)

    published = forms.BooleanField(required=False,
                                   widget=CheckboxInput(),
                                   label='Publicado',
                                   help_text='<br><small>Nota: si no se selecciona esta opción, la lista será guardada, pero no visible para los demás usuarios.</small>')

    tags = forms.CharField(label='Tags',
                           widget=SelectMultiple(attrs={'class': 'form-control',
                                                        'id': 'tagsinput'},),
                           help_text='<small>Nota: utilizá la tecla "enter" para confirmar los tags. Podés ingresar hasta 10.</small>',
                           required=False)

    items = forms.CharField(widget=forms.HiddenInput(attrs={'id':'items-list'},),
                            required=False,)

    item_input = forms.CharField(label='Elementos de la lista',
                                 widget=TextInput(attrs={'class': 'form-control itemInput'}, ),
                                 help_text='<small>Nota: comenzá a escribir el nombre de la película o serie y seleccioná la que desees para añadirla a la lista.</small>',
                                 required=False)

    class Meta:
        model = Content
        fields = ['title', 'description', 'published', 'tags',]
        widgets = {
            'description': Textarea(attrs={'rows': '4',
                                           'class': 'form-control'}),
        }

        labels = {
            'description': 'Descripción',
        }

        error_messages = {
            'description': {
                'required': 'Debes ingresar una descripción.',
            },
        }

    def clean_tags(self):
        data = ','.join([tag.replace(',', '') for tag in self.data.getlist('tags')])

        return data

    def clean(self):
        if 'items' not in self.cleaned_data.keys() or not self.cleaned_data['items']:
            raise forms.ValidationError("La lista debe contener, al menos, una película o serie.")

        return self.cleaned_data