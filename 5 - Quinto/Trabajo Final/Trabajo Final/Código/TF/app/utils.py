import locale
import math
import numpy as np
from bokeh.embed import components

from bokeh.layouts import grid
from bokeh.models import ColumnDataSource, HoverTool, Range1d, FactorRange, \
    NumeralTickFormatter, Legend, LegendItem, LabelSet
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh import palettes
from datetime import datetime
from math import pi

from django.core.exceptions import ObjectDoesNotExist
from pandas import DataFrame, notnull, to_datetime

from app.models import Movimpu, Imputaci, Movgan, Silos, Producto, Pendpago, \
    Pendcobro, Gf, Tractor, Maquina, Bolsas, Transp, Cultivo, Cheques

# Libroba

PLOT_PADDING = 0.04


def set_plot_properties(plot):
    plot.title.text_font_size = '14pt'
    plot.title.text_color = 'Black'
    plot.title.text_font = 'Montserrat'
    plot.title.text_font_style = 'normal'
    plot.axis.axis_label_text_color = 'Black'
    plot.axis.axis_label_text_font = 'Montserrat'
    plot.axis.major_label_text_font = 'Montserrat'
    plot.legend.label_text_font = 'Montserrat'
    plot.toolbar.autohide = True
    plot.grid.visible = False
    plot.outline_line_color = None


def delete_xaxis(plot):
    plot.xaxis.visible = False
    plot.xaxis.axis_label = None


def delete_yaxis(plot):
    plot.yaxis.visible = False
    plot.yaxis.axis_label = None


def set_num_ticks(plot, num_ticks, axis):
    if axis == 'x':
        if num_ticks > 10:
            plot.xaxis[0].ticker.desired_num_ticks = int(num_ticks / 2)
            plot.xaxis.major_label_orientation = 0.45
        elif num_ticks * 2 > 10:
            plot.xaxis[0].ticker.desired_num_ticks = num_ticks
        else:
            plot.xaxis[0].ticker.desired_num_ticks = num_ticks * 2
    else:
        if num_ticks > 25:
            plot.yaxis[0].ticker.desired_num_ticks = int(num_ticks / 2)
        elif num_ticks * 2 > 25:
            plot.yaxis[0].ticker.desired_num_ticks = num_ticks
        else:
            plot.yaxis[0].ticker.desired_num_ticks = num_ticks * 2


def palettes_greens(n):
    colors = ['#006633', '#006600', '#009933', '#009900', '#669933', '#669900',
              '#00CC33', '#00CC00', '#66CC33', '#66CC00', '#00FF33', '#00FF00',
              '#66FF33', '#66FF00', '#CCFF33', '#CCFF00']

    return [colors[int(math.floor(i))] for i in
            np.linspace(0, len(colors) - 1, num=n)]


def palettes_reds(n):
    colors = ['#FF0000', '#FF3300', '#FF0033', '#FF3333', '#CC6666', '#FF6666',
              '#FF6600', '#FF6633', '#FF9900', '#FF9933', '#FF9966', '#CC9966',
              '#FFCC00', '#FFCC33', '#FFCC66', '#FFCC99']

    return [colors[int(math.floor(i))] for i in
            np.linspace(0, len(colors) - 1, num=n)]


def palettes_category30(n):
    colors = ['#1f77b4', '#6baed6', '#aec7e8', '#ff7f0e', '#e6550d', '#fd8d3c',
              '#ffbb78', '#2ca02c', '#74c476', '#98df8a', '#843c39', '#d62728',
              '#ff9896', '#5254a3', '#9467bd', '#c5b0d5', '#8c6d31', '#bd9e39',
              '#e7ba52', '#a55194', '#ce6dbd', '#de9ed6', '#7f7f7f', '#bdbdbd',
              '#c7c7c7', '818209', '#bcbd22', '#dbdb8d', '#17becf', '5ebbcc',
              '#9edae5']

    return [colors[int(math.floor(i))] for i in
            np.linspace(0, len(colors) - 1, num=n)]


def get_palet(column, color=None):
    c_len = len(column)

    if color == 'greens':
        return palettes_greens(c_len)
    elif color == 'reds':
        return palettes_reds(c_len)

    if 3 <= c_len <= 10:
        return palettes.Category10[c_len]
    elif 10 < c_len <= 20:
        return palettes.Category20[c_len]
    else:
        return palettes_category30(c_len)


# def get_mensual():
#     mensual = Mensual.objects.values(
#         'fecha_comprob', 'periodo_contable', 'tipo_movim__descripcion',
#         'tipo_comprob', 'prefijo', 'cod_proveedor__razon_social',
#         'imp_exento', 'imp_gravado', 'imp_gravado_10', 'imp_gravado_27',
#         'importe_iva', 'imp_iva10', 'imp_iva27', 'imp_perc_iva',
#         'imp_varios', 'imp_total').order_by('periodo_contable')
#
#     return mensual


def get_movimpu():
    movimpu = Movimpu.objects.values(
        'cod_imput__descripcion',
        'cod_imput__donde_acumula',
        'cod_imput__donde_acumula__descripcion',
        'fecha_comprob', 'periodo_contable', 'tipo_movim',
        'num_comprob', 'descripcion', 'importe',
        'actividad__descripcion', 'cod_provincia__descripcion',
        'tipo_proveedor__descripcion') \
        .filter(importe__gt=0) \
        .order_by('periodo_contable')

    return movimpu


acumuladores_ingreso = [
    'Cobranza', 'Ingreso', 'Ventas Cuenta Corriente', 'Ventas De Contado', 'Nota De Crédito',
    'Nota De Débito Emitida'
]
acumuladores_egreso = [
    'Documento De Contado', 'Egreso', 'Facturas De Contado', 'Facturas Cuenta Corriente',
    'Orden De Pago', 'Nota De Crédito Emitida', 'Nota De Débito'
]


def get_df_mov_impu(movimpu):
    df = DataFrame(movimpu)
    df.rename(columns={
        'actividad__descripcion': 'actividad',
        'cod_imput__descripcion': 'imputacion',
        'cod_imput__donde_acumula__descripcion': 'acumulador',
        'cod_provincia__descripcion': 'provincia',
        'tipo_proveedor__descripcion': 'tipo_proveedor'
    }, inplace=True)
    # Diferenciar ingresos de egresos
    df.loc[df.tipo_movim.isin(acumuladores_ingreso), 'tipo'] = 'Ingreso'
    df.loc[df.tipo_movim.isin(acumuladores_egreso), 'tipo'] = 'Egreso'
    df.loc[df.acumulador == 'Ventas', 'tipo'] = 'Ingreso'
    df.dropna(subset=['tipo'], inplace=True)
    # imputaciones_ingresos = ['Venta De Leche', 'Venta De Hacienda I', 'Venta de Cereales',
    #                          'Cobranzas', 'Ventas Animales']
    # df.loc[df.acumulador.isin(imputaciones_ingresos), 'tipo'] = 'Ingreso'
    df = df.where((notnull(df)), None)  # Reemplazar los NaN que genera Pandas

    return df


def get_imputaci():
    """
    Obtener datos de Imputaci mayores a cero.
    """
    imputaci = Imputaci.objects.values(
        'descripcion', 'donde_acumula__descripcion', 'total_egresos',
        'compra_cta_cte', 'compra_contado', 'nota_credito_recibida',
        'nota_debito_recibida', 'egresos_cta_cte', 'egresos_contado',
        'venta_cta_cte', 'venta_contado', 'nota_credito_emitida',
        'nota_debito_emitida', 'cobranzas', 'unid_generadora',
        'cuenta_gastos', 'porcentaje') \
        .order_by('donde_acumula__descripcion', 'descripcion')

    return imputaci


