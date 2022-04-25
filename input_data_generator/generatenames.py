import csv

with open("random_names_fossbytes.csv", newline='') as f:
    file = csv.reader(f, delimiter=' ')
    names = []
    surnames = []
    for col in file:
        names.append(col[0])
        surnames.append(col[1])
    print(surnames)