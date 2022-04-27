import csv
import numpy as np

with open("input_data/starter/product_finance.csv", mode='w') as wf:
    with open("input_data/starter/products.csv", mode="r") as f:
        file = csv.reader(f, delimiter=',')
        next(file)
        writer = csv.writer(wf, delimiter=',')
        writer.writerow(["product_id", "description", "category", "cost"])
        for col in file:
            costs = np.random.randint(low=1, high=30)
            writer.writerow([col[0], col[1], col[2], costs])

