investment = LOAD '/user/cloudera/data/inv.txt' USING PigStorage(',') AS (time:int,location_num:chararray,location:chararray,industry_num:chararray,industry:chararray,num:int,money:double);
time = FILTER investment BY time >= 9701;
grouped = GROUP time BY location;
summed = FOREACH grouped GENERATE group, SUM(time.money), COUNT(time), SUM(time.money)/COUNT(time);
sorted = ORDER summed BY $3;
DUMP sorted;
