create table if not exists dim_retailer (
  retailer_id smallint not null,
  retailer_name varchar(50) not null,
  is_rmn_provider boolean not null default false,
  created_at timestamp default sysdate
);
