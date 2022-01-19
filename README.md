# Generator update files
You should take a look to [metaboss](https://metaboss.rs/overview.html) to understand some of the concepts used here like: snapshot mints and update data-all.

## Features

- generate folders with data for each token to update

## Input

Use [snapshot mints](https://metaboss.rs/snapshot.html#snapshot-mints) for getting list of tokens to update, replace data.json for path to your generated file.

## Config file structure 

You should add to this array as many divisions as you want. The sum of quantity can not be greater than your candy machine quantity. 
Follow this structure for each division of tokens

| Attribute | Description |
| ------ | ------ |
| name |  name for the token. |
|seller_fee_basis_points| a value for seller fee. |
|quantity| property that refers to the amount of tokens that are going to be selected. |
|uri| property that is an arweave link with the metadata what is going to be updated. |
|creators| list with values for each creator like: address, verify and share. |

```
{	
		"name": NFT_NAME,
		"quantity": QUANTITY_OF_SELECTED_NFTS, 
		"uri": ARWEAVE_METADATA_LINK,
		"seller_fee_basis_points": SELLER_FEE_BASIS_POINTS,
		"creators": [
	    	{
				"address": YOUR_CANDY_MACHINE_CREATOR_ADDRESS,
				"verified":True,
				"share":0,
			},
	        {
	            "address": CREATOR_ADDRESS_ADDRESS,
	            "verified": False,
	            "share": 100
	        }
        ]
	}
```

The generated data follow this structure, check [here](https://metaboss.rs/update.html#update-data-all) for more information. 

```
{
    "mint_account": "MINT_ADDRESS",
    "nft_data":
    {
        "name": NFT_NAME,
        "symbol": "",
        "uri": ARWEAVE_METADATA_LINK,
        "seller_fee_basis_points": SELLER_FEE_BASIS_POINTS,
        "creators": [
            {
                "address": "<YOUR_CANDY_MACHINE_CREATOR_ADDRESS>",
                "verified": true,
                "share": 0
            },
            {
                "address": "<CREATOR_ADDRESS>",
                "verified": true,
                "share": 100
            },
        ]
    }
}
```