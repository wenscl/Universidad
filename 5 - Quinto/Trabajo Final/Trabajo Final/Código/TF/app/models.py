from django.db import models


class TipoMovimiento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Tipo Movimiento')

    class Meta:
        db_table = 'tipo_movimiento'


class Actividad(models.Model):
    nro_actividad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'actividad'


class Acumula(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    codigo_contabilidad = models.CharField(max_length=255, blank=True,
                                           null=True)
    compra_cta_cte = models.FloatField(blank=True, null=True)
    compra_cont = models.FloatField(blank=True, null=True)
    nota_credito_recibida = models.FloatField(blank=True, null=True)
    nota_debito_recibida = models.FloatField(blank=True, null=True)
    egresos_cta_cte = models.FloatField(blank=True, null=True)
    egresos_cont = models.FloatField(blank=True, null=True)
    venta_cta_cte = models.FloatField(blank=True, null=True)
    venta_contado = models.FloatField(blank=True, null=True)
    nota_credito_emitida = models.FloatField(blank=True, null=True)
    nota_debito_emitida = models.FloatField(blank=True, null=True)
    cobranzas = models.FloatField(blank=True, null=True)
    unid_generadora = models.IntegerField(blank=True, null=True)
    cuenta_gastos = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'acumula'


class Agroquim(models.Model):
    nro_agroquimico = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    fecha_del_costo = models.DateField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'agroquim'


class Anexo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    linea1 = models.CharField(max_length=255, blank=True, null=True)
    linea2 = models.CharField(max_length=255, blank=True, null=True)
    linea3 = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    movil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'anexo'


class Banc(models.Model):
    id_banc = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    nrobanco = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'banc'


class Bancos(models.Model):
    nro_banco = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    nro_sucursal = models.CharField(max_length=255, blank=True, null=True)
    cuit = models.CharField(max_length=255, blank=True, null=True)
    nro_cuenta = models.CharField(max_length=255, blank=True, null=True)
    nombre_cuenta = models.CharField(max_length=255, blank=True, null=True)
    saldo_cta_libro = models.FloatField(blank=True, null=True)
    saldo_cta_disponibilidad = models.FloatField(blank=True, null=True)
    importe_descubierto = models.FloatField(blank=True, null=True)
    impoprte_negociado = models.FloatField(blank=True, null=True)
    banco_mutual = models.IntegerField(blank=True, null=True)
    cbu = models.CharField(max_length=255, blank=True, null=True)
    fecha_cierre_conciliacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'bancos'


class Cajas(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cuenta_contable = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'cajas'


class Categorias(models.Model):
    nro_categoria = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    kilos = models.IntegerField(blank=True, null=True)
    iva = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'categorias'


class Chofer(models.Model):
    nro_chofer = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    situacion_iva = models.CharField(max_length=255, blank=True, null=True)
    nro_cuit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'chofer'


class Clering(models.Model):
    codigo = models.IntegerField(primary_key=True)
    dias = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'clering'


class CodComprob(models.Model):
    codigo = models.CharField(primary_key=True, max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'cod_comprob'


class Config(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    nombreestado = models.CharField(max_length=255, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    vacio = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'config'


class Conpago(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cant_cuotas = models.IntegerField(blank=True, null=True)
    dias1 = models.IntegerField(blank=True, null=True)
    porcentaje1 = models.FloatField(blank=True, null=True)
    dias2 = models.IntegerField(blank=True, null=True)
    porcentaje2 = models.FloatField(blank=True, null=True)
    dias3 = models.IntegerField(blank=True, null=True)
    porcentaje3 = models.FloatField(blank=True, null=True)
    dias4 = models.IntegerField(blank=True, null=True)
    porcentaje4 = models.FloatField(blank=True, null=True)
    dias5 = models.IntegerField(blank=True, null=True)
    porcentaje5 = models.FloatField(blank=True, null=True)
    dias6 = models.IntegerField(blank=True, null=True)
    porcentaje6 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'conpago'


class Consocia(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cant_semillas = models.IntegerField(blank=True, null=True)
    semilla_1 = models.IntegerField(blank=True, null=True)
    kilos_1 = models.FloatField(blank=True, null=True)
    semilla_2 = models.IntegerField(blank=True, null=True)
    kilos_2 = models.FloatField(blank=True, null=True)
    semilla_3 = models.IntegerField(blank=True, null=True)
    kilos_3 = models.FloatField(blank=True, null=True)
    semilla_4 = models.IntegerField(blank=True, null=True)
    kilos_4 = models.FloatField(blank=True, null=True)
    semilla_5 = models.IntegerField(blank=True, null=True)
    kilos_5 = models.FloatField(blank=True, null=True)
    semilla_6 = models.IntegerField(blank=True, null=True)
    kilos_6 = models.FloatField(blank=True, null=True)
    kilosxhect = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'consocia'


class Contador(models.Model):
    cierre = models.IntegerField(blank=True, null=True)
    con_filtro_hora = models.IntegerField(blank=True, null=True)
    con_filtro_cajero = models.IntegerField(blank=True, null=True)
    ultimo_compr = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'contador'


class Contrat(models.Model):
    nro_contratista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'contrat'


class Cultivo(models.Model):
    nro_cultivo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    fecha_del_costo = models.DateField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'cultivo'


class DepositoStock(models.Model):
    nro_deposito = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'deposito_stock'


class Distancia(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    km_1 = models.IntegerField(blank=True, null=True)
    importe_1 = models.FloatField(blank=True, null=True)
    km_2 = models.IntegerField(blank=True, null=True)
    importe_2 = models.FloatField(blank=True, null=True)
    km_3 = models.IntegerField(blank=True, null=True)
    importe_3 = models.FloatField(blank=True, null=True)
    km_4 = models.IntegerField(blank=True, null=True)
    importe_4 = models.FloatField(blank=True, null=True)
    km_5 = models.IntegerField(blank=True, null=True)
    importe_5 = models.FloatField(blank=True, null=True)
    km_6 = models.IntegerField(blank=True, null=True)
    importe_6 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'distancia'


# class Feriados(models.Model):
#     fecha_feriado = models.DateField(blank=True, null=True)
#     motivo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#
#         db_table = 'feriados'


class Fertiliz(models.Model):
    nro_fertilizante = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    fecha_del_costo = models.DateField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'fertiliz'


class ForFer(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cant_fertilizante = models.IntegerField(blank=True, null=True)
    fer_1 = models.IntegerField(blank=True, null=True)
    kilos_1 = models.FloatField(blank=True, null=True)
    fer_2 = models.IntegerField(blank=True, null=True)
    kilos_2 = models.FloatField(blank=True, null=True)
    fer_3 = models.IntegerField(blank=True, null=True)
    kilos_3 = models.FloatField(blank=True, null=True)
    fer_4 = models.IntegerField(blank=True, null=True)
    kilos_4 = models.FloatField(blank=True, null=True)
    fer_5 = models.IntegerField(blank=True, null=True)
    kilos_5 = models.FloatField(blank=True, null=True)
    fer_6 = models.IntegerField(blank=True, null=True)
    kilos_6 = models.FloatField(blank=True, null=True)
    kilosxhect = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'for_fer'


class Formula(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cant_agroq = models.IntegerField(blank=True, null=True)
    agroq_1 = models.IntegerField(blank=True, null=True)
    dosis_1 = models.FloatField(blank=True, null=True)
    agroq_2 = models.IntegerField(blank=True, null=True)
    dosis_2 = models.FloatField(blank=True, null=True)
    agroq_3 = models.IntegerField(blank=True, null=True)
    dosis_3 = models.FloatField(blank=True, null=True)
    agroq_4 = models.IntegerField(blank=True, null=True)
    dosis_4 = models.FloatField(blank=True, null=True)
    agroq_5 = models.IntegerField(blank=True, null=True)
    dosis_5 = models.FloatField(blank=True, null=True)
    agroq_6 = models.IntegerField(blank=True, null=True)
    dosis_6 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'formula'


class Grado(models.Model):
    grado = models.IntegerField(primary_key=True)
    descripcion_grano = models.CharField(max_length=255, blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'grado'


class Grupos(models.Model):
    numero = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    campo_1 = models.CharField(max_length=255, blank=True, null=True)
    campo_2 = models.CharField(max_length=255, blank=True, null=True)
    campo_3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'grupos'


class Impuesto(models.Model):
    numero = models.IntegerField(primary_key=True)
    porcentaje_iva_inscripto = models.FloatField(blank=True, null=True)
    porcentaje_iva_no_inscripto = models.FloatField(blank=True, null=True)
    porcentaje_impuestos_internos = models.FloatField(blank=True, null=True)
    valor_del_impuesto_interno = models.FloatField(blank=True, null=True)
    porcentaje_ingresos_brutos = models.FloatField(blank=True, null=True)
    tipoiva = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'impuesto'


class Imputaci(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Imputación')
    compra_cta_cte = models.FloatField(blank=True, null=True,
                                       verbose_name='Compra Cta. Cte.')
    compra_contado = models.FloatField(blank=True, null=True,
                                       verbose_name='Compra Contado')
    nota_credito_recibida = models.FloatField(blank=True, null=True,
                                              verbose_name='Nota Crédito '
                                                           'Recibida')
    nota_debito_recibida = models.FloatField(blank=True, null=True,
                                             verbose_name='Nota Débito '
                                                          'Recibida')
    egresos_cta_cte = models.FloatField(blank=True, null=True,
                                        verbose_name='Egresos Cta. Cte.')
    egresos_contado = models.FloatField(blank=True, null=True,
                                        verbose_name='Egresos Contado')
    venta_cta_cte = models.FloatField(blank=True, null=True,
                                      verbose_name='Venta Cta. Cte.')
    venta_contado = models.FloatField(blank=True, null=True,
                                      verbose_name='Venta Contado')
    nota_credito_emitida = models.FloatField(blank=True, null=True,
                                             verbose_name='Nota Crédito '
                                                          'Emitida')
    nota_debito_emitida = models.FloatField(blank=True, null=True,
                                            verbose_name='Nota Débito Emitida')
    cobranzas = models.FloatField(blank=True, null=True,
                                  verbose_name='Cobranzas')
    unid_generadora = models.IntegerField(blank=True, null=True,
                                          verbose_name='Unidad Generadora')
    cuenta_gastos = models.IntegerField(blank=True, null=True,
                                        verbose_name='Cuenta Gastos')
    donde_acumula = models.ForeignKey(Acumula, models.DO_NOTHING,
                                      db_column='donde_acumula',
                                      blank=True, null=True,
                                      verbose_name='Acumulador')
    total_egresos = models.FloatField(blank=True, null=True,
                                      verbose_name='Total Egresos')
    porcentaje = models.FloatField(blank=True, null=True,
                                   verbose_name='Porcentaje')

    class Meta:
        db_table = 'imputaci'


class Indices(models.Model):
    nro = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'indices'


class Laboreo(models.Model):
    nro_laboreo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    fecha_del_costo = models.DateField(blank=True, null=True)
    cantidad_uta = models.FloatField(blank=True, null=True)
    indice = models.IntegerField(blank=True, null=True)
    centro_costo = models.IntegerField(blank=True, null=True)
    suma_resta = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'laboreo'


class Lineas(models.Model):
    num_linea = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    total_cantidad = models.FloatField(blank=True, null=True)
    total_kilos = models.FloatField(blank=True, null=True)
    total_importe_venta = models.FloatField(blank=True, null=True)
    total_precio_costo = models.FloatField(blank=True, null=True)
    total_diferencia = models.FloatField(blank=True, null=True)
    partic_rubro_emp = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'lineas'


class MotDeb(models.Model):
    nro_motivo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'mot_deb'


class Motipago(models.Model):
    motivo = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = 'motipago'


class Motivo(models.Model):
    motivo = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = 'motivo'


class Motivos(models.Model):
    nro_motivo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    suma_resta = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'motivos'


class Movim(models.Model):
    nro_movimiento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    comodin_1 = models.FloatField(blank=True, null=True)
    comodin_2 = models.FloatField(blank=True, null=True)
    comodin_3 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'movim'


class Ms(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ms'


class Multiempresa(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'multiempresa'


class Param(models.Model):
    con_final_caja = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    suc = models.IntegerField(blank=True, null=True)
    cred = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    solofact = models.IntegerField(blank=True, null=True)
    fact_lote = models.IntegerField(blank=True, null=True)
    cant_um = models.IntegerField(blank=True, null=True)
    multicaja = models.IntegerField(blank=True, null=True)
    digitable = models.IntegerField(blank=True, null=True)
    que_tomar = models.IntegerField(blank=True, null=True)
    que_caja_no_tomar = models.IntegerField(blank=True, null=True)
    guardar_4 = models.IntegerField(blank=True, null=True)
    guardar_5 = models.CharField(max_length=255, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    digitable_o_no = models.IntegerField(blank=True, null=True)
    ejecutable = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    controla_imputacion = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'param'


class Periodo(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    finicio = models.DateField(blank=True, null=True)
    ffinal = models.DateField(blank=True, null=True)
    cantinicial = models.IntegerField(blank=True, null=True)
    cantfinal = models.IntegerField(blank=True, null=True)
    kilosinicial = models.IntegerField(blank=True, null=True)
    kilosfinal = models.IntegerField(blank=True, null=True)
    ganancia1 = models.FloatField(blank=True, null=True)
    ganancia2 = models.FloatField(blank=True, null=True)
    ganancia3 = models.FloatField(blank=True, null=True)
    ganancia4 = models.FloatField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'periodo'


class PesIte(models.Model):
    fecha = models.DateField(blank=True, null=True)
    rodeo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    kilos = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'pes_ite'


class Pesadas(models.Model):
    fecha = models.DateField(blank=True, null=True)
    cabezas = models.IntegerField(blank=True, null=True)
    kilos = models.FloatField(blank=True, null=True)
    rodeo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'pesadas'


class PorcSueldos(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cant_porc = models.IntegerField(blank=True, null=True)
    nro_imputacion_1 = models.IntegerField(blank=True, null=True)
    porc_1 = models.FloatField(blank=True, null=True)
    nro_imputacion_2 = models.IntegerField(blank=True, null=True)
    porc_2 = models.FloatField(blank=True, null=True)
    nro_imputacion_3 = models.IntegerField(blank=True, null=True)
    porc_3 = models.FloatField(blank=True, null=True)
    nro_imputacion_4 = models.IntegerField(blank=True, null=True)
    porc_4 = models.FloatField(blank=True, null=True)
    nro_imputacion_5 = models.IntegerField(blank=True, null=True)
    porc_5 = models.FloatField(blank=True, null=True)
    nro_imputacion_6 = models.IntegerField(blank=True, null=True)
    porc_6 = models.FloatField(blank=True, null=True)
    nro_imputacion_7 = models.IntegerField(blank=True, null=True)
    porc_7 = models.FloatField(blank=True, null=True)
    nro_imputacion_8 = models.IntegerField(blank=True, null=True)
    porc_8 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'porc_sueldos'


class Printopa(models.Model):
    n = models.IntegerField(blank=True, null=True)
    nn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'printopa'


class Provincias(models.Model):
    nro_provincia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Provincia')
    cod_prov_afip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'provincias'
#

class Localidad(models.Model):
    codigo = models.CharField(primary_key=True, max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.ForeignKey('Provincias', models.DO_NOTHING,
                                  db_column='provincia', blank=True, null=True)
    prefijo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'localidad'


class RelHolistor(models.Model):
    efectivo = models.CharField(max_length=255, blank=True, null=True)
    cheques_terceros = models.CharField(max_length=255, blank=True, null=True)
    iva = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'rel_holistor'


class Respons(models.Model):
    nro_responsable = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'respons'


class Retencio(models.Model):
    nro_retencion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    porcentaje_inscripto = models.FloatField(blank=True, null=True)
    porcentaje_no_inscripto = models.FloatField(blank=True, null=True)
    imp_minimo_no_imponible = models.FloatField(blank=True, null=True)
    importe_minimo = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'retencio'


class RetIb(models.Model):
    nro_retencion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    imp_minimo_no_imponible = models.FloatField(blank=True, null=True)
    que_tomar = models.IntegerField(blank=True, null=True)
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING,
                                  db_column='provincia', blank=True, null=True)
    normativa = models.CharField(max_length=255, blank=True, null=True)
    numero_agente = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ret_ib'


class Rodados(models.Model):
    nro_rodado = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    imputcomb = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rodados'


class Rubros(models.Model):
    nro_rubro = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'rubros'


class Tambos(models.Model):
    nro_tambo = models.CharField(primary_key=True, max_length=255)
    vacas_total = models.IntegerField(blank=True, null=True)
    vacas_ordene = models.IntegerField(blank=True, null=True)
    stock_tanque = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'tambos'


class Tanque(models.Model):
    nro_tanque = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    stock_tanque = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'tanque'


class Tipoprov(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Tipo Proveedor')

    class Meta:
        db_table = 'tipoprov'


class Titular(models.Model):
    nro_cuit = models.CharField(primary_key=True, max_length=255)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    cantidad_ch = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    estado_cuenta = models.CharField(max_length=255, blank=True, null=True)
    maximo = models.IntegerField(blank=True, null=True)
    cantch_recha = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'titular'


class Transp(models.Model):
    numero = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, models.DO_NOTHING,
                                  db_column='localidad', blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    linea1 = models.CharField(max_length=255, blank=True, null=True)
    linea2 = models.CharField(max_length=255, blank=True, null=True)
    linea3 = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    inscripto_ganancias = models.IntegerField(blank=True, null=True)
    categoria_ganancias = models.IntegerField(blank=True, null=True)
    total_cantidad = models.FloatField(blank=True, null=True)
    total_kilos = models.FloatField(blank=True, null=True)
    total_importe = models.FloatField(blank=True, null=True)
    total_prd_e = models.FloatField(blank=True, null=True)
    propiotercero = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    patente = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_compra = models.DateField(blank=True, null=True)
    costo_de_compra = models.FloatField(blank=True, null=True)
    vida_util = models.IntegerField(blank=True, null=True)
    nro_imp_flete = models.IntegerField(blank=True, null=True)
    nro_imp_acarreo = models.IntegerField(blank=True, null=True)
    imputcomb = models.IntegerField(blank=True, null=True)
    situacion_iva = models.CharField(max_length=255, blank=True, null=True)
    nro_cuit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'transp'


# class Ugenerad(models.Model):
#     codigo = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 'ugenerad'


class Acoplado(models.Model):
    nro_acoplado = models.CharField(primary_key=True, max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    fecha_de_compra = models.DateField(blank=True, null=True)
    costo_de_compra = models.FloatField(blank=True, null=True)
    vida_util = models.IntegerField(blank=True, null=True)
    nro_imputacion = models.ForeignKey('Imputaci', models.DO_NOTHING,
                                       db_column='nro_imputacion', blank=True,
                                       null=True)

    class Meta:
        db_table = 'acoplado'


class Acredita(models.Model):
    nro_credito = models.IntegerField(primary_key=True)
    nro_cuenta = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    imputacion = models.ForeignKey('Imputaci', models.DO_NOTHING,
                                   db_column='imputacion', blank=True,
                                   null=True)
    importe = models.FloatField(blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    fecha_conciliacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'acredita'
        unique_together = (('nro_credito', 'nro_cuenta'),)


class AcredPend(models.Model):
    nro_banco = models.ForeignKey('Bancos', models.DO_NOTHING,
                                  db_column='nro_banco')
    fecha = models.DateField()
    nro_transaccion = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    importe_imputado = models.FloatField(blank=True, null=True)
    usar_parte = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    marca = models.IntegerField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha_conciliacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'acred_pend'
        unique_together = (('nro_banco', 'fecha'),)


class Bolsas(models.Model):
    id_bolsas = models.AutoField(primary_key=True)
    nro_cultivo = models.ForeignKey('Cultivo', models.DO_NOTHING,
                                    db_column='nro_cultivo', blank=True,
                                    null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    fecha_del_costo = models.DateField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'bolsas'


class Camion(models.Model):
    nro_camion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    patente = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_compra = models.DateField(blank=True, null=True)
    costo_de_compra = models.FloatField(blank=True, null=True)
    vida_util = models.IntegerField(blank=True, null=True)
    nro_imputacion = models.ForeignKey('Imputaci', models.DO_NOTHING,
                                       db_column='nro_imputacion', blank=True,
                                       null=True)

    class Meta:
        db_table = 'camion'


class Campana(models.Model):
    nro_campana = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    ano = models.CharField(max_length=255, blank=True, null=True)
    cultivo = models.ForeignKey('Cultivo', models.DO_NOTHING,
                                db_column='cultivo', blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
                                  db_column='actividad', blank=True, null=True)
    de_baja = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'campana'


class Sector(models.Model):
    nro_sector = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    responsable_sector = models.CharField(max_length=255, blank=True, null=True)
    profesional_agronomo = models.CharField(max_length=255, blank=True,
                                            null=True)
    profesional_veterinario = models.CharField(max_length=255, blank=True,
                                               null=True)
    cantidad_subsectores = models.IntegerField(blank=True, null=True)
    cantidad_de_campos = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sector'


class Subsecto(models.Model):
    nro_sub_sector = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    responsable_sub_sector = models.ForeignKey(Respons, models.DO_NOTHING,
                                               db_column='responsable_sub_sector',
                                               blank=True, null=True)
    profesional_agronomo = models.CharField(max_length=255, blank=True,
                                            null=True)
    profesional_veterinario = models.CharField(max_length=255, blank=True,
                                               null=True)
    sector = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sector',
                               blank=True, null=True)
    cantidad_de_campos = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'subsecto'


class Campos(models.Model):
    nro_campo = models.CharField(primary_key=True, max_length=255)
    nombre_del_campo = models.CharField(max_length=255, blank=True, null=True)
    sub_sector = models.ForeignKey('Subsecto', models.DO_NOTHING,
                                   db_column='sub_sector', blank=True,
                                   null=True)
    encargado = models.CharField(max_length=255, blank=True, null=True)
    propio_o_alquilado = models.CharField(max_length=255, blank=True, null=True)
    cantidad_de_hectareas = models.FloatField(blank=True, null=True)
    actividad_del_campo = models.CharField(max_length=255, blank=True, null=True)
    porcarrendado = models.FloatField(blank=True, null=True)
    imputacion = models.ForeignKey('Imputaci', models.DO_NOTHING,
                                   db_column='imputacion', blank=True,
                                   null=True)

    class Meta:
        db_table = 'campos'


class Cli(models.Model):
    codigo = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    iva = models.CharField(max_length=255, blank=True, null=True)
    cuit = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey('Localidad', models.DO_NOTHING,
                                  db_column='localidad', blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    tipo_factura = models.CharField(max_length=255, blank=True, null=True)
    tipo_cliente = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    linea1 = models.CharField(max_length=255, blank=True, null=True)
    linea2 = models.CharField(max_length=255, blank=True, null=True)
    linea3 = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    particip_total_compras = models.FloatField(blank=True, null=True)
    porcent_total_compras = models.FloatField(blank=True, null=True)
    nombre_fantasia = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'cli'


class Proctcte(models.Model):
    codigo = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, models.DO_NOTHING,
                                  db_column='localidad', blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    iva = models.CharField(max_length=255, blank=True, null=True)
    cuit = models.CharField(max_length=255, blank=True, null=True)
    saldo_cta_cte = models.FloatField(blank=True, null=True)
    tipo_proveedor = models.ForeignKey('Tipoprov', models.DO_NOTHING,
                                       db_column='tipo_proveedor', blank=True,
                                       null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    tipo_factura = models.CharField(max_length=255, blank=True, null=True)
    retenc_ing_brutos = models.IntegerField(blank=True, null=True)
    categoriaib = models.IntegerField(blank=True, null=True)
    porc_retencion_ib = models.FloatField(blank=True, null=True)
    retenc_ganancia = models.IntegerField(blank=True, null=True)
    retenc_iva = models.IntegerField(blank=True, null=True)
    porcentaje_iva = models.FloatField(blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    linea1 = models.CharField(max_length=255, blank=True, null=True)
    linea2 = models.CharField(max_length=255, blank=True, null=True)
    linea3 = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    inscripto_ganancias = models.IntegerField(blank=True, null=True)
    categoria_ganancias = models.IntegerField(blank=True, null=True)
    particip_total_compras = models.FloatField(blank=True, null=True)
    porcent_total_compras = models.FloatField(blank=True, null=True)
    tiene_credito = models.CharField(max_length=255, blank=True, null=True)
    total_cantidad = models.FloatField(blank=True, null=True)
    total_kilos = models.FloatField(blank=True, null=True)
    total_importe_deventa = models.FloatField(blank=True, null=True)
    total_preciocosto = models.FloatField(blank=True, null=True)
    total_diferencia = models.FloatField(blank=True, null=True)
    total_prd_e = models.FloatField(blank=True, null=True)
    fecha_vto_cuit = models.DateField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    nombre_fantasia = models.CharField(max_length=255, blank=True, null=True)
    tipo_calificacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'proctcte'


class Provedor(models.Model):
    codigo = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, models.DO_NOTHING,
                                  db_column='localidad', blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    iva = models.CharField(max_length=255, blank=True, null=True)
    cuit = models.CharField(max_length=255, blank=True, null=True)
    saldo_cta_cte = models.FloatField(blank=True, null=True)
    tipo_proveedor = models.ForeignKey('Tipoprov', models.DO_NOTHING,
                                       db_column='tipo_proveedor', blank=True,
                                       null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    tipo_factura = models.CharField(max_length=255, blank=True, null=True)
    retenc_ing_brutos = models.IntegerField(blank=True, null=True)
    categoriaib = models.IntegerField(blank=True, null=True)
    porc_retencion_ib = models.FloatField(blank=True, null=True)
    retenc_ganancia = models.IntegerField(blank=True, null=True)
    retenc_iva = models.IntegerField(blank=True, null=True)
    porc_retencion_iva = models.FloatField(blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    linea1 = models.CharField(max_length=255, blank=True, null=True)
    linea2 = models.CharField(max_length=255, blank=True, null=True)
    linea3 = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    inscripto_ganacias = models.IntegerField(blank=True, null=True)
    categoria_ganancias = models.IntegerField(blank=True, null=True)
    particip_total_compras = models.FloatField(blank=True, null=True)
    porcent_total_compras = models.FloatField(blank=True, null=True)
    tiene_credito = models.CharField(max_length=255, blank=True, null=True)
    total_cantidad = models.FloatField(blank=True, null=True)
    total_kilos = models.FloatField(blank=True, null=True)
    total_importe_deventa = models.FloatField(blank=True, null=True)
    total_preciocosto = models.FloatField(blank=True, null=True)
    total_diferencia = models.FloatField(blank=True, null=True)
    total_prd_e = models.FloatField(blank=True, null=True)
    fecha_vto_cuit = models.DateField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    nombre_fantasia = models.CharField(max_length=255, blank=True, null=True)
    tipo_calificacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'provedor'


# class Carga(models.Model):
#     id_carga = models.AutoField(primary_key=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     numero_proveedor = models.IntegerField(blank=True, null=True)
#     numero_deposito = models.ForeignKey('DepositoStock', models.DO_NOTHING,
#                                         db_column='numero_deposito', blank=True,
#                                         null=True,
#                                         related_name='carga_numerodeposito')
#     numero_actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                          db_column='numero_actividad',
#                                          blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateField(blank=True, null=True)
#     fecha_probable = models.DateField(blank=True, null=True)
#     tipo_factura = models.CharField(max_length=255, blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_movimiento = models.CharField(max_length=255, blank=True, null=True)
#     descuento = models.IntegerField(blank=True, null=True)
#     imp_varios = models.FloatField(blank=True, null=True)
#     iva = models.FloatField(blank=True, null=True)
#     impivadif1 = models.FloatField(blank=True, null=True)
#     impivadif2 = models.FloatField(blank=True, null=True)
#     excento = models.FloatField(blank=True, null=True)
#     netogrdo = models.FloatField(blank=True, null=True)
#     reten_ganancias = models.FloatField(blank=True, null=True)
#     percep_ingbrutos = models.FloatField(blank=True, null=True)
#     percep_iva = models.FloatField(blank=True, null=True)
#     total_factura = models.FloatField(blank=True, null=True)
#     total_facturadolares = models.FloatField(blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     cod_movimiento = models.ForeignKey('Movim', models.DO_NOTHING,
#                                        db_column='cod_movimiento', blank=True,
#                                        null=True)
#     nro_cliente = models.ForeignKey('Cli', models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     con_o_sin = models.IntegerField(blank=True, null=True)
#     total_cantidad = models.FloatField(blank=True, null=True)
#     total_kilos = models.FloatField(blank=True, null=True)
#     depositodestino = models.ForeignKey('DepositoStock', models.DO_NOTHING,
#                                         db_column='depositodestino', blank=True,
#                                         null=True,
#                                         related_name='carga_depositodestino')
#     tanque = models.ForeignKey('Tanque', models.DO_NOTHING, db_column='tanque',
#                                blank=True, null=True)
#     litros = models.FloatField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#     orden_compra = models.IntegerField(blank=True, null=True)
#     campana = models.ForeignKey(Campana, models.DO_NOTHING, db_column='campana',
#                                 blank=True, null=True)
#
#     class Meta:
#         db_table = 'carga'


# class Cargaoc(models.Model):
#     id_cargaoc = models.AutoField(primary_key=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     numero_proveedor = models.IntegerField(blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateField(blank=True, null=True)
#     fecha_probable = models.DateField(blank=True, null=True)
#     descuento = models.IntegerField(blank=True, null=True)
#     imp_varios = models.FloatField(blank=True, null=True)
#     iva = models.FloatField(blank=True, null=True)
#     impivadif1 = models.FloatField(blank=True, null=True)
#     impivadif2 = models.FloatField(blank=True, null=True)
#     excento = models.FloatField(blank=True, null=True)
#     netogrdo = models.FloatField(blank=True, null=True)
#     total_factura = models.FloatField(blank=True, null=True)
#     total_facturadolares = models.FloatField(blank=True, null=True)
#     cod_movimiento = models.ForeignKey('Movim', models.DO_NOTHING,
#                                        db_column='cod_movimiento', blank=True,
#                                        null=True)
#     total_cantidad = models.FloatField(blank=True, null=True)
#     total_kilos = models.FloatField(blank=True, null=True)
#     fecha_entrega = models.DateField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'cargaoc'


# class Ccarga(models.Model):
#     id_ccarga = models.AutoField(primary_key=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     numero_proveedor = models.IntegerField(blank=True, null=True)
#     numero_actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                          db_column='numero_actividad',
#                                          blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateField(blank=True, null=True)
#     fecha_probable = models.DateField(blank=True, null=True)
#     tipo_factura = models.CharField(max_length=255, blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_movimiento = models.CharField(max_length=255, blank=True, null=True)
#     descuento = models.IntegerField(blank=True, null=True)
#     imp_varios = models.FloatField(blank=True, null=True)
#     iva = models.FloatField(blank=True, null=True)
#     impivadif1 = models.FloatField(blank=True, null=True)
#     impivadif2 = models.FloatField(blank=True, null=True)
#     excento = models.FloatField(blank=True, null=True)
#     netogrdo = models.FloatField(blank=True, null=True)
#     reten_ganancias = models.FloatField(blank=True, null=True)
#     percep_ingbrutos = models.FloatField(blank=True, null=True)
#     percep_iva = models.FloatField(blank=True, null=True)
#     total_factura = models.FloatField(blank=True, null=True)
#     total_facturadolares = models.FloatField(blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     cod_movimiento = models.ForeignKey('Movim', models.DO_NOTHING,
#                                        db_column='cod_movimiento', blank=True,
#                                        null=True)
#     nro_cliente = models.ForeignKey('Cli', models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     con_o_sin = models.IntegerField(blank=True, null=True)
#     total_cantidad = models.FloatField(blank=True, null=True)
#     total_kilos = models.FloatField(blank=True, null=True)
#     depositodestino = models.ForeignKey('DepositoStock', models.DO_NOTHING,
#                                         db_column='depositodestino', blank=True,
#                                         null=True)

    class Meta:
        db_table = 'ccarga'


class Recibos(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    fecha_hoy = models.DateField(blank=True, null=True)
    nro_recibo = models.IntegerField(primary_key=True)
    nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
                                    db_column='nro_cliente', blank=True,
                                    null=True)
    importe = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'recibos'


class OrdPago(models.Model):
    codigo = models.IntegerField(primary_key=True)
    fecha_hoy = models.DateField(blank=True, null=True)
    nro_orden_pago = models.IntegerField(blank=True, null=True)
    nro_proveedor = models.ForeignKey('Proctcte', models.DO_NOTHING,
                                      db_column='nro_proveedor', blank=True,
                                      null=True)
    importe = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ord_pago'


class Cheqpag(models.Model):
    nro_usuario = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_cheque = models.DateField(primary_key=True)
    nro_cheque = models.IntegerField()
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco')
    nombre_banco = models.CharField(max_length=255, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    diroter = models.CharField(max_length=255, blank=True, null=True)
    cartera = models.CharField(max_length=255, blank=True, null=True)
    motivosalida = models.CharField(max_length=255, blank=True, null=True)
    descmot = models.CharField(max_length=255, blank=True, null=True)
    nro_ordenpago = models.ForeignKey('OrdPago', models.DO_NOTHING,
                                      db_column='nro_ordenpago', blank=True,
                                      null=True)

    class Meta:
        db_table = 'cheqpag'
        unique_together = (('fecha_cheque', 'nro_cheque', 'nro_banco'),)


class Cheqprop(models.Model):
    id_cheqprop = models.AutoField(primary_key=True)
    fecha_emision = models.DateField(blank=True, null=True)
    fecha_cheque = models.DateField(blank=True, null=True)
    nro_cheque = models.IntegerField(blank=True, null=True)
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    motivosalida = models.CharField(max_length=255, blank=True, null=True)
    descmot = models.CharField(max_length=255, blank=True, null=True)
    nro_ordenpago = models.ForeignKey('OrdPago', models.DO_NOTHING,
                                      db_column='nro_ordenpago', blank=True,
                                      null=True)
    nroproveedor = models.IntegerField(blank=True, null=True)
    concilado = models.IntegerField(blank=True, null=True)
    fecha_conciliado = models.DateField(blank=True, null=True)
    caja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='caja',
                             blank=True, null=True)
    banco_emisor = models.IntegerField(blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cheqprop'


# class Cheqrec(models.Model):
#     id_cheqrec = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey('Cli', models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     fecha_ingreso = models.DateField(blank=True, null=True)
#     fecha_cheque = models.DateField(blank=True, null=True)
#     nro_cheque = models.IntegerField(blank=True, null=True)
#     nro_banco = models.ForeignKey(Banc, models.DO_NOTHING,
#                                   db_column='nro_banco', blank=True, null=True)
#     nombre_banco = models.CharField(max_length=255, blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     diroter = models.CharField(max_length=255, blank=True, null=True)
#     cartera = models.IntegerField(blank=True, null=True)
#     motivosalida = models.CharField(max_length=255, blank=True, null=True)
#     descmot = models.CharField(max_length=255, blank=True, null=True)
#     nro_recibo = models.ForeignKey('Recibos', models.DO_NOTHING,
#                                    db_column='nro_recibo', blank=True,
#                                    null=True)
#
#     class Meta:
#         db_table = 'cheqrec'
#

class Cheques(models.Model):
    estado = models.CharField(max_length=255, blank=True, null=True)
    nro_cheque = models.IntegerField(primary_key=True)
    nrocliente = models.ForeignKey('Cli', models.DO_NOTHING,
                                   db_column='nrocliente', blank=True,
                                   null=True)
    descrip = models.CharField(max_length=255, blank=True, null=True)
    nom_banco = models.CharField(max_length=255, blank=True, null=True)
    fec_recepcion = models.DateField(blank=True, null=True)
    fec_cheque = models.DateField(blank=True, null=True)
    clearing = models.IntegerField(blank=True, null=True)
    directo_ter = models.CharField(max_length=255, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    banco_proveedor = models.CharField(max_length=255, blank=True, null=True)
    fec_salida = models.DateField(blank=True, null=True)
    salida = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey('Localidad', models.DO_NOTHING,
                                  db_column='localidad', blank=True, null=True)
    nrocuit = models.CharField(max_length=255, blank=True, null=True)
    cta_titular = models.CharField(max_length=255, blank=True, null=True)
    che_titular = models.CharField(max_length=255, blank=True, null=True)
    historico = models.CharField(max_length=255, blank=True, null=True)
    nrorecibo = models.ForeignKey('Recibos', models.DO_NOTHING,
                                  db_column='nrorecibo', blank=True, null=True)
    fecha_acreditacion = models.DateField(blank=True, null=True)
    negociado = models.IntegerField(blank=True, null=True)
    nroboleta = models.IntegerField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    marca = models.IntegerField(blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    prefijo_recibo = models.IntegerField(blank=True, null=True)
    nro_interno_cheque = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cheques'


# class Cheqant(models.Model):
#     estado = models.CharField(max_length=255, blank=True, null=True)
#     nro_cheque = models.ForeignKey('Cheques', models.DO_NOTHING,
#                                    db_column='nro_cheque')
#     nrocliente = models.ForeignKey('Cli', models.DO_NOTHING,
#                                    db_column='nrocliente', blank=True,
#                                    null=True)
#     descrip = models.CharField(max_length=255, blank=True, null=True)
#     nom_banco = models.CharField(max_length=255, blank=True, null=True)
#     fec_recepcion = models.DateField(blank=True, null=True)
#     fec_cheque = models.DateField(blank=True, null=True)
#     clearing = models.ForeignKey('Clering', models.DO_NOTHING,
#                                  db_column='clearing', blank=True, null=True)
#     directo_ter = models.CharField(max_length=255, blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     tipo = models.CharField(max_length=255, blank=True, null=True)
#     banco_proveedor = models.CharField(max_length=255, blank=True, null=True)
#     fec_salida = models.DateField(blank=True, null=True)
#     salida = models.CharField(max_length=255, blank=True, null=True)
#     localidad = models.ForeignKey('Localidad', models.DO_NOTHING,
#                                   db_column='localidad', blank=True, null=True)
#     nrocuit = models.CharField(max_length=255, blank=True, null=True)
#     cta_titular = models.CharField(max_length=255, blank=True, null=True)
#     che_titular = models.CharField(max_length=255, blank=True, null=True)
#     historico = models.CharField(max_length=255, blank=True, null=True)
#     nrorecibo = models.ForeignKey('Recibos', models.DO_NOTHING,
#                                   db_column='nrorecibo', blank=True, null=True)
#     fecha_acreditacion = models.DateField(blank=True, null=True)
#     negociado = models.IntegerField(blank=True, null=True)
#     nroboleta = models.IntegerField(blank=True, null=True)
#     conciliado = models.IntegerField(blank=True, null=True)
#     marca = models.IntegerField(blank=True, null=True)
#     fecha_pase = models.DateField(blank=True, null=True)
#     fecha_devolucion = models.DateField(blank=True, null=True)
#     motivo_devolucion = models.CharField(max_length=255, blank=True, null=True)
#     prefijo_recibo = models.IntegerField(blank=True, null=True)
#     nro_interno_cheque = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'cheqant'


# class Cobrados(models.Model):
#     id_cobrados = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     tipo_movim = models.CharField(max_length=255, blank=True, null=True)
#     nro_comprob = models.IntegerField(blank=True, null=True)
#     fecha_comprob = models.DateField(blank=True, null=True)
#     fecha_vencim = models.DateField(blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     imp_neto_grav = models.FloatField(blank=True, null=True)
#     pagoacuenta = models.FloatField(blank=True, null=True)
#     tipo_cliente = models.IntegerField(blank=True, null=True)
#     cant_cuotas = models.IntegerField(blank=True, null=True)
#     nro_cuotas = models.IntegerField(blank=True, null=True)
#     tipo_fact = models.IntegerField(blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     saldo = models.FloatField(blank=True, null=True)
#     codi = models.IntegerField(blank=True, null=True)
#     pagar_parte = models.FloatField(blank=True, null=True)
#     nro_recibo = models.ForeignKey(Recibos, models.DO_NOTHING,
#                                    db_column='nro_recibo', blank=True,
#                                    null=True)
#
#     class Meta:
#         db_table = 'cobrados'


class Creditos(models.Model):
    id_creditos = models.AutoField(primary_key=True)
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    imputacion = models.IntegerField(blank=True, null=True)
    nro_credito = models.IntegerField(blank=True, null=True)
    fecha = models.CharField(max_length=255, blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'creditos'


class CtaCte(models.Model):
    id_cta_cte = models.AutoField(primary_key=True)
    tipo_movim = models.ForeignKey(TipoMovimiento, models.DO_NOTHING,
                                   db_column='tipo_movim',
                                   blank=True, null=True)
    cod_proveedor = models.ForeignKey(Proctcte, models.DO_NOTHING,
                                      db_column='cod_proveedor', blank=True,
                                      null=True)
    fecha_comprob = models.DateField(blank=True, null=True,
                                     verbose_name='Fecha Comprobante')
    nro_comprob = models.IntegerField(blank=True, null=True,
                                      verbose_name='Nro. Comprobante')
    importe = models.FloatField(blank=True, null=True)
    importedolares = models.FloatField(blank=True, null=True)
    periodo_contable = models.DateField(blank=True, null=True,
                                        verbose_name='Periodo Contable')
    prefijo = models.IntegerField(blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=255, blank=True, null=True,
                                        verbose_name='Tipo Comprobante')

    class Meta:
        db_table = 'cta_cte'


class Ctepro(models.Model):
    id_ctepro = models.AutoField(primary_key=True)
    codcli = models.ForeignKey(Cli, models.DO_NOTHING, db_column='codcli',
                               blank=True, null=True)
    codpro = models.ForeignKey('Proctcte', models.DO_NOTHING,
                               db_column='codpro', blank=True, null=True)

    class Meta:
        db_table = 'ctepro'


# class Cteprocc(models.Model):
#     id_cteprocc = models.AutoField(primary_key=True)
#     tipocomprob = models.CharField(max_length=255, blank=True, null=True)
#     letracomp = models.CharField(max_length=255, blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     nro_comprob = models.IntegerField(blank=True, null=True)
#     codcliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                    db_column='codcliente', blank=True,
#                                    null=True)
#     codproveedor = models.ForeignKey('Proctcte', models.DO_NOTHING,
#                                      db_column='codproveedor', blank=True,
#                                      null=True)
#     fecha_comprob = models.DateField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     fecha_vencim = models.DateField(blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     importedolares = models.FloatField(blank=True, null=True)
#     cereal = models.CharField(max_length=255, blank=True, null=True)
#     kilos = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'cteprocc'


# class Cventa(models.Model):
#     id_cventa = models.AutoField(primary_key=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     numero_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                        db_column='numero_cliente', blank=True,
#                                        null=True)
#     numero_deposito = models.ForeignKey('DepositoStock', models.DO_NOTHING,
#                                         db_column='numero_deposito', blank=True,
#                                         null=True)
#     numero_actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                          db_column='numero_actividad',
#                                          blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateField(blank=True, null=True)
#     fecha_probable = models.DateField(blank=True, null=True)
#     tipo_factura = models.CharField(max_length=255, blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_movimiento = models.CharField(max_length=255, blank=True, null=True)
#     descuento = models.IntegerField(blank=True, null=True)
#     imp_varios = models.FloatField(blank=True, null=True)
#     iva = models.FloatField(blank=True, null=True)
#     impivadif1 = models.FloatField(blank=True, null=True)
#     impivadif2 = models.FloatField(blank=True, null=True)
#     excento = models.FloatField(blank=True, null=True)
#     gastos_exentos = models.FloatField(blank=True, null=True)
#     netogrdo = models.FloatField(blank=True, null=True)
#     reten_ganancias = models.FloatField(blank=True, null=True)
#     percep_ingbrutos = models.FloatField(blank=True, null=True)
#     percep_iva = models.FloatField(blank=True, null=True)
#     total_factura = models.FloatField(blank=True, null=True)
#     total_facturadolares = models.FloatField(blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     cod_movimiento = models.ForeignKey('Movim', models.DO_NOTHING,
#                                        db_column='cod_movimiento', blank=True,
#                                        null=True)
#     nro_cliente = models.IntegerField(blank=True, null=True)
#     con_o_sin = models.IntegerField(blank=True, null=True)
#     total_cantidad = models.FloatField(blank=True, null=True)
#     total_kilos = models.FloatField(blank=True, null=True)
#     depositodestino = models.IntegerField(blank=True, null=True)
#     tanque = models.ForeignKey('Tanque', models.DO_NOTHING, db_column='tanque',
#                                blank=True, null=True)
#     litros = models.FloatField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'cventa'


class Debitos(models.Model):
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    desc_motivo = models.CharField(max_length=255, blank=True, null=True)
    nro_debito = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    imputacion = models.CharField(max_length=255, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    iva_percepcion = models.FloatField(blank=True, null=True)
    periodo_contable = models.DateField(blank=True, null=True)
    fecha_conciliacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'debitos'


class Deposito(models.Model):
    id_deposito = models.AutoField(primary_key=True)
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    nro_boleta = models.IntegerField(blank=True, null=True)
    tipo_efectivo = models.IntegerField(blank=True, null=True)
    tipo_cheques = models.IntegerField(blank=True, null=True)
    desc_motivo = models.CharField(max_length=255, blank=True, null=True)
    tipo_interdep = models.IntegerField(blank=True, null=True)
    tipo_vta_valores = models.IntegerField(blank=True, null=True)
    fecha_boleta = models.DateField(blank=True, null=True)
    clearing = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    fecha_acreditacion = models.DateField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    caja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='caja',
                             blank=True, null=True)
    transpaso = models.IntegerField(blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    acred_pend_asig = models.IntegerField(blank=True, null=True)
    marca_anul = models.IntegerField(blank=True, null=True)
    prefijo_rec = models.IntegerField(blank=True, null=True)
    fecha_conciliacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'deposito'


class Destino(models.Model):
    codigo = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.ForeignKey('Localidad', models.DO_NOTHING,
                                  db_column='localidad', blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    linea1 = models.CharField(max_length=255, blank=True, null=True)
    linea2 = models.CharField(max_length=255, blank=True, null=True)
    linea3 = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    inscripto_ganancias = models.IntegerField(blank=True, null=True)
    categoria_ganancias = models.IntegerField(blank=True, null=True)
    particip_total_compras = models.FloatField(blank=True, null=True)
    porcent_total_compras = models.FloatField(blank=True, null=True)
    tiene_credito = models.CharField(max_length=255, blank=True, null=True)
    total_cantidad = models.FloatField(blank=True, null=True)
    total_kilos = models.FloatField(blank=True, null=True)
    total_importe_deventa = models.FloatField(blank=True, null=True)
    total_preciocosto = models.FloatField(blank=True, null=True)
    total_diferencia = models.FloatField(blank=True, null=True)
    total_prd_e = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'destino'


class Rodeo(models.Model):
    nro_rodeo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    kilos = models.IntegerField(blank=True, null=True)
    grupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='grupo',
                              blank=True, null=True)

    class Meta:
        db_table = 'rodeo'


class GanCar(models.Model):
    id_gan_car = models.AutoField(primary_key=True)
    movimiento = models.ForeignKey('Movim', models.DO_NOTHING,
                                   db_column='movimiento', blank=True,
                                   null=True)
    fecha = models.DateField(blank=True, null=True)
    nro_comprobante = models.IntegerField(blank=True, null=True)
    proveedor = models.IntegerField(blank=True, null=True)
    nro_categoria = models.IntegerField(blank=True, null=True)
    nro_rodeo = models.ForeignKey('Rodeo', models.DO_NOTHING,
                                  db_column='nro_rodeo', blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    kilos = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'gan_car'


class Gf(models.Model):
    id_gf = models.AutoField(primary_key=True)
    n_comp = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    rz_motivo = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    impu = models.IntegerField(blank=True, null=True)
    i_o_e = models.IntegerField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    nrocaja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='nrocaja',
                                blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    nrocajadestino = models.IntegerField(blank=True, null=True)
    imputacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'gf'


# class Gg(models.Model):
#     id_gg = models.AutoField(primary_key=True)
#     n_comp = models.IntegerField(blank=True, null=True)
#     nrocaja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='nrocaja',
#                                 blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     rz_motivo = models.CharField(max_length=255, blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     impu = models.IntegerField(blank=True, null=True)
#     i_o_e = models.IntegerField(blank=True, null=True)
#     efec_o_cheq = models.IntegerField(blank=True, null=True)
#     nrocajadestino = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'gg'


class Giros(models.Model):
    id_giros = models.AutoField(primary_key=True)
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    desc_motivo = models.CharField(max_length=255, blank=True, null=True)
    nro_interdep = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    nro_caja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='nro_caja',
                                 blank=True, null=True)
    nro_provee = models.IntegerField(blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    fecha_pase = models.DateField(blank=True, null=True)
    fecha_conciliacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'giros'


class Glibroba(models.Model):
    identificacion = models.IntegerField(blank=True, null=True)
    banco = models.ForeignKey(Bancos, models.DO_NOTHING, db_column='banco')
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    tipo_clearing = models.IntegerField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    nrocheque = models.ForeignKey(Cheques, models.DO_NOTHING,
                                  db_column='nrocheque')

    class Meta:
        db_table = 'glibroba'
        unique_together = (('banco', 'nrocheque'),)


class Grecibo(models.Model):
    nro_orden = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
                                    db_column='nro_cliente', blank=True,
                                    null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    pago_efectivo = models.FloatField(blank=True, null=True)
    nrocaja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='nrocaja',
                                blank=True, null=True)
    pagocheterceros = models.FloatField(blank=True, null=True)
    pagointerdeposito = models.FloatField(blank=True, null=True)
    bancointerdeposito = models.IntegerField(blank=True, null=True)
    ret_gan = models.FloatField(blank=True, null=True)
    ret_iva = models.FloatField(blank=True, null=True)
    ret_ib = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'grecibo'
        unique_together = (('nro_orden', 'fecha'),)


class Guareten(models.Model):
    fecha = models.DateField(primary_key=True)
    nro_retencion = models.ForeignKey('Retencio', models.DO_NOTHING,
                                      db_column='nro_retencion')
    nro_acreedor = models.IntegerField(blank=True, null=True)
    nro_orden_pago = models.ForeignKey('OrdPago', models.DO_NOTHING,
                                       db_column='nro_orden_pago', blank=True,
                                       null=True)
    pagos_anteriores = models.FloatField(blank=True, null=True)
    importe_neto = models.FloatField(blank=True, null=True)
    sub_acumulado_mes = models.FloatField(blank=True, null=True)
    minimo_imponible = models.FloatField(blank=True, null=True)
    monto_sujeto = models.FloatField(blank=True, null=True)
    retencion_calculada = models.FloatField(blank=True, null=True)
    retencion_anterior = models.FloatField(blank=True, null=True)
    retencion_efectuada = models.FloatField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'guareten'
        unique_together = (('fecha', 'nro_retencion'),)


class Guaretenib(models.Model):
    fecha = models.DateField(primary_key=True)
    nro_retencion = models.ForeignKey('Retencio', models.DO_NOTHING,
                                      db_column='nro_retencion')
    nro_acreedor = models.IntegerField(blank=True, null=True)
    nro_acreedor_contado = models.IntegerField(blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    nro_orden_pago = models.ForeignKey('OrdPago', models.DO_NOTHING,
                                       db_column='nro_orden_pago', blank=True,
                                       null=True)
    nro_categoria = models.IntegerField(blank=True, null=True)
    monto_retenido = models.FloatField(blank=True, null=True)
    alicuota = models.FloatField(blank=True, null=True)
    provincia = models.ForeignKey('Provincias', models.DO_NOTHING,
                                  db_column='provincia', blank=True, null=True)
    normativa = models.CharField(max_length=255, blank=True, null=True)
    numero_agente = models.CharField(max_length=255, blank=True, null=True)
    prefijo_op = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'guaretenib'
        unique_together = (('fecha', 'nro_retencion'),)


class Guareteniva(models.Model):
    fecha = models.DateField(primary_key=True)
    prefijo = models.IntegerField(blank=True, null=True)
    nro_retencion = models.ForeignKey('Retencio', models.DO_NOTHING,
                                      db_column='nro_retencion')
    nro_acreedor = models.IntegerField(blank=True, null=True)
    nro_orden_pago = models.ForeignKey('OrdPago', models.DO_NOTHING,
                                       db_column='nro_orden_pago', blank=True,
                                       null=True)
    monto_retenido = models.FloatField(blank=True, null=True)
    alicuota = models.FloatField(blank=True, null=True)
    prefijo_op = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'guareteniva'
        unique_together = (('fecha', 'nro_retencion'),)


class Humedad(models.Model):
    id_humedad = models.AutoField(primary_key=True)
    cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING, db_column='cultivo',
                                blank=True, null=True)
    descripcion_cultivo = models.CharField(max_length=255, blank=True,
                                           null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    porcentaje_merma = models.FloatField(blank=True, null=True)
    porcentaje_manipuleo = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'humedad'


class Interdep(models.Model):
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    desc_motivo = models.CharField(max_length=255, blank=True, null=True)
    nro_interdep = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    nro_ord_pago = models.ForeignKey('OrdPago', models.DO_NOTHING,
                                     db_column='nro_ord_pago', blank=True,
                                     null=True)
    importe = models.FloatField(blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'interdep'


class Potreros(models.Model):
    nro_potrero = models.CharField(primary_key=True, max_length=255)
    campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
                              blank=True, null=True)
    cantidad_de_hectareas_reales = models.FloatField(blank=True, null=True)
    cantidad_de_hectareas_efectivas = models.FloatField(blank=True, null=True)
    campana_actual = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='campana_actual', blank=True,
                                       null=True)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
                                  db_column='actividad', blank=True, null=True)
    porcarrendado = models.FloatField(blank=True, null=True)
    de_baja = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'potreros'


class Producto(models.Model):
    nro_producto = models.IntegerField(primary_key=True)
    nro_linea = models.ForeignKey(Lineas, models.DO_NOTHING,
                                  db_column='nro_linea', blank=True, null=True)
    nro_rubro = models.ForeignKey(Rubros, models.DO_NOTHING,
                                  db_column='nro_rubro', blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)
    precio_compra = models.FloatField(blank=True, null=True)
    consumo_mensual_unidades = models.FloatField(blank=True, null=True)
    fecha_ucompra = models.DateField(blank=True, null=True)
    venta_mensaul_kilos = models.FloatField(blank=True, null=True)
    gasto_mensual = models.FloatField(blank=True, null=True)
    stock_unidades = models.FloatField(blank=True, null=True)
    stock_kilos = models.FloatField(blank=True, null=True)
    imp_iva = models.IntegerField(blank=True, null=True)
    stock_minimo_unid = models.FloatField(blank=True, null=True)
    stock_minimo_kilos = models.FloatField(blank=True, null=True)
    baja = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'producto'


class Items(models.Model):
    id_items = models.AutoField(primary_key=True)
    movimiento = models.CharField(max_length=255, blank=True,
                                   null=True)
    fecha = models.DateField(blank=True, null=True)
    nro_comprobante = models.IntegerField(blank=True, null=True)
    nro_proveedor = models.IntegerField(blank=True, null=True)
    nro_deposito = models.ForeignKey(DepositoStock, models.DO_NOTHING,
                                     db_column='nro_deposito', blank=True,
                                     null=True)
    nro_centro_costo = models.IntegerField(blank=True, null=True)
    nro_rubro = models.ForeignKey(Rubros, models.DO_NOTHING,
                                  db_column='nro_rubro', blank=True, null=True)
    nro_producto = models.ForeignKey(Producto, models.DO_NOTHING,
                                     db_column='nro_producto', blank=True,
                                     null=True)
    cantidad = models.FloatField(blank=True, null=True)
    kilos = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    potrero = models.ForeignKey(Potreros, models.DO_NOTHING,
                                db_column='potrero', blank=True, null=True)
    campana = models.ForeignKey(Campana, models.DO_NOTHING, db_column='campana',
                                blank=True, null=True)

    class Meta:
        db_table = 'items'


# class Libroba(models.Model):
#     id_libroba = models.AutoField(primary_key=True)
#     identificacion = models.IntegerField(blank=True, null=True)
#     banco = models.ForeignKey(Bancos, models.DO_NOTHING, db_column='banco',
#                               blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     descripcion = models.CharField(max_length=255, blank=True, null=True)
#     numero = models.IntegerField(blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     tipo_clearing = models.IntegerField(blank=True, null=True)
#     conciliado = models.IntegerField(blank=True, null=True)
#     nrocheque = models.ForeignKey(Cheques, models.DO_NOTHING,
#                                   db_column='nrocheque', blank=True, null=True)
#
#     class Meta:
#         db_table = 'libroba'


# class Maeche(models.Model):
#     id_maeche = models.AutoField(primary_key=True)
#     nrocliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                    db_column='nrocliente', blank=True,
#                                    null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     dir_cantidad = models.IntegerField(blank=True, null=True)
#     dir0 = models.IntegerField(blank=True, null=True)
#     dir1_2 = models.IntegerField(blank=True, null=True)
#     dir3 = models.IntegerField(blank=True, null=True)
#     dir_fecha = models.DateField(blank=True, null=True)
#     dir_importe = models.FloatField(blank=True, null=True)
#     ter_cantidad = models.IntegerField(blank=True, null=True)
#     ter0 = models.IntegerField(blank=True, null=True)
#     ter1_2 = models.IntegerField(blank=True, null=True)
#     ter3 = models.IntegerField(blank=True, null=True)
#     ter_fecha = models.DateField(blank=True, null=True)
#     ter_importe = models.FloatField(blank=True, null=True)
#     saldo_total = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'maeche'
#
#
# class Maecli(models.Model):
#     id_maecli = models.AutoField(primary_key=True)
#     estado = models.CharField(max_length=255, blank=True, null=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 'maecli'


class Maquina(models.Model):
    nro_maquina = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    campo_asignada = models.ForeignKey(Campos, models.DO_NOTHING,
                                       db_column='campo_asignada', blank=True,
                                       null=True)
    fecha_de_compra = models.DateField(blank=True, null=True)
    costo_de_compra = models.FloatField(blank=True, null=True)
    vida_util = models.IntegerField(blank=True, null=True)
    nro_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
                                    db_column='nro_laboreo', blank=True,
                                    null=True)
    nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
                                       db_column='nro_imputacion', blank=True,
                                       null=True)
    imputcomb = models.IntegerField(blank=True, null=True)
    capacidad_tanque = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'maquina'


class Mensual(models.Model):
    id_mensual = models.AutoField(primary_key=True)
    tipo_movim = models.ForeignKey(TipoMovimiento, models.DO_NOTHING,
                                   db_column='tipo_movim',
                                   blank=True, null=True,
                                   verbose_name='Tipo Movimiento')
    fecha_comprob = models.DateField(blank=True, null=True,
                                     verbose_name='Fecha Comprobante')
    tipo_comprob = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name='Tipo Comprobante')
    prefijo = models.IntegerField(blank=True, null=True)
    nro_compro = models.IntegerField(blank=True, null=True,
                                     verbose_name='Nro. Comprobante')
    cod_proveedor = models.ForeignKey(Proctcte, models.DO_NOTHING,
                                      db_column='cod_proveedor',
                                      blank=True, null=True,
                                      verbose_name='Proveedor')
    imp_exento = models.FloatField(blank=True, null=True,
                                   verbose_name='Excento')
    imp_gravado = models.FloatField(blank=True, null=True,
                                    verbose_name='Gravado 21%')
    imp_gravado_10 = models.FloatField(blank=True, null=True,
                                       verbose_name='Gravado 10.5%')
    imp_gravado_27 = models.FloatField(blank=True, null=True,
                                       verbose_name='Gravado 27%')
    importe_iva = models.FloatField(blank=True, null=True,
                                    verbose_name='IVA 21%')
    imp_iva10 = models.FloatField(blank=True, null=True,
                                  verbose_name='IVA 10.5%')
    imp_iva27 = models.FloatField(blank=True, null=True,
                                  verbose_name='IVA 27%')
    imp_perc_iva = models.FloatField(blank=True, null=True,
                                     verbose_name='Percepción IVA')
    imp_per_ing_brutos = models.FloatField(blank=True, null=True,
                                           verbose_name='Per. Ing. Brutos')
    retenc_gananc = models.FloatField(blank=True, null=True,
                                      verbose_name='Retención Ganancias')
    imp_varios = models.FloatField(blank=True, null=True,
                                   verbose_name='Impuestos Varios')
    imp_total = models.FloatField(blank=True, null=True,
                                  verbose_name='Importe Total')
    imp_total_dolares = models.FloatField(blank=True, null=True)
    cod_provincia = models.ForeignKey('Provincias', models.DO_NOTHING,
                                      db_column='cod_provincia', blank=True,
                                      null=True)
    periodo_contable = models.DateField(blank=True, null=True,
                                        verbose_name='Periodo Contable')
    retencion_iva = models.FloatField(blank=True, null=True,
                                      verbose_name='Retención IVA')
    retencion_ib = models.FloatField(blank=True, null=True,
                                     verbose_name='Retención IB')

    class Meta:
        db_table = 'mensual'


class MontosParaGirar(models.Model):
    id_montos_para_girar = models.AutoField(primary_key=True)
    nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
                                  db_column='nro_banco', blank=True, null=True)
    fecha_desde = models.DateField(blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)
    limite_a_girar = models.FloatField(blank=True, null=True)
    montos_girados = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'montos_para_girar'


class MovCamp(models.Model):
    id_mov_camp = models.AutoField(primary_key=True)
    campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
                              blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector',
                               blank=True, null=True)
    sub_sector = models.ForeignKey('Subsecto', models.DO_NOTHING,
                                   db_column='sub_sector', blank=True,
                                   null=True)
    fecha = models.DateField(blank=True, null=True)
    laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING, db_column='laboreo',
                                blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    codigo_agroquimico = models.IntegerField(blank=True, null=True)
    codigo_fertilizante = models.IntegerField(blank=True, null=True)
    dosis = models.FloatField(blank=True, null=True)
    horas = models.IntegerField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    campana_actual = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='campana_actual', blank=True,
                                       null=True)

    class Meta:
        db_table = 'mov_camp'


class Tractor(models.Model):
    nro_tractor = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    campo_asignado = models.ForeignKey(Campos, models.DO_NOTHING,
                                       db_column='campo_asignado', blank=True,
                                       null=True)
    fecha_de_compra = models.DateField(blank=True, null=True)
    costo_de_compra = models.FloatField(blank=True, null=True)
    vida_util = models.IntegerField(blank=True, null=True)
    nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
                                       db_column='nro_imputacion', blank=True,
                                       null=True)
    imputcomb = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tractor'


class MovCons(models.Model):
    id_mov_cons = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    ing_egr = models.IntegerField(blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    nro_tractor = models.ForeignKey('Tractor', models.DO_NOTHING,
                                    db_column='nro_tractor', blank=True,
                                    null=True)
    nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
                                    db_column='nro_maquina', blank=True,
                                    null=True)
    nro_rodado = models.ForeignKey('Rodados', models.DO_NOTHING,
                                   db_column='nro_rodado', blank=True,
                                   null=True)
    nro_camion = models.ForeignKey(Camion, models.DO_NOTHING,
                                   db_column='nro_camion', blank=True,
                                   null=True)
    responsable = models.ForeignKey('Respons', models.DO_NOTHING,
                                    db_column='responsable', blank=True,
                                    null=True)
    tanque = models.ForeignKey('Tanque', models.DO_NOTHING, db_column='tanque',
                               blank=True, null=True)
    litros = models.FloatField(blank=True, null=True)
    centro_costo = models.IntegerField(blank=True, null=True)
    proveedor = models.IntegerField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'mov_cons'


class Silos(models.Model):
    nro_silo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    nro_cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING,
                                    db_column='nro_cultivo', blank=True,
                                    null=True)
    stock = models.FloatField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'silos'


class Tractori(models.Model):
    nro_tractorista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_ingreso = models.DateField(blank=True, null=True)
    sector_asignado = models.ForeignKey(Sector, models.DO_NOTHING,
                                        db_column='sector_asignado', blank=True,
                                        null=True)

    class Meta:
        db_table = 'tractori'


class MovCose(models.Model):
    id_mov_cose = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector',
                               blank=True, null=True)
    sub_sector = models.ForeignKey('Subsecto', models.DO_NOTHING,
                                   db_column='sub_sector', blank=True,
                                   null=True)
    campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
                              blank=True, null=True)
    potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
                                db_column='potrero', blank=True, null=True)
    codigo_campana = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='codigo_campana', blank=True,
                                       null=True)
    codigo_cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING,
                                       db_column='codigo_cultivo', blank=True,
                                       null=True)
    codigo_camion = models.ForeignKey(Camion, models.DO_NOTHING,
                                      db_column='codigo_camion', blank=True,
                                      null=True)
    codigo_destino = models.ForeignKey(Destino, models.DO_NOTHING,
                                       db_column='codigo_destino', blank=True,
                                       null=True)
    codigo_silo = models.ForeignKey('Silos', models.DO_NOTHING,
                                    db_column='codigo_silo', blank=True,
                                    null=True)
    codigo_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
                                           db_column='codigo_contratista',
                                           blank=True, null=True)
    codigo_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
                                           db_column='codigo_tractorista',
                                           blank=True, null=True)
    nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
                                    db_column='nro_maquina', blank=True,
                                    null=True)
    carta_porte = models.CharField(max_length=255, blank=True, null=True)
    kilos_origen = models.FloatField(blank=True, null=True)
    kilos_neto_origen = models.FloatField(blank=True, null=True)
    kilos_destino = models.FloatField(blank=True, null=True)
    kilos_neto_destino = models.FloatField(blank=True, null=True)
    hectareas = models.FloatField(blank=True, null=True)
    humedad = models.FloatField(blank=True, null=True)
    cuerpo_extrano = models.FloatField(blank=True, null=True)
    merma_volatil = models.FloatField(blank=True, null=True)
    merma = models.FloatField(blank=True, null=True)
    humedad_rec = models.FloatField(blank=True, null=True)
    cuerpo_extrano_rec = models.FloatField(blank=True, null=True)
    merma_volatil_rec = models.FloatField(blank=True, null=True)
    variedad_semilla = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'mov_cose'


class MovHora(models.Model):
    id_mov_hora = models.AutoField(primary_key=True)
    nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
                                        db_column='nro_tractorista', blank=True,
                                        null=True)
    fecha = models.DateField(blank=True, null=True)
    entrada_manana = models.IntegerField(blank=True, null=True)
    salida_manana = models.IntegerField(blank=True, null=True)
    entrada_tarde = models.IntegerField(blank=True, null=True)
    salida_tarde = models.IntegerField(blank=True, null=True)
    horas_trabajadas = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'mov_hora'


class MovLeche(models.Model):
    id_mov_leche = models.AutoField(primary_key=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, models.DO_NOTHING,
                                        db_column='tipo_movimiento',
                                        blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
                                    db_column='nro_cliente', blank=True,
                                    null=True)
    nro_comprobante = models.IntegerField(blank=True, null=True)
    litros = models.IntegerField(blank=True, null=True)
    kilos_grasa = models.FloatField(blank=True, null=True)
    kilos_proteinas = models.FloatField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'mov_leche'


class MovPotr(models.Model):
    id_mov_potr = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector',
                               blank=True, null=True)
    sub_sector = models.ForeignKey('Subsecto', models.DO_NOTHING,
                                   db_column='sub_sector', blank=True,
                                   null=True)
    campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
                              blank=True, null=True)
    nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
                                    db_column='nro_potrero', blank=True,
                                    null=True)
    codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
                                       db_column='codigo_laboreo', blank=True,
                                       null=True)
    contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
                                    db_column='contratista', blank=True,
                                    null=True)
    hectareas = models.FloatField(blank=True, null=True)
    codigo_agroquimico = models.ForeignKey(Agroquim, models.DO_NOTHING,
                                           db_column='codigo_agroquimico',
                                           blank=True, null=True)
    dosis = models.FloatField(blank=True, null=True)
    codigo_cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING,
                                       db_column='codigo_cultivo', blank=True,
                                       null=True)
    codigo_semilla = models.IntegerField(blank=True, null=True)
    codigo_fertilizante = models.ForeignKey(Fertiliz, models.DO_NOTHING,
                                            db_column='codigo_fertilizante',
                                            blank=True, null=True)
    codigo_bolsas = models.IntegerField(blank=True, null=True)
    codigo_campana = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='codigo_campana', blank=True,
                                       null=True)
    cantidad_rollo = models.IntegerField(blank=True, null=True)
    codigo_destino = models.ForeignKey(Destino, models.DO_NOTHING,
                                       db_column='codigo_destino', blank=True,
                                       null=True)
    codigo_silo = models.ForeignKey('Silos', models.DO_NOTHING,
                                    db_column='codigo_silo', blank=True,
                                    null=True)
    kilos_totales = models.FloatField(blank=True, null=True)
    humedad = models.IntegerField(blank=True, null=True)
    horas = models.IntegerField(blank=True, null=True)
    dias = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=255, blank=True, null=True)
    centro_costo = models.IntegerField(blank=True, null=True)
    euta = models.FloatField(blank=True, null=True)
    utas = models.FloatField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    sumaoresta = models.IntegerField(blank=True, null=True)
    dosis_est = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'mov_potr'


class MovProd(models.Model):
    id_mov_prod = models.AutoField(primary_key=True)
    nro_tambo = models.ForeignKey(Tambos, models.DO_NOTHING,
                                  db_column='nro_tambo', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    ing_egr = models.IntegerField(blank=True, null=True)
    m_t = models.CharField(max_length=255, blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    litros = models.FloatField(blank=True, null=True)
    destino = models.ForeignKey(Destino, models.DO_NOTHING, db_column='destino',
                                blank=True, null=True)
    vacas_ordene = models.IntegerField(blank=True, null=True)
    porc_grasa = models.FloatField(blank=True, null=True)
    porc_proteina = models.FloatField(blank=True, null=True)
    cel_somatica = models.IntegerField(blank=True, null=True)
    rec_bact = models.IntegerField(blank=True, null=True)
    crioscopia = models.FloatField(blank=True, null=True)
    temperatura = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'mov_prod'


class MovSilos(models.Model):
    id_mov_silos = models.AutoField(primary_key=True)
    movimiento = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    nro_comprobante = models.IntegerField(blank=True, null=True)
    nro_destino = models.ForeignKey(Destino, models.DO_NOTHING,
                                    db_column='nro_destino', blank=True,
                                    null=True)
    nro_silo_entrante = models.ForeignKey('Silos', models.DO_NOTHING,
                                          db_column='nro_silo_entrante',
                                          blank=True, null=True,
                                          related_name='movsilos_silo_entrante')
    nro_cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING,
                                    db_column='nro_cultivo', blank=True,
                                    null=True)
    nro_silo = models.ForeignKey(Silos, models.DO_NOTHING,
                                 db_column='nro_silo', blank=True, null=True,
                                 related_name='movsilos_nro_silo')
    nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
                                    db_column='nro_potrero', blank=True,
                                    null=True)
    kilos = models.FloatField(blank=True, null=True)
    humedad = models.FloatField(blank=True, null=True)
    cuerpos_extranos = models.FloatField(blank=True, null=True)
    merma_volatil = models.FloatField(blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING,
                                 db_column='producto', blank=True, null=True)
    cliente = models.ForeignKey(Cli, models.DO_NOTHING, db_column='cliente',
                                blank=True, null=True)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
                                  db_column='actividad', blank=True, null=True)

    class Meta:
        db_table = 'mov_silos'


class MovSuple(models.Model):
    id_mov_suple = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
                                  db_column='actividad', blank=True, null=True)
    nro_silo = models.ForeignKey('Silos', models.DO_NOTHING,
                                 db_column='nro_silo', blank=True, null=True)
    kilos = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    nro_impu_ingreso = models.IntegerField(blank=True, null=True)
    nro_impu_egreso = models.IntegerField(blank=True, null=True)
    nro_producto = models.ForeignKey('Producto', models.DO_NOTHING,
                                     db_column='nro_producto', blank=True,
                                     null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'mov_suple'


class MovTrac(models.Model):
    id_mov_trac = models.AutoField(primary_key=True)
    nro_tractor = models.ForeignKey('Tractor', models.DO_NOTHING,
                                    db_column='nro_tractor', blank=True,
                                    null=True)
    nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
                                        db_column='nro_tractorista', blank=True,
                                        null=True)
    nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
                                    db_column='nro_maquina', blank=True,
                                    null=True)
    fecha = models.DateField(blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector',
                               blank=True, null=True)
    sub_sector = models.ForeignKey('Subsecto', models.DO_NOTHING,
                                   db_column='sub_sector', blank=True,
                                   null=True)
    campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
                              blank=True, null=True)
    nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
                                    db_column='nro_potrero', blank=True,
                                    null=True)
    codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
                                       db_column='codigo_laboreo', blank=True,
                                       null=True)
    hectareas = models.FloatField(blank=True, null=True)
    horas = models.IntegerField(blank=True, null=True)
    dias = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    campana_actual = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='campana_actual', blank=True,
                                       null=True)
    centro_costo = models.IntegerField(blank=True, null=True)
    euta = models.FloatField(blank=True, null=True)
    uta = models.FloatField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    hodometro = models.IntegerField(blank=True, null=True)
    litros_gasoil = models.IntegerField(blank=True, null=True)
    litros_aceite = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'mov_trac'


