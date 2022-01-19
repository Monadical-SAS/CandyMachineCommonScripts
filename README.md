# Generator update files
You should take a look to [metaboss](https://metaboss.rs/overview.html) to understand some of the concepts used here like: snapshot mints and update data-all.

## Features

- generate folders with data for each token to update

## Input

Use [snapshot mints](https://metaboss.rs/snapshot.html#snapshot-mints) for getting list of tokens to update, replace data.json for path to your generated file.

## Token division structure 

You should follow this structure for each division of tokens

| Attribute | Description |
| ------ | ------ |
| name |  name for the token. |
|seller_fee_basis_points| a value for seller fee. |
|quantity| property that refers to the amount of tokens that are going to be selected. |
|uri| property that is an arweave link with the metadata what is going to be updated. |
|creators| list with values for each creator like: address, verify and share. |

```
{	
		"name": TOKEN_NAME,
		"quantity": QUANTITY_OF_SELECTED_TOKENS, 
		"uri": ARWEAVE_METADATA_LINK,
		"seller_fee_basis_points": SELLER_FEE_BASIS_POINTS,
		"creators": [
	    	{
				"address": YOUR_CANDY_MACHINE_ID,
				"verified":True,
				"share":0,
			},
	        {
	            "address": CREATOR_ADDRESS_ID,
	            "verified": False,
	            "share": 100
	        }
        ]
	}
```

The generated data follow this structure, check [here](https://metaboss.rs/update.html#update-data-all) for more information. 

```
{
    "mint_account": "CQNKXw1rw2eWwi812Exk4cKUjKuomZ2156STGRyXd2Mp",
    "nft_data":
    {
    "name": "FerrisCrab #4",
    "symbol": "FERRIS",
    "uri": "https://arweave.net/N36gZYJ6PEH8OE11i0MppIbPG4VXKV4iuQw1zaq3rls",
    "seller_fee_basis_points": 100,
    "creators": [
        {
            "address": "<YOUR_CANDY_MACHINE_ID>",
            "verified": true,
            "share": 0
        },
        {
            "address": "<KEYPAIR_CREATOR>",
            "verified": true,
            "share": 50
        },
        {
            "address": "42NevAWA6A8m9prDvZRUYReQmhNC3NtSZQNFUppPJDRB",
            "verified": false,
            "share": 50
        }
    }
}
```