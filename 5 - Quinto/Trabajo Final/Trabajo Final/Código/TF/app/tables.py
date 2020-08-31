import django_tables2 as tables
from django.utils.html import format_html

from app.models import Movimpu, Imputaci


class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        values = [bound_column.accessor.resolve(row) for row in table.data
                  if bound_column.accessor.resolve(row) is not None]
        values = set(values)
        total = sum(values)
        return format_html(f"<b>${total:,.1f}</b>")


# class MensualTable(tables.Table):
#     tipo_movim__descripcion = tables.Column(verbose_name='Tipo Movimiento')
#     cod_proveedor__razon_social = tables.Column(verbose_name='Razón Social')
#
#     class Meta:
#         model = Mensual
#         fields = ['periodo_contable', 'fecha_comprob',
#                   'tipo_movim__descripcion', 'tipo_comprob',
#                   'cod_proveedor__razon_social', 'imp_exento', 'imp_gravado',
#                   'imp_gravado_10', 'imp_gravado_27', 'importe_iva',
#                   'imp_iva10', 'imp_iva27', 'imp_perc_iva', 'imp_varios',
#                   'imp_total']
#         attrs = {"class": "table table-sm table-striped table-responsive "
#                           "table-hover"}
#
#     def render_fecha_comprob(self, value):
#         return f'{value.strftime("%d %b. %Y")}'
#
#     def render_periodo_contable(self, value):
#         return f'{value.strftime("%d %b. %Y")}'
#
#     def render_imp_exento(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_gravado(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_gravado_10(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_gravado_27(self, value):
#         return f'${value:,.1f}'
#
#     def render_importe_iva(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_iva10(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_iva27(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_perc_iva(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_varios(self, value):
#         return f'${value:,.1f}'
#
#     def render_imp_total(self, value):
#         return f'${value:,.1f}'
#
#
# class ProveedorTable(tables.Table):
#     tipo_movimiento = tables.Column(verbose_name='Tipo Movimiento')
#
#     class Meta:
#         model = CtaCte
#         fields = ['periodo_contable', 'fecha_comprob', 'nro_comprob',
#                   'tipo_comprobante', 'tipo_movimiento',
#                   'debe', 'haber']
#         attrs = {"class": "table table-sm table-striped table-hover"}


class IngEgMes(tables.Table):
    acumulador = tables.Column(
        verbose_name='Acumulador',
        accessor='cod_imput__donde_acumula__descripcion')
    imputacion = tables.Column(verbose_name='Imputación',
                               accessor='cod_imput__descripcion')
    actividad = tables.Column(verbose_name='Actividad',
                              accessor='actividad__descripcion')

    class Meta:
        model = Movimpu
        fields = ['periodo_contable', 'fecha_comprob',
                  'acumulador', 'imputacion', 'tipo_movim',
                  'actividad', 'descripcion', 'importe']
        attrs = {"class": "table table-sm table-striped table-hover"}

    def render_fecha_comprob(self, value):
        return f'{value.strftime("%d %b. %Y")}'

    def render_periodo_contable(self, value):
        return f'{value.strftime("%d %b. %Y")}'

    def render_importe(self, value):
        return f'${value:,.1f}'


class MovimpuTable(tables.Table):
    acumulador = tables.Column(
        verbose_name='Acumulador')
    imputacion = tables.Column(verbose_name='Imputación')
    actividad = tables.Column(verbose_name='Actividad')
    tipo_proveedor = tables.Column(verbose_name='Tipo Cliente/Proveedor')

    class Meta:
        model = Movimpu
        fields = ['periodo_contable', 'fecha_comprob',
                  'acumulador', 'imputacion', 'tipo_movim',
                  'num_comprob', 'descripcion', 'tipo_proveedor', 'actividad',
                  'importe', 'tipo']
        attrs = {"class": "table table-sm table-striped table-hover"}

    def render_importe(self, value):
        return f'${value:,.1f}'

    def render_num_comprob(self, value):
        return f'{value}'


