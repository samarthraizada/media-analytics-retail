create table if not exists fact_pos_sales_wk (
  week_id integer not null,
  dma_id integer not null,
  retailer_id smallint not null,
  product_id integer not null,
  units_sold integer not null default 0,
  revenue_usd numeric(18,4) not null default 0,
  inventory_on_hand integer,
  promo_flag boolean not null default false,
  created_at timestamp default sysdate
);
