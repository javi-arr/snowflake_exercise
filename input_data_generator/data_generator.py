import csv
import json
import math
import os
import random
from datetime import timedelta

import numpy as np

list_names = ['Kristine', 'Barbara', 'David', 'Amy', 'Brenda', 'Michael', 'Keith', 'Amy', 'Mr.', 'Marcus',
                       'Justin', 'Megan', 'Patricia', 'Mary', 'Jennifer', 'Robin', 'Lisa', 'Karen', 'Jeffrey',
                       'Dr.', 'Daniel', 'Rachel', 'Michael', 'Edward', 'Amanda', 'Kaitlyn', 'Donald', 'James',
                       'Jessica', 'Anthony', 'Audrey', 'Dana', 'Tiffany', 'Keith', 'Brian', 'Michael', 'Amanda',
                       'Christopher', 'Lisa', 'Casey', 'Justin', 'Rachel', 'Danielle', 'Michele', 'Kyle',
                       'William', 'Kyle', 'James', 'Sherry', 'Bonnie']
list_surnames = ['Miller', 'Mitchell', 'Schwartz', 'Li', 'Castro', 'Fleming', 'Patterson', 'Morton',
                          'Randall', 'Ramirez', 'Lopez', 'Morales', 'Thompson', 'Miles', 'Bailey', 'Baldwin',
                          'Velasquez', 'Hernandez', 'Barnes', 'Amber', 'Mckee', 'Williams', 'Morris', 'Chang',
                          'Walker', 'Frazier', 'Carpenter', 'Davis', 'Barnes', 'Snyder', 'Carlson', 'Carrillo',
                          'Oconnor', 'Beltran', 'Hall', 'Obrien', 'Spence', 'Padilla', 'Rodriguez', 'Berry',
                          'Stephens', 'Thomas', 'Nguyen', 'Harris', 'Wolfe', 'Vincent', 'Tran', 'Long', 'Paul',
                          'Miller']
roles = ["Store clerk", "Cleaner", "Cashier", "Bagger", "Meat cutters"]

class Customer(object):
    def __init__(self,
                 customer_id,
                 loyalty_score,
                 customer_name,
                 customer_surname,
                 customer_dob,
                 customer_postcode,
                 customer_email,
                 customer_phone_number):
        self.customer_id = customer_id
        self.value_score = loyalty_score
        self.name = customer_name
        self.surname = customer_surname
        self.dob = customer_dob
        self.post_code = customer_postcode
        self.email = customer_email
        self.phone_number = customer_phone_number

class Stores(object):
    def __init__(self,
                 store_id,
                 store_address,
                 rent):
        self.store_id = store_id
        self.store_address = store_address
        self.rent = rent


class Managers(object):
    def __init__(self,
                 manager_id,
                 manager_name,
                 manager_surname,
                 salary):
        self.manager_id = manager_id
        self.manager_name = manager_name
        self.manager_surname = manager_surname
        self.salary = salary


class Employees(object):
    def __init__(self,
                 employee_id,
                 store_id,
                 role,
                 salary,
                 manager_id):
        self.employee_id = employee_id
        self.store_id = store_id
        self.role = role
        self.salary = salary
        self.manager_id = manager_id


