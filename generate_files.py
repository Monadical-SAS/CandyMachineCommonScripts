import random 
import json
import os


# This should be the list returned by metaboss snapshot mints. (https://metaboss.rs/snapshot.html)
f = open('data.json')
participants = set(json.load(f))

# this is a list with division of the tokens, each element of the list must contain a 
# "name":  name for the token
# "seller_fee_basis_points": a value for seller fee
# "quantity": property that refers to the amount of tokens that are going to be selected 
# "uri": property that is an arweave link with the metadata what is going to be updated 
# "creators": list with values for each creator like: address, verify and share
# you should change this values for your tokens e.g.
token_division = [
	{	
		"name": "Token 12",
		"quantity": "12", 
		"uri": "https://arweave.net/KlQVZ2wiSuw1QT7RNeeLD903y5hNoipOOqC5NmOHPMY",
		"seller_fee_basis_points": 0,
		"creators": [
	    	{
				"address": "DfB7FF214VRCJxHgqAXx6uqaBGqMr8RoKHt3t5MFwgh1",
				"verified":True,
				"share":0,
			},
	        {
	            "address": "8xDHDA1pffkaNqYQs6p5KxdPNg9MpP72Fb6XJxjPrBE5",
	            "verified": False,
	            "share": 100
	        }
        ]
	}, 
	{	
		"name": "Token 10",
		"quantity": "10", 
		"uri": "https://arweave.net/XUwnnHggswzJ6ROgGSEx9fHVYEGjNGIGS2fZ3SyBjco",
		"seller_fee_basis_points": 0,
		"creators": [
	    	{
				"address": "DfB7FF214VRCJxHgqAXx6uqaBGqMr8RoKHt3t5MFwgh1",
				"verified":True,
				"share":0,
			},
	        {
	            "address": "8xDHDA1pffkaNqYQs6p5KxdPNg9MpP72Fb6XJxjPrBE5",
	            "verified": False,
	            "share": 100
	        }
        ]
	}
]	

for element in token_division:

	try:
		os.mkdir(str(element["quantity"]))
	except FileExistsError as e:
		print(f"directory already exists: {element['quantity']}")
	

	# here the quantity of winner are selected 
	selected_participants = random.sample(participants, int(element['quantity']))

	for index, participant in enumerate(selected_participants):
		participants.remove(participant)
		uptaded_data = {
		    "mint_account": participant,
		    "nft_data": {
			    "name": element['name'],
			    "symbol": "",
			    "uri": element["uri"],
			    "seller_fee_basis_points": element["seller_fee_basis_points"],
			    "creators": element["creators"]
			}
		}

		json_object = json.dumps(uptaded_data, indent = 4)

		# this will generate a folder with files for each token to update
		with open(f"{element['quantity']}/{index}selected.json", "w") as outfile:
		    outfile.write(json_object)

