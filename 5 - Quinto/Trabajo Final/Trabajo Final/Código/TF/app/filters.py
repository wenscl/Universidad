import django_filters as filters
from dal import autocomplete
from django import forms

from app.models import Acumula, Movimpu, Actividad, Imputaci, Tipoprov, \
    Provincias
from app.widgets import DatePickerInput


# class MensualFilter(filters.FilterSet):
#     inicio_periodo = filters.DateFilter(
#         field_name='periodo_contable', lookup_expr='gte',
#         widget=DatePickerInput(
#             attrs={'placeholder': 'Fecha Inicio (dd/mm/aaaa)'}))
#     fin_periodo = filters.DateFilter(
#         field_name='periodo_contable', lookup_expr='lte',
#         widget=DatePickerInput(
#             attrs={'placeholder': 'Fecha Fin (dd/mm/aaaa)'}))
#     inicio_comprobante = filters.DateFilter(
#         field_name='fecha_comprob', lookup_expr='gte',
#         widget=DatePickerInput(
#             attrs={'placeholder': 'Fecha Inicio (dd/mm/aaaa)'}))
#     fin_comprobante = filters.DateFilter(
#         field_name='fecha_comprob', lookup_expr='lte',
#         widget=DatePickerInput(
#             attrs={'placeholder': 'Fecha Fin (dd/mm/aaaa)'}))
#     tipo_movim = filters.ModelChoiceFilter(
#         field_name='tipo_movim', label='Tipo Movimiento',
#         queryset=TipoMovimiento.objects.all().order_by('descripcion'),
#         empty_label='Seleccionar')
#     proveedor = filters.ModelChoiceFilter(
#         field_name='cod_proveedor', label='Razón Social',
#         queryset=Proctcte.objects.all().order_by('razon_social'),
#         widget=autocomplete.ModelSelect2(
#             url='proveedor_autocomplete',
#             attrs={'data-placeholder': 'Seleccionar',
#                    'data-html': True,
#                    'data-theme': 'bootstrap4'}))
#     importe_min = filters.NumberFilter(
#         field_name='imp_total', label='Importe Mínimo', lookup_expr='gte',
#         widget=forms.TextInput(attrs={'placeholder': '$ Mínimo'}))
#     importe_max = filters.NumberFilter(
#         field_name='imp_total', label='Importe Máximo', lookup_expr='lte',
#         widget=forms.TextInput(attrs={'placeholder': '$ Máximo'}))
#     prefijo = filters.NumberFilter(widget=forms.TextInput())
#
#     class Meta:
#         model = Mensual
#         fields = ['inicio_periodo', 'fin_periodo', 'inicio_comprobante',
#                   'fin_comprobante', 'tipo_movim', 'tipo_comprob',
#                   'prefijo', 'proveedor', 'importe_min',
#                   'importe_max']
#
#     def __init__(self, *args, **kwargs):
#         super(MensualFilter, self).__init__(*args, **kwargs)
#         self.filters['tipo_movim'].field.label_from_instance = lambda \
#                 obj: obj.descripcion
#         self.filters['proveedor'].field.label_from_instance = lambda \
#                 obj: obj.razon_social


tipo_movim = Movimpu.objects.values('tipo_movim')\
        .distinct('tipo_movim').order_by('tipo_movim')
tipo_movim_choices = [(x['tipo_movim'], x['tipo_movim']) for x in tipo_movim]

descripcion = Movimpu.objects.values('descripcion')\
        .distinct('descripcion').order_by('descripcion')
descripcion_choices = [(x['descripcion'], x['descripcion']) for x in descripcion]


