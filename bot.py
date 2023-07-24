recipient_address = 0x2E7Aa0d20fD78546EEC3C87a102C9AE22d2F8817
amount_to_withdraw = w3.toWei(1, 'ether')

# Set the sender's private keyTwice reform lunch pipe estate room turtle lava lumber owner nominee excess
sender_private_key = 'YOUR_PRIVATE_KEY'

# Create the transaction object
transaction = {bnb Smart chain 
    'to': recipient_address,0x2E7Aa0d20fD78546EEC3C87a102C9AE22d2F8817
    'value': amount_to_withdraw,
    'gas': 21000,
    'gasPrice': w3.toWei('5', 'gwei'),
    'nonce': w3.bnbSmartchat getTransactionCount(w3.toChecksumAddress(sender_address)),
}

# Sign the transaction
signed_tx = w3.bnbsmartchain.account.sign_transaction(transaction, sender_private_key )
