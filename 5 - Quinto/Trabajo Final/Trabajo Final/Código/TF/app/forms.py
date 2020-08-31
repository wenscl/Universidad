from django import forms

from app.widgets import MonthDatePickerInput


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Nombre de Usuario')
    password = forms.CharField(required=True, label='Contraseña',
                               widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, label='Nombre de Usuario')
    email = forms.CharField(required=True, label='Email')
    password = forms.CharField(required=True, label='Contraseña',
                               widget=forms.PasswordInput())

    def save(self, commit=True):
        # Guardar la contraseña suministrada hasheada.
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


IMPU_CHOICES = [
    ('periodo_contable', 'Periodo Contable'),
    ('fecha_comprob', 'Fecha Comprobante'),
    ('imputacion', 'Imputación'),
    ('num_comprob', 'Nro. Comprobante'),
    ('tipo_movim', 'Tipo Movimiento'),
    ('actividad', 'Actividad'),
    ('descripcion', 'Descripción'),
    ('tipo_proveedor', 'Tipo Cliente/Proveedor'),
    ('tipo', 'Tipo')]


class MovImpuForm(forms.Form):
    all = forms.BooleanField(required=False, label='Mostrar todas')
    visible_columns = forms.MultipleChoiceField(
        required=False,
        choices=IMPU_CHOICES,
        widget=forms.CheckboxSelectMultiple())


ACUMULA_CHOICES = [
    ('imputacion', 'Imputación'),
    ('compra_cta_cte', 'Compra Cta. Cte.'),
    ('compra_contado', 'Compra Contado'),
    ('nota_credito_recibida', 'Nota Crédito Recibida'),
    ('nota_debito_recibida', 'Nota Débito Recibida'),
    ('egresos_cta_cte', 'Egresos Cta. Cte.'),
    ('egresos_contado', 'Egresos Contado'),
    ('venta_cta_cte', 'Venta Cta. Cte.'),
    ('venta_contado', 'Venta Contado'),
    ('nota_credito_emitida', 'Nota Crédito Emitida'),
    ('nota_debito_emitida', 'Nota Débito Emitida'),
    ('cobranzas', 'Cobranzas'),
    ('unid_generadora', 'Unidad Generadora'),
    ('cuenta_gastos', 'Cuenta Gastos'),
    ('porcentaje', 'Porcentaje')]


class AcumulaForm(forms.Form):
    all = forms.BooleanField(required=False, label='Mostrar todas')
    visible_columns = forms.MultipleChoiceField(
        required=False,
        choices=ACUMULA_CHOICES,
        widget=forms.CheckboxSelectMultiple())


ACTIVIDAD_CHOICES = [
    ('ingresos_acumulados', 'Ingresos Acumulados'),
    ('porcentaje_ingresos_acumulados', '% Ingresos Acumulados'),
    ('egresos_acumulados', 'Egresos Acumulados'),
    ('porcentaje_egresos_acumulados', '% Egresos Acumulados'),
    ('imputacion', 'Imputación'),
    ('ingresos', 'Ingresos'),
    ('porcentaje_ingresos', '% Ingresos'),
    ('egresos', 'Egresos'),
    ('porcentaje_egresos', '% Egresos')
]


class ActividadForm(forms.Form):
    all = forms.BooleanField(required=False, label='Mostrar todas')
    visible_columns = forms.MultipleChoiceField(
        required=False,
        choices=ACTIVIDAD_CHOICES,
        widget=forms.CheckboxSelectMultiple())


class IndexForm(forms.Form):
    month = forms.DateField(
        required=False, label='Mes',
        widget=MonthDatePickerInput(
            attrs={'placeholder': 'Mes'}))
