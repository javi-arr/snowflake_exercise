USE ROLE SYSADMIN;

--CREATE A NEW WAREHOUSE FOR ANALYTICS
CREATE WAREHOUSE ANALYTICS_WH
WAREHOUSE_SIZE = SMALL;

--RESIZE WAREHOUSE
ALTER WAREHOUSE SET
WAREHOUSE_SIZE = XSMALL;

USE WAREHOUSE ANALYTICS_WH;
USE DATABASE RAW_DATA;
USE SCHEMA SALES;

--GRANT PRIVILEDGES TO ROLE MRK_ROLE
--https://docs.snowflake.com/en/user-guide/security-access-control-overview.html

GRANT USAGE ON WAREHOUSE ANALYTICS_WH
TO ROLE MRK_ROLE;

GRANT USAGE ON DATABASE RAW_DATA
TO ROLE MRK_ROLE;

GRANT USAGE ON SCHEMA SALES
TO ROLE MRK_ROLE;

GRANT SELECT ON ALL TABLES IN SCHEMA RAW_DATA.SALES
TO ROLE MRK_ROLE;

GRANT USAGE ON SCHEMA MARKETING
TO ROLE MRK_ROLE;

GRANT CREATE TABLE ON SCHEMA MARKETING
TO ROLE MRK_ROLE;

GRANT CREATE VIEW ON SCHEMA MARKETING
TO ROLE MRK_ROLE;

GRANT CREATE SEQUENCE ON SCHEMA MARKETING
TO ROLE MRK_ROLE;

--GRANT PRIVILEGES FINANCE MANAGER
CREATE SCHEMA FINANCES;

GRANT USAGE ON WAREHOUSE ANALYTICS_WH
TO ROLE FNC_ROLE;

GRANT USAGE ON DATABASE RAW_DATA
TO ROLE FNC_ROLE;

GRANT USAGE ON SCHEMA SALES
TO ROLE FNC_ROLE;

GRANT SELECT ON ALL TABLES IN SCHEMA RAW_DATA.SALES
TO ROLE FNC_ROLE;

GRANT USAGE ON SCHEMA FINANCES
TO ROLE FNC_ROLE;

GRANT CREATE TABLE ON SCHEMA FINANCES
TO ROLE MRK_ROLE;

GRANT CREATE VIEW ON SCHEMA FINANCES
TO ROLE FNC_ROLE;

GRANT CREATE SEQUENCE ON SCHEMA FINANCES
TO ROLE FNC_ROLE;
