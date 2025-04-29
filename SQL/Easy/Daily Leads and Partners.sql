--обычная легкая задачка
select date_id, make_name, count(distinct(lead_id)) AS unique_leads, count(distinct(partner_id)) as unique_partners
from DailySales
GROUP BY 1,2