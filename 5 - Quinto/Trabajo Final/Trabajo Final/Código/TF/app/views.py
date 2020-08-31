from bokeh.embed import components
from bokeh.models import ColumnDataSource
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from numpy import pi
from pandas import DataFrame, to_datetime
from psycopg2 import Error

from Utils.update_db import update_db
from app.filters import MovImpuFilter, AcumulaFilter, ActividadFilter, \
    PeriodoContableFilter
from app.forms import MovImpuForm, IMPU_CHOICES, AcumulaForm, ACUMULA_CHOICES, \
    ActividadForm, ACTIVIDAD_CHOICES, LoginForm, RegisterForm
from app.models import MovCons, Gf, Items, Movgan, MovSilos, MovProd, Movimpu
from app.tables import MovimpuTable, AcumulaTable, ActividadTable
from app.utils import get_movimpu, detalle_actividad_pie, \
    detalle_actividad_vbar, actividad_pie, get_palet, get_imputaci, \
    acumula_vbar, acumula_pie, actividad_vbar, get_df_mov_impu, \
    title_period, gb_actividad, \
    acumula_gb_impu_acumulada, index_ingresos_egresos_anual_line, impu_plots, \
    detalle_impu_plots, mapper, get_ingresos_egresos, detalle_acumula_plots, \
    rentabilidad_actividad, get_liquidez, get_activos, get_pasivos, \
    get_patrimonio_neto, get_endeudamiento, activos_vbar, pasivos_vbar, \
    patrimonio_neto_pie, rentabilidad_actividad_table, rentabilidad_pie, \
    rentabilidad_bars

PER_PAGE = 15


def register_user(request):
    # Comprobar que no haya un usuario actualmente logueado.
    # if request.user.is_authenticated:
    #     return redirect('index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear usuario.
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            user = authenticate(request,
                                username=user.username,
                                password=user.password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'app/register.html', {'form': form})
    else:
        form = RegisterForm()

    return render(request, 'app/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Los datos ingresados no son '
                                        'válidos.')
    else:
        # if request.user.is_authenticated:
        #     return redirect('index')

        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(index)


