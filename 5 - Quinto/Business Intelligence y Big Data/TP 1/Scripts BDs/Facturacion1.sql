-- secuencias

CREATE SEQUENCE public.familia_id_categoria_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.familia_id_categoria_seq
    OWNER TO postgres;

CREATE SEQUENCE public.producto_id_producto_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.producto_id_producto_seq
    OWNER TO postgres;

CREATE SEQUENCE public.subcategoria_id_subcategoria_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.subcategoria_id_subcategoria_seq
    OWNER TO postgres;


--familia

CREATE TABLE public.familia
(
    id_categoria integer NOT NULL DEFAULT nextval('familia_id_categoria_seq'::regclass),
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT familia_pkey PRIMARY KEY (id_categoria)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.familia
    OWNER to postgres;


--subcategoria

CREATE TABLE public.subcategoria
(
    id_subcategoria integer NOT NULL DEFAULT nextval('subcategoria_id_subcategoria_seq'::regclass),
    id_categoria integer NOT NULL,
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT subcategoria_pkey PRIMARY KEY (id_subcategoria),
    CONSTRAINT fk_familia_subcategoria FOREIGN KEY (id_categoria)
        REFERENCES public.familia (id_categoria) MATCH SIMPLE
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
    id_producto integer NOT NULL DEFAULT nextval('producto_id_producto_seq'::regclass),
    id_subcategoria integer NOT NULL,
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    precio_actual real NOT NULL,
    CONSTRAINT producto_pkey PRIMARY KEY (id_producto),
    CONSTRAINT fk_subcategoria_producto FOREIGN KEY (id_subcategoria)
        REFERENCES public.subcategoria (id_subcategoria) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.producto
    OWNER to postgres;


--empleado

CREATE TABLE public.empleado
(
    id_empleado integer NOT NULL,
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellido character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT empleado_pkey PRIMARY KEY (id_empleado)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.empleado
    OWNER to postgres;


--cliente

CREATE TABLE public.cliente
(
    id_cliente integer NOT NULL,
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    domicilio character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.cliente
    OWNER to postgres;


--telefono cliente

CREATE TABLE public.telefono_cliente
(
    id_cliente integer NOT NULL,
    telefono_cliente integer NOT NULL,
    CONSTRAINT telefono_cliente_pkey PRIMARY KEY (id_cliente, telefono_cliente),
    CONSTRAINT fk_cliente_telefono FOREIGN KEY (id_cliente)
        REFERENCES public.cliente (id_cliente) MATCH SIMPLE
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
    numero_ticket character varying COLLATE pg_catalog."default" NOT NULL,
    fecha_venta date NOT NULL,
    id_empleado integer NOT NULL,
    id_cliente integer NOT NULL,
    CONSTRAINT venta_pkey PRIMARY KEY (numero_ticket),
    CONSTRAINT fk_cliente_venta FOREIGN KEY (id_cliente)
        REFERENCES public.cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_empleado_venta FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
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
    numero_ticket character varying COLLATE pg_catalog."default" NOT NULL,
    id_producto integer NOT NULL,
    cantidad integer NOT NULL,
    precio real NOT NULL,
    CONSTRAINT item_venta_pkey PRIMARY KEY (id_producto, numero_ticket),
    CONSTRAINT fk_producto_item_venta FOREIGN KEY (id_producto)
        REFERENCES public.producto (id_producto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT item_venta_numero_ticket_fkey FOREIGN KEY (numero_ticket)
        REFERENCES public.venta (numero_ticket) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.item_venta
    OWNER to postgres;