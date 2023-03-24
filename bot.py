recipient_address = '0x1234567890123456789012345678901234567890'
amount_to_withdraw = w3.toWei(1, 'ether')

# Set the sender's private key
sender_private_key = 'YOUR_PRIVATE_KEY'

# Create the transaction object
transaction = {
    'to': recipient_address,
    'value': amount_to_withdraw,
    'gas': 21000,
    'gasPrice': w3.toWei('5', 'gwei'),
    'nonce': w3.eth.getTransactionCount(w3.toChecksumAddress(sender_address)),
}

# Sign the transaction
signed_tx = w3.eth.account.sign_transaction(transaction, sender_private_key)