# def get_proctcte():
#     proctcte = Proctcte.objects.values(
#         'cod_proveedor__razon_social', 'iva', 'saldo_cta_cte', 'tipo_factura',
#         'tipo_proveedor', 'particip_total_compras', 'prefijo',
#         'porcent_total_compras')
#     df = DataFrame(proctcte)
#     df.rename(columns={'saldo_cta_cte': 'saldo',
#                        'cod_proveedor__razon_social': 'razon_social'},
#               inplace=True)
#
#     return df
#
#
# def get_proveedor_ctacte():
#     proveedor = CtaCte.objects.values(
#         'tipo_movim__descripcion',
#         'cod_proveedor__razon_social',
#         'cod_proveedor__direccion',
#         'cod_proveedor__localidad__descripcion',
#         'cod_proveedor__cuit',
#         'cod_proveedor__saldo_cta_cte',
#         'fecha_comprob', 'nro_comprob',
#         'importe', 'periodo_contable',
#         'tipo_comprobante') \
#         .order_by('periodo_contable')
#
#     return proveedor
#
#
# def get_df_proveedor_ctacte(proveedor):
#     df = DataFrame(proveedor)
#     df.rename(columns={'cod_proveedor__cuit': 'cuit',
#                        'cod_proveedor__direccion': 'direccion',
#                        'cod_proveedor__localidad__descripcion': 'localidad',
#                        'cod_proveedor__razon_social': 'razon_social',
#                        'tipo_movim__descripcion': 'tipo_movimiento',
#                        'cod_proveedor__saldo_cta_cte': 'saldo'},
#               inplace=True)
#     df['debe'] = df.loc[df.tipo_movimiento == 'Orden de Pago'].importe
#     df['haber'] = df.loc[df.tipo_movimiento == 'Factura Cuenta Corriente'] \
#         .importe
#     df = df.where((notnull(df)), None)  # Reemplazar los NaN que genera Pandas
#     datos_proveedor = {
#         'razon_social': df.razon_social.unique()[0],
#         'localidad': df.localidad.unique()[0],
#         'direccion': df.direccion.unique()[0],
#         'cuit': df.cuit.unique()[0],
#         'saldo': df.saldo.unique()[0]}
#
#     return df, datos_proveedor
#
#
# def get_cliente():
#     cli = Cli.objects.values(
#         'razon_social', 'iva', 'saldo', 'prefijo',
#         'tipo_factura', 'tipo_cliente',
#         'particip_total_compras', 'porcent_total_compras', ) \
#         .order_by('saldo')
#     df = DataFrame(cli)
#
#     return df


def filter_period(start, end, df):
    title = ''
    if start and end:
        df = df[(df['periodo_contable'] >= start) &
                (df['periodo_contable'] <= end)].copy()
        title = f"Periodo contable: {start.day}/{start.month}" \
                f"/{start.year} - {end.day}/{end.month}/{end.year}"
    elif start and not end:
        df = df[df['periodo_contable'] >= start].copy()
        title = f"Periodo contable: {start.day}/{start.month}" \
                f"/{start.year} - Hoy"
    elif end and not start:
        df = df[df['periodo_contable'] <= end].copy()
        title = f"Periodo contable: Inicio - {end.day}/{end.month}/{end.year}"

    return df, title


def title_period(start, end):
    title = ''
    if start and end:
        title = f"Periodo contable: {start.day}/{start.month}" \
                f"/{start.year} - {end.day}/{end.month}/{end.year}"
    elif start and not end:
        title = f"Periodo contable: {start.day}/{start.month}" \
                f"/{start.year} - Hoy"
    elif end and not start:
        title = f"Periodo contable: Inicio - {end.day}/{end.month}/{end.year}"

    return title


def format_period(start, end):
    start = None if start == 'None' else datetime.strptime(start,
                                                           '%Y-%m-%d').date()
    end = None if end == 'None' else datetime.strptime(end, '%Y-%m-%d').date()

    return start, end


def add_sample_data_movimpu(df, col):
    df = df.append(
        {col: 'Ejemplo', 'tipo': 1, 'importe': 5000000},
        ignore_index=True)
    df = df.append(
        {col: 'Ejemplo 2', 'tipo': 1, 'importe': 8000000},
        ignore_index=True)
    df = df.append(
        {col: 'Ejemplo 3', 'tipo': 1, 'importe': 12000000},
        ignore_index=True)
    df = df.append(
        {col: 'Ejemplo 4', 'tipo': 1, 'importe': 3000000},
        ignore_index=True)

    return df


def sum_importe(df, col):
    _ = DataFrame(df.groupby([col, 'tipo'], as_index=False)
                  .agg({'importe': 'sum'}))
    gb = DataFrame(df.groupby(col, as_index=False).tipo.count())
    for x in gb[col]:
        total = 0
        dato = _[_[col] == x].copy()
        ingreso = dato[dato.tipo == 'Ingreso'].importe.copy()
        if not ingreso.empty:
            total += ingreso.array
        egreso = dato[dato.tipo == 'Egreso'].importe.copy()
        if not egreso.empty:
            total -= egreso.array
        gb.loc[gb[col] == x, 'importe'] = total

    # df = add_sample_data_movimpu(df, col)

    positive = gb[gb.importe >= 0]
    negative = gb[gb.importe < 0]

    return positive, negative


def impu_plots(tipo, df, radius, color=None, negative=False):
    df.sort_values('importe', inplace=True, ascending=False)
    df['percentage'] = abs(df.importe / df.importe.sum() * 100)
    df['angle'] = df.importe / df.importe.sum() * 2 * pi

    if tipo == 'ingresos':
        df = df[(df.percentage >= 0.1)]
    else:
        df = df[(df.percentage >= 0.5)]
    percentage = abs(df.importe / df.importe.sum() * 100)
    df['percentage'] = round(percentage, 1)
    df['angle'] = df.importe / df.importe.sum() * 2 * pi
    df['color'] = get_palet(df['importe'], color)
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]
    bar = impu_vbar(source, negative)
    pie = impu_pie(source, radius)

    return bar, pie


