import requests

target = input("enter your target website: ")

with open("domainlist.txt", "r") as domain_list:
    for word in domain_list:
        word = word.strip()
        url = "https://" + word + "." + target
        try:
            response = requests.get(url)
            if response:
                print(f"found subdomain adress --> {url}")
        except requests.exceptions.ConnectionError:
            pass
