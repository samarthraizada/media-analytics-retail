create table if not exists dim_product (
  product_id integer not null,
  brand varchar(50) not null,
  line_name varchar(100) not null,
  variant varchar(100),
  upc varchar(32),
  asin varchar(20),
  size_ounces numeric(9,2),
  pack_count integer,
  created_at timestamp default sysdate
);
