import requests
from time import sleep

url= 'http://0.0.0.0:8000/ingestion'
payment = {"event_type":"payments", "data":[{"paymentId": "6cc91d611267beb0448764f9f5d18bf1", "installmentId": "ac1ca1ff51ce6fbe4d56a6f1d0c820cc", "paymentDate": "2021-03-09T00:00:00", "paymentValue": "30"}]}
originations= {"event_type":"originations", "data":[{"originationId": "0b14c011b0056b74ca9aab7d3e84ed64", "clientId": "3fcc43605a621c2f1eaf923292bb0363", "registerDate": "2021-06-28T00:00:00", "installments": [{"installmentId": "5a141c180b5b6b582925c1801b909190", "dueDate": "2021-11-10T00:00:00", "installmentValue": "31.59"}, {"installmentId": "b94da5e3a7b91bceaaf10ad1299e20f3", "dueDate": "2021-08-10T00:00:00", "installmentValue": "31.59"}, {"installmentId": "822092f2b3dfeae9c0d060ec4033c548", "dueDate": "2021-10-10T00:00:00", "installmentValue": "31.59"}, {"installmentId": "88d849a69ca95448cc3faaf2c8bdcdcd", "dueDate": "2021-09-10T00:00:00", "installmentValue": "31.59"}, {"installmentId": "2adddbb03742df87cde0660ab27c4b65", "dueDate": "2021-12-10T00:00:00", "installmentValue": "31.59"}]}]}
print(requests.post(url, json=payment).text)
print(requests.post(url, json=originations).text)

sleep(1)
url_2 = 'http://0.0.0.0:8000/get_table_payments'
print("## Get Payments ##")
print(requests.get('http://0.0.0.0:8000/get_table_payments').text)
print("## Get Originations ##")
print(requests.get('http://0.0.0.0:8000/get_table_originations').text)


