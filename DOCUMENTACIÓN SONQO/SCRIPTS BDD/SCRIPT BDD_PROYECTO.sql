PGDMP                      |            BDD_PROJECT_ANXIETY    14.12    16.3 .    "           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            #           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            $           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            %           1262    16418    BDD_PROJECT_ANXIETY    DATABASE     �   CREATE DATABASE "BDD_PROJECT_ANXIETY" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Ecuador.1252';
 %   DROP DATABASE "BDD_PROJECT_ANXIETY";
                postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            &           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    4            �            1259    16452    actividades    TABLE     0  CREATE TABLE public.actividades (
    id integer NOT NULL,
    nivel character varying(10) NOT NULL,
    descripcion text NOT NULL,
    CONSTRAINT actividades_nivel_check CHECK (((nivel)::text = ANY ((ARRAY['bajo'::character varying, 'medio'::character varying, 'alto'::character varying])::text[])))
);
    DROP TABLE public.actividades;
       public         heap    postgres    false    4            �            1259    16451    actividades_id_seq    SEQUENCE     �   CREATE SEQUENCE public.actividades_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.actividades_id_seq;
       public          postgres    false    4    214            '           0    0    actividades_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.actividades_id_seq OWNED BY public.actividades.id;
          public          postgres    false    213            �            1259    16438    niveles_ansiedad    TABLE     �  CREATE TABLE public.niveles_ansiedad (
    id integer NOT NULL,
    usuario_id integer,
    nivel character varying(10) NOT NULL,
    pulsaciones integer NOT NULL,
    fecha_registro timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT niveles_ansiedad_nivel_check CHECK (((nivel)::text = ANY ((ARRAY['bajo'::character varying, 'medio'::character varying, 'alto'::character varying])::text[])))
);
 $   DROP TABLE public.niveles_ansiedad;
       public         heap    postgres    false    4            �            1259    16437    niveles_ansiedad_id_seq    SEQUENCE     �   CREATE SEQUENCE public.niveles_ansiedad_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.niveles_ansiedad_id_seq;
       public          postgres    false    4    212            (           0    0    niveles_ansiedad_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.niveles_ansiedad_id_seq OWNED BY public.niveles_ansiedad.id;
          public          postgres    false    211            �            1259    16480    promedios_mensuales    TABLE       CREATE TABLE public.promedios_mensuales (
    id integer NOT NULL,
    usuario_id integer,
    mes integer NOT NULL,
    anio integer NOT NULL,
    promedio_nivel numeric(5,2) NOT NULL,
    fecha_calculo timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
 '   DROP TABLE public.promedios_mensuales;
       public         heap    postgres    false    4            �            1259    16479    promedios_mensuales_id_seq    SEQUENCE     �   CREATE SEQUENCE public.promedios_mensuales_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.promedios_mensuales_id_seq;
       public          postgres    false    218    4            )           0    0    promedios_mensuales_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.promedios_mensuales_id_seq OWNED BY public.promedios_mensuales.id;
          public          postgres    false    217            �            1259    16462    registros_actividades    TABLE     �   CREATE TABLE public.registros_actividades (
    id integer NOT NULL,
    usuario_id integer,
    actividad_id integer,
    fecha_registro timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
 )   DROP TABLE public.registros_actividades;
       public         heap    postgres    false    4            �            1259    16461    registros_actividades_id_seq    SEQUENCE     �   CREATE SEQUENCE public.registros_actividades_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.registros_actividades_id_seq;
       public          postgres    false    216    4            *           0    0    registros_actividades_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.registros_actividades_id_seq OWNED BY public.registros_actividades.id;
          public          postgres    false    215            �            1259    16428    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    fecha_registro timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false    4            �            1259    16427    usuarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public          postgres    false    4    210            +           0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public          postgres    false    209            t           2604    16455    actividades id    DEFAULT     p   ALTER TABLE ONLY public.actividades ALTER COLUMN id SET DEFAULT nextval('public.actividades_id_seq'::regclass);
 =   ALTER TABLE public.actividades ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214            r           2604    16441    niveles_ansiedad id    DEFAULT     z   ALTER TABLE ONLY public.niveles_ansiedad ALTER COLUMN id SET DEFAULT nextval('public.niveles_ansiedad_id_seq'::regclass);
 B   ALTER TABLE public.niveles_ansiedad ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    211    212            w           2604    16483    promedios_mensuales id    DEFAULT     �   ALTER TABLE ONLY public.promedios_mensuales ALTER COLUMN id SET DEFAULT nextval('public.promedios_mensuales_id_seq'::regclass);
 E   ALTER TABLE public.promedios_mensuales ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            u           2604    16465    registros_actividades id    DEFAULT     �   ALTER TABLE ONLY public.registros_actividades ALTER COLUMN id SET DEFAULT nextval('public.registros_actividades_id_seq'::regclass);
 G   ALTER TABLE public.registros_actividades ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            p           2604    16431    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    210    210                      0    16452    actividades 
   TABLE DATA           =   COPY public.actividades (id, nivel, descripcion) FROM stdin;
    public          postgres    false    214   �8                 0    16438    niveles_ansiedad 
   TABLE DATA           ^   COPY public.niveles_ansiedad (id, usuario_id, nivel, pulsaciones, fecha_registro) FROM stdin;
    public          postgres    false    212   �8                 0    16480    promedios_mensuales 
   TABLE DATA           g   COPY public.promedios_mensuales (id, usuario_id, mes, anio, promedio_nivel, fecha_calculo) FROM stdin;
    public          postgres    false    218   �8                 0    16462    registros_actividades 
   TABLE DATA           ]   COPY public.registros_actividades (id, usuario_id, actividad_id, fecha_registro) FROM stdin;
    public          postgres    false    216   �8                 0    16428    usuarios 
   TABLE DATA           E   COPY public.usuarios (id, nombre, email, fecha_registro) FROM stdin;
    public          postgres    false    210   9       ,           0    0    actividades_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.actividades_id_seq', 1, false);
          public          postgres    false    213            -           0    0    niveles_ansiedad_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.niveles_ansiedad_id_seq', 1, false);
          public          postgres    false    211            .           0    0    promedios_mensuales_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.promedios_mensuales_id_seq', 1, false);
          public          postgres    false    217            /           0    0    registros_actividades_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.registros_actividades_id_seq', 1, false);
          public          postgres    false    215            0           0    0    usuarios_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.usuarios_id_seq', 1, false);
          public          postgres    false    209            �           2606    16460    actividades actividades_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.actividades
    ADD CONSTRAINT actividades_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.actividades DROP CONSTRAINT actividades_pkey;
       public            postgres    false    214            �           2606    16445 &   niveles_ansiedad niveles_ansiedad_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.niveles_ansiedad
    ADD CONSTRAINT niveles_ansiedad_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.niveles_ansiedad DROP CONSTRAINT niveles_ansiedad_pkey;
       public            postgres    false    212            �           2606    16486 ,   promedios_mensuales promedios_mensuales_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.promedios_mensuales
    ADD CONSTRAINT promedios_mensuales_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.promedios_mensuales DROP CONSTRAINT promedios_mensuales_pkey;
       public            postgres    false    218            �           2606    16468 0   registros_actividades registros_actividades_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.registros_actividades
    ADD CONSTRAINT registros_actividades_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.registros_actividades DROP CONSTRAINT registros_actividades_pkey;
       public            postgres    false    216            |           2606    16436    usuarios usuarios_email_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_email_key UNIQUE (email);
 E   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_email_key;
       public            postgres    false    210            ~           2606    16434    usuarios usuarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    210            �           2606    16446 1   niveles_ansiedad niveles_ansiedad_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.niveles_ansiedad
    ADD CONSTRAINT niveles_ansiedad_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);
 [   ALTER TABLE ONLY public.niveles_ansiedad DROP CONSTRAINT niveles_ansiedad_usuario_id_fkey;
       public          postgres    false    212    210    3198            �           2606    16487 7   promedios_mensuales promedios_mensuales_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.promedios_mensuales
    ADD CONSTRAINT promedios_mensuales_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);
 a   ALTER TABLE ONLY public.promedios_mensuales DROP CONSTRAINT promedios_mensuales_usuario_id_fkey;
       public          postgres    false    210    3198    218            �           2606    16474 =   registros_actividades registros_actividades_actividad_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.registros_actividades
    ADD CONSTRAINT registros_actividades_actividad_id_fkey FOREIGN KEY (actividad_id) REFERENCES public.actividades(id);
 g   ALTER TABLE ONLY public.registros_actividades DROP CONSTRAINT registros_actividades_actividad_id_fkey;
       public          postgres    false    3202    216    214            �           2606    16469 ;   registros_actividades registros_actividades_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.registros_actividades
    ADD CONSTRAINT registros_actividades_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);
 e   ALTER TABLE ONLY public.registros_actividades DROP CONSTRAINT registros_actividades_usuario_id_fkey;
       public          postgres    false    3198    216    210                  x������ � �            x������ � �            x������ � �            x������ � �            x������ � �     