class AcumulaTable(tables.Table):
    acumulador = tables.Column(verbose_name='Acumulador')
    imputacion = tables.Column(verbose_name='Imputación')
    total_egresos = SummingColumn('Total Egresos')

    class Meta:
        model = Imputaci
        fields = ['acumulador', 'imputacion', 'compra_cta_cte',
                  'compra_contado', 'nota_credito_recibida',
                  'nota_debito_recibida', 'egresos_cta_cte', 'egresos_contado',
                  'venta_cta_cte', 'venta_contado', 'nota_credito_emitida',
                  'nota_debito_emitida', 'cobranzas', 'unid_generadora',
                  'cuenta_gastos', 'total_egresos', 'porcentaje']
        attrs = {"class": "table table-sm table-striped table-hover "
                          "table-responsive"}

    def render_compra_cta_cte(self, value):
        return f'${value:,.1f}'

    def render_compra_contado(self, value):
        return f'${value:,.1f}'

    def render_nota_credito_recibida(self, value):
        return f'${value:,.1f}'

    def render_nota_debito_recibida(self, value):
        return f'${value:,.1f}'

    def render_egresos_cta_cte(self, value):
        return f'${value:,.1f}'

    def render_egresos_contado(self, value):
        return f'${value:,.1f}'

    def render_venta_cta_cte(self, value):
        return f'${value:,.1f}'

    def render_venta_contado(self, value):
        return f'${value:,.1f}'

    def render_nota_credito_emitida(self, value):
        return f'${value:,.1f}'

    def render_nota_debito_emitida(self, value):
        return f'${value:,.1f}'

    def render_cobranzas(self, value):
        return f'${value:,.1f}'

    def render_total_egresos(self, value):
        return f'${value:,.1f}'

    def render_porcentaje(self, value):
        return f'{value:.1f}%'


class ActividadTable(tables.Table):
    porcentaje_ingresos_acumulados = tables.Column(
        verbose_name='% Ingresos Acumulado')
    porcentaje_egresos_acumulados = tables.Column(
        verbose_name='% Egresos Acumulado')
    imputacion = tables.Column(verbose_name='Imputación')
    acumulador = tables.Column(verbose_name='Acumulador')
    egresos_acumulados = SummingColumn(verbose_name='Egresos Acumulados')
    ingresos_acumulados = SummingColumn(verbose_name='Ingresos Acumulados')
    porcentaje_ingresos = tables.Column(verbose_name='% Ingresos')
    porcentaje_egresos = tables.Column(verbose_name='% Egresos')
    egresos = SummingColumn(verbose_name='Egresos')
    ingresos = SummingColumn(verbose_name='Ingresos')

    class Meta:
        model = Movimpu
        fields = ['actividad', 'acumulador',
                  'ingresos_acumulados', 'porcentaje_ingresos_acumulados',
                  'egresos_acumulados', 'porcentaje_egresos_acumulados',
                  'imputacion',
                  'ingresos', 'porcentaje_ingresos',
                  'egresos', 'porcentaje_egresos']
        attrs = {"class": "table table-sm table-striped table-hover"}

    def render_porcentaje_ingresos_acumulados(self, value):
        return f'{value:.1f}%'

    def render_porcentaje_egresos_acumulados(self, value):
        return f'{value:.1f}%'

    def render_ingresos_acumulados(self, value):
        return f'${value:,.1f}'

    def render_egresos_acumulados(self, value):
        return f'${value:,.1f}'

    def render_porcentaje_ingresos(self, value):
        return f'{value:.1f}%'

    def render_porcentaje_egresos(self, value):
        return f'{value:.1f}%'

    def render_ingresos(self, value):
        return f'${value:,.1f}'

    def render_egresos(self, value):
        return f'${value:,.1f}'
