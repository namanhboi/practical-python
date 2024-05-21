# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(path):
    with open(path, 'rt') as file:
        rows = csv.reader(file)
        _ = next(rows)
        total = 0

        for row in rows:
            try:
                _, num, price = row
                total += int(num) * float(price)
            except ValueError:
                print("Missing value")
        return total
    


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data\\portfolio.csv"

print(f"Total cost: {portfolio_cost(filename)}")