class MovTrans(models.Model):
    id_mov_trans = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    carta_porte = models.CharField(max_length=255, blank=True, null=True)
    nro_transporte = models.ForeignKey('Transp', models.DO_NOTHING,
                                       db_column='nro_transporte', blank=True,
                                       null=True)
    nro_chofer = models.ForeignKey(Chofer, models.DO_NOTHING,
                                   db_column='nro_chofer', blank=True,
                                   null=True)
    distancia = models.IntegerField(blank=True, null=True)
    tarifa_km = models.FloatField(blank=True, null=True)
    patente_camion = models.CharField(max_length=255, blank=True, null=True)
    patente_acoplado = models.CharField(max_length=255, blank=True, null=True)
    campana = models.ForeignKey(Campana, models.DO_NOTHING, db_column='campana',
                                blank=True, null=True)
    kilos = models.IntegerField(blank=True, null=True)
    destino = models.ForeignKey(Destino, models.DO_NOTHING, db_column='destino',
                                blank=True, null=True)
    silo = models.ForeignKey('Silos', models.DO_NOTHING, db_column='silo',
                             blank=True, null=True)
    cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING, db_column='cultivo',
                                blank=True, null=True)
    potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
                                db_column='potrero', blank=True, null=True)
    cliente = models.ForeignKey(Cli, models.DO_NOTHING, db_column='cliente',
                                blank=True, null=True)

    class Meta:
        db_table = 'mov_trans'