def update_data(request):
    # if not request.user.is_authenticated:
    #     return redirect(login_user)

    try:
        update_db()
        messages.success(request, 'Base de datos actualizada correctamente.')
    except Error:
        messages.error(request, 'No se pudo actualizar la Base de datos.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def index(request):
    # mov_cons = DataFrame(
    #     MovCons.objects.values('fecha', 'nro_comprob', 'ing_egr', 'costo'))
    # gb = mov_cons.groupby(['ing_egr'])
    # combustible = {
    #     'ingreso': gb.get_group(1).costo.sum(),
    #     'egreso': gb.get_group(2).costo.sum(),
    # }
    # gf = DataFrame(Gf.objects.values('n_comp', 'fecha', 'i_o_e', 'importe'))
    # gb = gf.groupby(['i_o_e'])
    # caja = {
    #     'ingreso': gb.get_group(1).importe.sum(),
    #     'egreso': gb.get_group(2).importe.sum(),
    # }
    # items = DataFrame(
    #     Items.objects.values('fecha', 'nro_comprobante', 'movimiento',
    #                          'nro_producto__nro_linea__nombre'))
    # gb = items.groupby(['movimiento'])
    # productos = {
    #     'ingreso': gb.get_group(1),
    #     # 'egreso': gb.get_group(2),
    # }
    # mov_silos = DataFrame(MovSilos.objects.values('movimiento', 'fecha',
    #                                               'nro_comprobante'))
    # gb = mov_silos.groupby(['movimiento'])
    # granos = {
    #     'ingreso': gb.get_group(1),
    #     'egreso': gb.get_group(2),
    # }
    # mov_prod = DataFrame(
    #     MovProd.objects.values('fecha', 'ing_egr', 'nro_comprob'))
    # gb = mov_prod.groupby(['ing_egr'])
    # leche = {
    #     # 'ingreso': gb.get_group(1),
    #     'egreso': gb.get_group(2),
    # }
    #
    # imputacion_ganado = ['Crianza I', 'Flete Ganaderia', 'Gastos Ganaderia',
    #                      'Gastos Veterinaria', 'Suplementación Recría']
    # movimpu_df = DataFrame(
    #     Movimpu.objects.values('cod_imput__donde_acumula__descripcion',
    #                            'importe'))
    # movimpu_df = movimpu_df[
    #     movimpu_df.cod_imput__donde_acumula__descripcion.isin(
    #     imputacion_ganado)]
    # costos = movimpu_df.importe.sum()
    # mov_gan = DataFrame(
    #     Movgan.objects.values('nro_novedad', 'fecha', 'entrada_salida',
    #                           'categoria__descripcion', 'total'))
    # gb = mov_gan.groupby('entrada_salida')
    # compras = gb.get_group(1).total.sum()
    # ventas = gb.get_group(2).total.sum()
    # ganancia = (ventas - (compras + costos)) / ventas
    # rentabilidad = (ventas - compras) / ventas * 100
    # ganado = {
    #     'compras': compras,
    #     'ventas': ventas,
    #     'ganancia': ganancia,
    #     'rentabilidad': rentabilidad,
    # }

    # delete_problematic_records()

    movimpu = get_movimpu()
    movimpu_df = get_df_mov_impu(movimpu)
    agricultura, tambo = rentabilidad_actividad(movimpu_df)
    utilidad_neta = agricultura['utilidad_neta'] + tambo['utilidad_neta']
    ventas = agricultura['ventas'] + tambo['ventas']
    rentabilidad_total = utilidad_neta / ventas * 100
    activos = get_activos()
    pasivos = get_pasivos()
    liquidez = get_liquidez()
    patrimonio_neto = get_patrimonio_neto()
    endeudamiento = get_endeudamiento()
    script, div = components({
        'rentabilidad': rentabilidad_pie(movimpu_df, background=True),
        'patrimonio_neto': patrimonio_neto_pie(background=True)
    })

    return render(request, 'app/index.html',
                  {'agricultura': agricultura,
                   'tambo': tambo,
                   'liquidez': liquidez,
                   'activos': activos, 'pasivos': pasivos,
                   'patrimonio_neto': patrimonio_neto,
                   'endeudamiento': endeudamiento,
                   'rentabilidad_total': rentabilidad_total,
                   'script': script, 'div': div})


def detail_patrimonio_neto(request):
    patrimonio_neto = get_patrimonio_neto()
    activos = get_activos()
    pasivos = get_pasivos()
    plot_activos = activos_vbar()
    plot_pasivos = pasivos_vbar()
    plot_patrimonio_neto = patrimonio_neto_pie()
    script, div = components({'plot_activos': plot_activos,
                              'plot_pasivos': plot_pasivos,
                              'plot_patrimonio_neto': plot_patrimonio_neto})

    return render(request, 'app/detail_patrimonio_neto.html',
                  {'activos': activos, 'pasivos': pasivos,
                   'patrimonio_neto': patrimonio_neto,
                   'script': script, 'div': div})


def detail_rentabilidad_actividad(request):
    title_periodo = None
    movimpu = get_movimpu()
    movimpu_filter = MovImpuFilter(request.GET, queryset=movimpu)
    if movimpu_filter.data and movimpu_filter.qs:
        movimpu = movimpu_filter.qs
        inicio = movimpu_filter.form.cleaned_data['inicio_periodo']
        fin = movimpu_filter.form.cleaned_data['fin_periodo']
        title_periodo = title_period(inicio, fin)

    if not movimpu_filter.qs:
        messages.error(request, 'No se encontraron resultados.')

    movimpu_df = get_df_mov_impu(movimpu)
    rentabilidad = rentabilidad_actividad_table(movimpu_df)
    table_ganado = MovimpuTable(rentabilidad['ganado'].to_dict('records'))
    table_agricultura = MovimpuTable(
        rentabilidad['agricultura'].to_dict('records'))
    table_tambo = MovimpuTable(rentabilidad['tambo'].to_dict('records'))
    RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(
        table_ganado)
    RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(
        table_agricultura)
    RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(
        table_tambo)
    tables = {
        'ganado': table_ganado,
        'agricultura': table_agricultura,
        'tambo': table_tambo,
    }

    agricultura, tambo = rentabilidad_actividad(movimpu_df)
    utilidad_neta = agricultura['utilidad_neta'] + tambo['utilidad_neta']
    total_ventas = agricultura['ventas'] + tambo['ventas']
    rentabilidad_total = utilidad_neta / total_ventas * 100

    plots, ventas = rentabilidad_bars(movimpu_df)
    script, div = components(plots)

    return render(request, 'app/detail_rentabilidad_actividad.html',
                  {'tables': tables, 'title_periodo': title_periodo,
                   'script': script, 'div': div, 'filter': movimpu_filter,
                   'agricultura': agricultura,
                   'tambo': tambo, 'rentabilidad_total': rentabilidad_total,
                   'ventas': ventas})


# def compras_ventas(request):
#     if request.method == 'GET':
#         form = VentasForm()
#
#         importe_ventas = Ventas.objects.values('descripcion', 'imp_total')
#         df = DataFrame(importe_ventas)
#         df.rename(columns={'descripcion': 'cliente',
#                            'imp_total': 'importe'}, inplace=True)
#
#         df_group = DataFrame(df.groupby('cliente')
#                              .importe.sum())
#         df_group.sort_values('importe', inplace=True)
#         q = quantile(df_group.importe, q=0.75)
#         df_group = df_group[df_group.importe > q]
#         source = ColumnDataSource(df_group)
#
#         tooltips = [
#             ("Cliente", "@cliente"),
#             ("Importe", "@importe{($ 0)}"),
#         ]
#
#         # Crear figura.
#         plot = figure(
#             y_range=FactorRange(*source.data['cliente'], bounds='auto'),
#             x_range=Range1d(start=min(source.data['importe']),
#                             end=max(source.data['importe']),
#                             bounds='auto'),
#             tools="tap,reset,save",
#             tooltips=tooltips,
#             # active_scroll='wheel_zoom',
#             toolbar_location='above',
#             title="Importe total de Ventas",
#             x_axis_label='Importe',
#             y_axis_label='Clientes'
#         )
#
#         # Agregar gráfico.
#         plot.hbar(
#             source=source,
#             y='cliente', right='importe', left=0, height=0.8,
#             # legend='Importe',
#             fill_color=linear_cmap(field_name='importe',
#                                    palette=GnBu9,
#                                    low=min(source.data['importe']),
#                                    high=max(source.data['importe'])),
#             nonselection_fill_alpha=0.2,
#             line_color='Grey'
#         )
#         plot.grid.visible = False
#         plot.sizing_mode = 'scale_both'
#         plot.toolbar.autohide = True
#         plot.xaxis[0].formatter = NumeralTickFormatter(format="$0")
#
#         # Generar script y div para mostrar el gráfico.
#         script, div = components(plot)
#
#         return render(request, 'app/compras_ventas.html',
#                       {'form': form,
#                        'script': script,
#                        'div': div})
#     else:
#         form = VentasForm(request.POST)
#         if form.is_valid():
#             cliente = form.cleaned_data['cliente']
#             year = form.cleaned_data['año_periodo_contable']
#             month = form.cleaned_data['mes_periodo_contable']
#
#             filter_periodo = Ventas.objects.filter(descripcion=cliente)
#
#             # Ver de tirar un mensaje.
#             if not month and not year:
#                 filter_periodo = Ventas.objects.all()
#             elif not month:
#                 filter_periodo = Ventas.objects.filter(
#                     periodo_contable__year=year)
#             elif not year:
#                 filter_periodo = Ventas.objects.filter(
#                     periodo_contable__month=month)
#             else:
#                 filter_periodo = Ventas.objects.filter(
#                     periodo_contable__year=year,
#                     periodo_contable__month=month)
#
#             filter_periodo = filter_periodo.values('descripcion',
#                                                    'imp_total',
#                                                    'periodo_contable')
#
#             df = DataFrame(filter_periodo)
#             df.rename(columns={'descripcion': 'cliente',
#                                'imp_total': 'importe'},
#                       inplace=True)
#             df['periodo_contable'] = to_datetime(df.periodo_contable)
#             df['año'] = df['periodo_contable'].dt.year.astype(str)
#             df['mes'] = df['periodo_contable'].dt.month.astype(str)
#
#             df_group = DataFrame(df.groupby(['año', 'mes'])
#                                  .importe.sum())
#             df_group.sort_values(['año', 'mes'], inplace=True)
#             source = ColumnDataSource(df_group)
#
#             tooltips = [
#                 ("Fecha", "@año_mes"),
#                 ("Importe", "@importe{($ 0)}"),
#             ]
#
#             plot = figure(
#                 y_range=Range1d(start=min(source.data['importe']),
#                                 end=max(source.data['importe']),
#                                 bounds='auto'),
#                 x_range=FactorRange(*source.data['año_mes'],
#                                     bounds='auto'),
#                 tools="tap,reset,save",
#                 tooltips=tooltips,
#                 # active_scroll='wheel_zoom',
#                 toolbar_location='above',
#                 title="Importe total de Ventas",
#                 x_axis_label='Clientes',
#                 y_axis_label='Importe'
#             )
#
#             # Agregar gráfico.
#             plot.vbar(
#                 x='año_mes',
#                 top='importe',
#                 width=0.9,
#                 source=source,
#                 # legend='Importe',
#                 fill_color=factor_cmap(field_name='año_mes',
#                                        palette=Category20_20,
#                                        factors=df.año.unique(),
#                                        start=1, end=2),
#                 nonselection_fill_alpha=0.2,
#                 line_color=None
#             )
#             plot.yaxis[0].formatter = NumeralTickFormatter(format="$0")
#             plot.x_range.range_padding = 0.1
#             plot.xgrid.grid_line_color = None
#
#             # Generar script y div para mostrar el gráfico.
#             script, div = components(plot)
#
#             return render(request, 'app/compras_ventas.html',
#                           {'script': script,
#                            'div': div,
#                            'cliente': cliente})


# class ProveedorAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = Proctcte.objects.all().order_by('razon_social')
#         if self.q:
#             qs = qs.filter(razon_social__icontains=self.q)
#
#         return qs
#
#     def get_result_label(self, item):
#         return item.razon_social
#
#     def get_selected_result_label(self, item):
#         return item.razon_social


# def cta_cte_proveedor(request):
#     datos_proveedor = None
#     table = None
#     proveedor = get_proveedor_ctacte()
#     proveedor_filter = ProveedorFilter(request.GET, queryset=proveedor)
#     if proveedor_filter.data and proveedor_filter.qs:
#         proveedor = proveedor_filter.qs
#         df, datos_proveedor = get_df_proveedor_ctacte(proveedor)
#         table = ProveedorTable(df.to_dict('records'))
#         table.paginate(page=request.GET.get("page", 1), per_page=PER_PAGE)
#
#     if not proveedor_filter.qs:
#         messages.error(request, 'No se encontraron resultados.')
#
#     return render(request, 'app/proveedores.html',
#                   {'datos_proveedor': datos_proveedor,
#                    'table': table,
#                    'filter': proveedor_filter})


# def clientes(request):
#     df = get_cliente()
#     df_minor = df[df.saldo < 0].copy()
#     df_mayor = df[df.saldo > 0].copy()
#     df_equal = df[df.saldo == 0].copy()
#
#     tooltips = [("Saldo", "@saldo{$0.00}"),
#                 ("Participación total de compras",
#                  "@particip_total_compras{$0.00}"),
#                 ("Porcentaje total de compras", "@porcent_total_compras{0%}"),
#                 ("Tipo de cliente", "@tipo_cliente"),
#                 ("Iva", "@iva")]
#     _tabs = []
#     if not df_minor.empty:
#         source_minor = ColumnDataSource(df_minor)
#         source_minor.data['color'] = get_palet(source_minor.data['saldo'],
#                                                'reds')
#         hovertool = HoverTool(mode='hline', attachment='below',
#                               names=['hbar'], tooltips=tooltips)
#         plot_minor = figure(
#             title="Clientes con saldo mayor a cero",
#             y_range=FactorRange(*source_minor.data['razon_social'],
#                                 bounds='auto'),
#             x_range=Range1d(start=0,
#                             end=(max(source_minor.data['saldo']) +
#                                  max(source_minor.data[
#                                          'saldo']) * PLOT_PADDING),
#                             bounds='auto'),
#             tools=["tap,reset,save", hovertool],
#             toolbar_location='above',
#             y_axis_label='Cliente', x_axis_label='Saldo',
#             height=300)
#
#         plot_minor.hbar(
#             y='razon_social', right='saldo', height=0.8, source=source_minor,
#             fill_color='color', nonselection_fill_alpha=0.2,
#             line_color=None, name='hbar')
#         set_plot_properties(plot_minor)
#         plot_minor.xaxis[0].formatter = NumeralTickFormatter(format="$0")
#         _tabs.append(Panel(child=plot_minor, title="Saldo < 0"))
#
#     if not df_equal.empty:
#         df_equal.sort_values('razon_social', inplace=True)
#         source_equal = ColumnDataSource(df_equal)
#         columns = [
#             TableColumn(field='razon_social', title='Razón Social'),
#             TableColumn(field='iva', title='Iva', width=100),
#             TableColumn(field='prefijo', title='Prefijo', width=70),
#             TableColumn(field='tipo_factura', title='Tipo Factura',
#             width=100),
#             TableColumn(field='tipo_cliente', title='Tipo de Cliente',
#                         width=100),
#             TableColumn(field='particip_total_compras',
#                         title='Participación Total de Compras',
#                         width=200),
#             TableColumn(field='porcent_total_compras',
#                         title='Porcentaje Total de Compras',
#                         width=200)]
#         data_table = DataTable(source=source_equal,
#                                columns=columns,
#                                fit_columns=False)
#         data_table.sizing_mode = 'scale_both'
#         _tabs.append(Panel(child=data_table, title="Saldo = 0"))
#
#     if not df_mayor.empty:
#         source_mayor = ColumnDataSource(df_mayor)
#         source_mayor.data['color'] = get_palet(source_mayor.data['saldo'],
#                                                'greens')
#         hovertool = HoverTool(mode='hline', attachment='below',
#                               names=['hbar'], tooltips=tooltips)
#         plot_mayor = figure(
#             title="Clientes con saldo mayor a cero",
#             y_range=FactorRange(*source_mayor.data['razon_social'],
#                                 bounds='auto'),
#             x_range=Range1d(start=0,
#                             end=(max(source_mayor.data['saldo']) +
#                                  max(source_mayor.data[
#                                          'saldo']) * PLOT_PADDING),
#                             bounds='auto'),
#             tools=["tap,reset,save", hovertool],
#             toolbar_location='above',
#             y_axis_label='Cliente', x_axis_label='Saldo',
#             height=300)
#         plot_mayor.hbar(
#             y='razon_social', right='saldo', height=0.8, source=source_mayor,
#             fill_color='color', nonselection_fill_alpha=0.2,
#             line_color=None, name='hbar')
#         set_plot_properties(plot_mayor)
#         plot_mayor.xaxis[0].formatter = NumeralTickFormatter(format="$0")
#
#         _tabs.append(Panel(child=plot_mayor, title="Saldo > 0"))
#
#     tabs = Tabs(tabs=_tabs)
#     script, div = components(tabs)
#
#     return render(request, 'app/clientes.html',
#                   {'script': script,
#                    'div': div})


def imputacion(request):
    # if not request.user.is_authenticated:
    #     return redirect(login_user)

    title_detalle, title_periodo = None, None
    tipo_impu = ''
    acumulador, impu = None, None
    exclude = []
    columns = [columns[0] for columns in IMPU_CHOICES]
    form = MovImpuForm(request.GET)
    if form.is_valid():
        all_columns = form.cleaned_data['all']
        visible_columns = form.cleaned_data['visible_columns']
        if not visible_columns or all_columns:
            visible_columns = columns.copy()
        exclude = list(set(columns).difference(set(visible_columns)))

    movimpu = get_movimpu()
    movimpu_filter = MovImpuFilter(request.GET, queryset=movimpu)

    if movimpu_filter.data and movimpu_filter.qs:
        movimpu = movimpu_filter.qs
        acumulador = movimpu_filter.form.cleaned_data[
            'acumulador']
        impu = movimpu_filter.form.cleaned_data[
            'imputacion']
        inicio = movimpu_filter.form.cleaned_data['inicio_periodo']
        fin = movimpu_filter.form.cleaned_data['fin_periodo']
        title_periodo = title_period(inicio, fin)
        if acumulador or impu:
            exclude.append('acumulador')
            if 'imputacion' in exclude:
                exclude.remove('imputacion')
    exclude = tuple(exclude)

    if not movimpu_filter.qs:
        messages.error(request, 'No se encontraron resultados.')

    df = get_df_mov_impu(movimpu)
    df_ingresos = df[df.tipo == 'Ingreso'].copy()
    df_egresos = df[df.tipo == 'Egreso'].copy()

    ingresos, egresos, pie_ingresos_egresos = get_ingresos_egresos(df)
    div_components = {'pie_ingresos_egresos': pie_ingresos_egresos}

    if impu:
        title_detalle = f'Detalle de ' \
                        f'{impu.donde_acumula.descripcion} - ' \
                        f'{impu.descripcion}'
    else:
        if acumulador:
            tipo_impu = 'Imputación'
            title_detalle = f'Detalle de {acumulador.descripcion}'

            if not df_egresos.empty:
                gb_egresos = DataFrame(df_egresos.groupby('imputacion')
                                       .agg({'importe': 'sum'}))
                bar_egresos, pie_egresos = detalle_impu_plots(gb_egresos, 0.9,
                                                              'reds')
                div_components['bar_egresos'] = bar_egresos
                div_components['pie_egresos'] = pie_egresos
            if not df_ingresos.empty:
                gb_ingresos = DataFrame(df_ingresos.groupby('imputacion')
                                        .agg({'importe': 'sum'}))
                bar_ingresos, pie_ingresos = detalle_impu_plots(gb_ingresos,
                                                                0.9,
                                                                'greens')
                div_components['bar_ingresos'] = bar_ingresos
                div_components['pie_ingresos'] = pie_ingresos
        else:
            tipo_impu = 'Acumulador'
            if not df_egresos.empty:
                gb_egresos = DataFrame(
                    df_egresos.groupby('acumulador').agg({'importe': 'sum'}))
                if not gb_egresos.empty:
                    bar_egresos, pie_egresos = impu_plots('egresos', gb_egresos, 0.9, 'reds')
                    div_components['bar_egresos'] = bar_egresos
                    div_components['pie_egresos'] = pie_egresos
            if not df_ingresos.empty:
                gb_ingresos = DataFrame(
                    df_ingresos.groupby('acumulador').agg({'importe': 'sum'}))
                if not gb_ingresos.empty:
                    bar_ingresos, pie_ingresos = impu_plots('ingresos', gb_ingresos, 0.9, 'greens')
                    div_components['bar_ingresos'] = bar_ingresos
                    div_components['pie_ingresos'] = pie_ingresos

    script, div = components(div_components)

    table = MovimpuTable(df.to_dict('records'), exclude=exclude)
    RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(table)

    return render(request, 'app/imputacion.html',
                  {'script': script, 'div': div,
                   'title_detalle': title_detalle, 'tipo_impu': tipo_impu,
                   'title_periodo': title_periodo, 'filter': movimpu_filter,
                   'table': table, 'form': form,
                   'imputacion': impu,
                   'ingresos': ingresos, 'egresos': egresos})


def acumula(request):
    # if not request.user.is_authenticated:
    #     return redirect(login_user)

    script, div = None, None
    exclude = []
    columns = [columns[0] for columns in ACUMULA_CHOICES]
    form = AcumulaForm(request.GET)
    if form.is_valid():
        all_columns = form.cleaned_data['all']
        visible_columns = form.cleaned_data['visible_columns']
        if not visible_columns or all_columns:
            visible_columns = columns.copy()
        exclude = list(set(columns).difference(set(visible_columns)))

    title = ''
    imputaci = get_imputaci()
    acumula_filter = AcumulaFilter(request.GET, queryset=imputaci)
    acumulador, imputacion = None, None
    if acumula_filter.data and acumula_filter.qs:
        imputaci = acumula_filter.qs
        acumulador = acumula_filter.form.cleaned_data[
            'acumulador']
        imputacion = acumula_filter.form.cleaned_data[
            'imputacion']
        if acumulador:
            exclude.append('acumulador')
            if 'imputacion' in exclude:
                exclude.remove('imputacion')
    exclude = tuple(exclude)

    if not acumula_filter.qs:
        messages.error(request, 'No se encontró detalle para la imputación '
                                'seleccionada.')

    df = DataFrame(imputaci)
    df.rename(columns={'donde_acumula__descripcion': 'acumulador',
                       'descripcion': 'imputacion'}, inplace=True)

    if not imputacion:
        if acumulador:
            df_gt_0 = df[df['total_egresos'] > 0]
            if not df_gt_0.empty:
                script, div = detalle_acumula_plots(df_gt_0)
                title = f'Detalle de {acumulador.descripcion}'
        else:
            gb_imputaci = DataFrame(df.groupby('acumulador')
                                    .total_egresos.sum())
            gb_imputaci.sort_values('total_egresos', ascending=False,
                                    inplace=True)
            gb_imputaci['percentage'] = gb_imputaci.total_egresos / \
                         gb_imputaci.total_egresos.sum() * 100

            gb_imputaci = gb_imputaci[(gb_imputaci.percentage >= 0.5)]
            percentage = gb_imputaci.total_egresos / \
                         gb_imputaci.total_egresos.sum() * 100
            gb_imputaci['percentage'] = round(percentage, 1)
            gb_imputaci['angle'] = gb_imputaci.total_egresos / \
                                   gb_imputaci.total_egresos.sum() * 2 * pi
            gb_imputaci['color'] = get_palet(gb_imputaci['total_egresos'])

            source = ColumnDataSource(gb_imputaci)
            source.data['percentage'] = [f'{x}%' for x in source.data['percentage']]

            vbar_plot = acumula_vbar(source)
            pie_plot = acumula_pie(source)
            script, div = components({'vbar_plot': vbar_plot,
                                      'pie_plot': pie_plot})

            if 'imputacion' in exclude:
                df = acumula_gb_impu_acumulada(df)

    table = AcumulaTable(df.to_dict('records'), exclude=exclude)
    RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(table)

    return render(request, 'app/acumula.html',
                  {'script': script, 'div': div,
                   'title': title, 'filter': acumula_filter,
                   'table': table, 'form': form,
                   'imputacion': imputacion})


def actividad(request):
    # if not request.user.is_authenticated:
    #     return redirect(login_user)

    title, title_periodo = None, None
    actividad_form, acumulador, imputacion = None, None, None
    visible_columns = []
    impu_simple_cols = ['imputacion', 'ingresos', 'porcentaje_ingresos',
                        'egresos', 'porcentaje_egresos']
    columns = [columns[0] for columns in ACTIVIDAD_CHOICES]
    form = ActividadForm(request.GET)
    if form.is_valid():
        all_columns = form.cleaned_data['all']
        visible_columns = form.cleaned_data['visible_columns']
        if not visible_columns or all_columns:
            visible_columns = columns.copy()

    movimpu = get_movimpu()
    movimpu = movimpu.order_by('periodo_contable', 'actividad__descripcion',
                               'cod_imput__donde_acumula__descripcion')

    actividad_filter = ActividadFilter(request.GET, queryset=movimpu)
    if actividad_filter.data and actividad_filter.qs:
        movimpu = actividad_filter.qs
        actividad_form = actividad_filter.form.cleaned_data['actividad']
        acumulador = actividad_filter.form.cleaned_data[
            'acumulador']
        imputacion = actividad_filter.form.cleaned_data[
            'imputacion']
        inicio = actividad_filter.form.cleaned_data['inicio_periodo']
        fin = actividad_filter.form.cleaned_data['fin_periodo']
        title_periodo = title_period(inicio, fin)
    if not actividad_filter.qs:
        messages.error(request, 'No se encontraron resultados.')

    df = get_df_mov_impu(movimpu)

    ingresos, egresos, pie_ingresos_egresos = get_ingresos_egresos(df)
    div_components = {'pie_ingresos_egresos': pie_ingresos_egresos}
    if actividad_form or acumulador or imputacion:
        if actividad_form:
            title = f'Ingresos y Egresos de la actividad ' \
                    f'{actividad_form.descripcion}'
        if not df.empty:
            if not imputacion:
                df_ingresos = df[df.tipo == 'Ingreso'].copy()
                df_egresos = df[df.tipo == 'Egreso'].copy()
                if not df_ingresos.empty:
                    bar_ingresos = detalle_actividad_vbar(df_ingresos, 'greens')
                    pie_ingresos = detalle_actividad_pie(df_ingresos, 'greens')
                    div_components['pie_ingresos_detalle'] = pie_ingresos
                    div_components['bar_ingresos'] = bar_ingresos
                if not df_egresos.empty:
                    bar_egresos = detalle_actividad_vbar(df_egresos, 'reds')
                    pie_egresos = detalle_actividad_pie(df_egresos, 'reds')
                    div_components['pie_egresos_detalle'] = pie_egresos
                    div_components['bar_egresos'] = bar_egresos

            script, div = components(div_components)

            exclude = tuple(set(columns).difference(set(visible_columns)))
            if all(_ in exclude for _ in impu_simple_cols):
                gb = gb_actividad(df, impu_simple=False)
            else:
                gb = gb_actividad(df, impu_simple=True)

            table = ActividadTable(gb.to_dict('records'), exclude=exclude)
            RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(
                table)

            return render(request, 'app/actividad.html',
                          {'script': script, 'div': div,
                           'title': title, 'title_periodo': title_periodo,
                           'filter': actividad_filter,
                           'table': table, 'form': form,
                           'ingresos': ingresos, 'egresos': egresos,
                           'imputacion': imputacion})

    div_components['bar_total'] = actividad_vbar(df)
    df_ingresos = DataFrame(df[df.tipo == 'Ingreso']
                            .groupby(['actividad']).importe.sum())
    df_egresos = DataFrame(df[df.tipo == 'Egreso']
                           .groupby(['actividad']).importe.sum())
    if not df_ingresos.empty:
        pie_ingresos = actividad_pie(df_ingresos, 'greens')
        div_components['pie_ingresos'] = pie_ingresos
    if not df_egresos.empty:
        pie_egresos = actividad_pie(df_egresos, 'reds')
        div_components['pie_egresos'] = pie_egresos
    script, div = components(div_components)

    exclude = tuple(set(columns).difference(set(visible_columns)))
    if all(_ in exclude for _ in impu_simple_cols):
        gb = gb_actividad(df, impu_simple=False)
    else:
        gb = gb_actividad(df, impu_simple=True)

    table = ActividadTable(gb.to_dict('records'), exclude=exclude)
    RequestConfig(request, paginate={"per_page": PER_PAGE}).configure(table)

    return render(request, 'app/actividad.html',
                  {'script': script, 'div': div,
                   'title': title, 'title_periodo': title_periodo,
                   'filter': actividad_filter, 'table': table,
                   'form': form, 'ingresos': ingresos,
                   'egresos': egresos})

# def sub_diario_iva_compras(request):
#     mensual = get_mensual()
#     mensual_filter = MensualFilter(request.GET, queryset=mensual)
#     if mensual_filter.data and mensual_filter.qs:
#         mensual = mensual_filter.qs
#
#     if not mensual_filter.qs:
#         messages.error(request, 'No se encontraron resultados.')
#
#     table = MensualTable(mensual)
#     table.paginate(page=request.GET.get("page", 1), per_page=PER_PAGE)
#
#     return render(request, 'app/sub_diario_iva_compras.html',
#                   {"table": table,
#                    'filter': mensual_filter})
