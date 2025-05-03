--классная задачка
select name, sum(amount) as balance
from Users
JOIN Transactions on Users.account = Transactions.account
GROUP BY name
HAVING sum(amount) > 10000