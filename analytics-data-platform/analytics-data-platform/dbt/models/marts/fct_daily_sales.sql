with orders as (
    select * from {{ ref('stg_orders') }}
)
select
    order_date,
    country,
    count(*) as orders,
    count(distinct customer_id) as customers,
    sum(net_amount) as net_revenue,
    avg(amount) as average_order_value
from orders
group by 1, 2
