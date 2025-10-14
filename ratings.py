import requests
from bs4 import BeautifulSoup

session = requests.Session()
url = "http://t3ga.pythonanywhere.com/contact/"
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

form = soup.find("form")
action_url = form.get("/contact/")
inputs = form.find_all("input")

form_data = {
    "name": "Mark",
    "email": "mark@example.com",
    "message": "Hello from my Termux automation!"
}

submit_url = action_url if action_url.startswith("http") else f"https://your-portfolio.com{action_url}"
response = session.post(submit_url, data=form_data)

print("Form submitted. Status code:", response.status_code)
print("Response preview:", response.text[:500])
