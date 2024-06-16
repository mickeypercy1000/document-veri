import requests
import json
import os
from decouple import config

# Create your views here.
def wingipay_name_check(phone, network):
    print("inside function")
    url = "https://test.wingipay.com/client/mobile-money/namecheck/" 
    payload = json.dumps({
        "apikey": config("api_key"),
        "phone": phone,
        "network": network
    })
    print(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    trimmed_response = (json.loads(response.text.replace('\"', '"')))
    return trimmed_response


def wingipayDebitCustomer(transaction):

    url = "https://test.wingipay.com/client/mobile-money/debit_call/" 
    payload = json.dumps({
        "apikey": config("api_key"),
        "external_transaction_ref": str(transaction.id),
        "source_phone": transaction.source_data["source_phone"],
        "source_name": transaction.source_data["source_name"],
        "network": transaction.source_data["network"],
        "amount": float(transaction.source_data["amount"]),
        "note": transaction.source_data["note"],
        "debit_callback_url": "https://webhook.site/292c889a-1f1d-47f8-a4d2-3ebc5c2fdc41"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    responseData = json.loads(response.text.replace('\"', '"'))
    return responseData