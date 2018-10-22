##Vending Machine

Contact Christian.Thai3@gmail.com for comments and questions.

### What is Vending Machine?

Vending Machine is the software intended for a vending machine. This Software accepts two JSON files as input:

#### Inventory:
A JSON file specifying how the vending machine is stocked, with product names, quantities, 
and prices (in dollars) for each product.

#### Transactions:
A JSON file containing a list of purchase transactions, with the product name and value (in cents) of coins deposited.

## Installation
Vending Machine can be installed by downloading this repository as a ZIP file and extracting into a Windows System.
This installation is compatible with Python 3.x.

## Usage
In order to run this software, use src/vending.py <inventory file> <transaction file> with Python 3.x.

To run the tests, use the run_tests.py script with Python 3.x.

## Assumptions & Design
This Project was made with the following assumptions:
	* Valid JSON files will always be used as inputs.
	* The only valid values for coins were : 1, 5, 10, 25, 100.
	* The order that transactions occured followed the order demonstrated in the given transaction JSON file.
	* The vending machine always returns exact change.
	* The vending machine prioritizes bigger coins first when returning change.
	* The vending machine always delivers product correctly.

#### Design Choices

Python was used to develop this software, because it allows for clean and simple handling of JSON files.
JSON Files were decoded to allow for easier comparisons and to allow quick handling of transaction information.
By storing the values of the JSON Files in dictionaries (Hash Maps for Python) the software is able to look up 
information in O(1) time. Futhermore, iterating through the transaction list only needs to occur once in O(n) time.
A Helper function was created to calculate the change returned after a transaction. This function was created, 
because change needs to be calculated for every transaction that occured essentially. Thus cutting down on redundancy
in the code allowing for more readability.



This project was implemented using Python 3.6.3
