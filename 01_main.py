import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def display_users(data):
    print("Users and their connections\n")
    for user in data['users']:
        print(f"{user['name']} is friends with: {user['friends']} and liked pages are {user['liked_pages']}")

    print("Pages Information")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

data = load_data("Data.json")
display_users(data)