def generate_customers(
    output_location_root, number_of_customers, return_data=True
):
    customers = []
    post_codes = [
        "E1", "E2", "WC1", "WC2", "N1", "N2", "NW1", "NW2", "SE1", "SE2", "SW1", "SW2", "W1", "W2"
    ]
    range_ages = np.arange(0, 32850)
    start_date = np.datetime64('1930-01-01')
    with open(
        f"{output_location_root}/customers.csv", mode="w"
    ) as customers_file:
        csv_writer = csv.writer(
            customers_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow(["customer_id", "loyalty_score", "name", "surname", "Date of Birht", "post_code", "email", "mobile_number"])
        for cid in range(1, number_of_customers + 1):
            score = np.random.randint(low=1, high=11)
            customer_id = f"C{cid}"
            customer_name = np.random.choice(list_names)
            customer_surname = np.random.choice(list_surnames)
            customer_dob = start_date + np.random.choice(range_ages)
            customer_postcode = np.random.choice(post_codes)
            customer_email = f"{customer_name}{customer_surname}@snowflakeexercise.com"
            customer_phone_number = np.random.randint(low=7000000000, high = 8000000000)
            csv_writer.writerow([customer_id,
                                 score,
                                 customer_name,
                                 customer_surname,
                                 customer_dob,
                                 customer_postcode,
                                 customer_email,
                                 customer_phone_number])
            if return_data:
                customers.append(Customer(customer_id,
                                          score,
                                          customer_name,
                                          customer_surname,
                                          customer_dob,
                                          customer_postcode,
                                          customer_email,
                                          customer_phone_number))
    return customers if return_data else None


def generate_stores(output_location_root, number_of_stores, return_data=True):
    stores = []
    post_codes = [
        "E1", "E2", "WC1", "WC2", "N1", "N2", "NW1", "NW2", "SE1", "SE2", "SW1", "SW2", "W1", "W2"
    ]
    with open(
        f"{output_location_root}/stores.csv", mode="w"
    ) as stores_file:
        csv_writer = csv.writer(
            stores_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow(
            ["store_id", "store_address", "rent"]
        )
        for sid in range(1, number_of_stores + 1):
            store_id = f"S{sid}"
            store_address = np.random.choice(post_codes)
            store_rent = np.random.randint(low=500, high=2000)
            csv_writer.writerow([store_id, store_address, store_rent])
            if return_data:
                stores.append(Stores(store_id, store_address, store_rent))
    return stores if return_data else None


def generate_managers(output_location_root, number_of_managers, return_data=True):
    managers = []
    with open(
            f"{output_location_root}/managers.csv", mode="w"
    ) as managers_file:
        csv_writer = csv.writer(
            managers_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow(
            ["manager_id", "name", "surname", "salary"]
        )
        for mid in range(1,number_of_managers + 1):
            manager_id = f"M{mid}"
            manager_name = np.random.choice(list_names)
            manager_surname = np.random.choice(list_surnames)
            salary = np.random.randint(low=2000, high=4000)
            csv_writer.writerow([manager_id, manager_name, manager_surname, salary])
            if return_data:
                managers.append(Managers(manager_id, manager_name, manager_surname, salary))
    return managers if return_data else None


def generate_employees(output_location_root, number_of_employees, stores, managers, return_data=True):
    employees = []
    stores_ids = []
    managers_ids = []
    for store in stores:
        stores_ids.append(store.store_id)
    for manager in managers:
        managers_ids.append(manager.manager_id)
    with open(
            f"{output_location_root}/employees.csv", mode="w"
    ) as employees_file:
        csv_writer = csv.writer(
            employees_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow(
            ["employee_id", "store_id", "role", "salary", "manager_id"]
        )
        for eid in range(1, number_of_employees+1):
            employee_id = f"E{eid}"
            store_id = np.random.choice(stores_ids)
            role = np.random.choice(roles)
            salary = np.random.randint(low=1000, high=2500)
            manager_id = np.random.choice(managers_ids)
            csv_writer.writerow([employee_id, store_id, role, salary, manager_id])
            if return_data:
                employees.append(Employees(employee_id, store_id, role, salary, manager_id))
    return employees if return_data else None


def generate_products(output_location_root, products_to_generate):
    product_count_digits = int(
        math.log10(len(sum(products_to_generate.values(), []))) + 1
    )

    product_id_lookup = {k: {} for k, v in products_to_generate.items()}
    with open(
        f"{output_location_root}/products.csv", mode="w"
    ) as products_file:
        csv_writer = csv.writer(
            products_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow(
            ["product_id", "product_description", "product_category"]
        )
        item_index = 1
        for category in products_to_generate:
            for item in products_to_generate[category]:
                product_id = f"P{str(item_index).zfill(product_count_digits)}"
                csv_writer.writerow([product_id, item, category])
                product_id_lookup[category][item] = product_id
                item_index += 1
    return product_id_lookup


def generate_transactions(
    output_location_root,
    customers,
    products,
    product_id_lookup,
    products_cats_frequency,
    start_datetime,
    end_datetime,
):
    open_files = open_transaction_sinks(
        output_location_root, start_datetime, end_datetime
    )
    product_cats_count = len(products.keys())
    num_days = (end_datetime - start_datetime).days
    all_days = [
        start_datetime + timedelta(days=d) for d in range(0, num_days + 1)
    ]
    customer_frequency_type = [
        int(num_days / 14),
        int(num_days / 10),
        int(num_days / 7),
        int(num_days / 5),
        int(num_days / 4),
        int(num_days / 3),
    ]

    for customer in customers:
        num_transaction_days = random.choice(customer_frequency_type)
        num_cats = random.randint(1, product_cats_count)
        customer_transaction_days = sorted(
            random.sample(all_days, num_transaction_days)
        )
        cats = random.sample(products_cats_frequency, num_cats)
        for day in customer_transaction_days:
            transaction = {
                "customer_id": customer.customer_id,
                "basket": generate_basket(products, product_id_lookup, cats),
                "date_of_purchase": str(
                    day + timedelta(minutes=random.randint(168, 1439))
                ),
            }
            open_files[to_canonical_date_str(day)].write(
                json.dumps(transaction) + "\n"
            )

    for f in open_files.values():
        f.close()


def to_canonical_date_str(date_to_transform):
    return date_to_transform.strftime("%Y-%m-%d")


def open_transaction_sinks(output_location_root, start_datetime, end_datetime):
    root_transactions_dir = f"{output_location_root}/transactions/"
    open_files = {}
    days_to_generate = (end_datetime - start_datetime).days
    for next_day_offset in range(0, days_to_generate + 1):
        next_day = to_canonical_date_str(
            start_datetime + timedelta(days=next_day_offset)
        )
        day_directory = f"{root_transactions_dir}/d={next_day}"
        os.makedirs(day_directory, exist_ok=True)
        open_files[next_day] = open(
            f"{day_directory}/transactions.json", mode="w"
        )
    return open_files


def generate_basket(products, product_id_lookup, cats):
    num_items_in_basket = random.randint(1, 3)
    basket = []
    product_category = random.choice(cats)
    for item in [
        random.choice(products[product_category])
        for _ in range(0, num_items_in_basket)
    ]:
        product_id = product_id_lookup[product_category][item]
        basket.append(
            {"product_id": product_id, "price": random.randint(1, 100)}
        )
    return basket