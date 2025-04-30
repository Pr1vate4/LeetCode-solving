--прикольно освежать память, после прохождения курса
Select tweet_id
from Tweets
where LENGTH(content) > 15;