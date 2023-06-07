import requests

user = "arshashiri"
response = requests.get(f"https://api.github.com/users/{user}/repos")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")
