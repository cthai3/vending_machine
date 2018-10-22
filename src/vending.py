#!/usr/bin/env python

import json
from pathlib import Path
import sys
import io
import os.path

#Helper function to determine amount of change needed for a transaction
def makeChange(amount):
	change = []
	while (amount > 0):
		if(amount >= 100):
			change.append(100)
			amount -= 100
		elif(amount >= 25):
			change.append(25)
			amount -= 25
		elif(amount >= 10):
			change.append(10)
			amount -= 10
		elif(amount >= 5):
			change.append(5)
			amount -= 5
		elif(amount >= 1):
			change.append(1)
			amount -= 1
	return change;


inventory_json = open(sys.argv[1])
transactions_json = open(sys.argv[2])

# Parse Inventory & Create Mapping
parsed_inventory = json.load(inventory_json)

#Parse Transactions 
parsed_transactions = json.load(transactions_json)

#Output List
result = [] 

#Iterating through the transactions to create the history.
for transaction in parsed_transactions: 
	name = transaction['name']
	funds = sum(transaction['funds'])

	#Check the inventory validity
	itemInfo = parsed_inventory[name]
	itemQuantity = itemInfo['quantity']
	itemPrice = (itemInfo['price']*100)
	productDelivered = False
	change = transaction['funds']
	difference = 0

	#Check to see if the item is in stock
	if (itemQuantity > 0):
		#Check to see if funds are available
		if (funds >= itemPrice):
			difference = (funds - itemPrice)
			change = makeChange(difference)
			itemInfo['quantity'] = (itemQuantity-1)
			productDelivered = True

	resultDict = {'product_delivered' : productDelivered, 'change': change}
	result.append(resultDict)
jsonResult = json.dumps(result)

#Finds the path of the input files
path = os.path.dirname(sys.argv[1])
completeName = os.path.join(path, 'output.json')

print(jsonResult)
#Saves Output Json file to the same directory as Input files
with open(completeName, 'w') as outfile:
	outfile.write(jsonResult)
