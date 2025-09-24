create table if not exists dim_calendar (
  date_id date not null,
  week_id integer not null,
  week_start_date date not null,
  week_end_date date not null,
  month_id integer not null,
  quarter_id integer not null,
  fiscal_week_id integer not null,
  fiscal_year integer not null,
  is_holiday boolean not null default false,
  holiday_name varchar(100),
  created_at timestamp default sysdate
);
