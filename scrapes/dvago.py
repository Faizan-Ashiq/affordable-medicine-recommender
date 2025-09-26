from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv, time

# ---------------- CONFIG ----------------
BASE_URL = "https://www.dvago.pk/cat/medicine?page="
TOTAL_PAGES = 179
BATCH_SIZE = 20                 # restart browser every 20 pages
OUTPUT_FILE = "dvago_medicines.csv"

# ---------- Setup Driver ----------
def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")      # New headless mode (Chrome 109+)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# ---------- Scrape One Page ----------
def scrape_page(driver, page_number):
    url = f"{BASE_URL}{page_number}"
    print(f"Scraping page: {page_number}")
    driver.get(url)

    # Wait for product cards to appear
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ProductCard_productContent__HFMgl"))
    )

    rows = []
    products = driver.find_elements(By.CSS_SELECTOR, ".ProductCard_productContent__HFMgl")

    for p in products:
        try:
            # Medicine name & link
            name_tag = p.find_element(By.CSS_SELECTOR, "p a")
            name = name_tag.text.strip()
            link = name_tag.get_attribute("href")

            # Discounted price
            try:
                market_price = p.find_element(By.CSS_SELECTOR, "[class*='ProductCard_salePrice']").text.strip()
            except:
                market_price = ""

            # Original price
            try:
                original_price = p.find_element(By.CSS_SELECTOR, "[class*='ProductCard_regularPrice']").text.strip()
            except:
                original_price = ""

            rows.append([name, market_price, original_price, link])
        except Exception as e:
            print("⚠️ Skipping product:", e)
            continue

    return rows

# ---------- Main Scraping ----------
def main():
    # Create CSV with header
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Market Price", "Original Price", "Detail URL"])

    # Batch scraping to avoid long sessions
    for start in range(1, TOTAL_PAGES + 1, BATCH_SIZE):
        driver = start_driver()
        for page in range(start, min(start + BATCH_SIZE, TOTAL_PAGES + 1)):
            try:
                rows = scrape_page(driver, page)
                with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
                    csv.writer(f).writerows(rows)
            except Exception as e:
                print(f"⚠️ Error on page {page}: {e}")
                continue
        driver.quit()
        time.sleep(3)  # small pause between batches

    print(f"✅ Scraping completed. Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