class Movgan(models.Model):
    id_movgan = models.AutoField(primary_key=True)
    nro_novedad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    motivo = models.ForeignKey(Motivos, models.DO_NOTHING, db_column='motivo',
                               blank=True, null=True)
    motivo_traslado = models.CharField(max_length=255, blank=True, null=True)
    derodeo = models.IntegerField(blank=True, null=True)
    arodeo = models.IntegerField(blank=True, null=True)
    rodeo = models.ForeignKey(Rodeo, models.DO_NOTHING, db_column='rodeo',
                              blank=True, null=True)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING,
                                  db_column='categoria',
                                  blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    kilos = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    entrada_salida = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    comprador = models.IntegerField(blank=True, null=True)
    grupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='grupo',
                              blank=True, null=True)

    class Meta:
        db_table = 'movgan'


class Movimpu(models.Model):
    id_movimpu = models.AutoField(primary_key=True)
    cod_imput = models.ForeignKey(Imputaci, models.DO_NOTHING,
                                  db_column='cod_imput', blank=True, null=True,
                                  verbose_name='Cod. Imput.')
    tipo_movim = models.CharField(max_length=255, blank=True, null=True,
                                  verbose_name='Tipo Movimiento')
    fecha_comprob = models.DateField(blank=True, null=True,
                                     verbose_name='Fecha Comprob.')
    periodo_contable = models.DateField(blank=True, null=True,
                                        verbose_name='Periodo Contable')
    num_comprob = models.IntegerField(blank=True, null=True,
                                      verbose_name='Nro. Comprob.')
    descripcion = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Descripción')
    importe = models.FloatField(blank=True, null=True,
                                verbose_name='Importe')
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
                                  db_column='actividad',
                                  blank=True, null=True,
                                  verbose_name='Actividad')
    tipo_proveedor = models.ForeignKey(Tipoprov, models.DO_NOTHING,
                                       db_column='tipo_proveedor', blank=True,
                                       null=True,
                                       verbose_name='Tipo Proveedor')
    cod_provincia = models.ForeignKey(Provincias, models.DO_NOTHING,
                                      db_column='cod_provincia', blank=True,
                                      null=True,
                                      verbose_name='Provincia')
    nro_ordenpago = models.ForeignKey(OrdPago, models.DO_NOTHING,
                                      db_column='nro_ordenpago', blank=True,
                                      null=True,
                                      verbose_name='Nro. Orden de Pago')
    memo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'movimpu'


