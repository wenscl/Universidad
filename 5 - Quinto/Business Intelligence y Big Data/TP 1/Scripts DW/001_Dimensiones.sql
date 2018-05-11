--secuencias

CREATE SEQUENCE public.d_horario_id_horario_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.d_horario_id_horario_seq
    OWNER TO postgres;
	
CREATE SEQUENCE public.d_tiempo_id_tiempo_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.d_tiempo_id_tiempo_seq
    OWNER TO postgres;
	
--tablas

-- Table: public.d_actividad

CREATE TABLE public.d_actividad
(
    id_actividad integer NOT NULL,
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT d_actividad_pkey PRIMARY KEY (id_actividad)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_actividad
    OWNER to postgres;
	
-- Table: public.d_cliente

CREATE TABLE public.d_cliente
(
    id_cliente integer NOT NULL,
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    apellido character varying COLLATE pg_catalog."default" NOT NULL,
    sexo character varying COLLATE pg_catalog."default" NOT NULL,
    nivel_estudio character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT d_cliente_pkey PRIMARY KEY (id_cliente)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_cliente
    OWNER to postgres;
	
-- Table: public.d_empleado

CREATE TABLE public.d_empleado
(
    id_empleado integer NOT NULL,
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    apellido character varying COLLATE pg_catalog."default" NOT NULL,
    es_profesor boolean NOT NULL,
    horas_capacitacion integer NOT NULL,
    sueldo real NOT NULL,
    fecha_ingreso date NOT NULL,
    CONSTRAINT d_empleado_pkey PRIMARY KEY (id_empleado)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_empleado
    OWNER to postgres;
	
-- Table: public.d_gimnasio

CREATE TABLE public.d_gimnasio
(
    id_gimnasio integer NOT NULL,
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT d_gimnasio_pkey PRIMARY KEY (id_gimnasio)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_gimnasio
    OWNER to postgres;
	
-- Table: public.d_horario

CREATE TABLE public.d_horario
(
    id_horario integer NOT NULL DEFAULT nextval('d_horario_id_horario_seq'::regclass),
    hora_inicio integer NOT NULL,
    hora_fin integer NOT NULL,
    CONSTRAINT d_horario_pkey PRIMARY KEY (id_horario)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_horario
    OWNER to postgres;
	
-- Table: public.d_producto

CREATE TABLE public.d_producto
(
    id_producto integer NOT NULL,
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT d_producto_pkey PRIMARY KEY (id_producto)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_producto
    OWNER to postgres;
	
-- Table: public.d_tiempo

CREATE TABLE public.d_tiempo
(
    id_tiempo integer NOT NULL DEFAULT nextval('d_tiempo_id_tiempo_seq'::regclass),
    dia integer NOT NULL,
    mes integer NOT NULL,
    anio integer NOT NULL,
    trimestre integer NOT NULL,
    estacion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT d_tiempo_pkey PRIMARY KEY (id_tiempo)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.d_tiempo
    OWNER to postgres;