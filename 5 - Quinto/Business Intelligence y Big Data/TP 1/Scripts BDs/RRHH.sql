-- secuencias

CREATE SEQUENCE public.actividad_id_actividad_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.actividad_id_actividad_seq
    OWNER TO postgres;

CREATE SEQUENCE public.empleado_legajo_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.empleado_legajo_seq
    OWNER TO postgres;

CREATE SEQUENCE public.especialidad_cod_especialidad_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.especialidad_cod_especialidad_seq
    OWNER TO postgres;


--actividad

CREATE TABLE public.actividad
(
    id_actividad integer NOT NULL DEFAULT nextval('actividad_id_actividad_seq'::regclass),
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    fecha_inicio date NOT NULL,
    CONSTRAINT actividad_pkey PRIMARY KEY (id_actividad)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.actividad
    OWNER to postgres;


--empleado

CREATE TABLE public.empleado
(
    legajo integer NOT NULL DEFAULT nextval('empleado_legajo_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default" NOT NULL,
    apellido character varying COLLATE pg_catalog."default" NOT NULL,
    direccion character varying COLLATE pg_catalog."default" NOT NULL,
    sueldo real NOT NULL,
    fecha_ingreso date NOT NULL,
    gimnasio integer NOT NULL,
    CONSTRAINT empleado_pkey PRIMARY KEY (legajo)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.empleado
    OWNER to postgres;


--actividad instructor

CREATE TABLE public.actividad_instructor
(
    id_actividad integer NOT NULL,
    legajo integer NOT NULL,
    hora_inicio integer NOT NULL,
    hora_fin integer NOT NULL,
    CONSTRAINT actividad_instructor_pkey PRIMARY KEY (id_actividad, legajo),
    CONSTRAINT fk_actividad_ai FOREIGN KEY (id_actividad)
        REFERENCES public.actividad (id_actividad) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_empleado_ai FOREIGN KEY (legajo)
        REFERENCES public.empleado (legajo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.actividad_instructor
    OWNER to postgres;


--especialidad

CREATE TABLE public.especialidad
(
    cod_especialidad integer NOT NULL DEFAULT nextval('especialidad_cod_especialidad_seq'::regclass),
    descripcion character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT especialidad_pkey PRIMARY KEY (cod_especialidad)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.especialidad
    OWNER to postgres;


--especialidad empleado

CREATE TABLE public.especialidades_empleado
(
    cod_especialidad integer NOT NULL,
    legajo integer NOT NULL,
    nivel_conocimiento character varying(100) COLLATE pg_catalog."default" NOT NULL,
    horas_capacitacion integer NOT NULL,
    CONSTRAINT especialidades_empleado_pkey PRIMARY KEY (cod_especialidad, legajo),
    CONSTRAINT fk_empleado_em FOREIGN KEY (legajo)
        REFERENCES public.empleado (legajo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_especialidad_em FOREIGN KEY (cod_especialidad)
        REFERENCES public.especialidad (cod_especialidad) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.especialidades_empleado
    OWNER to postgres;


--telefono empleado

CREATE TABLE public.telefono_empleado
(
    legajo integer NOT NULL,
    telefono_empleado integer NOT NULL,
    CONSTRAINT telefono_empleado_pkey PRIMARY KEY (legajo, telefono_empleado),
    CONSTRAINT fk_empleado_telefono FOREIGN KEY (legajo)
        REFERENCES public.empleado (legajo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.telefono_empleado
    OWNER to postgres;
