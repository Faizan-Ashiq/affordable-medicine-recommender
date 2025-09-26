from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv, string, time

# Setup driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

base_url = 'https://dawaai.pk/all-medicines/'
data = []
try:
    for letter in string.ascii_lowercase[string.ascii_lowercase.index('a'):string.ascii_lowercase.index('p')+1]:

        # a to z
        print(f"Scraping letter: {letter}")
        driver.get(f"{base_url}{letter}")
        time.sleep(3)  # allow page to fully load

        # ✅ Inspect dawaai.pk with DevTools and update selectors if needed
        products = driver.find_elements(By.CSS_SELECTOR, ".card-body")  # Example class

        for p in products:
            try:
                name_tag = p.find_element(By.CSS_SELECTOR, "h2 a")
                name = name_tag.text
                link = name_tag.get_attribute("href")
                ps    = p.find_elements(By.CSS_SELECTOR, ".card-body p")
                type_ = ps[0].text if len(ps) > 0 else ""
                size  = ps[1].text if len(ps) > 1 else ""
                price = p.find_element(By.CSS_SELECTOR, ".card-body h4").text
                data.append([name, type_, size, price, link])
            except Exception as e:
                print("Skipping a product:", e)
                continue
except:
    driver.quit()

# Save CSV
with open("dawaai_medicines1.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Type", "Size", "Price","Detail_url"])
    writer.writerows(data)

print("✅ Scraping completed. Data saved to dawaai_medicines.csv")
