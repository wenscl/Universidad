--secuencias

CREATE SEQUENCE public.cliente_codigo_cliente_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.cliente_codigo_cliente_seq
    OWNER TO postgres;

CREATE SEQUENCE public.empleado_codigo_empleado_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.empleado_codigo_empleado_seq
    OWNER TO postgres;

CREATE SEQUENCE public.familia_cod_familia_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.familia_cod_familia_seq
    OWNER TO postgres;
	
CREATE SEQUENCE public.nivel_estudio_cod_nivel_estudio_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.nivel_estudio_cod_nivel_estudio_seq
    OWNER TO postgres;
	
CREATE SEQUENCE public.producto_codigo_producto_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.producto_codigo_producto_seq
    OWNER TO postgres;
	
CREATE SEQUENCE public.tipo_producto_cod_tipo_producto_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.tipo_producto_cod_tipo_producto_seq
    OWNER TO postgres;
	
	
--nivel estudio

CREATE TABLE public.nivel_estudio
(
    cod_nivel_estudio integer NOT NULL DEFAULT nextval('nivel_estudio_cod_nivel_estudio_seq'::regclass),
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT nivel_estudio_pkey PRIMARY KEY (cod_nivel_estudio)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.nivel_estudio
    OWNER to postgres;
	
	
--cliente

CREATE TABLE public.cliente
(
    codigo_cliente integer NOT NULL DEFAULT nextval('cliente_codigo_cliente_seq'::regclass),
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellido character varying(100) COLLATE pg_catalog."default" NOT NULL,
    direccion character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    cod_nivel_estudio integer NOT NULL,
    sexo integer NOT NULL,
    CONSTRAINT cliente_pkey PRIMARY KEY (codigo_cliente),
    CONSTRAINT fk_cliente_nivel_estudio FOREIGN KEY (cod_nivel_estudio)
        REFERENCES public.nivel_estudio (cod_nivel_estudio) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.cliente
    OWNER to postgres;
	
	
--empleado

CREATE TABLE public.empleado
(
    codigo_empleado integer NOT NULL DEFAULT nextval('empleado_codigo_empleado_seq'::regclass),
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellido character varying(100) COLLATE pg_catalog."default" NOT NULL,
    fecha_nacimiento date NOT NULL,
    CONSTRAINT empleado_pkey PRIMARY KEY (codigo_empleado)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.empleado
    OWNER to postgres;


--telefono cliente

CREATE TABLE public.telefono_cliente
(
    codigo_cliente integer NOT NULL,
    item integer NOT NULL,
    telefono_cliente integer,
    CONSTRAINT telefono_cliente_pkey PRIMARY KEY (codigo_cliente, item),
    CONSTRAINT fk_cliente_telefono FOREIGN KEY (codigo_cliente)
        REFERENCES public.cliente (codigo_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.telefono_cliente
    OWNER to postgres;

CREATE INDEX fki_fk_cliente_telefono
    ON public.telefono_cliente USING btree
    (codigo_cliente)
    TABLESPACE pg_default;

	
--familia

CREATE TABLE public.familia
(
    cod_familia integer NOT NULL DEFAULT nextval('familia_cod_familia_seq'::regclass),
    descripcion_familia character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT familia_pkey PRIMARY KEY (cod_familia)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.familia
    OWNER to postgres;

	
--tipo producto

CREATE TABLE public.tipo_producto
(
    cod_tipo_producto integer NOT NULL DEFAULT nextval('tipo_producto_cod_tipo_producto_seq'::regclass),
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tipo_producto_pkey PRIMARY KEY (cod_tipo_producto)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.tipo_producto
    OWNER to postgres;
	

-- producto

CREATE TABLE public.producto
(
    codigo_producto integer NOT NULL DEFAULT nextval('producto_codigo_producto_seq'::regclass),
    descripcion_producto character varying COLLATE pg_catalog."default" NOT NULL,
    costo real NOT NULL,
    cod_tipo_producto integer NOT NULL,
    cod_familia integer NOT NULL,
    CONSTRAINT producto_pkey PRIMARY KEY (codigo_producto),
    CONSTRAINT fk_familia_producto FOREIGN KEY (cod_familia)
        REFERENCES public.familia (cod_familia) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_tipo_producto FOREIGN KEY (cod_tipo_producto)
        REFERENCES public.tipo_producto (cod_tipo_producto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.producto
    OWNER to postgres;

CREATE INDEX fki_fk_familia_producto
    ON public.producto USING btree
    (cod_familia)
    TABLESPACE pg_default;

CREATE INDEX fki_fk_tipo_producto
    ON public.producto USING btree
    (cod_tipo_producto)
    TABLESPACE pg_default;


--venta

CREATE TABLE public.venta
(
    nro_ticket character varying COLLATE pg_catalog."default" NOT NULL,
    fecha date NOT NULL,
    cod_empleado integer NOT NULL,
    cod_cliente integer NOT NULL,
    monto real NOT NULL,
    CONSTRAINT venta_pkey PRIMARY KEY (nro_ticket),
    CONSTRAINT fk_codigo_cliente FOREIGN KEY (cod_cliente)
        REFERENCES public.cliente (codigo_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_codigo_empleado FOREIGN KEY (cod_empleado)
        REFERENCES public.empleado (codigo_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.venta
    OWNER to postgres;

	
--item venta

CREATE TABLE public.item_venta
(
    nro_ticket character varying COLLATE pg_catalog."default" NOT NULL,
    codigo_producto integer NOT NULL,
    cantidad integer NOT NULL,
    monto_item real NOT NULL,
    CONSTRAINT item_venta_pkey PRIMARY KEY (codigo_producto, nro_ticket),
    CONSTRAINT fk_producto_item_venta FOREIGN KEY (codigo_producto)
        REFERENCES public.producto (codigo_producto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT item_venta_nro_ticket_fkey FOREIGN KEY (nro_ticket)
        REFERENCES public.venta (nro_ticket) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.item_venta
    OWNER to postgres;

CREATE INDEX fki_fk_producto_item_venta
    ON public.item_venta USING btree
    (codigo_producto)
    TABLESPACE pg_default;
	
	
--asistencia
	
CREATE TABLE public.asistencia
(
    codigo_cliente integer NOT NULL,
    fecha date NOT NULL,
    hora integer NOT NULL,
    CONSTRAINT asistencia_pkey PRIMARY KEY (codigo_cliente, fecha, hora),
    CONSTRAINT fk_cliente_asistencia FOREIGN KEY (codigo_cliente)
        REFERENCES public.cliente (codigo_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.asistencia
    OWNER to postgres;

CREATE INDEX fki_fk_cliente_asistencia
    ON public.asistencia USING btree
    (codigo_cliente)
    TABLESPACE pg_default;