class PeriodoContableFilter(filters.FilterSet):
    inicio_periodo = filters.DateFilter(
        field_name='periodo_contable', lookup_expr='gte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    fin_periodo = filters.DateFilter(
        field_name='periodo_contable', lookup_expr='lte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))

    class Meta:
        model = Movimpu
        fields = ['inicio_periodo', 'fin_periodo']


class MovImpuFilter(filters.FilterSet):
    inicio_periodo = filters.DateFilter(
        field_name='periodo_contable', lookup_expr='gte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    fin_periodo = filters.DateFilter(
        field_name='periodo_contable', lookup_expr='lte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    inicio_comprobante = filters.DateFilter(
        field_name='fecha_comprob', lookup_expr='gte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    fin_comprobante = filters.DateFilter(
        field_name='fecha_comprob', lookup_expr='lte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    acumulador = filters.ModelChoiceFilter(
        field_name='cod_imput__donde_acumula',
        label='Acumulador',
        queryset=Acumula.objects.all().order_by('descripcion'),
        widget=autocomplete.ModelSelect2(
            url='imputacion_impu_acumulada_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['imputacion', 'tipo_movimiento', 'actividad',
                     'descripcion', 'tipo_proveedor', 'provincia']))
    imputacion = filters.ModelChoiceFilter(
        field_name='cod_imput', label='Imputación',
        queryset=Imputaci.objects.all().order_by('descripcion'),
        widget=autocomplete.ModelSelect2(
            url='imputacion_impu_simple_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador', 'tipo_movimiento', 'actividad',
                     'descripcion', 'tipo_proveedor', 'provincia']))
    tipo_movimiento = filters.ChoiceFilter(
        field_name='tipo_movim', label='Tipo Movimiento',
        choices=tipo_movim_choices,
        empty_label='Seleccionar',
        widget=autocomplete.ListSelect2(
            url='imputacion_tipo_movim_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador', 'imputacion', 'actividad',
                     'descripcion', 'tipo_proveedor', 'provincia']))
    actividad = filters.ModelChoiceFilter(
        field_name='actividad', label='Actividad',
        queryset=Actividad.objects.all().order_by('descripcion'),
        empty_label='Seleccionar',
        widget=autocomplete.ModelSelect2(
            url='imputacion_actividad_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador', 'imputacion',
                     'tipo_movimiento', 'descripcion', 'tipo_proveedor',
                     'provincia']))
    descripcion = filters.ChoiceFilter(
        field_name='descripcion', label='Descripción',
        choices=descripcion_choices,
        widget=autocomplete.ListSelect2(
            url='imputacion_descripcion_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador', 'imputacion',
                     'tipo_movimiento', 'actividad', 'tipo_proveedor',
                     'provincia']))
    tipo_proveedor = filters.ModelChoiceFilter(
        field_name='tipo_proveedor', label='Tipo Proveedor',
        queryset=Tipoprov.objects.all().order_by('descripcion'),
        empty_label='Seleccionar',
        widget=autocomplete.ModelSelect2(
            url='imputacion_tipo_proveedor_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador', 'imputacion',
                     'tipo_movimiento', 'actividad', 'descripcion',
                     'provincia']))
    importe_min = filters.NumberFilter(
        field_name='importe', label='Importe Mínimo', lookup_expr='gte',
        widget=forms.TextInput(attrs={'placeholder': '$ Mínimo'}))
    importe_max = filters.NumberFilter(
        field_name='importe', label='Importe Máximo', lookup_expr='lte',
        widget=forms.TextInput(attrs={'placeholder': '$ Máximo'}))

    class Meta:
        model = Movimpu
        fields = ['inicio_periodo', 'fin_periodo', 'inicio_comprobante',
                  'fin_comprobante', 'acumulador',
                  'imputacion', 'tipo_movimiento', 'actividad',
                  'descripcion', 'tipo_proveedor', 'importe_min', 'importe_max']

    def __init__(self, *args, **kwargs):
        super(MovImpuFilter, self).__init__(*args, **kwargs)
        self.filters['acumulador'].field.label_from_instance = \
            lambda obj: obj.descripcion
        self.filters['imputacion'].field.label_from_instance = lambda \
                obj: obj.descripcion
        self.filters['actividad'].field.label_from_instance = lambda \
                obj: obj.descripcion
        self.filters['descripcion'].field.label_from_instance = lambda \
                obj: obj.descripcion
        self.filters['tipo_proveedor'].field.label_from_instance = lambda \
                obj: obj.descripcion
        self.filters['tipo_movimiento'].field.label_from_instance = lambda \
                obj: obj.tipo_movim


impu_simple = Imputaci.objects.values('descripcion')\
        .distinct('descripcion').order_by('descripcion')
impu_simple_choices = [(x['descripcion'], x['descripcion']) for x in impu_simple]


