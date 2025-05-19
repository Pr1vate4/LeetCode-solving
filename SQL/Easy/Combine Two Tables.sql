--приколья задачка
select firstName as firstName, lastName as lastName, address.city, state
from Person
left join Address on Person.personId = address.personId