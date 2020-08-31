dicts = [
    {
        'name': 'acoplado',
        'pk': 'nro_acoplado',
        'fk': [('nro_imputacion', 'imputaci', 'codigo')]
        # 'fk': None
    }, {
        'name': 'acred_pend',
        'pk': 'nro_banco, fecha',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco')]
        'fk': None
    }, {
        'name': 'acredita',
        'pk': 'nro_credito, nro_cuenta',
        'fk': [('imputacion', 'imputaci', 'codigo')]
        # 'fk': None
    }, {
        'name': 'actividad',
        'pk': 'nro_actividad',
        'fk': None
    }, {
        'name': 'acumula',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'agroquim',
        'pk': 'nro_agroquimico',
        'fk': None
    }, {
        'name': 'anexo',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'banc',
        'pk': 'id_banc',
        'fk': None
    }, {
        'name': 'bancos',
        'pk': 'nro_banco',
        'fk': None
    }, {
        'name': 'bolsas',
        'pk': 'id_bolsas',
        # 'fk': [('nro_cultivo', 'cultivo', 'nro_cultivo')]
        'fk': None
    }, {
        'name': 'cajas',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'camion',
        'pk': 'nro_camion',
        'fk': [('nro_imputacion', 'imputaci', 'codigo')]
        # 'fk': None
    }, {
        'name': 'campana',
        'pk': 'nro_campana',
        # 'fk': [('cultivo', 'cultivo', 'nro_cultivo'),
        #        ('actividad', 'actividad', 'nro_actividad')]
        'fk': None
    }, {
        'name': 'campos',
        'pk': 'nro_campo',
        # 'fk': [('sub_sector', 'subsecto', 'nro_sub_sector'),
        'fk': [('imputacion', 'imputaci', 'codigo')]
        # 'fk': None
    }, {
        'name': 'carga',
        'pk': 'id_carga',
        # 'fk': [('numero_deposito', 'deposito_stock', 'nro_deposito'),
        #        ('numero_actividad', 'actividad', 'nro_actividad'),
        #        ('nro_cliente', 'cli', 'codigo'),
        #        ('campana', 'campana', 'nro_campana'),
        #        ('depositodestino', 'deposito_stock', 'nro_deposito'),
        #        ('tanque', 'tanque', 'nro_tanque'),
        #        ('cod_movimiento', 'movim', 'nro_movimiento')]
        # ('numero_proveedor'),
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'cargaoc',
        'pk': 'id_cargaoc',
        # 'fk': [('cod_movimiento', 'movim', 'nro_movimiento')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        # ('numero_proveedor'),
        'fk': None
    }, {
        'name': 'categorias',
        'pk': 'nro_categoria',
        'fk': None
    }, {
        'name': 'ccarga',
        'pk': 'id_ccarga',
        # 'fk': [('numero_actividad', 'actividad', 'nro_actividad'),
        #        ('nro_cliente', 'cli', 'codigo'),
        #        ('depositodestino', 'deposito_stock', 'nro_deposito'),
        #        ('cod_movimiento', 'movim', 'nro_movimiento')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        # ('numero_proveedor'),
        'fk': None
    }, {
        'name': 'cheqant',
        'pk': 'nro_cheque',
        # 'fk': [('nrocliente', 'cli', 'codigo'),
        #        ('nro_cheque', 'cheques', 'nro_cheque'),
        #        ('clearing', 'clering', 'codigo'),
        #        ('localidad', 'localidad', 'codigo'),
        #        ('nrorecibo', 'recibos', 'nro_recibo')]
        'fk': None
    }, {
        'name': 'cheqpag',
        'pk': 'fecha_cheque, nro_cheque, nro_banco',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco'),
        #        ('nro_ordenpago', 'ord_pago', 'codigo')]
        # ('nro_cheque', 'cheques', 'nro_cheque'),
        'fk': None
    }, {
        'name': 'cheqprop',
        'pk': 'id_cheqprop',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco'),
        #        ('nro_ordenpago', 'ord_pago', 'codigo'),
        #        ('caja', 'cajas', 'numero')]
        # ('nro_cheque', 'cheques', 'nro_cheque'),
        # ('nroproveedor'),
        'fk': None
    }, {
        'name': 'cheqrec',
        'pk': 'id_cheqrec',
        # 'fk': [('nro_cliente', 'cli', 'codigo'),
        #        ('nro_banco', 'banc', 'id_banc'),
        #        ('nro_recibo', 'recibos', 'nro_recibo')]
        'fk': None
    }, {
        'name': 'cheques',
        'pk': 'nro_cheque',
        # 'fk': [('nrocliente', 'cli', 'codigo'),
        #        ('localidad', 'localidad', 'codigo'),
        #        ('nrorecibo', 'recibos', 'nro_recibo')]
        # ('banco_proveedor', 'bancos', 'nro_banco'),
        'fk': None
    }, {
        'name': 'chofer',
        'pk': 'nro_chofer',
        'fk': None
    }, {
        'name': 'clering',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'cli',
        'pk': 'codigo',
        # 'fk': [('localidad', 'localidad', 'codigo')]
        # ('cod_comprobante', 'cod_comprob', 'codigo')
        'fk': None
    }, {
        'name': 'cobrados',
        'pk': 'id_cobrados',
        # 'fk': [('nro_cliente', 'cli', 'codigo'),
        #        ('nro_recibo', 'recibos', 'nro_recibo')]
        # ('nro_comprob', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'cod_comprob',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'conpago',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'consocia',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'contrat',
        'pk': 'nro_contratista',
        'fk': None
    }, {
        'name': 'creditos',
        'pk': 'id_creditos',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco')]
        'fk': None
    }, {
        'name': 'cta_cte',
        'pk': 'id_cta_cte',
        # 'fk': [('cod_proveedor', 'proctcte', 'codigo'),
        #        ('tipo_movim', 'tipo_movimiento', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo')]
        'fk': None
    }, {
        'name': 'ctepro',
        'pk': 'id_ctepro',
        # 'fk': [('codcli', 'cli', 'codigo'),
        #        ('codpro', 'proctcte', 'codigo')]
        'fk': None
    }, {
        'name': 'cteprocc',
        'pk': 'id_cteprocc',
        # 'fk': [('codcliente', 'cli', 'codigo'),
        #        ('codproveedor', 'proctcte', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'cultivo',
        'pk': 'nro_cultivo',
        'fk': None
    }, {
        'name': 'cventa',
        'pk': 'id_cventa',
        # 'fk': [('numero_cliente', 'cli', 'codigo'),
        #        ('numero_deposito', 'deposito_stock', 'nro_deposito'),
        #        ('numero_actividad', 'actividad', 'nro_actividad'),
        #        ('cod_movimiento', 'movim', 'nro_movimiento'),
        #        ('tanque', 'tanque', 'nro_tanque')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'debitos',
        'pk': 'nro_debito',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco')]
        'fk': None
    }, {
        'name': 'deposito',
        'pk': 'id_deposito',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco'),
        #        ('caja', 'cajas', 'numero')]
        'fk': None
    }, {
        'name': 'deposito_stock',
        'pk': 'nro_deposito',
        'fk': None
    }, {
        'name': 'destino',
        'pk': 'codigo',
        # 'fk': [('localidad', 'localidad', 'codigo')]
        'fk': None
    }, {
        'name': 'distancia',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'fertiliz',
        'pk': 'nro_fertilizante',
        'fk': None
    }, {
        'name': 'for_fer',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'formula',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'gan_car',
        'pk': 'id_gan_car',
        # 'fk': [('movimiento', 'movim', 'nro_movimiento'),
        #        ('nro_rodeo', 'rodeo', 'nro_rodeo')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        # ('proveedor'),
        'fk': None
    }, {
        'name': 'gf',
        'pk': 'id_gf',
        # 'fk': [('nrocaja', 'cajas', 'numero')]
        # ('n_comp', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'gg',
        'pk': 'id_gg',
        # 'fk': [('nrocaja', 'cajas', 'numero')]
        # ('n_comp', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'giros',
        'pk': 'id_giros',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco'),
        #        ('nro_caja', 'cajas', 'numero')]
        # ('nro_provee'),
        # ('n_comp', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'glibroba',
        'pk': 'banco, nrocheque',
        # 'fk': [('banco', 'bancos', 'nro_banco'),
        #        ('nrocheque', 'cheques', 'nro_cheque')]
        'fk': None
    }, {
        'name': 'grado',
        'pk': 'grado',
        'fk': None
    }, {
        'name': 'grecibo',
        'pk': 'nro_orden, fecha',
        # 'fk': [('nro_cliente', 'cli', 'codigo'),
        #        ('nrocaja', 'cajas', 'numero')]
        'fk': None
    }, {
        'name': 'grupos',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'guareten',
        'pk': 'fecha, nro_retencion',
        # 'fk': [('nro_retencion', 'retencio', 'nro_retencion'),
        #        ('nro_orden_pago', 'ord_pago', 'codigo')]
        'fk': None
    }, {
        'name': 'guaretenib',
        'pk': 'fecha, nro_retencion',
        # 'fk': [('nro_retencion', 'retencio', 'nro_retencion'),
        #        ('nro_orden_pago', 'ord_pago', 'codigo'),
        #        ('provincia', 'provincias', 'nro_provincia')]
        'fk': [('provincia', 'provincias', 'nro_provincia')]
    },
    {
        'name': 'guareteniva',
        'pk': 'fecha, nro_retencion',
        # 'fk': [('nro_retencion', 'retencio', 'nro_retencion'),
        #        ('nro_orden_pago', 'ord_pago', 'codigo')]
        'fk': None
    }, {
        'name': 'humedad',
        'pk': 'id_humedad',
        # 'fk': [('cultivo', 'cultivo', 'nro_cultivo')]
        'fk': None
    }, {
        'name': 'impuesto',
        'pk': 'numero',
        'fk': None
    }, {
        'name': 'imputaci',
        'pk': 'codigo',
        'fk': [('donde_acumula', 'acumula', 'codigo')]
        # 'fk': None
    }, {
        'name': 'indices',
        'pk': 'nro',
        'fk': None
    }, {
        'name': 'interdep',
        'pk': 'nro_interdep',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco'),
        #        ('nro_ord_pago', 'ord_pago', 'codigo')]
        'fk': None
    }, {
        'name': 'items',
        'pk': 'id_items',
        # 'fk': [('nro_deposito', 'deposito_stock', 'nro_deposito'),
        #        ('nro_rubro', 'rubros', 'nro_rubro'),
        #        ('nro_producto', 'producto', 'nro_producto'),
        #        ('potrero', 'potreros', 'nro_potrero'),
        #        ('campana', 'campana', 'nro_campana')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        # ('nro_proveedor'),
        'fk': None
    }, {
        'name': 'laboreo',
        'pk': 'nro_laboreo',
        'fk': None
    }, {
        'name': 'libroba',
        'pk': 'id_libroba',
        # 'fk': [('banco', 'bancos', 'nro_banco'),
        #        ('nrocheque', 'cheques', 'nro_cheque')]
        'fk': None
    }, {
        'name': 'lineas',
        'pk': 'num_linea',
        'fk': None
    }, {
        'name': 'localidad',
        'pk': 'codigo',
        'fk': [('provincia', 'provincias', 'nro_provincia')]
        # 'fk': None
    }, {
        'name': 'maeche',
        'pk': 'id_maeche',
        # 'fk': [('nrocliente', 'cli', 'codigo')]
        'fk': None
    }, {
        'name': 'maecli',
        'pk': 'id_maecli',
        # 'fk': [('nro_cliente', 'cli', 'codigo')]
        'fk': None
    }, {
        'name': 'maquina',
        'pk': 'nro_maquina',
        # 'fk': [('campo_asignada', 'campos', 'nro_campo'),
        #        ('nro_laboreo', 'laboreo', 'nro_laboreo'),
        'fk': [('nro_imputacion', 'imputaci', 'codigo')]
        # 'fk': None
    }, {
        'name': 'mensual',
        'pk': 'id_mensual',
        'fk': [('cod_provincia', 'provincias', 'nro_provincia'),]
        #        ('tipo_movim', 'tipo_movimiento', 'codigo'),
        #        ('cod_proveedor', 'proctcte', 'codigo')]
        # ('nro_compro', 'cod_comprob', 'codigo'),
        # 'fk': None
    }, {
        'name': 'montos_para_girar',
        'pk': 'id_montos_para_girar',
        # 'fk': [('nro_banco', 'bancos', 'nro_banco')]
        'fk': None
    }, {
        'name': 'mot_deb',
        'pk': 'nro_motivo',
        'fk': None
    }, {
        'name': 'motipago',
        'pk': 'motivo',
        'fk': None
    }, {
        'name': 'motivo',
        'pk': 'motivo',
        'fk': None
    }, {
        'name': 'motivos',
        'pk': 'nro_motivo',
        'fk': None
    }, {
        'name': 'mov_camp',
        'pk': 'id_mov_camp',
        # 'fk': [('campo', 'campos', 'nro_campo'),
        #        ('sector', 'sector', 'nro_sector'),
        #        ('sub_sector', 'subsecto', 'nro_sub_sector'),
        #        ('laboreo', 'laboreo', 'nro_laboreo'),
        #        ('campana_actual', 'campana', 'nro_campana')]
        'fk': None
    }, {
        'name': 'mov_cons',
        'pk': 'id_mov_cons',
        # 'fk': [('nro_tractor', 'tractor', 'nro_tractor'),
        #        ('nro_maquina', 'maquina', 'nro_maquina'),
        #        ('nro_rodado', 'rodados', 'nro_rodado'),
        #        ('responsable', 'respons', 'nro_responsable'),
        #        ('nro_camion', 'camion', 'nro_camion'),
        #        ('tanque', 'tanque', 'nro_tanque')]
        # ('nro_comprob', 'cod_comprob', 'codigo'),
        # ('proveedor'),
        'fk': None
    }, {
        'name': 'mov_cose',
        'pk': 'id_mov_cose',
        # 'fk': [('sector', 'sector', 'nro_sector'),
        #        ('sub_sector', 'subsecto', 'nro_sub_sector'),
        #        ('campo', 'campos', 'nro_campo'),
        #        ('potrero', 'potreros', 'nro_potrero'),
        #        ('codigo_campana', 'campana', 'nro_campana'),
        #        ('codigo_cultivo', 'cultivo', 'nro_cultivo'),
        #        ('codigo_destino', 'destino', 'codigo'),
        #        ('codigo_silo', 'silos', 'nro_silo'),
        #        ('codigo_contratista', 'contrat', 'nro_contratista'),
        #        ('codigo_tractorista', 'tractori', 'nro_tractorista'),
        #        ('codigo_camion', 'camion', 'nro_camion'),
        #        ('nro_maquina', 'maquina', 'nro_maquina')]
        'fk': None
    }, {
        'name': 'mov_hora',
        'pk': 'id_mov_hora',
        # 'fk': [('nro_tractorista', 'tractori', 'nro_tractorista')]
        'fk': None
    }, {
        'name': 'mov_leche',
        'pk': 'id_mov_leche',
        # 'fk': [('nro_cliente', 'cli', 'codigo'),
        #        ('tipo_movimiento', 'tipo_movimiento', 'codigo')]
        # ('nro_comprobante', 'cod_comprob', 'codigo')]
        'fk': None
    }, {
        'name': 'mov_potr',
        'pk': 'id_mov_potr',
        # 'fk': [('sector', 'sector', 'nro_sector'),
        #        ('sub_sector', 'subsecto', 'nro_sub_sector'),
        #        ('campo', 'campos', 'nro_campo'),
        #        ('nro_potrero', 'potreros', 'nro_potrero'),
        #        ('codigo_laboreo', 'laboreo', 'nro_laboreo'),
        #        ('contratista', 'contrat', 'nro_contratista'),
        #        ('codigo_agroquimico', 'agroquim', 'nro_agroquimico'),
        #        ('codigo_cultivo', 'cultivo', 'nro_cultivo'),
        #        ('codigo_fertilizante', 'fertiliz', 'nro_fertilizante'),
        #        ('codigo_campana', 'campana', 'nro_campana'),
        #        ('codigo_destino', 'destino', 'codigo'),
        #        ('codigo_silo', 'silos', 'nro_silo')]
        'fk': None
    }, {
        'name': 'mov_prod',
        'pk': 'id_mov_prod',
        # 'fk': [('nro_tambo', 'tambos', 'nro_tambo'),
        #        ('destino', 'destino', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'mov_silos',
        'pk': 'id_mov_silos',
        # 'fk': [('nro_destino', 'destino', 'codigo'),
        #        ('nro_silo_entrante', 'silos', 'nro_silo'),
        #        ('nro_cultivo', 'cultivo', 'nro_cultivo'),
        #        ('nro_silo', 'silos', 'nro_silo'),
        #        ('nro_potrero', 'potreros', 'nro_potrero'),
        #        ('producto', 'producto', 'nro_producto'),
        #        ('cliente', 'cli', 'codigo'),
        #        ('actividad', 'actividad', 'nro_actividad')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'mov_suple',
        'pk': 'id_mov_suple',
        # 'fk': [('actividad', 'actividad', 'nro_actividad'),
        #        ('nro_silo', 'silos', 'nro_silo'),
        #        ('nro_producto', 'producto', 'nro_producto')]
        'fk': None
    }, {
        'name': 'mov_trac',
        'pk': 'id_mov_trac',
        # 'fk': [('nro_tractor', 'tractor', 'nro_tractor'),
        #        ('nro_tractorista', 'tractori', 'nro_tractorista'),
        #        ('nro_maquina', 'maquina', 'nro_maquina'),
        #        ('sector', 'sector', 'nro_sector'),
        #        ('sub_sector', 'subsecto', 'nro_sub_sector'),
        #        ('campo', 'campos', 'nro_campo'),
        #        ('nro_potrero', 'potreros', 'nro_potrero'),
        #        ('codigo_laboreo', 'laboreo', 'nro_laboreo'),
        #        ('campana_actual', 'campana', 'nro_campana')]
        'fk': None
    }, {
        'name': 'mov_trans',
        'pk': 'id_mov_trans',
        # 'fk': [('nro_transporte', 'transp', 'numero'),
        #        ('nro_chofer', 'chofer', 'nro_chofer'),
        #        ('campana', 'campana', 'nro_campana'),
        #        ('destino', 'destino', 'codigo'),
        #        ('silo', 'silos', 'nro_silo'),
        #        ('cultivo', 'cultivo', 'nro_cultivo'),
        #        ('potrero', 'potreros', 'nro_potrero'),
        #        ('cliente', 'cli', 'codigo')]
        'fk': None
    }, {
        'name': 'movgan',
        'pk': 'id_movgan',
        # 'fk': [('grupo', 'grupos', 'numero'),
        #        ('motivo', 'motivos', 'nro_motivo'),
        #        ('categoria', 'categorias', 'nro_categoria'),
        #        ('rodeo', 'rodeo', 'nro_rodeo')]
        'fk': None
    }, {
        'name': 'movim',
        'pk': 'nro_movimiento',
        'fk': None
    }, {
        'name': 'movimpu',
        'pk': 'id_movimpu',
        'fk': [('cod_imput', 'imputaci', 'codigo'),
               ('tipo_proveedor', 'tipoprov', 'codigo'),
               # ('nro_ordenpago', 'ord_pago', 'codigo'),
               ('actividad', 'actividad', 'nro_actividad'),
               ('cod_provincia', 'provincias', 'nro_provincia')]
        # ('num_comprob', 'cod_comprob', 'codigo'),
        # 'fk': None
    }, {
        'name': 'ms',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'observop',
        'pk': 'id_observop',
        # 'fk': [('nro_orden_pago', 'ord_pago', 'codigo')]
        'fk': None
    }, {
        'name': 'ord_pago',
        'pk': 'codigo',
        # 'fk': [('nro_proveedor', 'proctcte', 'codigo')]
        'fk': None
    }, {
        'name': 'pagados',
        'pk': 'id_pagados',
        # 'fk': [('nro_orden_pago', 'ord_pago', 'codigo'),
        #        ('cod_prove', 'proctcte', 'codigo'),
        #        ('tipo_prove', 'tipoprov', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'pendcobro',
        'pk': 'id_pendcobro',
        # 'fk': [('nro_cliente', 'cli', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo')]
        'fk': None
    }, {
        'name': 'pendpago',
        'pk': 'id_pendpago',
        # 'fk': [('tipo_prove', 'tipoprov', 'codigo'),
        #        ('cod_prove', 'proctcte', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'potreros',
        'pk': 'nro_potrero',
        # 'fk': [('campo', 'campos', 'nro_campo'),
        #        ('campana_actual', 'campana', 'nro_campana'),
        #        ('actividad', 'actividad', 'nro_actividad')]
        'fk': None
    }, {
        'name': 'prgastos',
        'pk': 'id_prgastos',
        # 'fk': [('nro_orden_pago', 'ord_pago', 'codigo'),
        #        ('nro_recibo', 'recibos', 'nro_recibo'),
        #        ('nro_retencion', 'retencio', 'nro_retencion')]
        'fk': None
    }, {
        'name': 'pro_car',
        'pk': 'id_pro_car',
        # 'fk': [('movimiento', 'movim', 'nro_movimiento'),
        #        ('nro_producto', 'producto', 'nro_producto')]
        # ('proveedor'),
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'pro_car_oc',
        'pk': 'id_pro_car_oc',
        # 'fk': [('movimiento', 'movim', 'nro_movimiento'),
        #        ('nro_producto', 'producto', 'nro_producto')]
        # ('proveedor'),
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'pro_ven',
        'pk': 'movimiento, nro_comprobante, nro_producto',
        # 'fk': [('movimiento', 'movim', 'nro_movimiento'),
        #        ('nro_producto', 'producto', 'nro_producto')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'proctcte',
        'pk': 'codigo',
        # 'fk': [('localidad', 'localidad', 'codigo'),
        #        ('tipo_proveedor', 'tipoprov', 'codigo')]
        'fk': None
    }, {
        'name': 'producto',
        'pk': 'nro_producto',
        # 'fk': [('nro_linea', 'lineas', 'num_linea'),
        #        ('nro_rubro', 'rubros', 'nro_rubro')]
        'fk': None
    }, {
        'name': 'provedor',
        'pk': 'codigo',
        # 'fk': [('localidad', 'localidad', 'codigo'),
        #        ('tipo_proveedor', 'tipoprov', 'codigo')]
        'fk': None
    }, {
        'name': 'provincias',
        'pk': 'nro_provincia',
        'fk': None
    }, {
        'name': 'recibos',
        'pk': 'nro_recibo',
        # 'fk': [('nro_cliente', 'cli', 'codigo')]
        'fk': None
    }, {
        'name': 'resopago',
        'pk': 'id_resopago',
        # 'fk': [('nro_orden', 'ord_pago', 'codigo'),
        #        ('nro_provedor', 'proctcte', 'codigo'),
        #        ('nrocaja', 'cajas', 'numero')]
        'fk': None
    }, {
        'name': 'respons',
        'pk': 'nro_responsable',
        'fk': None
    }, {
        'name': 'ret_ib',
        'pk': 'nro_retencion',
        'fk': [('provincia', 'provincias', 'nro_provincia')]
        # 'fk': None
    }, {
        'name': 'ret_prov',
        'pk': 'id_ret_prov',
        # 'fk': [('cod_prove', 'proctcte', 'codigo')]
        'fk': None
    }, {
        'name': 'retencio',
        'pk': 'nro_retencion',
        'fk': None
    }, {
        'name': 'rodados',
        'pk': 'nro_rodado',
        'fk': None
    }, {
        'name': 'rodeo',
        'pk': 'nro_rodeo',
        # 'fk': [('grupo', 'grupos', 'numero')]
        'fk': None
    }, {
        'name': 'rubros',
        'pk': 'nro_rubro',
        'fk': None
    }, {
        'name': 'sector',
        'pk': 'nro_sector',
        # 'fk': [('responsable_sector', 'respons', 'nro_responsable')]
        'fk': None
    }, {
        'name': 'silos',
        'pk': 'nro_silo',
        # 'fk': [('nro_cultivo', 'cultivo', 'nro_cultivo')]
        'fk': None
    }, {
        'name': 'stockdep',
        'pk': 'id_stockdep',
        # 'fk': [('nro_producto', 'producto', 'nro_producto'),
        #        ('nro_deposito', 'deposito_stock', 'nro_deposito')]
        'fk': None
    }, {
        'name': 'stocksil',
        'pk': 'id_stocksil',
        # 'fk': [('nro_silo', 'silos', 'nro_silo'),
        #        ('campana_actual', 'campana', 'nro_campana'),
        #        ('nro_cultivo', 'cultivo', 'nro_cultivo')]
        'fk': None
    }, {
        'name': 'subsecto',
        'pk': 'nro_sub_sector',
        # 'fk': [('sector', 'sector', 'nro_sector'),
        #        ('responsable_sub_sector', 'respons', 'nro_responsable')]
        'fk': None
    }, {
        'name': 'tambos',
        'pk': 'nro_tambo',
        'fk': None
    }, {
        'name': 'tanque',
        'pk': 'nro_tanque',
        'fk': None
    }, {
        'name': 'terceros',
        'pk': 'id_terceros',
        # 'fk': [('nro_ordenpago', 'ord_pago', 'codigo'),
        #        ('clering', 'clering', 'codigo')]
        'fk': None
    }, {
        'name': 'tipoprov',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'titular',
        'pk': 'nro_cuit',
        'fk': None
    }, {
        'name': 'tractor',
        'pk': 'nro_tractor',
        # 'fk': [('campo_asignado', 'campos', 'nro_campo'),
        'fk': [('nro_imputacion', 'imputaci', 'codigo')]
        # 'fk': None
    }, {
        'name': 'tractori',
        'pk': 'nro_tractorista',
        # 'fk': [('sector_asignado', 'sector', 'nro_sector')]
        'fk': None
    }, {
        'name': 'transp',
        'pk': 'numero',
        # 'fk': [('localidad', 'localidad', 'codigo')]
        'fk': None
    }, {
        'name': 'ugenerad',
        'pk': 'codigo',
        'fk': None
    }, {
        'name': 'vcarga',
        'pk': 'id_vcarga',
        # 'fk': [('numero_cliente', 'cli', 'codigo'),
        #        ('numero_deposito', 'deposito_stock', 'nro_deposito'),
        #        ('numero_actividad', 'actividad', 'nro_actividad'),
        #        ('cod_movimiento', 'movim', 'nro_movimiento'),
        #        ('tanque', 'tanque', 'nro_tanque')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'vcta_cte',
        'pk': 'id_vcta_cte',
        # 'fk': [('cod_cliente', 'cli', 'codigo'),
        #        ('tipo_movim', 'tipo_movimiento', 'codigo')]
        # ('nro_comprob', 'cod_comprob', 'codigo')]
        'fk': None
    }, {
        'name': 'ven_car',
        'pk': 'id_ven_car',
        # 'fk': [('movimiento', 'movim', 'nro_movimiento'),
        #        ('cliente', 'cli', 'codigo'),
        #        ('nro_categoria', 'categorias', 'nro_categoria'),
        #        ('nro_rodeo', 'rodeo', 'nro_rodeo')]
        # ('nro_comprobante', 'cod_comprob', 'codigo'),
        'fk': None
    }, {
        'name': 'ventas',
        'pk': 'id_ventas',
        'fk': [('cod_provincia', 'provincias', 'nro_provincia'),]
        #        ('tipo_movim', 'tipo_movimiento', 'codigo')]
        # ('nro_compro', 'cod_comprob', 'codigo'),
        # 'fk': None
    },
]
