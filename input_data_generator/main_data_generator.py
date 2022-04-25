import os
import numpy as np

from datetime import datetime
from dateutil.relativedelta import relativedelta

from data_generator import (
    generate_customers,
    generate_products,
    generate_transactions,
    generate_stores,
    generate_managers,
    generate_employees
)

if __name__ == "__main__":
    np.random.seed(seed=42)

    products_data = {
        "house": [
            "detergent",
            "kitchen roll",
            "bin liners",
            "shower gel",
            "scented candles",
            "fabric softener",
            "cling film",
            "aluminium foil",
            "toilet paper",
            "kitchen knife",
            "dishwasher tablets",
            "ice pack",
        ],
        "clothes": [
            "men's dark green trousers",
            "women's shoes",
            "jumper",
            "men's belt",
            "women's black socks",
            "men's striped socks",
            "men's trainers",
            "women's blouse",
            "women's red dress",
        ],
        "fruit_veg": [
            "avocado",
            "cherries",
            "scotch bonnets",
            "peppers",
            "broccoli",
            "potatoes",
            "grapes",
            "easy peeler",
            "mango",
            "lemon grass",
            "onions",
            "apples",
            "raspberries",
        ],
        "sweets": [
            "carrot cake",
            "salted caramel dark chocolate",
            "gummy bears",
            "kombucha",
            "ice cream",
            "irn bru",
        ],
        "food": [
            "steak",
            "chicken",
            "mince beef",
            "milk",
            "hummus",
            "activated charcoal croissant",
            "whole chicken",
            "tuna",
            "smoked salmon",
            "camembert",
            "pizza",
            "oats",
            "peanut butter",
            "almond milk",
            "lentil soup",
            "greek yoghurt",
            "parmesan",
            "coconut water",
            "chicken stock",
            "water",
        ],
        "bws": ["red wine", "gin", "cognac", "cigarettes"]
    }
    products_cats_frequency = (
        ["house"] * 15
        + ["clothes"] * 5
        + ["fruit_veg"] * 25
        + ["sweets"] * 20
        + ["food"] * 25
        + ["bws"] * 10
    )

    gen_id = "starter"
    output_location = f"./input_data/{gen_id}"
    os.makedirs(output_location, exist_ok=True)

    number_of_customers = 400
    number_of_stores = 10
    number_of_managers = 15
    number_of_employees = 50

    gen_customers = generate_customers(output_location, number_of_customers)
    get_stores = generate_stores(output_location, number_of_stores)
    get_managers = generate_managers(output_location, number_of_managers)
    generate_employees(output_location, number_of_employees, get_stores, get_managers)
    product_id_lookup = generate_products(output_location, products_data)

    end_date = datetime.today()
    delta = relativedelta(months=4)
    start_date = end_date - delta

    generate_transactions(
        output_location,
        gen_customers,
        products_data,
        product_id_lookup,
        products_cats_frequency,
        start_date,
        end_date,
    )