def impu_vbar(source, negative=False):
    tooltips = [
        ("Acumulador", "@{acumulador}"),
        ("Importe", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(
        x_range=FactorRange(*source.data['acumulador'],
                            bounds='auto'),
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above', x_axis_label="Acumulador")
    if negative:
        plot.y_range = Range1d(start=0,
                               end=min(source.data['importe']) +
                                   min(source.data['importe']) * PLOT_PADDING,
                               bounds='auto')
    else:
        plot.y_range = Range1d(start=0,
                               end=max(source.data['importe']) +
                                   max(source.data['importe']) * PLOT_PADDING,
                               bounds='auto')
    plot.vbar(
        x='acumulador', top='importe',
        width=0.9, source=source,
        nonselection_fill_alpha=0.2, line_color=None,
        fill_color='color', name='vbar')
    plot.text(
        y=source.data['importe'],
        x=source.data['acumulador'],
        text=source.data['percentage'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat',
        text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis.formatter = NumeralTickFormatter(format="$ 0")
    if len(source.data['acumulador']) > 8:
        plot.xaxis[0].major_label_orientation = 0.45
    plot.sizing_mode = 'stretch_width'

    return plot


def impu_pie(source, radius):
    tooltips = [("Acumulador", "@{acumulador}"),
                ("Importe total", "@importe{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(tools=["tap,reset,save", hovertool],
                  toolbar_location='above')
    w = plot.wedge(x=0, y=0, radius=radius,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4,
                   fill_color='color',
                   source=source, name='wedge')
    # Crear legends aparte para ponerlas afuera del gráfico y que no lo tapen.
    legend = Legend(
        items=[LegendItem(label=dict(field="acumulador"),
                          renderers=[w])])
    plot.add_layout(legend, 'right')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


def detalle_impu_plots(df, radius, color=None, negative=False):
    df.sort_values('importe', inplace=True, ascending=False)
    df['color'] = get_palet(df['importe'], color)
    percentage = abs(df.importe / df.importe.sum() * 100)
    df['percentage'] = round(percentage, 1)
    df['angle'] = df.importe / df.importe.sum() * 2 * pi
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]
    bar = detalle_impu_vbar(source, negative)
    pie = detalle_impu_pie(source, radius)

    return bar, pie


def detalle_impu_vbar(source, negative):
    tooltips = [('Imputación', '@{imputacion}'),
                ("Importe", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(x_range=FactorRange(*source.data['imputacion'],
                                      bounds='auto'),
                  tools=["tap,reset,save,crosshair", hovertool],
                  toolbar_location='above', x_axis_label='Imputación')
    if negative:
        plot.y_range = Range1d(start=0,
                               end=min(source.data['importe']) +
                                   min(source.data['importe']) * PLOT_PADDING,
                               bounds='auto')
    else:
        plot.y_range = Range1d(start=0,
                               end=max(source.data['importe']) +
                                   max(source.data['importe']) * PLOT_PADDING,
                               bounds='auto')
    plot.vbar(
        x='imputacion', top='importe', width=0.9, source=source,
        nonselection_fill_alpha=0.2, line_color=None,
        fill_color='color', name='vbar')
    plot.text(
        x=source.data['imputacion'],
        y=source.data['importe'],
        text=source.data['percentage'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(format="$0")
    if len(source.data['imputacion']) > 6:
        plot.xaxis[0].major_label_orientation = 0.3
    plot.sizing_mode = 'stretch_width'

    return plot


def detalle_impu_pie(source, radius):
    tooltips = [("Imputación", "@{imputacion}"),
                ("Importe total", "@importe{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(tools=["tap,reset,save", hovertool],
                  toolbar_location='above')
    w = plot.wedge(x=0, y=0, radius=radius,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4,
                   fill_color='color',
                   source=source, name='wedge')
    # Crear legends aparte para ponerlas afuera del gráfico y que no lo tapen.
    legend = Legend(
        items=[LegendItem(label=dict(field="imputacion"),
                          renderers=[w])])
    plot.add_layout(legend, 'right')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


def detalle_actividad_vbar(df, color):
    gb_mov_impu = DataFrame(df.groupby(
        ['acumulador', 'imputacion']).agg({'importe': 'sum'}))
    gb_mov_impu.sort_values('importe', ascending=False, inplace=True)
    percentage = abs(gb_mov_impu.importe / gb_mov_impu.importe.sum() * 100)
    gb_mov_impu['porcentaje'] = round(percentage, 2)
    gb_mov_impu['color'] = get_palet(gb_mov_impu['importe'], color)
    source = ColumnDataSource(gb_mov_impu)
    source.data['porcentaje'] = [f'{x}%' for x in source.data[
        'porcentaje']]
    tooltips = [("Acumulador, Imputación",
                 "@{acumulador_imputacion}"),
                ("Importe total", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(
        x_range=FactorRange(
            *source.data['acumulador_imputacion']),
        y_range=Range1d(start=0,
                        end=max(source.data['importe']) +
                            max(source.data['importe']) * PLOT_PADDING,
                        bounds='auto'),
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above')
    plot.vbar(
        x='acumulador_imputacion', width=0.9, top='importe',
        source=source, fill_color='color',
        nonselection_fill_alpha=0.2, line_color=None,
        name='vbar')
    plot.text(
        x=source.data['acumulador_imputacion'],
        y=source.data['importe'],
        text=source.data['porcentaje'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(
        format="$0")
    plot.sizing_mode = 'stretch_width'
    plot.xaxis.group_text_font = 'Montserrat'

    return plot


def detalle_actividad_pie(df, color):
    plot_grid = []
    df_gb = DataFrame(
        df.groupby(['acumulador', 'imputacion'],
                   as_index=False).agg({'importe': 'sum'}))
    for x in df_gb['acumulador'].unique():
        df_actividad = df_gb[df_gb['acumulador'] == x].copy()
        df_actividad.sort_values('importe', ascending=False, inplace=True)
        percentage = abs(df_actividad.importe / df_actividad.importe.sum() *
                         100)
        df_actividad['percentage'] = round(percentage, 2)
        df_actividad['angle'] = df_actividad.importe / \
                                df_actividad.importe.sum() * 2 * pi
        df_actividad['color'] = get_palet(df_actividad['importe'], color)
        source = ColumnDataSource(df_actividad)
        source.data['percentage'] = [f'{x}%' for x in source.data[
            'percentage']]
        tooltips = [("Imputación", "@{imputacion}"),
                    ("Importe total", "@importe{$0,0.00}"),
                    ('% del total', '@percentage')]
        hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
        plot = figure(
            title=x,
            tools=["tap,reset,save", hovertool],
            toolbar_location='above', height=400)
        plot.wedge(x=0, y=0, radius=0.3,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4, fill_color='color',
                   legend_field='imputacion',
                   source=source, name='wedge')
        set_plot_properties(plot)
        delete_xaxis(plot)
        delete_yaxis(plot)
        plot.sizing_mode = 'stretch_width'
        plot_grid.append(plot)

    return grid(children=plot_grid,
                sizing_mode='stretch_width',
                ncols=2)


def actividad_vbar(df):
    gb_tipo = DataFrame(df.groupby(
        ['actividad', 'tipo'], as_index=False).agg({'importe': 'sum'}))
    gb_tipo.loc[gb_tipo.tipo == 'Ingreso', 'color'] = get_palet('1', 'greens')
    gb_tipo.loc[gb_tipo.tipo == 'Egreso', 'color'] = get_palet('1', 'reds')
    gb_tipo.loc[gb_tipo.tipo == 'Egreso', 'Porcentaje'] = \
        gb_tipo[gb_tipo.tipo == 'Egreso'].importe / gb_tipo[
            gb_tipo.tipo == 'Egreso'].importe.sum() * 100
    gb_tipo.loc[gb_tipo.tipo == 'Ingreso', 'Porcentaje'] = \
        gb_tipo[gb_tipo.tipo == 'Ingreso'].importe / gb_tipo[
            gb_tipo.tipo == 'Ingreso'].importe.sum() * 100
    gb_tipo['Porcentaje'] = round(gb_tipo.Porcentaje, 2)
    gb_tipo.set_index(['actividad', 'tipo'], inplace=True)
    gb_tipo.sort_values('importe', ascending=False,
                        inplace=True)
    source = ColumnDataSource(gb_tipo)
    source.data['Porcentaje'] = [f'{x}%' for x in source.data[
        'Porcentaje']]
    tooltips = [
        ("Importe", "@importe{$0,0.00}"), ]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(
        y_range=Range1d(start=0,
                        end=max(source.data['importe']) +
                            max(source.data['importe']) * PLOT_PADDING,
                        bounds='auto'),
        x_range=FactorRange(
            *source.data['actividad_tipo'],
            bounds='auto'),
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above', x_axis_label='Actividad')
    plot.vbar(
        x='actividad_tipo', top='importe',
        width=0.9, source=source,
        nonselection_fill_alpha=0.2, line_color=None,
        fill_color='color', name='vbar')
    plot.text(
        y=source.data['importe'],
        x=source.data['actividad_tipo'],
        text=source.data['Porcentaje'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(
        format="$0")
    if len(source.data['actividad_tipo']) > 6:
        plot.xaxis[0].major_label_orientation = 0.3
    plot.sizing_mode = 'stretch_width'
    plot.xaxis.group_text_font = 'Montserrat'

    return plot


def actividad_pie(df_actividad, color):
    percentage = abs(df_actividad.importe / df_actividad.importe.sum() * 100)
    df_actividad['percentage'] = round(percentage, 1)
    df_actividad['angle'] = df_actividad.importe / df_actividad.importe.sum() \
                            * 2 * pi
    df_actividad.sort_values('angle', ascending=False, inplace=True)
    df_actividad['color'] = get_palet(df_actividad['importe'], color)
    source = ColumnDataSource(df_actividad)
    source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]

    tooltips = [("Actividad", "@actividad"),
                ("Importe total", "@importe{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["tap,reset,save", hovertool],
        toolbar_location='above', height=400)
    w = plot.wedge(x=0, y=0, radius=0.7,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4, fill_color='color',
                   # legend_field='actividad',
                   source=source, name='wedge')
    # Crear legends aparte para ponerlas afuera del gráfico y que no lo tapen.
    legend = Legend(
        items=[LegendItem(label=dict(field="actividad"),
                          renderers=[w])])
    plot.add_layout(legend, 'right')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


def ingresos_egresos_mes_pie(df):
    # Mostrar gráfico del mes actual.
    # start = datetime.today() - relativedelta(months=+0, day=1)
    # end = datetime.today()
    start = datetime(2014, 4, 1)
    end = datetime(2014, 4, 30)
    df, title = filter_period(start, end, df)
    gb_mov_impu = DataFrame(df.groupby(['tipo'], as_index=False)
                            .agg({'importe': 'sum'}))
    gb_mov_impu.sort_values('importe', ascending=False, inplace=True)
    percentage = abs(gb_mov_impu.importe / gb_mov_impu.importe.sum() * 100)
    gb_mov_impu['percentage'] = round(percentage, 2)
    gb_mov_impu['angle'] = gb_mov_impu.importe / \
                           gb_mov_impu.importe.sum() * 2 * pi
    gb_mov_impu.sort_values('angle', ascending=False, inplace=True)
    gb_mov_impu.loc[gb_mov_impu.tipo == 'Ingreso', 'color'] = get_palet('1',
                                                                        'greens')
    gb_mov_impu.loc[gb_mov_impu.tipo == 'Egreso', 'color'] = get_palet('1',
                                                                       'reds')
    source = ColumnDataSource(gb_mov_impu)
    source.data['percentage'] = [f'{x}%' for x in source.data[
        'percentage']]
    tooltips = [("", "@tipo"),
                ("Importe total", "@importe{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["tap,reset,save", hovertool],
        toolbar_location='above',
        height=300, width=300)
    plot.wedge(x=0, y=0, radius=0.2,
               start_angle=cumsum('angle', include_zero=True),
               end_angle=cumsum('angle'),
               line_color='white', line_width=0.4,
               fill_color='color', legend_field='tipo',
               source=source, name='wedge', )
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


def ingresos_egresos_mes_line(df):
    # today = datetime.today()
    today = datetime(2015, 4, 1)
    df_filter = df[(df['periodo_contable'].dt.month == today.month) &
                   (df['periodo_contable'].dt.year == today.year)]
    df_gb = DataFrame(df_filter.groupby(['periodo_contable', 'tipo',
                                         'tipo_movim',
                                         'acumulador',
                                         'imputacion'],
                                        as_index=False)
                      .agg({'importe': 'sum'}))
    source = ColumnDataSource(df_gb)
    source_ingresos = ColumnDataSource(df_gb[df_gb['tipo'] == 'Ingreso'])
    source_egresos = ColumnDataSource(df_gb[df_gb['tipo'] == 'Egreso'])
    tooltips = [("", "@tipo"),
                ("Tipo Movimiento", "@{tipo_movim}"),
                (
                    "Imputación",
                    "@{acumulador} (@{imputacion})"),
                ("Importe Total", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['circle'], tooltips=tooltips)
    plot = figure(
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above',
        x_axis_type="datetime",
        y_range=Range1d(start=0,
                        end=max(source.data['importe']) +
                            max(source.data['importe']) * PLOT_PADDING,
                        bounds='auto'))
    # Ingresos
    plot.line(x='periodo_contable', y='importe',
              source=source_ingresos, name='line',
              line_color='green')
    plot.circle(x='periodo_contable', y='importe',
                fill_color="white", size=8, name='circle',
                source=source_ingresos,
                line_color='green')
    # Egresos
    plot.line(x='periodo_contable', y='importe',
              source=source_egresos, name='line',
              line_color='red')
    plot.circle(x='periodo_contable', y='importe',
                fill_color="white", size=8, name='circle',
                source=source_egresos,
                line_color='red')
    set_plot_properties(plot)
    plot.sizing_mode = 'scale_both'
    plot.yaxis.formatter = NumeralTickFormatter(
        format="$0")
    plot.yaxis[0].ticker.desired_num_ticks = 20

    return plot


def acumula_vbar(source):
    tooltips = [
        ("Imputación", "@acumulador"),
        ("Total Egresos", "@total_egresos{$0,0.00}"),
    ]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(
        y_range=Range1d(start=0,
                        end=max(source.data['total_egresos']) +
                            max(source.data['total_egresos']) * PLOT_PADDING,
                        bounds='auto'),
        x_range=FactorRange(*source.data['acumulador'],
                            bounds='auto'),
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above',
        x_axis_label='Imputación',
        title='Total de Egresos por Acumulador')
    plot.vbar(
        x='acumulador', top='total_egresos',
        width=0.9, source=source,
        fill_color='color', nonselection_fill_alpha=0.2,
        line_color=None, name='vbar')
    plot.text(
        y=source.data['total_egresos'],
        x=source.data['acumulador'],
        text=source.data['percentage'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(format="$0")
    if len(source.data['acumulador']) > 6:
        plot.xaxis[0].major_label_orientation = 0.45
    plot.sizing_mode = 'stretch_width'

    return plot


def acumula_pie(source):
    tooltips = [("Dónde Acumula", "@acumulador"),
                ("Total Egresos", "@total_egresos{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above',
        title='Total de Egresos por Acumulador',
        height=800)
    w = plot.wedge(x=0, y=0, radius=0.6,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4, fill_color='color',
                   # legend_field='acumulador',
                   source=source, name='wedge')
    # Crear legends aparte para ponerlas afuera del gráfico y que no lo tapen.
    legend = Legend(
        items=[LegendItem(label=dict(field="acumulador"),
                          renderers=[w])])
    plot.add_layout(legend, 'right')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


def detalle_acumula_vbar(source):
    tooltips = [
        ("Imputación", "@imputacion"),
        ("Total Egresos", "@total_egresos{$0,0.00}")]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(
        y_range=Range1d(start=0,
                        end=max(source.data['total_egresos']) +
                            max(source.data['total_egresos']) * PLOT_PADDING,
                        bounds='auto'),
        x_range=FactorRange(*source.data['imputacion'],
                            bounds='auto'),
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above',
        x_axis_label='Imputación',
        title='Total de Egresos por Imputación')
    plot.vbar(
        x='imputacion', top='total_egresos',
        width=0.9, source=source,
        fill_color='color', nonselection_fill_alpha=0.2,
        line_color=None, name='vbar')
    plot.text(
        y=source.data['total_egresos'],
        x=source.data['imputacion'],
        text=source.data['percentage'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(format="$0")
    if len(source.data['imputacion']) > 6:
        plot.xaxis[0].major_label_orientation = 0.3
    plot.sizing_mode = 'stretch_width'

    return plot


def detalle_acumula_pie(source):
    tooltips = [("Imputación", "@imputacion"),
                ("Total Egresos", "@total_egresos{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above',
        title='Total de Egresos por Imputación')
    plot.wedge(x=0, y=0, radius=0.3,
               start_angle=cumsum('angle', include_zero=True),
               end_angle=cumsum('angle'),
               line_color='white', line_width=0.4, fill_color='color',
               legend_field='imputacion',
               source=source, name='wedge')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


def detalle_acumula_plots(df):
    gb_imputaci = DataFrame(df.groupby(
        'imputacion').total_egresos.sum())
    gb_imputaci.sort_values('total_egresos', ascending=False, inplace=True)
    gb_imputaci['color'] = get_palet(gb_imputaci['total_egresos'])
    percentage = gb_imputaci.total_egresos / gb_imputaci.total_egresos.sum() \
                 * 100
    gb_imputaci['percentage'] = round(percentage, 1)
    gb_imputaci['angle'] = gb_imputaci.total_egresos / \
                           gb_imputaci.total_egresos.sum() * 2 * pi
    source = ColumnDataSource(gb_imputaci)
    source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]
    vbar_plot = detalle_acumula_vbar(source)
    pie_plot = detalle_acumula_pie(source)

    script, div = components({'vbar_plot': vbar_plot, 'pie_plot': pie_plot})

    return script, div


def mensual_hbar(df):
    gb = DataFrame(df.groupby(['Razón Social'], as_index=False)
                   .agg({'importe': 'sum'}))
    gb.sort_values('importe', inplace=True)
    gb['color'] = get_palet(gb['importe'], 'reds')
    source = ColumnDataSource(gb)
    tooltips = [
        # ('', '@tipo'),
        ("Razón Social", "@{Razón Social}"),
        # ("Tipo Movimiento", "@{tipo_movim}"),
        # ("Tipo Comprobante", "@{Tipo Comprobante}"),
        # ('Fecha Comprobante', '@{fecha_comprobante}{%d/%m/%y}'),
        ("Importe total", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['hbar'], tooltips=tooltips,
                          formatters={'fecha_comprobante': 'datetime'})
    plot = figure(
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above',
        x_range=Range1d(start=0,
                        end=max(source.data['importe'], ),
                        bounds='auto'),
        y_range=FactorRange(*source.data['Razón Social'],
                            bounds='auto'),
        y_axis_label='Razón Social',
        x_axis_label='Importe Total'
    )
    plot.hbar(source=source, y='Razón Social', right='importe',
              height=0.8, fill_color='color', nonselection_fill_alpha=0.2,
              line_color=None, name='hbar', )
    set_plot_properties(plot)
    plot.xaxis.formatter = NumeralTickFormatter(format="$0")
    # plot.sizing_mode = 'scale_height'

    return plot


def detalle_proveedor_pie(df):
    gb = DataFrame(df.groupby('tipo_movimiento').agg({'importe': 'sum'}))
    gb['angle'] = gb.importe / gb.importe.sum() * 2 * pi
    gb['color'] = get_palet(gb['importe'])
    source = ColumnDataSource(gb)
    tooltips = [("Tipo Movimiento", "@tipo_movimiento"),
                ("Importe", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["tap,reset,save", hovertool],
        toolbar_location='above',
        height=400)
    plot.wedge(x=0, y=0, radius=0.3,
               start_angle=cumsum('angle', include_zero=True),
               end_angle=cumsum('angle'), fill_color='color',
               line_color='white', line_width=0.4,
               legend_field='tipo_movimiento',
               source=source, name='wedge')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_width'

    return plot


# def add_sample_data_actividad(df):
#     df = df.append({'actividad': 'Ganaderia',
#                     'importe': 15000,
#                     'tipo': 'Ingreso',
#                     'acumulador': 'Impu acumulada',
#                     'imputacion': 'Impu simple'}, ignore_index=True)
#     df = df.append({'actividad': 'Ganaderia',
#                     'importe': 256000,
#                     'tipo': 'Ingreso',
#                     'acumulador': 'Impu acumulada',
#                     'imputacion': 'Impu simple 2'}, ignore_index=True)
#     df = df.append({'actividad': 'Ganaderia',
#                     'importe': 86000,
#                     'tipo': 'Ingreso',
#                     'acumulador': 'Impu acumulada',
#                     'imputacion': 'Impu simple 3'}, ignore_index=True)
#     df = df.append({'actividad': 'Ganaderia',
#                     'importe': 58000,
#                     'tipo': 'Ingreso',
#                     'acumulador': 'Impu acumulada 2',
#                     'imputacion': 'Impu simple'}, ignore_index=True)
#
#     df = df.append({'actividad': 'Ganaderia',
#                     'importe': 1888000,
#                     'tipo': 'Egreso',
#                     'acumulador': 'Impu acumulada',
#                     'imputacion': 'Impu simple'}, ignore_index=True)
#     df = df.append({'actividad': 'Ganaderia',
#                     'importe': 855000,
#                     'tipo': 'Egreso',
#                     'acumulador': 'Impu acumulada 2',
#                     'imputacion': 'Impu simple'}, ignore_index=True)
#
#     return df


def gb_actividad(df, impu_simple=False):
    if impu_simple:
        gb = DataFrame(
            df.groupby(['actividad', 'acumulador', 'tipo',
                        'imputacion'], as_index=False)
                .agg({'importe': 'sum'}))
        gb['egresos_acumulados'] = gb.loc[gb.tipo == 'Egreso'].groupby(
            ['actividad', 'acumulador']).importe.transform('sum')
        gb['porcentaje_egresos_acumulados'] = gb.egresos_acumulados / \
                                              gb.egresos_acumulados.sum() * 100
        gb['ingresos_acumulados'] = gb.loc[gb.tipo == 'Ingreso'].groupby(
            ['actividad', 'acumulador']).importe.transform('sum')
        gb['porcentaje_ingresos_acumulados'] = gb.ingresos_acumulados / \
                                               gb.ingresos_acumulados.sum() * \
                                               100
        gb['egresos'] = gb.loc[gb.tipo == 'Egreso'].importe
        gb['porcentaje_egresos'] = gb.egresos / gb.egresos_acumulados * 100
        gb['ingresos'] = gb.loc[gb.tipo == 'Ingreso'].importe
        gb['porcentaje_ingresos'] = gb.ingresos / gb.ingresos_acumulados * 100
    else:
        gb = DataFrame(
            df.groupby(['actividad', 'acumulador', 'tipo'],
                       as_index=False).agg({'importe': 'sum'}))
        gb['ingresos_acumulados'] = gb.loc[gb.tipo == 'Ingreso'].importe
        gb['porcentaje_ingresos_acumulados'] = gb.ingresos_acumulados / \
                                               gb.ingresos_acumulados.sum() * \
                                               100
        gb['egresos_acumulados'] = gb.loc[gb.tipo == 'Egreso'].importe
        gb['porcentaje_egresos_acumulados'] = gb.egresos_acumulados / \
                                              gb.egresos_acumulados.sum() * 100

    gb = gb.where((notnull(gb)), None)

    return gb


def acumula_gb_impu_acumulada(df):
    cols = {'compra_cta_cte': sum,
            'compra_contado': sum,
            'nota_credito_recibida': sum,
            'nota_debito_recibida': sum,
            'egresos_cta_cte': sum,
            'egresos_contado': sum,
            'venta_cta_cte': sum,
            'venta_contado': sum,
            'nota_credito_emitida': sum,
            'nota_debito_emitida': sum,
            'cobranzas': sum,
            'total_egresos': sum}
    gb = DataFrame(df.groupby('acumulador', as_index=False).agg(cols))

    return gb


def imputacion_gb_impu_acumulada(df):
    cols = ['acumulador', 'tipo_movim', ]
    gb = DataFrame(df.groupby(cols, as_index=False).agg({'importe': 'sum'}))

    return gb


def mapper(month):
    # locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
    return month.strftime('%b').capitalize()


def filter_movimpu(df):
    # Esto se haría con el año actual, pero acá no tengo datos.
    # Habría que controlar que existan datos para los meses del año actual.
    # year = today().year
    # year = 2017
    # start = datetime(year - 1, 7, 1)
    # end = datetime(year, 6, 30)
    # title = title_period(start, end)

    df.loc[:, 'periodo_contable'] = to_datetime(df['periodo_contable'])
    df.loc[:, 'nro_mes'] = df['periodo_contable'].dt.month
    df.loc[:, 'mes'] = df['periodo_contable'].apply(mapper)
    df.loc[:, 'año'] = df['periodo_contable'].dt.year \
        .astype('str')

    return df


def index_ingresos_egresos_anual_line(df):
    gb = DataFrame(df.groupby(['año', 'mes', 'nro_mes'], as_index=False)
                   .agg({'importe': 'sum'})).sort_values(['año', 'nro_mes'])
    gb = gb.set_index(['año', 'mes'])
    source = ColumnDataSource(gb)

    ingresos = df[df['tipo'] == 'Ingreso'].copy()
    egresos = df[df['tipo'] == 'Egreso'].copy()

    gb_ingresos = DataFrame(ingresos.groupby(['año', 'mes', 'nro_mes'],
                                             as_index=False)
                            .agg({'importe': 'sum'})).sort_values(['año',
                                                                   'nro_mes'])
    gb_ingresos = gb_ingresos.set_index(['año', 'mes'])
    gb_ingresos['tipo'] = 'Ingreso'
    source_ingresos = ColumnDataSource(gb_ingresos)
    gb_egresos = DataFrame(egresos.groupby(['año', 'mes', 'nro_mes'],
                                           as_index=False)
                           .agg({'importe': 'sum'})).sort_values(['año',
                                                                  'nro_mes'])
    gb_egresos = gb_egresos.set_index(['año', 'mes'])
    gb_egresos['tipo'] = 'Egreso'
    source_egresos = ColumnDataSource(gb_egresos)

    tooltips = [
        ('', '@tipo'),
        ("Año, Mes", "@{año_mes}"),
        ("Importe total", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['circle'], tooltips=tooltips)
    plot = figure(
        x_range=FactorRange(*source.data['año_mes']),
        tools=["tap,reset,save,crosshair", hovertool],
        toolbar_location='above')
    plot.line(x='año_mes', y='importe', source=source_ingresos,
              line_color='green')
    plot.circle(x='año_mes', y='importe', source=source_ingresos,
                fill_color='green', line_color='green',
                name='circle', size=8, nonselection_fill_alpha=0.2)
    plot.line(x='año_mes', y='importe', source=source_egresos,
              line_color='red')
    plot.circle(x='año_mes', y='importe', source=source_egresos,
                fill_color='red', line_color='red',
                name='circle', size=8, nonselection_fill_alpha=0.2)
    set_plot_properties(plot)
    plot.xaxis.group_text_font = 'Montserrat'
    plot.yaxis.formatter = NumeralTickFormatter(format="$0")
    plot.sizing_mode = 'stretch_width'

    return plot


def ingresos_egresos_pie(df):
    df.loc[df['tipo'] == 'Ingreso', 'color'] = get_palet('1', color='greens')
    df.loc[df['tipo'] == 'Egreso', 'color'] = get_palet('1', color='reds')
    percentage = abs(df.importe / df.importe.sum() * 100)
    df['percentage'] = round(percentage, 2)
    df['angle'] = df.importe / df.importe.sum() * 2 * pi
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]
    tooltips = [("", "@{tipo}"),
                ("Total", "@importe{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(tools=[hovertool], toolbar_location='right')
    plot.wedge(x=0, y=0, source=source, radius=0.5,
               start_angle=cumsum('angle', include_zero=True),
               end_angle=cumsum('angle'),
               line_color='white', line_width=0.4,
               fill_color='color', name='wedge')
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)
    plot.sizing_mode = 'stretch_both'

    return plot


def get_ingresos_egresos(df):
    gb = DataFrame(df.groupby(['tipo'], as_index=False).agg({'importe': 'sum'}))

    ingresos = gb.loc[gb.tipo == 'Ingreso'].importe.copy()
    ingresos = round(float(ingresos), 2) if not ingresos.empty else None

    egresos = gb.loc[gb.tipo == 'Egreso'].importe.copy()
    egresos = round(float(egresos), 2) if not egresos.empty else None

    plot = ingresos_egresos_pie(gb)

    return ingresos, egresos, plot


# Separación de categorías de Imputaciones.
venta_mixta = ['Ventas Animales', 'Venta De Hacienda I']
venta_tambo = ['Venta De Leche']
venta_agricultura = ['Ventas De Cereales']
impu_mixta = ['Crianza I', 'Flete Ganaderia', 'Gastos Ganaderia',
              'Gastos Veterinaria', 'Suplementación I',
              'Suplementación Recría', 'Compra Hacienda']
impu_agricultura = ['Agroquimicos', 'Combustible', 'Fertilizantes',
                    'Flete Agricultura', 'Gastos Varios Maquinaria',
                    'Inoculantes', 'Insumos De Semillas',
                    'Lubricante Maquinaria', 'Mixer',
                    'Personal Maquinaria', 'Reparación Tractores',
                    'Semillas', 'Silos', 'Rollos', 'Gastos De Forraje']
impu_tambo = ['Control Lechero', 'Energía Tambo', 'Higiene Tambo',
              'Higiene Tambo I', 'Honorarios Tambero', 'Ordeñadora I',
              'Otros Gastos Tambo', 'Sanidad Tambo',
              'Suplementación Tambo', 'Suplementación Guachera']


def get_costos(movimpu_df, actividad, acumuladores):
    return movimpu_df[((movimpu_df.tipo == 'Egreso') & (movimpu_df.actividad == actividad)) |
                      movimpu_df.acumulador.isin(acumuladores)].importe.sum()


def get_ventas(movimpu_df, actividad, acumuladores):
    return movimpu_df[((movimpu_df.tipo == 'Ingreso') & (movimpu_df.actividad == actividad)) |
                      movimpu_df.acumulador.isin(acumuladores)].importe.sum()


def rentabilidad_actividad(movimpu_df):
    patrimonio_neto = get_patrimonio_neto()
    activos = get_activos()

    # Agricultura
    costos = get_costos(movimpu_df, 'Agricultura', impu_agricultura)
    ventas = get_ventas(movimpu_df, 'Agricultura', venta_agricultura)
    utilidad_neta = ventas - costos
    utilidad = utilidad_neta / ventas * 100
    roa = utilidad_neta / activos['total']
    roe = (ventas - costos) / patrimonio_neto
    agricultura = {
        'ventas': ventas,
        'costos': costos,
        'utilidad_neta': utilidad_neta,
        'utilidad': utilidad,
        'roa': roa,
        'roe': roe,
    }

    # Tambo
    costos = get_costos(movimpu_df, 'Tambo', impu_tambo)
    ventas = get_ventas(movimpu_df, 'Tambo', venta_tambo)
    utilidad_neta = ventas - costos
    if utilidad_neta < 0:
        utilidad = utilidad_neta * 100
    else:
        utilidad = utilidad_neta / ventas * 100
    roa = utilidad_neta / activos['total']
    roe = (ventas - costos) / patrimonio_neto
    tambo = {
        'ventas': ventas,
        'costos': costos,
        'utilidad_neta': utilidad_neta,
        'utilidad': utilidad,
        'roa': roa,
        'roe': roe,
    }

    return agricultura, tambo


def get_vbar_plot(source, x, y, tooltips, height=None):
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(x_range=FactorRange(*source.data[x],
                                      bounds='auto'),
                  y_range=Range1d(start=0,
                                  end=max(source.data[y]) +
                                      max(source.data[y]) * PLOT_PADDING,
                                  bounds='auto'),
                  tools=["tap,reset,save,crosshair", hovertool],
                  toolbar_location='above')
    plot.vbar(
        x=x, top=y, width=0.9, source=source,
        nonselection_fill_alpha=0.2, line_color=None,
        fill_color='color', name='vbar')
    if height:
        plot.height = height
    plot.text(
        y=source.data[y],
        x=source.data[x],
        text=source.data['percentage'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(format="$0")
    if len(source.data[x]) > 6:
        plot.xaxis[0].major_label_orientation = 0.3
    plot.sizing_mode = 'stretch_width'

    return plot


def rentabilidad_bars(movimpu_df):
    plots = {'rentabilidad_pie': rentabilidad_pie(movimpu_df)}
    detalle_ventas = {}

    # Agricultura
    costos = movimpu_df[((movimpu_df.tipo == 'Egreso') & (movimpu_df.actividad == 'Agricultura')) |
                        movimpu_df.acumulador.isin(impu_agricultura)].copy()
    # costos = movimpu_df[movimpu_df.acumulador.isin(impu_agricultura)].copy()
    df = DataFrame(costos.groupby(['acumulador']).importe.sum())
    df.sort_values('importe', ascending=False, inplace=True)
    df['color'] = get_palet(df.importe, 'reds')
    percentage = abs(df.importe) / abs(df.importe).sum() * 100
    df['percentage'] = round(percentage, 1)
    df['angle'] = abs(df.importe) / abs(df.importe).sum() * 2 * pi
    source_costos = ColumnDataSource(df)
    source_costos.data['percentage'] = [f'{x}%' for x in source_costos.data['percentage']]
    tooltips = [('Acumulador', '@{acumulador}'),
                ("Importe", "@importe{$0,0.00}")]
    plots['agricultura_costos'] = get_vbar_plot(source=source_costos, x='acumulador', y='importe',
                                                tooltips=tooltips, height=450)

    ventas = movimpu_df[((movimpu_df.tipo == 'Ingreso') & (movimpu_df.actividad == 'Agricultura')) |
                        movimpu_df.acumulador.isin(venta_agricultura)].copy()
    # ventas = movimpu_df[movimpu_df.acumulador.isin(venta_agricultura)].copy()
    df = DataFrame(ventas.groupby(['acumulador']).importe.sum())
    df.sort_values('importe', ascending=False, inplace=True)
    lista = []
    for index, row in df.iterrows():
        lista.append((index, row['importe']))
    detalle_ventas['agricultura_ventas'] = lista

    # Tambo
    costos = movimpu_df[((movimpu_df.tipo == 'Egreso') & (movimpu_df.actividad == 'Tambo')) |
                        movimpu_df.acumulador.isin(impu_tambo)].copy()
    # costos = movimpu_df[movimpu_df.acumulador.isin(impu_tambo)].copy()
    df = DataFrame(costos.groupby(['acumulador']).importe.sum())
    df.sort_values('importe', ascending=False, inplace=True)
    df['color'] = get_palet(df.importe, 'reds')
    percentage = abs(df.importe) / abs(df.importe).sum() * 100
    df['percentage'] = round(percentage, 1)
    df['angle'] = abs(df.importe) / abs(df.importe).sum() * 2 * pi
    source_costos = ColumnDataSource(df)
    source_costos.data['percentage'] = [f'{x}%' for x in source_costos.data['percentage']]
    tooltips = [('Acumulador', '@{acumulador}'),
                ("Importe", "@importe{$0,0.00}")]
    plots['tambo_costos'] = get_vbar_plot(source=source_costos, x='acumulador', y='importe',
                                          tooltips=tooltips, height=450)

    ventas = movimpu_df[((movimpu_df.tipo == 'Ingreso') & (movimpu_df.actividad == 'Tambo')) |
                        movimpu_df.acumulador.isin(venta_tambo)].copy()
    # ventas = movimpu_df[movimpu_df.acumulador.isin(venta_tambo)].copy()
    df = DataFrame(ventas.groupby(['acumulador']).importe.sum())
    df.sort_values('importe', ascending=False, inplace=True)
    lista = []
    for index, row in df.iterrows():
        lista.append((index, row['importe']))
    detalle_ventas['tambo_ventas'] = lista

    return plots, detalle_ventas


def rentabilidad_actividad_table(movimpu_df):
    imputaciones_costos = ['Crianza I', 'Flete Ganaderia', 'Gastos Ganaderia',
                           'Gastos Veterinaria',
                           'Suplementación I', 'Suplementación Recría',
                           'Compra Hacienda', 'Agroquimicos', 'Combustible',
                           'Fertilizantes', 'Flete Agricultura',
                           'Gastos Varios Maquinaria', 'Inoculantes',
                           'Insumos De Semillas',
                           'Lubricante Maquinaria', 'Mixer',
                           'Personal Maquinaria',
                           'Reparación Tractores',
                           'Semillas', 'Silos', 'Rollos', 'Gastos De Forraje',
                           'Control Lechero', 'Energía Tambo', 'Higiene Tambo',
                           'Higiene Tambo I',
                           'Honorarios Tambero', 'Ordeñadora I',
                           'Otros Gastos Tambo',
                           'Sanidad Tambo',
                           'Suplementación Tambo', 'Suplementación Guachera']
    imputaciones_ventas = ['Ventas Animales', 'Venta De Hacienda I',
                           'Venta De Leche',
                           'Ventas De Cereales']
    imputaciones_ganado = ['Crianza I', 'Flete Ganaderia', 'Gastos Ganaderia',
                           'Gastos Veterinaria',
                           'Suplementación I', 'Suplementación Recría',
                           'Compra Hacienda',
                           'Ventas Animales', 'Venta De Hacienda I']
    imputaciones_agricultura = ['Agroquimicos', 'Combustible', 'Fertilizantes',
                                'Flete Agricultura',
                                'Gastos Varios Maquinaria', 'Inoculantes',
                                'Insumos De Semillas',
                                'Lubricante Maquinaria', 'Mixer',
                                'Personal Maquinaria',
                                'Reparación Tractores',
                                'Semillas', 'Silos', 'Rollos',
                                'Gastos De Forraje',
                                'Ventas De Cereales']
    imputaciones_tambo = ['Control Lechero', 'Energía Tambo', 'Higiene Tambo',
                          'Higiene Tambo I', 'Honorarios Tambero',
                          'Ordeñadora I', 'Otros Gastos Tambo', 'Sanidad Tambo',
                          'Suplementación Tambo',
                          'Suplementación Guachera', 'Venta De Leche']

    movimpu_df.loc[movimpu_df.acumulador.isin(
        imputaciones_costos), 'tipo'] = 'Costos'
    movimpu_df.loc[movimpu_df.acumulador.isin(
        imputaciones_ventas), 'tipo'] = 'Ventas'

    ganado = movimpu_df.loc[movimpu_df.acumulador
        .isin(imputaciones_ganado)].copy()
    agricultura = movimpu_df.loc[movimpu_df.acumulador
        .isin(imputaciones_agricultura)].copy()
    tambo = movimpu_df.loc[movimpu_df.acumulador
        .isin(imputaciones_tambo)].copy()

    rentabilidad = {
        'ganado': ganado,
        'agricultura': agricultura,
        'tambo': tambo,
    }

    return rentabilidad


def rentabilidad_pie(movimpu_df, background=False):
    agricultura, tambo = rentabilidad_actividad(movimpu_df)
    rentabilidad = {
        'categoria': ['Agricultura', 'Tambo'],
        'utilidad': [agricultura['utilidad'], tambo['utilidad']]
    }

    df = DataFrame(rentabilidad)
    df.loc[df.utilidad < 0, 'color'] = get_palet(
        df.loc[df.utilidad < 0], 'reds')
    df.loc[df.utilidad > 0, 'color'] = get_palet(
        df.loc[df.utilidad > 0], 'greens')
    percentage = abs(df.utilidad) / abs(df.utilidad).sum() * 100
    df['percentage'] = round(percentage, 1)
    df['angle'] = abs(df.utilidad) / abs(df.utilidad).sum() * 2 * pi
    # df['cumulative_angle'] = (abs(df.utilidad)/2) / abs(
    #     df.utilidad).sum() * 2 * pi
    # df['cos'] = np.cos(df['cumulative_angle']) * 0.3
    # df['sin'] = np.sin(df['cumulative_angle']) * 0.3
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]
    source.data['utilidad'] = [f'{round(x, 2)}%' for x in source.data[
        'utilidad']]

    tooltips = [("Categoría", "@categoria"),
                ("Utilidad", "@utilidad"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["save", hovertool],
        toolbar_location='above', height=200, width=300)
    w = plot.wedge(x=0, y=0, radius=0.8,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4, fill_color='color',
                   source=source, name='wedge')
    legend = Legend(
        items=[LegendItem(label=dict(field="categoria"),
                          renderers=[w])])
    plot.add_layout(legend, 'right')
    if background:
        plot.background_fill_color = '#343a40'
        plot.border_fill_color = '#343a40'
        plot.legend.background_fill_color = '#343a40'
        plot.legend.label_text_color = 'white'
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)

    return plot


def get_activos():
    activos = {}
    """Activos"""
    # Activo Corriente
    # Ganado
    mov_gan = DataFrame(
        Movgan.objects.values('nro_novedad', 'fecha', 'entrada_salida',
                              'total'))
    valor_ganado = mov_gan[mov_gan.entrada_salida == 1].total.sum()

    # Silos
    silos = DataFrame(Silos.objects.values())
    silos['total'] = silos[["stock", "valor"]].product(axis=1)
    valor_silos = silos.total.sum()

    # Bolsas
    bolsas = DataFrame(Bolsas.objects.values('costo'))
    valor_bolsas = bolsas.costo.sum()

    # Productos
    productos = DataFrame(
        Producto.objects.values('descripcion', 'stock_unidades',
                                'precio_compra'))
    productos['total'] = productos[["stock_unidades", "precio_compra"]].product(
        axis=1)
    valor_productos = productos.total.sum()

    # Cultivo
    cultivo = DataFrame(Cultivo.objects.values('costo'))
    valor_cultivo = cultivo.costo.sum()

    # Saldo Banco
    # libro_banco = DataFrame(Libroba.objects.values('identificacion', 'importe'))
    # gb = libro_banco.groupby(['identificacion'])
    # ingresos = gb.get_group(2).importe.sum() + gb.get_group(4).importe.sum()
    # egresos = gb.get_group(1).importe.sum() + gb.get_group(
    #     3).importe.sum() + gb.get_group(6).importe.sum() + gb.get_group(
    #     7).importe.sum()
    # saldo_banco = ingresos - egresos

    # Saldo Cajas
    gf = DataFrame(Gf.objects.values('i_o_e', 'importe'))
    gb = gf.groupby(['i_o_e'])
    egresos = gb.get_group(2).importe.sum()
    ingresos = gb.get_group(1).importe.sum() + 1212 + 25000
    saldo_cajas = ingresos - egresos

    # Documentos Pendientes de Cobro
    pendiente_cobro = DataFrame(Pendcobro.objects.values('saldo'))
    cobros_pendientes = pendiente_cobro.saldo.sum()

    # Cheques en Cartera
    cheques_cartera = DataFrame(Cheques.objects.values('importe').filter(fec_salida__isnull=True))
    valor_cheques_cartera = cheques_cartera.importe.sum()

    activos['inventario'] = valor_ganado + valor_productos + \
                            valor_silos + valor_bolsas + valor_cultivo
    activos['corriente'] = valor_ganado + valor_productos + \
                           valor_silos + valor_bolsas + valor_cultivo + \
                           saldo_cajas + cobros_pendientes + valor_cheques_cartera

    # Activo no corriente
    # Maquinas
    maquinas = DataFrame(Maquina.objects.values('costo_de_compra'))
    valor_maquinas = maquinas.costo_de_compra.sum()

    # Transporte
    transporte = DataFrame(Transp.objects.values('costo_de_compra'))
    valor_transporte = transporte.costo_de_compra.sum()

    activos['no_corriente'] = valor_maquinas + valor_transporte

    activos['total'] = activos['corriente'] + activos['no_corriente']

    return activos


def get_pasivos():
    pasivos = {}
    """Pasivos"""
    # Pendientes de Pago
    pendiente_pago = DataFrame(Pendpago.objects.values('saldo'))
    pagos_pendientes = pendiente_pago.saldo.sum()

    pasivos['corriente'] = pagos_pendientes
    pasivos['no_corriente'] = 0
    pasivos['total'] = pasivos['corriente'] + pasivos['no_corriente']

    return pasivos


def get_liquidez():
    indices_liquidez = {}
    activos = get_activos()
    pasivos = get_pasivos()

    indices_liquidez['liquidez_corriente'] = \
        activos['corriente'] / pasivos['corriente']
    indices_liquidez['liquidez_seca'] = \
        (activos['corriente'] - activos['inventario']) / pasivos['corriente']
    indices_liquidez['capital_trabajo'] = \
        activos['corriente'] - pasivos['corriente']

    return indices_liquidez


def get_patrimonio_neto():
    activos = get_activos()
    pasivos = get_pasivos()
    patrimonio_neto = activos['total'] - pasivos['total']
    return patrimonio_neto


def get_endeudamiento():
    endeudamiento = {}
    patrimonio_neto = get_patrimonio_neto()
    activos = get_activos()
    pasivos = get_pasivos()

    endeudamiento['sobre_patrimonio_neto'] = \
        pasivos['total'] * 100 / patrimonio_neto
    endeudamiento['sobre_activo_total'] = \
        pasivos['total'] * 100 / activos['total']

    return endeudamiento


def get_activos_pasivos_plot(source):
    tooltips = [('Categoría', '@{categoria}'),
                ("Importe", "@importe{$0,0.00}")]
    hovertool = HoverTool(names=['vbar'], tooltips=tooltips)
    plot = figure(x_range=FactorRange(*source.data['categoria'],
                                      bounds='auto'),
                  y_range=Range1d(start=0,
                                  end=max(source.data['importe']) +
                                      max(source.data[
                                              'importe']) * PLOT_PADDING,
                                  bounds='auto'),
                  tools=["tap,reset,save,crosshair", hovertool],
                  toolbar_location='above', height=450)
    plot.vbar(
        x='categoria', top='importe', width=0.9, source=source,
        nonselection_fill_alpha=0.2, line_color=None,
        fill_color='color', name='vbar')
    plot.text(
        y=source.data['importe'],
        x=source.data['categoria'],
        text=source.data['percentage'],
        y_offset=-8, text_align='center',
        text_baseline="middle",
        text_font='Montserrat', text_font_size='1em')
    set_plot_properties(plot)
    plot.yaxis[0].formatter = NumeralTickFormatter(format="$0")
    if len(source.data['categoria']) > 6:
        plot.xaxis[0].major_label_orientation = 0.3
    plot.sizing_mode = 'stretch_width'

    return plot


def activos_vbar():
    activos = {}
    # Ganado
    mov_gan = DataFrame(
        Movgan.objects.values('nro_novedad', 'fecha', 'entrada_salida', 'total'))
    valor_ganado = mov_gan[mov_gan.entrada_salida == 1].total.sum()

    # Silos
    silos = DataFrame(Silos.objects.values())
    silos['total'] = silos[["stock", "valor"]].product(axis=1)
    valor_silos = silos.total.sum()

    # Bolsas
    bolsas = DataFrame(Bolsas.objects.values('costo'))
    valor_bolsas = bolsas.costo.sum()

    # Productos
    productos = DataFrame(
        Producto.objects.values('descripcion', 'stock_unidades', 'precio_compra'))
    productos['total'] = productos[["stock_unidades", "precio_compra"]].product(
        axis=1)
    valor_productos = productos.total.sum()

    # Cultivo
    cultivo = DataFrame(Cultivo.objects.values('costo'))
    valor_cultivo = cultivo.costo.sum()

    # Saldo Cajas
    gf = DataFrame(Gf.objects.values('i_o_e', 'importe'))
    gb = gf.groupby(['i_o_e'])
    egresos = gb.get_group(2).importe.sum()
    ingresos = gb.get_group(1).importe.sum() + 1212 + 25000
    saldo_cajas = ingresos - egresos

    # Documentos Pendientes de Cobro
    pendiente_cobro = DataFrame(Pendcobro.objects.values('saldo'))
    cobros_pendientes = pendiente_cobro.saldo.sum()

    # Cheques en Cartera
    cheques_cartera = DataFrame(Cheques.objects.values('importe').filter(fec_salida__isnull=True))
    valor_cheques_cartera = cheques_cartera.importe.sum()

    # Maquinas
    maquinas = DataFrame(Maquina.objects.values('costo_de_compra'))
    valor_maquinas = maquinas.costo_de_compra.sum()

    # Transporte
    transporte = DataFrame(Transp.objects.values('costo_de_compra'))
    valor_transporte = transporte.costo_de_compra.sum()

    activos['categoria'] = ['Ganado', 'Silos', 'Bolsas', 'Productos',
                            'Cultivo', 'Cajas', 'Cobros Pendientes',
                            'Maquinas', 'Transporte', 'Cheques Cartera']
    activos['importe'] = [valor_ganado, valor_silos, valor_bolsas,
                          valor_productos, valor_cultivo,
                          saldo_cajas, cobros_pendientes,
                          valor_maquinas, valor_transporte, valor_cheques_cartera]

    df = DataFrame(activos)
    df.sort_values('importe', ascending=False, inplace=True)
    df['color'] = get_palet(df['importe'], color='greens')
    percentage = df.importe / df.importe.sum() * 100
    df['percentage'] = round(percentage, 1)
    df = df[(df.percentage >= 0.1)]
    df['angle'] = df.importe / df.importe.sum() * 2 * pi
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in
                                 source.data['percentage']]
    plot = get_activos_pasivos_plot(source)

    return plot


def pasivos_vbar():
    pasivos = {}
    # Pendientes de Pago
    pendiente_pago = DataFrame(Pendpago.objects.values('saldo'))
    pagos_pendientes = pendiente_pago.saldo.sum()

    pasivos['categoria'] = ['Pagos Pendientes']
    pasivos['importe'] = [pagos_pendientes]

    df = DataFrame(pasivos)
    df.sort_values('importe', ascending=False, inplace=True)
    df['color'] = get_palet(df['importe'], color='reds')
    percentage = df.importe / df.importe.sum() * 100
    df['percentage'] = round(percentage, 1)
    df['angle'] = df.importe / df.importe.sum() * 2 * pi
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in
                                 source.data['percentage']]
    plot = get_activos_pasivos_plot(source)

    return plot


def patrimonio_neto_pie(background=False):
    patrimonio_neto = {}
    activos = get_activos()
    pasivos = get_pasivos()
    patrimonio_neto['categoria'] = ['Activos', 'Pasivos']
    patrimonio_neto['importe'] = [activos['total'], pasivos['total']]

    df = DataFrame(patrimonio_neto)
    df.sort_values('importe', ascending=False, inplace=True)
    df.loc[df['categoria'] == 'Activos', 'color'] = get_palet('1',
                                                              color='greens')
    df.loc[df['categoria'] == 'Pasivos', 'color'] = get_palet('1', color='reds')
    percentage = df.importe / df.importe.sum() * 100
    df['percentage'] = round(percentage, 1)
    df['angle'] = df.importe / df.importe.sum() * 2 * pi
    source = ColumnDataSource(df)
    source.data['percentage'] = [f'{x}%' for x in
                                 source.data['percentage']]
    plot = patrimonio_neto_plot(source, background)

    return plot


def patrimonio_neto_plot(source, background=False):
    tooltips = [("Categoría", "@categoria"),
                ("Importe", "@importe{$0,0.00}"),
                ('% del total', '@percentage')]
    hovertool = HoverTool(names=['wedge'], tooltips=tooltips)
    plot = figure(
        tools=["save", hovertool],
        toolbar_location='above', height=200, width=300)
    w = plot.wedge(x=0, y=0, radius=0.7,
                   start_angle=cumsum('angle', include_zero=True),
                   end_angle=cumsum('angle'),
                   line_color='white', line_width=0.4, fill_color='color',
                   # legend_field='categoria',
                   source=source, name='wedge')
    legend = Legend(
        items=[LegendItem(label=dict(field="categoria"),
                          renderers=[w])])
    plot.add_layout(legend, 'right')
    if background:
        plot.border_fill_color = '#343a40'
        plot.background_fill_color = '#343a40'
        plot.legend.background_fill_color = '#343a40'
        plot.legend.label_text_color = 'white'
    set_plot_properties(plot)
    delete_xaxis(plot)
    delete_yaxis(plot)

    return plot
