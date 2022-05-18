create table if not exists devices
(
    id bigserial not null
        constraint devices_pk
            primary key,
    dev_id   varchar(200) not null,
    dev_type varchar(120) not null
);


create index if not exists devices_dev_id_dev_type_index
    on devices (dev_id, dev_type);

create table if not exists endpoints
(
    id bigserial not null
        constraint endpoints_pk
            primary key,
    device_id integer
        constraint endpoints_devices_id_fk
            references devices
            on update cascade on delete cascade,
    comment   text
);
