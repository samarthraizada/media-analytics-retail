create table if not exists fact_media_spend_wk (
  week_id integer not null,
  dma_id integer not null,
  channel_id smallint not null,
  retailer_id smallint,
  impressions bigint not null default 0,
  reach_persons bigint,
  frequency numeric(6,2),
  viewability_rate numeric(5,2),
  clicks bigint,
  video_completes bigint,
  cost_usd numeric(18,4) not null default 0,
  created_at timestamp default sysdate
);
