-- Table: public.h_clientes_asistencias

CREATE TABLE public.h_clientes_asistencias
(
    id_tiempo integer NOT NULL,
    id_cliente integer NOT NULL,
    id_horario integer NOT NULL,
    cantidad integer NOT NULL,
    CONSTRAINT h_clientes_asistencias_pkey PRIMARY KEY (id_tiempo, id_cliente, id_horario),
    CONSTRAINT fk_h_clientes_asistencias_d_cliente FOREIGN KEY (id_cliente)
        REFERENCES public.d_cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_clientes_asistencias_d_horario FOREIGN KEY (id_horario)
        REFERENCES public.d_horario (id_horario) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_clientes_asistencias_d_tiempo FOREIGN KEY (id_tiempo)
        REFERENCES public.d_tiempo (id_tiempo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.h_clientes_asistencias
    OWNER to postgres;
	
-- Table: public.h_empleados_actividades

CREATE TABLE public.h_empleados_actividades
(
    id_empleado integer NOT NULL,
    id_actividad integer NOT NULL,
    cantidad_alumnos integer NOT NULL,
    CONSTRAINT h_empleados_actividades_pkey PRIMARY KEY (id_empleado, id_actividad),
    CONSTRAINT fk_h_empleados_actividades_d_actividad FOREIGN KEY (id_actividad)
        REFERENCES public.d_actividad (id_actividad) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_empleados_actividades_d_empleado FOREIGN KEY (id_empleado)
        REFERENCES public.d_empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.h_empleados_actividades
    OWNER to postgres;
	
-- Table: public.h_ventas_abonos

CREATE TABLE public.h_ventas_abonos
(
    id_tiempo integer NOT NULL,
    id_gimnasio integer NOT NULL,
    id_actividad integer NOT NULL,
    id_empleado integer NOT NULL,
    id_cliente integer NOT NULL,
    monto real NOT NULL,
    cantidad integer NOT NULL,
    CONSTRAINT h_venta_abonos_pkey PRIMARY KEY (id_tiempo, id_gimnasio, id_actividad, id_empleado, id_cliente),
    CONSTRAINT fk_h_venta_abonos_d_actividad FOREIGN KEY (id_actividad)
        REFERENCES public.d_actividad (id_actividad) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_venta_abonos_d_cliente FOREIGN KEY (id_cliente)
        REFERENCES public.d_cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_venta_abonos_d_empleado FOREIGN KEY (id_empleado)
        REFERENCES public.d_empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_venta_abonos_d_gimnasio FOREIGN KEY (id_gimnasio)
        REFERENCES public.d_gimnasio (id_gimnasio) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_venta_abonos_d_tiempo FOREIGN KEY (id_tiempo)
        REFERENCES public.d_tiempo (id_tiempo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.h_ventas_abonos
    OWNER to postgres;
	
-- Table: public.h_ventas_productos

CREATE TABLE public.h_ventas_productos
(
    id_producto integer NOT NULL,
    id_cliente integer NOT NULL,
    id_tiempo integer NOT NULL,
    id_gimnasio integer NOT NULL,
    cantidad integer NOT NULL,
    precio real NOT NULL,
    monto_total real NOT NULL,
    CONSTRAINT h_ventas_productos_pkey PRIMARY KEY (id_producto, id_cliente, id_tiempo, id_gimnasio),
    CONSTRAINT fk_h_ventas_productos_d_cliente FOREIGN KEY (id_cliente)
        REFERENCES public.d_cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_ventas_productos_d_gimnasio FOREIGN KEY (id_gimnasio)
        REFERENCES public.d_gimnasio (id_gimnasio) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_ventas_productos_d_producto FOREIGN KEY (id_producto)
        REFERENCES public.d_producto (id_producto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_h_ventas_productos_d_tiempo FOREIGN KEY (id_tiempo)
        REFERENCES public.d_tiempo (id_tiempo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.h_ventas_productos
    OWNER to postgres;