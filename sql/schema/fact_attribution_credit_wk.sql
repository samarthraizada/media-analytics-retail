create table if not exists fact_attribution_credit_wk (
  week_id integer not null,
  dma_id integer not null,
  channel_id smallint not null,
  credited_units numeric(18,6) not null default 0,
  credited_value_usd numeric(18,6) not null default 0,
  model_version varchar(20) not null,
  last_touch_share numeric(6,4),
  first_touch_share numeric(6,4),
  assist_share numeric(6,4),
  vt_eligible boolean not null default false,
  created_at timestamp default sysdate
);
