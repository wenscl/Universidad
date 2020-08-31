from dal import autocomplete
from pandas import DataFrame

from app.models import Imputaci, Acumula, Movimpu, Actividad, Provincias, \
    Tipoprov


class AcumulaImpuAcumulada(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        acumula = Acumula.objects.all().order_by('descripcion')
        qs = Imputaci.objects.all().filter(donde_acumula__isnull=False) \
            .distinct('donde_acumula').order_by('donde_acumula')

        imputacion = self.forwarded.get('imputacion', None)
        if imputacion:
            qs = qs.filter(descripcion=imputacion)

        if self.q:
            qs = qs.filter(descripcion__icontains=self.q)

        acum = [x.donde_acumula.descripcion for x in qs if x.donde_acumula in acumula]
        qs = acumula.filter(descripcion__in=acum)

        return qs

    def get_result_label(self, item):
        return item.descripcion

    def get_selected_result_label(self, item):
        return item.descripcion


class AcumulaImpuSimple(autocomplete.Select2ListView):
    def get_list(self):
        impu_simple = Imputaci.objects.values('descripcion') \
            .distinct('descripcion').order_by('descripcion')

        acumulador = self.forwarded.get('acumulador', None)
        if acumulador:
            impu_simple = impu_simple.filter(donde_acumula=acumulador)

        if self.q:
            impu_simple = impu_simple.filter(descripcion__icontains=self.q)

        impu_simple_choices = [x['descripcion'] for x in impu_simple]

        return impu_simple_choices


class ImputacionImpuAcumulada(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        acumula = Acumula.objects.all().order_by('descripcion')
        qs = Movimpu.objects.all()\
            .filter(cod_imput__donde_acumula__isnull=False) \
            .distinct('cod_imput__donde_acumula')\
            .order_by('cod_imput__donde_acumula')

        imputacion = self.forwarded.get('imputacion', None)
        tipo_movimiento = self.forwarded.get('tipo_movimiento', None)
        actividad = self.forwarded.get('actividad', None)
        descripcion = self.forwarded.get('descripcion', None)
        tipo_proveedor = self.forwarded.get('tipo_proveedor', None)
        provincia = self.forwarded.get('provincia', None)
        if imputacion:
            qs = qs.filter(cod_imput=imputacion)
        if tipo_movimiento:
            qs = qs.filter(tipo_movim=tipo_movimiento)
        if actividad:
            qs = qs.filter(actividad=actividad)
        if descripcion:
            qs = qs.filter(descripcion=descripcion)
        if tipo_proveedor:
            qs = qs.filter(tipo_proveedor=tipo_proveedor)
        if provincia:
            qs = qs.filter(cod_provincia=provincia)

        if self.q:
            qs = qs.filter(cod_imput__donde_acumula__descripcion__icontains=self.q)

        acum = [x.cod_imput.donde_acumula.descripcion for x in qs
                if x.cod_imput.donde_acumula in acumula]
        qs = acumula.filter(descripcion__in=acum)

        return qs

    def get_result_label(self, item):
        return item.descripcion

    def get_selected_result_label(self, item):
        return item.descripcion


class ImputacionDescripcion(autocomplete.Select2ListView):
    def get_list(self):
        qs = Movimpu.objects.values('descripcion') \
            .distinct('descripcion').order_by('descripcion')

        acumulador = self.forwarded.get('acumulador', None)
        imputacion = self.forwarded.get('imputacion', None)
        tipo_movimiento = self.forwarded.get('tipo_movimiento', None)
        actividad = self.forwarded.get('actividad', None)
        tipo_proveedor = self.forwarded.get('tipo_proveedor', None)
        provincia = self.forwarded.get('provincia', None)
        if acumulador:
            qs = qs.filter(
                cod_imput__donde_acumula=acumulador)
        if imputacion:
            qs = qs.filter(cod_imput=imputacion)
        if tipo_movimiento:
            qs = qs.filter(tipo_movim=tipo_movimiento)
        if actividad:
            qs = qs.filter(actividad=actividad)
        if tipo_proveedor:
            qs = qs.filter(tipo_proveedor=tipo_proveedor)
        if provincia:
            qs = qs.filter(cod_provincia=provincia)

        if self.q:
            qs = qs.filter(descripcion__icontains=self.q)

        descripcion_choices = [x['descripcion'] for x in qs]

        return descripcion_choices


class ImputacionImpuSimple(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        imputaci = Imputaci.objects.all().order_by('descripcion')
        qs = Movimpu.objects.all().filter(cod_imput__isnull=False) \
            .distinct('cod_imput').order_by('cod_imput')

        acumulador = self.forwarded.get('acumulador', None)
        tipo_movimiento = self.forwarded.get('tipo_movimiento', None)
        actividad = self.forwarded.get('actividad', None)
        descripcion = self.forwarded.get('descripcion', None)
        tipo_proveedor = self.forwarded.get('tipo_proveedor', None)
        provincia = self.forwarded.get('provincia', None)
        if acumulador:
            qs = qs.filter(cod_imput__donde_acumula=acumulador)
        if tipo_movimiento:
            qs = qs.filter(tipo_movim=tipo_movimiento)
        if actividad:
            qs = qs.filter(actividad=actividad)
        if descripcion:
            qs = qs.filter(descripcion=descripcion)
        if tipo_proveedor:
            qs = qs.filter(tipo_proveedor=tipo_proveedor)
        if provincia:
            qs = qs.filter(cod_provincia=provincia)

        if self.q:
            qs = qs.filter(cod_imput__descripcion__icontains=self.q)

        imput = [x.cod_imput.descripcion for x in qs if x.cod_imput in imputaci]
        qs = imputaci.filter(descripcion__in=imput)

        return qs

    def get_result_label(self, item):
        return item.descripcion

    def get_selected_result_label(self, item):
        return item.descripcion


class ImputacionTipoMovim(autocomplete.Select2ListView):
    def get_list(self):
        qs = Movimpu.objects.values('tipo_movim') \
            .distinct('tipo_movim').order_by('tipo_movim')

        acumulador = self.forwarded.get('acumulador', None)
        imputacion = self.forwarded.get('imputacion', None)
        actividad = self.forwarded.get('actividad', None)
        descripcion = self.forwarded.get('descripcion', None)
        tipo_proveedor = self.forwarded.get('tipo_proveedor', None)
        provincia = self.forwarded.get('provincia', None)
        if acumulador:
            qs = qs.filter(
                cod_imput__donde_acumula=acumulador)
        if imputacion:
            qs = qs.filter(cod_imput=imputacion)
        if actividad:
            qs = qs.filter(actividad=actividad)
        if descripcion:
            qs = qs.filter(descripcion=descripcion)
        if tipo_proveedor:
            qs = qs.filter(tipo_proveedor=tipo_proveedor)
        if provincia:
            qs = qs.filter(cod_provincia=provincia)

        if self.q:
            qs = qs.filter(tipo_movim__icontains=self.q)

        tipo_movim_choices = [x['tipo_movim'] for x in qs]

        return tipo_movim_choices


class ImputacionActividad(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        actividad = Actividad.objects.all().order_by('descripcion')
        qs = Movimpu.objects.all().filter(actividad__isnull=False)\
            .distinct('actividad').order_by('actividad')

        acumulador = self.forwarded.get('acumulador', None)
        imputacion = self.forwarded.get('imputacion', None)
        tipo_movimiento = self.forwarded.get('tipo_movimiento', None)
        descripcion = self.forwarded.get('descripcion', None)
        tipo_proveedor = self.forwarded.get('tipo_proveedor', None)
        provincia = self.forwarded.get('provincia', None)
        if acumulador:
            qs = qs.filter(cod_imput__donde_acumula=acumulador)
        if imputacion:
            qs = qs.filter(cod_imput=imputacion)
        if tipo_movimiento:
            qs = qs.filter(tipo_movim=tipo_movimiento)
        if descripcion:
            qs = qs.filter(descripcion=descripcion)
        if tipo_proveedor:
            qs = qs.filter(tipo_proveedor=tipo_proveedor)
        if provincia:
            qs = qs.filter(cod_provincia=provincia)

        if self.q:
            qs = qs.filter(actividad__descripcion__icontains=self.q)

        act = [x.actividad.descripcion for x in qs if x.actividad in actividad]
        qs = actividad.filter(descripcion__in=act)

        return qs

    def get_result_label(self, item):
        return item.descripcion

    def get_selected_result_label(self, item):
        return item.descripcion


class ImputacionTipoProveedor(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        tipo_proveedor = Tipoprov.objects.all().order_by('descripcion')
        qs = Movimpu.objects.all().filter(tipo_proveedor__isnull=False)\
            .distinct('tipo_proveedor').order_by('tipo_proveedor')

        acumulador = self.forwarded.get('acumulador', None)
        imputacion = self.forwarded.get('imputacion', None)
        tipo_movimiento = self.forwarded.get('tipo_movimiento', None)
        actividad = self.forwarded.get('actividad', None)
        descripcion = self.forwarded.get('descripcion', None)
        provincia = self.forwarded.get('provincia', None)
        if acumulador:
            qs = qs.filter(cod_imput__donde_acumula=acumulador)
        if imputacion:
            qs = qs.filter(cod_imput=imputacion)
        if tipo_movimiento:
            qs = qs.filter(tipo_movim=tipo_movimiento)
        if actividad:
            qs = qs.filter(actividad=actividad)
        if descripcion:
            qs = qs.filter(descripcion=descripcion)
        if provincia:
            qs = qs.filter(cod_provincia=provincia)

        if self.q:
            qs = qs.filter(tipo_proveedor__descripcion__icontains=self.q)

        tipo_prov = [x.tipo_proveedor.descripcion for x in qs if x.tipo_proveedor in
               tipo_proveedor]
        qs = tipo_proveedor.filter(descripcion__in=tipo_prov)

        return qs

    def get_result_label(self, item):
        return item.descripcion

    def get_selected_result_label(self, item):
        return item.descripcion


class ImputacionProvincia(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        provincia = Provincias.objects.all().order_by('descripcion')
        qs = Movimpu.objects.all().filter(cod_provincia__isnull=False)\
            .distinct('cod_provincia').order_by('cod_provincia')

        acumulador = self.forwarded.get('acumulador', None)
        imputacion = self.forwarded.get('imputacion', None)
        tipo_movimiento = self.forwarded.get('tipo_movimiento', None)
        actividad = self.forwarded.get('actividad', None)
        descripcion = self.forwarded.get('descripcion', None)
        tipo_proveedor = self.forwarded.get('tipo_proveedor', None)
        if acumulador:
            qs = qs.filter(cod_imput__donde_acumula=acumulador)
        if imputacion:
            qs = qs.filter(cod_imput=imputacion)
        if tipo_movimiento:
            qs = qs.filter(tipo_movim=tipo_movimiento)
        if actividad:
            qs = qs.filter(actividad=actividad)
        if descripcion:
            qs = qs.filter(descripcion=descripcion)
        if tipo_proveedor:
            qs = qs.filter(tipo_proveedor=tipo_proveedor)

        if self.q:
            qs = qs.filter(cod_provincia__descripcion__icontains=self.q)

        prov = [x.cod_provincia.descripcion for x in qs if x.cod_provincia in
               provincia]
        qs = provincia.filter(descripcion__in=prov)

        return qs

    def get_result_label(self, item):
        return item.descripcion

    def get_selected_result_label(self, item):
        return item.descripcion
