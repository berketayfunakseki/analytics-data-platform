select
    cast(order_id as integer) as order_id,
    cast(customer_id as text) as customer_id,
    cast(order_ts as timestamp) as order_ts,
    cast(order_ts as date) as order_date,
    upper(country) as country,
    cast(amount as numeric(12,2)) as amount,
    lower(status) as status,
    case when lower(status) = 'refunded' then -cast(amount as numeric(12,2))
         else cast(amount as numeric(12,2)) end as net_amount
from raw_orders
