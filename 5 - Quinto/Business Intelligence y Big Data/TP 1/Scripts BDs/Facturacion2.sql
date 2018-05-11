-- secuencias

CREATE SEQUENCE public.cat_cod_cat_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.cat_cod_cat_seq
    OWNER TO postgres;

CREATE SEQUENCE public.producto_cod_producto_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.producto_cod_producto_seq
    OWNER TO postgres;

CREATE SEQUENCE public.subcategoria_cod_subcategoria_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.subcategoria_cod_subcategoria_seq
    OWNER TO postgres;


--categoria

CREATE TABLE public.categoria
(
    cod_categoria integer NOT NULL DEFAULT nextval('cat_cod_cat_seq'::regclass),
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT categoria_pkey PRIMARY KEY (cod_categoria)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.categoria
    OWNER to postgres;


--subcategoria

CREATE TABLE public.subcategoria
(
    cod_subcategoria integer NOT NULL DEFAULT nextval('subcategoria_cod_subcategoria_seq'::regclass),
    cod_categoria integer NOT NULL,
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT subcategoria_pkey PRIMARY KEY (cod_subcategoria),
    CONSTRAINT fk_categoria_subcategoria FOREIGN KEY (cod_categoria)
        REFERENCES public.categoria (cod_categoria) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.subcategoria
    OWNER to postgres;


--producto

CREATE TABLE public.producto
(
    cod_producto integer NOT NULL DEFAULT nextval('producto_cod_producto_seq'::regclass),
    cod_subcategoria integer NOT NULL,
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    precio_actual real NOT NULL,
    CONSTRAINT producto_pkey PRIMARY KEY (cod_producto),
    CONSTRAINT fk_subcategoria_producto FOREIGN KEY (cod_subcategoria)
        REFERENCES public.subcategoria (cod_subcategoria) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.producto
    OWNER to postgres;


--cliente

CREATE TABLE public.cliente
(
    cod_cliente integer NOT NULL,
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    domicilio character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cliente_pkey PRIMARY KEY (cod_cliente)
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
    cod_empleado integer NOT NULL,
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellido character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT empleado_pkey PRIMARY KEY (cod_empleado)
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
    cod_cliente integer NOT NULL,
    tel_cliente integer NOT NULL,
    CONSTRAINT telefono_cliente_pkey PRIMARY KEY (cod_cliente, tel_cliente),
    CONSTRAINT fk_cliente_telefono FOREIGN KEY (cod_cliente)
        REFERENCES public.cliente (cod_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.telefono_cliente
    OWNER to postgres;


--venta

CREATE TABLE public.venta
(
    nro_ticket character varying COLLATE pg_catalog."default" NOT NULL,
    fecha_venta date NOT NULL,
    cod_empleado integer NOT NULL,
    cod_cliente integer NOT NULL,
    CONSTRAINT venta_pkey PRIMARY KEY (nro_ticket),
    CONSTRAINT fk_cliente_venta FOREIGN KEY (cod_cliente)
        REFERENCES public.cliente (cod_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_empleado_venta FOREIGN KEY (cod_empleado)
        REFERENCES public.empleado (cod_empleado) MATCH SIMPLE
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
    cod_producto integer NOT NULL,
    cantidad integer NOT NULL,
    precio real NOT NULL,
    CONSTRAINT item_venta_pkey PRIMARY KEY (cod_producto, nro_ticket),
    CONSTRAINT fk_producto_item_venta FOREIGN KEY (cod_producto)
        REFERENCES public.producto (cod_producto) MATCH SIMPLE
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

