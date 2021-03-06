USE ROLE SYSADMIN;

--CREATE DATABASE
CREATE DATABASE RAW_DATA;

--CREATE SCHEMA
USE DATABASE RAW_DATA;
CREATE SCHEMA SALES;

CREATE SCHEMA MARKETING;
CREATE SCHEMA FINANCE;

USE SCHEMA SALES;

--CREATE TABLE
CREATE OR REPLACE TABLE CUSTOMERS
(
  CUSTOMER_ID VARCHAR(10) NOT NULL PRIMARY KEY,
  LOYALTY_SCORE INT,
  NAME VARCHAR(30) NOT NULL,
  SURNAME VARCHAR(50) NOT NULL,
  DATE_OF_BIRTH DATE NOT NULL,
  POST_CODE VARCHAR(10) NOT NULL,
  EMAIL VARCHAR(50) NOT NULL UNIQUE,
  MOBILE_NUMBER INT NOT NULL
);

CREATE OR REPLACE TABLE STORES
(
  STORE_ID VARCHAR(10) NOT NULL PRIMARY KEY,
  STORE_ADDRESS VARCHAR(10) NOT NULL,
  RENT INT
);

CREATE OR REPLACE TABLE PRODUCTS
(
  PRODUCT_ID VARCHAR(10) NOT NULL PRIMARY KEY,
  DESCRIPTION VARCHAR(250) NOT NULL,
  CATEGORY VARCHAR(250) NOT NULL
);

CREATE TABLE EMPLOYEES
(
  EMPLOYEE_ID VARCHAR(10) NOT NULL PRIMARY KEY,
  STORE_ID VARCHAR(10) NOT NULL references stores(store_id),
  ROLE VARCHAR(100) NOT NULL,
  SALARY INT NOT NULL,
  MANAGER_ID VARCHAR(10) NOT NULL references managers(manager_id)
);

CREATE TABLE MANAGERS
(
  MANAGER_ID VARCHAR(10) NOT NULL PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL,
  SURNAME VARCHAR(50) NOT NULL,
  SALARY INT NOT NULL
);

CREATE TABLE TRANSACTIONS
(PAYLOAD VARIANT);

--CREATE FILE FORMAT
CREATE FILE FORMAT CSV_FACTS
TYPE = CSV
SKIP_HEADER = 1
FIELD_DELIMITER = ",";

CREATE FILE FORMAT JSON_TRANSACTIONS
TYPE = JSON;

SHOW FILE FORMATS;