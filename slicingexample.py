import json

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[10:15])

my_friend = {
    "Name":"John",
    "Phone":"1800111",
    "Address":"21 Pilot St",
    "Friends":["Bob","Bert","Bill","Ferdinand"]
}

with open("JSON_example.json", "wt") as file_handle:
    json_data = json.dumps(my_friend)
    file_handle.write(json_data)
