# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint

def read_portfolio(path):
	with open(path, 'rt') as file:
		rows = csv.reader(file)
		header = next(rows)
		portfolio = []
		for row in rows:
			name,num_shares,price = row
			num_shares = int(num_shares)
			price = float(price)
			portfolio.append({'name': name, 'shares':num_shares, 'price':price})
		return portfolio 


def read_prices(path):
	with open(path, 'rt') as file:
		rows = csv.reader(file)
		prices = {}
		for row in rows:
			if len(row) == 0:
				continue
			prices[row[0]] = float(row[1])
		return prices
  
def make_report(path_portfolio, path_prices):
    portfolios = read_portfolio(path_portfolio)
    prices = read_prices(path_prices)
    total = 0
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format("Name", "Shares", "Price", "Change"))
    print('{:->10s} {:->10s} {:->10s} {:->10s}'.format("", "", "", ""))
    for portfolio in portfolios:
        name = portfolio['name']
        shares = portfolio['shares']
        price = prices[portfolio['name']]
        change = price - portfolio['price']
        print(f'{name:>10s} {shares:>10d} {f'${price:0.2f}':>10s} {change:>10.2f}')
	
	  