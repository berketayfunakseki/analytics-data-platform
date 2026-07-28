create table if not exists raw_orders (
  order_id integer primary key,
  customer_id text not null,
  order_ts timestamp not null,
  country text not null,
  amount numeric(12,2) not null check (amount >= 0),
  status text not null check (status in ('paid','refunded'))
);
create index if not exists idx_raw_orders_order_ts on raw_orders(order_ts);