class Nimpvta(models.Model):
    id_nimpvta = models.AutoField(primary_key=True)
    nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
                                    db_column='nro_cliente', blank=True,
                                    null=True)
    nrocomp = models.IntegerField(blank=True, null=True)
    nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
                                       db_column='nro_imputacion', blank=True,
                                       null=True)
    importe = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'nimpvta'


# class NovAgro(models.Model):
#     id_nov_agro = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     nro_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
#                                         db_column='nro_contratista', blank=True,
#                                         null=True)
#     nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                     db_column='nro_potrero', blank=True,
#                                     null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
#                                        db_column='codigo_laboreo', blank=True,
#                                        null=True)
#     actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                   db_column='actividad', blank=True, null=True)
#     cantidad_hectareas = models.FloatField(blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     km = models.IntegerField(blank=True, null=True)
#     codigo_formula = models.ForeignKey(Formula, models.DO_NOTHING,
#                                        db_column='codigo_formula', blank=True,
#                                        null=True)
#     hora = models.TimeField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#     unidad_medida = models.CharField(max_length=255, blank=True, null=True)
#     nro_deposito = models.ForeignKey(DepositoStock, models.DO_NOTHING,
#                                      db_column='nro_deposito', blank=True,
#                                      null=True)
#
#     class Meta:
#         db_table = 'nov_agro'
#
#
# class NovCamp(models.Model):
#     id_nov_camp = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     campana = models.ForeignKey(Campana, models.DO_NOTHING, db_column='campana',
#                                 blank=True, null=True)
#     potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                 db_column='potrero', blank=True, null=True)
#     hectareas = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_camp'
#
#
# class NovCons(models.Model):
#     id_nov_cons = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     ing_egr = models.IntegerField(blank=True, null=True)
#     nro_comprob = models.IntegerField(blank=True, null=True)
#     nro_tractor = models.ForeignKey('Tractor', models.DO_NOTHING,
#                                     db_column='nro_tractor', blank=True,
#                                     null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     nro_rodado = models.ForeignKey('Rodados', models.DO_NOTHING,
#                                    db_column='nro_rodado', blank=True,
#                                    null=True)
#     nro_camion = models.ForeignKey(Camion, models.DO_NOTHING,
#                                    db_column='nro_camion', blank=True,
#                                    null=True)
#     responsable = models.ForeignKey('Respons', models.DO_NOTHING,
#                                     db_column='responsable', blank=True,
#                                     null=True)
#     tanque = models.ForeignKey('Tanque', models.DO_NOTHING, db_column='tanque',
#                                blank=True, null=True)
#     litros = models.FloatField(blank=True, null=True)
#     centro_costo = models.IntegerField(blank=True, null=True)
#     proveedor = models.IntegerField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_cons'
#
#
# class NovCose(models.Model):
#     id_nov_cose = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
#                                         db_column='nro_contratista', blank=True,
#                                         null=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                     db_column='nro_potrero', blank=True,
#                                     null=True)
#     hectareas = models.FloatField(blank=True, null=True)
#     codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
#                                        db_column='codigo_laboreo', blank=True,
#                                        null=True)
#     variedad_semilla = models.IntegerField(blank=True, null=True)
#     codigo_destino = models.ForeignKey(Destino, models.DO_NOTHING,
#                                        db_column='codigo_destino', blank=True,
#                                        null=True)
#     codigo_silo_saliente = models.ForeignKey('Silos', models.DO_NOTHING,
#                                              db_column='codigo_silo_saliente',
#                                              blank=True, null=True,
#                                              related_name='novcose_silo_saliente')
#     codigo_silo = models.ForeignKey('Silos', models.DO_NOTHING,
#                                     db_column='codigo_silo', blank=True,
#                                     null=True,
#                                     related_name='novcose_codigo_silo')
#     valor = models.FloatField(blank=True, null=True)
#     carta_porte = models.CharField(max_length=255, blank=True, null=True)
#     kilos_totales = models.IntegerField(blank=True, null=True)
#     humedad = models.FloatField(blank=True, null=True)
#     cuerpo_extrano = models.FloatField(blank=True, null=True)
#     merma_volatil = models.FloatField(blank=True, null=True)
#     transporte = models.ForeignKey('Transp', models.DO_NOTHING,
#                                    db_column='transporte', blank=True,
#                                    null=True)
#     chofer = models.ForeignKey(Chofer, models.DO_NOTHING, db_column='chofer',
#                                blank=True, null=True)
#     patente_camion = models.CharField(max_length=255, blank=True, null=True)
#     patente_acoplado = models.CharField(max_length=255, blank=True, null=True)
#     distancia = models.IntegerField(blank=True, null=True)
#     tarifa_km = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_cose'
#
#
# class NovFert(models.Model):
#     id_nov_fert = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     nro_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
#                                         db_column='nro_contratista', blank=True,
#                                         null=True)
#     nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                     db_column='nro_potrero', blank=True,
#                                     null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
#                                        db_column='codigo_laboreo', blank=True,
#                                        null=True)
#     actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                   db_column='actividad', blank=True, null=True)
#     cantidad_hectareas = models.FloatField(blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     km = models.IntegerField(blank=True, null=True)
#     codigo_formula = models.ForeignKey(Formula, models.DO_NOTHING,
#                                        db_column='codigo_formula', blank=True,
#                                        null=True)
#     hora = models.TimeField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#     unidad_medida = models.CharField(max_length=255, blank=True, null=True)
#     nro_deposito = models.ForeignKey(DepositoStock, models.DO_NOTHING,
#                                      db_column='nro_deposito', blank=True,
#                                      null=True)
#
#     class Meta:
#         db_table = 'nov_fert'
#
#
# class NovFin(models.Model):
#     id_nov_fin = models.AutoField(primary_key=True)
#     cod_movimiento = models.ForeignKey(Movim, models.DO_NOTHING,
#                                        db_column='cod_movimiento', blank=True,
#                                        null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_proveedor = models.IntegerField(blank=True, null=True)
#     nro_deposito = models.ForeignKey(DepositoStock, models.DO_NOTHING,
#                                      db_column='nro_deposito', blank=True,
#                                      null=True)
#     centro_costo = models.IntegerField(blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     total_comprobante = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_fin'
#
#
# class NovGanado(models.Model):
#     nro_novedad = models.IntegerField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     motivo = models.IntegerField(blank=True, null=True)
#     rodeo = models.ForeignKey('Rodeo', models.DO_NOTHING, db_column='rodeo',
#                               blank=True, null=True)
#     categoria = models.IntegerField(blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     kilos = models.IntegerField(blank=True, null=True)
#     a_rodeo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_ganado'
#
#
# class NovGran(models.Model):
#     id_nov_gran = models.AutoField(primary_key=True)
#     codigo = models.IntegerField(blank=True, null=True)
#     tipo_movim = models.CharField(max_length=255, blank=True, null=True)
#     fecha_comprobante = models.DateField(blank=True, null=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencim = models.CharField(max_length=255, blank=True, null=True)
#     imp_exento = models.FloatField(blank=True, null=True)
#     imp_gastos_grav = models.FloatField(blank=True, null=True)
#     imp_neto_grav = models.FloatField(blank=True, null=True)
#     imp_iva = models.FloatField(blank=True, null=True)
#     imp_iva_percep = models.FloatField(blank=True, null=True)
#     imp_imp_vs = models.FloatField(blank=True, null=True)
#     retenc_iva = models.FloatField(blank=True, null=True)
#     perc_ing_brutos = models.FloatField(blank=True, null=True)
#     retencion_ganancias = models.FloatField(blank=True, null=True)
#     imp_total = models.FloatField(blank=True, null=True)
#     fecha_prob_pago = models.CharField(max_length=255, blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_factura = models.IntegerField(blank=True, null=True)
#     codi = models.IntegerField(blank=True, null=True)
#     resta_impu = models.FloatField(blank=True, null=True)
#     lista_imputaciones = models.CharField(max_length=255, blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     silo = models.ForeignKey('Silos', models.DO_NOTHING, db_column='silo',
#                              blank=True, null=True)
#     campana = models.ForeignKey(Campana, models.DO_NOTHING, db_column='campana',
#                                 blank=True, null=True)
#     kilos = models.IntegerField(blank=True, null=True)
#     precio_referencia = models.FloatField(blank=True, null=True)
#     precio_flete = models.FloatField(blank=True, null=True)
#     precio_operacion = models.FloatField(blank=True, null=True)
#     factor = models.FloatField(blank=True, null=True)
#     grado = models.ForeignKey(Grado, models.DO_NOTHING, db_column='grado',
#                               blank=True, null=True)
#     porcentaje_grado = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_gran'
#
#
# class NovHora(models.Model):
#     id_nov_hora = models.AutoField(primary_key=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     fecha = models.DateField(blank=True, null=True)
#     entrada_manana = models.IntegerField(blank=True, null=True)
#     salida_manana = models.IntegerField(blank=True, null=True)
#     entrada_tarde = models.IntegerField(blank=True, null=True)
#     salida_tarde = models.IntegerField(blank=True, null=True)
#     horas_trabajadas = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_hora'
#
#
# class NovLluv(models.Model):
#     id_nov_lluv = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_lluv'
#
#
# class NovMaqu(models.Model):
#     id_nov_maqu = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     nro_tractor = models.ForeignKey('Tractor', models.DO_NOTHING,
#                                     db_column='nro_tractor', blank=True,
#                                     null=True)
#     nro_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
#                                         db_column='nro_contratista', blank=True,
#                                         null=True)
#     horas_tractor = models.IntegerField(blank=True, null=True)
#     litros_gasoil = models.IntegerField(blank=True, null=True)
#     litros_aceite = models.FloatField(blank=True, null=True)
#     potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                 db_column='potrero', blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
#                                        db_column='codigo_laboreo', blank=True,
#                                        null=True)
#     actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                   db_column='actividad', blank=True, null=True)
#     codigo_semilla = models.IntegerField(blank=True, null=True)
#     codigo_fertilizante = models.ForeignKey(Fertiliz, models.DO_NOTHING,
#                                             db_column='codigo_fertilizante',
#                                             blank=True, null=True)
#     hectareas = models.FloatField(blank=True, null=True)
#     horas = models.TimeField(blank=True, null=True)
#     dias = models.FloatField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#     unidad_medida = models.CharField(max_length=255, blank=True, null=True)
#     depsemilla = models.IntegerField(blank=True, null=True)
#     depfertilizante = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_maqu'
#
#
# class NovPlan(models.Model):
#     id_nov_plan = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING, db_column='laboreo',
#                                 blank=True, null=True)
#     potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                 db_column='potrero', blank=True, null=True)
#     cantidad = models.FloatField(blank=True, null=True)
#     unidad_medida = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_plan'
#
#
# class NovProd(models.Model):
#     id_nov_prod = models.AutoField(primary_key=True)
#     nro_tambo = models.ForeignKey('Tambos', models.DO_NOTHING,
#                                   db_column='nro_tambo', blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     ing_egr = models.IntegerField(blank=True, null=True)
#     m_t = models.CharField(max_length=255, blank=True, null=True)
#     nro_comprob = models.IntegerField(blank=True, null=True)
#     litros = models.FloatField(blank=True, null=True)
#     destino = models.ForeignKey(Destino, models.DO_NOTHING, db_column='destino',
#                                 blank=True, null=True)
#     vacas_ordene = models.IntegerField(blank=True, null=True)
#     porc_grasa = models.FloatField(blank=True, null=True)
#     porc_proteina = models.FloatField(blank=True, null=True)
#     cel_somatica = models.IntegerField(blank=True, null=True)
#     rec_bact = models.IntegerField(blank=True, null=True)
#     crioscopia = models.FloatField(blank=True, null=True)
#     temperatura = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_prod'
#
#
# class NovRoll(models.Model):
#     id_nov_roll = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
#                                         db_column='nro_contratista', blank=True,
#                                         null=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     nro_tractor = models.ForeignKey('Tractor', models.DO_NOTHING,
#                                     db_column='nro_tractor', blank=True,
#                                     null=True)
#     horas_tractor = models.IntegerField(blank=True, null=True)
#     litros_gasoil = models.IntegerField(blank=True, null=True)
#     litros_aceite = models.FloatField(blank=True, null=True)
#     nro_potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                     db_column='nro_potrero', blank=True,
#                                     null=True)
#     nro_campo = models.ForeignKey(Campos, models.DO_NOTHING,
#                                   db_column='nro_campo', blank=True, null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
#                                        db_column='codigo_laboreo', blank=True,
#                                        null=True)
#     centro_costo = models.IntegerField(blank=True, null=True)
#     cantidad_hectareas = models.FloatField(blank=True, null=True)
#     cantidad_rollos = models.IntegerField(blank=True, null=True)
#     cultivo_enrrolado = models.IntegerField(blank=True, null=True)
#     hora = models.IntegerField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#     nro_producto = models.ForeignKey('Producto', models.DO_NOTHING,
#                                      db_column='nro_producto', blank=True,
#                                      null=True)
#
#     class Meta:
#         db_table = 'nov_roll'
#
#
# class NovServ(models.Model):
#     id_nov_serv = models.AutoField(primary_key=True)
#     codigo = models.IntegerField(blank=True, null=True)
#     tipo_movim = models.CharField(max_length=255, blank=True, null=True)
#     fecha_comprobante = models.DateField(blank=True, null=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencim = models.CharField(max_length=255, blank=True, null=True)
#     imp_exento = models.FloatField(blank=True, null=True)
#     imp_neto_grav = models.FloatField(blank=True, null=True)
#     imp_iva = models.FloatField(blank=True, null=True)
#     imp_iva_percep = models.FloatField(blank=True, null=True)
#     imp_imp_vs = models.FloatField(blank=True, null=True)
#     retenc_gananc = models.FloatField(blank=True, null=True)
#     perc_ing_brutos = models.FloatField(blank=True, null=True)
#     imp_total = models.FloatField(blank=True, null=True)
#     fecha_prob_pago = models.CharField(max_length=255, blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_factura = models.IntegerField(blank=True, null=True)
#     codi = models.IntegerField(blank=True, null=True)
#     resta_impu = models.FloatField(blank=True, null=True)
#     lista_imputaciones = models.CharField(max_length=255, blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='maquina',
#                                 blank=True, null=True)
#     hectareas = models.FloatField(blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     kilos = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_serv'
#
#
# class NovSiem(models.Model):
#     id_nov_siem = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     nro_tractorista = models.ForeignKey('Tractori', models.DO_NOTHING,
#                                         db_column='nro_tractorista', blank=True,
#                                         null=True)
#     nro_tractor = models.ForeignKey('Tractor', models.DO_NOTHING,
#                                     db_column='nro_tractor', blank=True,
#                                     null=True)
#     nro_contratista = models.ForeignKey(Contrat, models.DO_NOTHING,
#                                         db_column='nro_contratista', blank=True,
#                                         null=True)
#     potrero = models.ForeignKey('Potreros', models.DO_NOTHING,
#                                 db_column='potrero', blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     codigo_laboreo = models.ForeignKey(Laboreo, models.DO_NOTHING,
#                                        db_column='codigo_laboreo', blank=True,
#                                        null=True)
#     actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                   db_column='actividad', blank=True, null=True)
#     hectareas = models.FloatField(blank=True, null=True)
#     horas = models.TimeField(blank=True, null=True)
#     dias = models.FloatField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#     unidad_medida = models.CharField(max_length=255, blank=True, null=True)
#     codigo_semilla = models.IntegerField(blank=True, null=True)
#     depsemilla = models.IntegerField(blank=True, null=True)
#     codigo_fertilizante = models.ForeignKey(Fertiliz, models.DO_NOTHING,
#                                             db_column='codigo_fertilizante',
#                                             blank=True, null=True)
#     depfertilizante = models.IntegerField(blank=True, null=True)
#     codigo_formula = models.ForeignKey(Formula, models.DO_NOTHING,
#                                        db_column='codigo_formula', blank=True,
#                                        null=True)
#     depformula = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_siem'
#
#
# class NovSuel(models.Model):
#     id_nov_suel = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     porcentaje = models.IntegerField(blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     nro_proveedor = models.IntegerField(blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_suel'
#
#
# class NovSuple(models.Model):
#     id_nov_suple = models.AutoField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                   db_column='actividad', blank=True, null=True)
#     nro_silo = models.ForeignKey('Silos', models.DO_NOTHING,
#                                  db_column='nro_silo', blank=True, null=True)
#     kilos = models.FloatField(blank=True, null=True)
#     precio = models.FloatField(blank=True, null=True)
#     nro_impu_ingreso = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                          db_column='nro_impu_ingreso',
#                                          blank=True, null=True,
#                                          related_name='novsuple_nro_impu_ingreso')
#     nro_impu_egreso = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                         db_column='nro_impu_egreso', blank=True,
#                                         null=True,
#                                         related_name='novsuple_nro_impu_egreso')
#     nro_producto = models.ForeignKey('Producto', models.DO_NOTHING,
#                                      db_column='nro_producto', blank=True,
#                                      null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_suple'
#
#
# class NovTransp(models.Model):
#     id_nov_transp = models.AutoField(primary_key=True)
#     codigo = models.IntegerField(blank=True, null=True)
#     tipo_movim = models.CharField(max_length=255, blank=True, null=True)
#     fecha_comprobante = models.DateField(blank=True, null=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencim = models.CharField(max_length=255, blank=True, null=True)
#     imp_exento = models.FloatField(blank=True, null=True)
#     imp_neto_grav = models.FloatField(blank=True, null=True)
#     imp_iva = models.FloatField(blank=True, null=True)
#     imp_iva_percep = models.FloatField(blank=True, null=True)
#     imp_imp_vs = models.FloatField(blank=True, null=True)
#     retenc_gananc = models.FloatField(blank=True, null=True)
#     perc_ing_brutos = models.FloatField(blank=True, null=True)
#     imp_total = models.FloatField(blank=True, null=True)
#     fecha_prob_pago = models.CharField(max_length=255, blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_factura = models.IntegerField(blank=True, null=True)
#     codi = models.IntegerField(blank=True, null=True)
#     resta_impu = models.FloatField(blank=True, null=True)
#     lista_imputaciones = models.CharField(max_length=255, blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     transporte = models.ForeignKey('Transp', models.DO_NOTHING,
#                                    db_column='transporte', blank=True,
#                                    null=True)
#     tarifa = models.IntegerField(blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     kilos = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'nov_transp'
#
#
# class Novcherec(models.Model):
#     id_novcherec = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     fecha_ingreso = models.DateField(blank=True, null=True)
#     fecha_cheque = models.DateField(blank=True, null=True)
#     nro_cheque = models.IntegerField(blank=True, null=True)
#     nro_banco = models.ForeignKey(Banc, models.DO_NOTHING,
#                                   db_column='nro_banco', blank=True, null=True)
#     nombre_banco = models.CharField(max_length=255, blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     diroter = models.CharField(max_length=255, blank=True, null=True)
#     cartera = models.IntegerField(blank=True, null=True)
#     motivosalida = models.CharField(max_length=255, blank=True, null=True)
#     descmot = models.CharField(max_length=255, blank=True, null=True)
#     nro_recibo = models.ForeignKey('Recibos', models.DO_NOTHING,
#                                    db_column='nro_recibo', blank=True,
#                                    null=True)
#     localidad = models.ForeignKey(Localidad, models.DO_NOTHING,
#                                   db_column='localidad', blank=True, null=True)
#     nro_cuit = models.CharField(max_length=255, blank=True, null=True)
#     cta_titular = models.CharField(max_length=255, blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     clering = models.ForeignKey(Clering, models.DO_NOTHING, db_column='clering',
#                                 blank=True, null=True)
#
#     class Meta:
#         db_table = 'novcherec'
#
#
# class Novchpro(models.Model):
#     id_novchpro = models.AutoField(primary_key=True)
#     fecha_cheque = models.DateField(blank=True, null=True)
#     nro_cheque = models.IntegerField(blank=True, null=True)
#     nro_banco = models.ForeignKey(Bancos, models.DO_NOTHING,
#                                   db_column='nro_banco', blank=True, null=True)
#     importe = models.FloatField(blank=True, null=True)
#     motivosalida = models.CharField(max_length=255, blank=True, null=True)
#     descmot = models.CharField(max_length=255, blank=True, null=True)
#     nro_orden_pago = models.ForeignKey('OrdPago', models.DO_NOTHING,
#                                        db_column='nro_orden_pago', blank=True,
#                                        null=True)
#
#     class Meta:
#         db_table = 'novchpro'
#
#
# class Novctcte(models.Model):
#     id_novctcte = models.AutoField(primary_key=True)
#     nro_proveedor = models.IntegerField(blank=True, null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novctcte'
#
#
# class Novedad(models.Model):
#     id_novedad = models.AutoField(primary_key=True)
#     codigo = models.IntegerField(blank=True, null=True)
#     tipo_movim = models.CharField(max_length=255, blank=True, null=True)
#     fecha_comprobante = models.DateField(blank=True, null=True)
#     nro_proveedor = models.IntegerField(blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencim = models.CharField(max_length=255, blank=True, null=True)
#     imp_exento = models.FloatField(blank=True, null=True)
#     imp_neto_grav = models.FloatField(blank=True, null=True)
#     imp_neto_grav_10 = models.FloatField(blank=True, null=True)
#     imp_neto_grav_27 = models.FloatField(blank=True, null=True)
#     imp_iva = models.FloatField(blank=True, null=True)
#     imp_ivad10 = models.FloatField(blank=True, null=True)
#     imp_iva27 = models.FloatField(blank=True, null=True)
#     imp_iva_percep = models.FloatField(blank=True, null=True)
#     imp_imp_vs = models.FloatField(blank=True, null=True)
#     retenc_gananc = models.FloatField(blank=True, null=True)
#     perc_ing_brutos = models.FloatField(blank=True, null=True)
#     imp_total = models.FloatField(blank=True, null=True)
#     imp_total_dolares = models.FloatField(blank=True, null=True)
#     fecha_prob_pago = models.CharField(max_length=255, blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_factura = models.CharField(max_length=255, blank=True, null=True)
#     codi = models.IntegerField(blank=True, null=True)
#     resta_impu = models.FloatField(blank=True, null=True)
#     lista_imputaciones = models.CharField(max_length=255, blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novedad'
#
#
# class NovedadGanado(models.Model):
#     nro_novedad = models.IntegerField(primary_key=True)
#     fecha = models.DateField(blank=True, null=True)
#     motivo = models.IntegerField(blank=True, null=True)
#     rodeo = models.ForeignKey('Rodeo', models.DO_NOTHING, db_column='rodeo',
#                               blank=True, null=True)
#     categoria = models.IntegerField(blank=True, null=True)
#     cantidad = models.IntegerField(blank=True, null=True)
#     kilos = models.IntegerField(blank=True, null=True)
#     a_rodeo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novedad_ganado'
#
#
# class Noventas(models.Model):
#     id_noventas = models.AutoField(primary_key=True)
#     codigo = models.IntegerField(blank=True, null=True)
#     tipo_movim = models.CharField(max_length=255, blank=True, null=True)
#     fecha_comprobante = models.DateField(blank=True, null=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencim = models.CharField(max_length=255, blank=True, null=True)
#     imp_exento = models.FloatField(blank=True, null=True)
#     imp_neto_grav = models.FloatField(blank=True, null=True)
#     imp_iva = models.FloatField(blank=True, null=True)
#     imp_iva_percep = models.FloatField(blank=True, null=True)
#     imp_imp_vs = models.FloatField(blank=True, null=True)
#     retenc_gananc = models.FloatField(blank=True, null=True)
#     perc_ing_brutos = models.FloatField(blank=True, null=True)
#     imp_total = models.FloatField(blank=True, null=True)
#     fecha_prob_pago = models.DateField(blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_factura = models.IntegerField(blank=True, null=True)
#     codi = models.IntegerField(blank=True, null=True)
#     resta_impu = models.FloatField(blank=True, null=True)
#     lista_imputaciones = models.CharField(max_length=255, blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     nro_maquina = models.ForeignKey(Maquina, models.DO_NOTHING,
#                                     db_column='nro_maquina', blank=True,
#                                     null=True)
#     hectareas = models.IntegerField(blank=True, null=True)
#     campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
#                               blank=True, null=True)
#     litros_leche = models.IntegerField(blank=True, null=True)
#     kilos_grasa = models.FloatField(blank=True, null=True)
#     kilos_proteinas = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'noventas'
#
#
# class Novimp(models.Model):
#     id_novimp = models.AutoField(primary_key=True)
#     nro_proveedor = models.IntegerField(blank=True, null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novimp'
#
#
# class Novimpgran(models.Model):
#     id_novimpgran = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novimpgran'
#
#
# class Novimpserv(models.Model):
#     id_novimpserv = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novimpserv'
#
#
# class Novimptransp(models.Model):
#     id_novimptransp = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novimptransp'
#
#
# class Novimpu(models.Model):
#     id_novimpu = models.AutoField(primary_key=True)
#     nro_proveedor = models.IntegerField(blank=True, null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novimpu'
#
#
# class Novimpvta(models.Model):
#     id_novimpvta = models.AutoField(primary_key=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     nrocomp = models.IntegerField(blank=True, null=True)
#     nro_imputacion = models.ForeignKey(Imputaci, models.DO_NOTHING,
#                                        db_column='nro_imputacion', blank=True,
#                                        null=True)
#     importe = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novimpvta'
#
#
# class Novpref(models.Model):
#     id_novpref = models.AutoField(primary_key=True)
#     tipo = models.CharField(max_length=255, blank=True, null=True)
#     nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                     db_column='nro_cliente', blank=True,
#                                     null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     nro_prefactura = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'novpref'

