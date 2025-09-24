create table if not exists dim_dma (
  dma_id integer not null,
  dma_name varchar(100) not null,
  state_list varchar(200),
  nielsen_rank integer,
  created_at timestamp default sysdate
);
