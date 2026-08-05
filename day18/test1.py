
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.ambitionbox.com/list-of-companies?page=1"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

time.sleep(5)

# Auto scroll until all cards are loaded
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        break  # no more content loaded
    last_height = new_height

# Now extract page source
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

# Selector for company cards
company_cards = soup.select('div[data-widget="CompanyListCard"]')

print("Found Cards:", len(company_cards))

data = []

for card in company_cards:
    name = card.select_one("h2")
    rating = card.select_one("span[class*='rating']")
    details = card.select_one("p")  # update if needed later

    data.append({
        "Company Name": name.get_text(strip=True) if name else None,
        "Rating": rating.get_text(strip=True) if rating else None,
        "Industry / Details": details.get_text(strip=True) if details else None,
    })

df = pd.DataFrame(data)
print(df)
df.to_csv("ambitionbox_scraped.csv", index=False)