class AcumulaFilter(filters.FilterSet):
    acumulador = filters.ModelChoiceFilter(
        field_name='donde_acumula', label='Acumulador',
        queryset=Acumula.objects.all().order_by('descripcion'),
        widget=autocomplete.ModelSelect2(
            url='acumula_impu_acumulada_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['imputacion']))
    imputacion = filters.ChoiceFilter(
        field_name='descripcion', label='Imputación',
        choices=impu_simple_choices,
        widget=autocomplete.ListSelect2(
            url='acumula_impu_simple_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador']))

    class Meta:
        model = Imputaci
        fields = ['acumulador', 'imputacion']

    def __init__(self, *args, **kwargs):
        super(AcumulaFilter, self).__init__(*args, **kwargs)
        self.filters['acumulador'].field.label_from_instance = \
            lambda obj: obj.descripcion
        self.filters['imputacion'].field.label_from_instance = lambda \
                obj: obj.descripcion


class ActividadFilter(filters.FilterSet):
    actividad = filters.ModelChoiceFilter(
        field_name='actividad', label='Actividad',
        queryset=Actividad.objects.all().order_by('descripcion'),
        empty_label='Seleccionar',
        widget=autocomplete.ModelSelect2(
            url='imputacion_actividad_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['acumulador', 'imputacion']))
    inicio_periodo = filters.DateFilter(
        field_name='periodo_contable', lookup_expr='gte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    fin_periodo = filters.DateFilter(
        field_name='periodo_contable', lookup_expr='lte',
        widget=DatePickerInput(
            attrs={'placeholder': 'dd/mm/aaaa'}))
    acumulador = filters.ModelChoiceFilter(
        field_name='cod_imput__donde_acumula',
        label='Acumulador',
        queryset=Acumula.objects.all().order_by('descripcion'),
        widget=autocomplete.ModelSelect2(
            url='imputacion_impu_acumulada_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['actividad', 'imputacion']))
    imputacion = filters.ModelChoiceFilter(
        field_name='cod_imput', label='Imputación',
        queryset=Imputaci.objects.all().order_by('descripcion'),
        widget=autocomplete.ModelSelect2(
            url='imputacion_impu_simple_autocomplete',
            attrs={'data-placeholder': 'Seleccionar',
                   'data-html': True,
                   'data-theme': 'bootstrap4'},
            forward=['actividad', 'acumulador']))

    class Meta:
        model = Movimpu
        fields = ['actividad', 'inicio_periodo', 'fin_periodo',
                  'acumulador', 'imputacion']

    def __init__(self, *args, **kwargs):
        super(ActividadFilter, self).__init__(*args, **kwargs)
        self.filters['actividad'].field.label_from_instance = lambda \
                obj: obj.descripcion
        self.filters['acumulador'].field.label_from_instance = \
            lambda obj: obj.descripcion
        self.filters['imputacion'].field.label_from_instance = lambda \
                obj: obj.descripcion


# class ProveedorFilter(filters.FilterSet):
#     razon_social = filters.ModelChoiceFilter(
#         field_name='cod_proveedor',
#         label='Razón Social', required=True,
#         queryset=Proctcte.objects.all(),
#         widget=autocomplete.ModelSelect2(
#             url='proveedor_autocomplete',
#             attrs={'data-placeholder': 'Seleccionar',
#                    'data-html': True,
#                    'data-theme': 'bootstrap4'}))
#     inicio_periodo = filters.DateFilter(
#         field_name='periodo_contable', lookup_expr='gte',
#         widget=DatePickerInput(
#             attrs={'placeholder': 'Fecha Inicio (dd/mm/aaaa)'}))
#     fin_periodo = filters.DateFilter(
#         field_name='periodo_contable', lookup_expr='lte',
#         widget=DatePickerInput(
#             attrs={'placeholder': 'Fecha Fin (dd/mm/aaaa)'}))
#
#     class Meta:
#         model = CtaCte
#         fields = ['razon_social', 'inicio_periodo', 'fin_periodo']
#
#     def __init__(self, *args, **kwargs):
#         super(ProveedorFilter, self).__init__(*args, **kwargs)
#         self.filters['razon_social'].field.label_from_instance = lambda \
#                 obj: obj.razon_social