#
# class Observop(models.Model):
#     id_observop = models.AutoField(primary_key=True)
#     nro_orden_pago = models.ForeignKey('OrdPago', models.DO_NOTHING,
#                                        db_column='nro_orden_pago', blank=True,
#                                        null=True)
#
#     class Meta:
#         db_table = 'observop'


class Pagados(models.Model):
    id_pagados = models.AutoField(primary_key=True)
    cod_prove = models.ForeignKey('Proctcte', models.DO_NOTHING,
                                  db_column='cod_prove', blank=True, null=True)
    tipo_movim = models.CharField(max_length=255, blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    fecha_comprob = models.DateField(blank=True, null=True)
    fecha_vencim = models.DateField(blank=True, null=True)
    fecha_prob_pago = models.DateField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    imp_neto_grav = models.FloatField(blank=True, null=True)
    pagoacuenta = models.FloatField(blank=True, null=True)
    tipo_prove = models.ForeignKey('Tipoprov', models.DO_NOTHING,
                                   db_column='tipo_prove', blank=True,
                                   null=True)
    cant_cuotas = models.IntegerField(blank=True, null=True)
    nro_cuotas = models.IntegerField(blank=True, null=True)
    tipo_fact = models.IntegerField(blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    codi = models.IntegerField(blank=True, null=True)
    pagar_parte = models.FloatField(blank=True, null=True)
    nro_orden_pago = models.ForeignKey(OrdPago, models.DO_NOTHING,
                                       db_column='nro_orden_pago', blank=True,
                                       null=True)
    importe_retencion = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'pagados'


class Pendcobro(models.Model):
    id_pendcobro = models.AutoField(primary_key=True)
    nro_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
                                    db_column='nro_cliente', blank=True,
                                    null=True)
    corte = models.CharField(max_length=255, blank=True, null=True)
    tipo_movim = models.CharField(max_length=255, blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    fecha_comprob = models.DateField(blank=True, null=True)
    fecha_vencim = models.DateField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    imp_neto_grav = models.FloatField(blank=True, null=True)
    pagoacuenta = models.FloatField(blank=True, null=True)
    tipo_cliente = models.IntegerField(blank=True, null=True)
    cant_cuotas = models.IntegerField(blank=True, null=True)
    nro_cuotas = models.IntegerField(blank=True, null=True)
    tipo_fact = models.CharField(max_length=255, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    codi = models.IntegerField(blank=True, null=True)
    pagar_parte = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'pendcobro'


class Pendpago(models.Model):
    id_pendpago = models.AutoField(primary_key=True)
    cod_prove = models.ForeignKey('Proctcte', models.DO_NOTHING,
                                  db_column='cod_prove', blank=True, null=True)
    corte = models.CharField(max_length=255, blank=True, null=True)
    tipo_movim = models.CharField(max_length=255, blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    fecha_comprob = models.DateField(blank=True, null=True)
    fecha_vencim = models.DateField(blank=True, null=True)
    fecha_prob_pago = models.DateField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    importe_dolares = models.FloatField(blank=True, null=True)
    imp_neto_grav = models.FloatField(blank=True, null=True)
    pagoacuenta = models.FloatField(blank=True, null=True)
    tipo_prove = models.ForeignKey('Tipoprov', models.DO_NOTHING,
                                   db_column='tipo_prove', blank=True,
                                   null=True)
    cant_cuotas = models.IntegerField(blank=True, null=True)
    nro_cuotas = models.IntegerField(blank=True, null=True)
    tipo_fact = models.CharField(max_length=255, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    codi = models.IntegerField(blank=True, null=True)
    pagar_parte = models.FloatField(blank=True, null=True)
    retencion_parcial = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'pendpago'


class Prgastos(models.Model):
    id_prgastos = models.AutoField(primary_key=True)
    nro_orden_pago = models.ForeignKey(OrdPago, models.DO_NOTHING,
                                       db_column='nro_orden_pago', blank=True,
                                       null=True)
    nro_recibo = models.ForeignKey('Recibos', models.DO_NOTHING,
                                   db_column='nro_recibo', blank=True,
                                   null=True)
    nro_retencion = models.ForeignKey('Retencio', models.DO_NOTHING,
                                      db_column='nro_retencion', blank=True,
                                      null=True)
    fecha = models.DateField(blank=True, null=True)
    clienteprov = models.CharField(max_length=255, blank=True, null=True)
    cierrecaja = models.CharField(max_length=255, blank=True, null=True)
    multiplescaja = models.CharField(max_length=255, blank=True, null=True)
    nro_retencion_ib = models.IntegerField(blank=True, null=True)
    nro_retencion_iva = models.IntegerField(blank=True, null=True)
    fecha_cierre_periodo = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'prgastos'


# class ProCar(models.Model):
#     id_pro_car = models.AutoField(primary_key=True)
#     movimiento = models.ForeignKey(Movim, models.DO_NOTHING,
#                                    db_column='movimiento', blank=True,
#                                    null=True)
#     fecha = models.DateField(blank=True, null=True)
#     proveedor = models.IntegerField(blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     nro_producto = models.ForeignKey('Producto', models.DO_NOTHING,
#                                      db_column='nro_producto', blank=True,
#                                      null=True)
#     cantidad = models.FloatField(blank=True, null=True)
#     kilos = models.FloatField(blank=True, null=True)
#     precio = models.FloatField(blank=True, null=True)
#     descuento = models.FloatField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'pro_car'


# class ProCarOc(models.Model):
#     id_pro_car_oc = models.AutoField(primary_key=True)
#     movimiento = models.ForeignKey(Movim, models.DO_NOTHING,
#                                    db_column='movimiento', blank=True,
#                                    null=True)
#     fecha = models.DateField(blank=True, null=True)
#     proveedor = models.IntegerField(blank=True, null=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     nro_producto = models.ForeignKey('Producto', models.DO_NOTHING,
#                                      db_column='nro_producto', blank=True,
#                                      null=True)
#     cantidad = models.FloatField(blank=True, null=True)
#     kilos = models.FloatField(blank=True, null=True)
#     precio = models.FloatField(blank=True, null=True)
#     descuento = models.FloatField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#     fecha_entrega = models.DateField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'pro_car_oc'


# class ProVen(models.Model):
#     movimiento = models.ForeignKey(Movim, models.DO_NOTHING,
#                                    db_column='movimiento')
#     fecha = models.DateField(blank=True, null=True)
#     cliente = models.IntegerField(blank=True, null=True)
#     nro_comprobante = models.IntegerField()
#     nro_producto = models.ForeignKey('Producto', models.DO_NOTHING,
#                                      db_column='nro_producto')
#     cantidad = models.FloatField(blank=True, null=True)
#     kilos = models.FloatField(blank=True, null=True)
#     precio = models.FloatField(blank=True, null=True)
#     descuento = models.FloatField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'pro_ven'
#         unique_together = (('movimiento', 'nro_comprobante', 'nro_producto'),)


class Resopago(models.Model):
    id_resopago = models.AutoField(primary_key=True)
    nro_orden = models.ForeignKey(OrdPago, models.DO_NOTHING,
                                  db_column='nro_orden', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    nro_provedor = models.ForeignKey(Proctcte, models.DO_NOTHING,
                                     db_column='nro_provedor', blank=True,
                                     null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    pago_efectivo = models.FloatField(blank=True, null=True)
    nrocaja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='nrocaja',
                                blank=True, null=True)
    pagochepropios = models.FloatField(blank=True, null=True)
    pagocheterceros = models.FloatField(blank=True, null=True)
    pagointerdeposito = models.FloatField(blank=True, null=True)
    bancointerdeposito = models.IntegerField(blank=True, null=True)
    retencion_ganancias = models.FloatField(blank=True, null=True)
    retencion_iva = models.FloatField(blank=True, null=True)
    retencion_ib = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'resopago'


class RetProv(models.Model):
    id_ret_prov = models.AutoField(primary_key=True)
    cod_prove = models.ForeignKey(Proctcte, models.DO_NOTHING,
                                  db_column='cod_prove', blank=True, null=True)
    tot_importes = models.FloatField(blank=True, null=True)
    acumula_importes_aplicados = models.FloatField(blank=True, null=True)
    acumula_retenciones = models.FloatField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ret_prov'


class Stockdep(models.Model):
    id_stockdep = models.AutoField(primary_key=True)
    nro_producto = models.ForeignKey(Producto, models.DO_NOTHING,
                                     db_column='nro_producto', blank=True,
                                     null=True)
    nro_deposito = models.ForeignKey(DepositoStock, models.DO_NOTHING,
                                     db_column='nro_deposito', blank=True,
                                     null=True)
    stock_unidades = models.FloatField(blank=True, null=True)
    stock_kilos = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'stockdep'


class Stocksil(models.Model):
    id_stocksil = models.AutoField(primary_key=True)
    nro_silo = models.ForeignKey(Silos, models.DO_NOTHING, db_column='nro_silo',
                                 blank=True, null=True)
    campana_actual = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='campana_actual', blank=True,
                                       null=True)
    nro_cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING,
                                    db_column='nro_cultivo', blank=True,
                                    null=True)
    stock = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'stocksil'


class TempC(models.Model):
    id_temp_c = models.AutoField(primary_key=True)
    potreros = models.ForeignKey(Potreros, models.DO_NOTHING,
                                 db_column='potreros', blank=True, null=True)
    campo = models.ForeignKey(Campos, models.DO_NOTHING, db_column='campo',
                              blank=True, null=True)
    sector = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sector',
                               blank=True, null=True)
    sub_sector = models.ForeignKey(Subsecto, models.DO_NOTHING,
                                   db_column='sub_sector', blank=True,
                                   null=True)
    fecha = models.DateField(blank=True, null=True)
    agroq = models.ForeignKey(Agroquim, models.DO_NOTHING, db_column='agroq',
                              blank=True, null=True)
    dosis = models.FloatField(blank=True, null=True)
    hectareas = models.FloatField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    horas = models.IntegerField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    campana_actual = models.ForeignKey(Campana, models.DO_NOTHING,
                                       db_column='campana_actual', blank=True,
                                       null=True)

    class Meta:
        db_table = 'temp_c'


class TempProd(models.Model):
    id_temp_prod = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    tambo = models.ForeignKey(Tambos, models.DO_NOTHING, db_column='tambo',
                              blank=True, null=True)
    m_t = models.CharField(max_length=255, blank=True, null=True)
    vacas = models.IntegerField(blank=True, null=True)
    produccion = models.FloatField(blank=True, null=True)
    fabrica = models.FloatField(blank=True, null=True)
    guachera = models.FloatField(blank=True, null=True)
    consumo = models.FloatField(blank=True, null=True)
    descarte = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'temp_prod'


class TempSto(models.Model):
    id_temp_sto = models.AutoField(primary_key=True)
    nro_producto = models.ForeignKey(Producto, models.DO_NOTHING,
                                     db_column='nro_producto', blank=True,
                                     null=True)
    nro_actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
                                      db_column='nro_actividad', blank=True,
                                      null=True)
    cantidad_ingreso = models.FloatField(blank=True, null=True)
    kilos_ingreso = models.FloatField(blank=True, null=True)
    cantidad_egreso = models.FloatField(blank=True, null=True)
    kilos_egresos = models.FloatField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'temp_sto'


class Terceros(models.Model):
    id_terceros = models.AutoField(primary_key=True)
    nro_usuario = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_cheque = models.DateField(blank=True, null=True)
    nro_cheque = models.IntegerField(blank=True, null=True)
    nro_banco = models.IntegerField(blank=True, null=True)
    nombre_banco = models.CharField(max_length=255, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    diroter = models.CharField(max_length=255, blank=True, null=True)
    cartera = models.IntegerField(blank=True, null=True)
    motivosalida = models.CharField(max_length=255, blank=True, null=True)
    descmot = models.CharField(max_length=255, blank=True, null=True)
    nro_ordenpago = models.ForeignKey(OrdPago, models.DO_NOTHING,
                                      db_column='nro_ordenpago', blank=True,
                                      null=True)
    clering = models.ForeignKey(Clering, models.DO_NOTHING, db_column='clering',
                                blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'terceros'


class Tmpcajas(models.Model):
    id_tmpcajas = models.AutoField(primary_key=True)
    caja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='caja',
                             blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    ingegr = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    descri = models.CharField(max_length=255, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'tmpcajas'


# class Vcarga(models.Model):
#     id_vcarga = models.AutoField(primary_key=True)
#     nro_comprobante = models.IntegerField(blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     periodo_contable = models.DateField(blank=True, null=True)
#     numero_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
#                                        db_column='numero_cliente', blank=True,
#                                        null=True)
#     numero_deposito = models.ForeignKey(DepositoStock, models.DO_NOTHING,
#                                         db_column='numero_deposito', blank=True,
#                                         null=True)
#     numero_actividad = models.ForeignKey(Actividad, models.DO_NOTHING,
#                                          db_column='numero_actividad',
#                                          blank=True, null=True)
#     razon_social = models.CharField(max_length=255, blank=True, null=True)
#     condicion_pago = models.IntegerField(blank=True, null=True)
#     fecha_vencimiento = models.DateField(blank=True, null=True)
#     fecha_probable = models.DateField(blank=True, null=True)
#     tipo_factura = models.CharField(max_length=255, blank=True, null=True)
#     prefijo = models.IntegerField(blank=True, null=True)
#     tipo_movimiento = models.CharField(max_length=255, blank=True, null=True)
#     descuento = models.IntegerField(blank=True, null=True)
#     imp_varios = models.FloatField(blank=True, null=True)
#     iva = models.FloatField(blank=True, null=True)
#     impivadif1 = models.FloatField(blank=True, null=True)
#     impivadif2 = models.FloatField(blank=True, null=True)
#     excento = models.FloatField(blank=True, null=True)
#     netogrdo = models.FloatField(blank=True, null=True)
#     reten_ganancias = models.FloatField(blank=True, null=True)
#     percep_ingbrutos = models.FloatField(blank=True, null=True)
#     percep_iva = models.FloatField(blank=True, null=True)
#     total_factura = models.FloatField(blank=True, null=True)
#     total_facturadolares = models.FloatField(blank=True, null=True)
#     ya_imputado = models.IntegerField(blank=True, null=True)
#     cod_movimiento = models.ForeignKey(Movim, models.DO_NOTHING,
#                                        db_column='cod_movimiento', blank=True,
#                                        null=True)
#     nro_cliente = models.IntegerField(blank=True, null=True)
#     con_o_sin = models.IntegerField(blank=True, null=True)
#     total_cantidad = models.FloatField(blank=True, null=True)
#     total_kilos = models.FloatField(blank=True, null=True)
#     depositodestino = models.IntegerField(blank=True, null=True)
#     tanque = models.ForeignKey(Tanque, models.DO_NOTHING, db_column='tanque',
#                                blank=True, null=True)
#     litros = models.FloatField(blank=True, null=True)
#     costo = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'vcarga'


class VctaCte(models.Model):
    id_vcta_cte = models.AutoField(primary_key=True)
    tipo_movim = models.ForeignKey(TipoMovimiento, models.DO_NOTHING,
                                   db_column='tipo_movim',
                                   blank=True, null=True)
    cod_cliente = models.ForeignKey(Cli, models.DO_NOTHING,
                                    db_column='cod_cliente', blank=True,
                                    null=True)
    fecha_comprob = models.DateField(blank=True, null=True)
    nro_comprob = models.IntegerField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    periodo_contable = models.DateField(blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    tipo_factura = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'vcta_cte'


class VenCar(models.Model):
    id_ven_car = models.AutoField(primary_key=True)
    movimiento = models.ForeignKey(Movim, models.DO_NOTHING,
                                   db_column='movimiento', blank=True,
                                   null=True)
    fecha = models.DateField(blank=True, null=True)
    nro_comprobante = models.IntegerField(blank=True, null=True)
    cliente = models.ForeignKey(Cli, models.DO_NOTHING, db_column='cliente',
                                blank=True, null=True)
    nro_categoria = models.ForeignKey(Categorias, models.DO_NOTHING,
                                      db_column='nro_categoria', blank=True,
                                      null=True)
    nro_rodeo = models.ForeignKey(Rodeo, models.DO_NOTHING,
                                  db_column='nro_rodeo', blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    kilos = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'ven_car'


class Ventas(models.Model):
    id_ventas = models.AutoField(primary_key=True)
    tipo_movim = models.ForeignKey(TipoMovimiento, models.DO_NOTHING,
                                   db_column='tipo_movim',
                                   blank=True, null=True)
    fecha_comprob = models.DateField(blank=True, null=True)
    tipo_comprob = models.CharField(max_length=255, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    nro_compro = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    nro_cuit = models.CharField(max_length=255, blank=True, null=True)
    imp_exento = models.FloatField(blank=True, null=True)
    imp_gravado = models.FloatField(blank=True, null=True)
    importe_iva = models.FloatField(blank=True, null=True)
    importe_iva_difer1 = models.FloatField(blank=True, null=True)
    importe_iva_difer2 = models.FloatField(blank=True, null=True)
    imp_perc_iva = models.FloatField(blank=True, null=True)
    imp_per_ing_brutos = models.FloatField(blank=True, null=True)
    retenc_gananc = models.FloatField(blank=True, null=True)
    retenc_iva = models.FloatField(blank=True, null=True)
    imp_varios = models.FloatField(blank=True, null=True)
    imp_total = models.FloatField(blank=True, null=True)
    importe_total_dolares = models.FloatField(blank=True, null=True)
    cod_provincia = models.ForeignKey(Provincias, models.DO_NOTHING,
                                      db_column='cod_provincia', blank=True,
                                      null=True)
    periodo_contable = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'ventas'
