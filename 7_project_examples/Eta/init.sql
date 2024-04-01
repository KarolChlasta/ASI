CREATE SCHEMA IF NOT EXISTS cwur;

-- Table: your_schema.cwur

DROP TABLE IF EXISTS cwur.cwur;
DROP TABLE IF EXISTS cwur.synthetic_cwur;

CREATE TABLE IF NOT EXISTS cwur.cwur
(
    world_rank integer,
    institution character varying COLLATE pg_catalog."default",
    country character varying COLLATE pg_catalog."default",
    national_rank integer,
    quality_of_education integer,
    alumni_employment integer,
    quality_of_faculty integer,
    publications integer,
    influence integer,
    citations integer,
    broad_impact double precision,
    patents integer,
    score double precision,
    year integer
)

CREATE TABLE IF NOT EXISTS cwur.synthetic_cwur
(
    world_rank integer,
    institution character varying COLLATE pg_catalog."default",
    country character varying COLLATE pg_catalog."default",
    national_rank integer,
    quality_of_education integer,
    alumni_employment integer,
    quality_of_faculty integer,
    publications integer,
    influence integer,
    citations integer,
    broad_impact double precision,
    patents integer,
    score double precision,
    year integer
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS cwur.cwur
    OWNER to postgres;

ALTER TABLE IF EXISTS cwur.synthetic_cwur
    OWNER to postgres;