USE ROLE ACCOUNTADMIN;
USE SCHEMA SNOWFLAKE.ACCOUNT_USAGE;


-- USER FAILED LOGGINGS AND TIME BETWEEN TRIALS
select user_name,
       count(*) as failed_logins,
       avg(seconds_between_login_attempts) as average_seconds_between_login_attempts
from (
      select user_name,
             timediff(seconds, event_timestamp, lead(event_timestamp)
                 over(partition by user_name order by event_timestamp)) as seconds_between_login_attempts
      from login_history
      where event_timestamp > date_trunc(month, current_date)
      and is_success = 'NO'
     )
group by 1
order by 3;

--WAREHOSE CREDIT USAGE
select warehouse_name,
       sum(credits_used) as total_credits_used
from warehouse_metering_history
where start_time >= date_trunc(month, current_date)
group by 1
order by 2 desc;