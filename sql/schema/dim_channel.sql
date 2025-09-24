create table if not exists dim_channel (
  channel_id smallint not null,
  channel_group varchar(50) not null,
  channel_name varchar(100) not null,
  is_rmn boolean not null default false,
  created_at timestamp default sysdate
);
