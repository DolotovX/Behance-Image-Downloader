from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import requests
from urllib.parse import urlparse


project_url = input("🔗 Введите ссылку на проект Behance: ").strip()

try:
    project_slug = urlparse(project_url).path.strip("/").split("/")[-1].lower()
except:
    project_slug = "project"

ecommerce_keywords = ["e-commerce", "ecommerce", "commerce", "shop", "store", "market", "boutique", "retail"]
corporate_keywords = ["corporate"]
mobile_keywords = ["mobile", "app"]


if any(keyword in project_slug for keyword in corporate_keywords):
    target_folder = os.path.join("downloads", "corporate")
elif any(keyword in project_slug for keyword in ecommerce_keywords):
    target_folder = os.path.join("downloads", "ecommerce")
elif any(keyword in project_slug for keyword in mobile_keywords):
    target_folder = os.path.join("downloads", "mobile")
else:
    target_folder = "downloads/corporate"

os.makedirs(target_folder, exist_ok=True)

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get(project_url)
time.sleep(10)

imgs = driver.find_elements(By.TAG_NAME, "img")
print(f"🔍 Найдено {len(imgs)} изображений")

downloaded = set()
count = 0

def get_high_res_from_srcset(srcset):
    candidates = []
    for part in srcset.split(","):
        url_part = part.strip().split(" ")[0]
        if "mir-s3-cdn-cf.behance.net" in url_part and "/project_modules/" in url_part:
            candidates.append(url_part)
    return candidates[-1] if candidates else None

for img in imgs:
    src = img.get_attribute("src")
    srcset = img.get_attribute("srcset")

    best_url = None

    if srcset:
        best_url = get_high_res_from_srcset(srcset)
    elif src and "mir-s3-cdn-cf.behance.net" in src and "/project_modules/" in src:
        best_url = src

    if best_url and best_url not in downloaded:
        try:
            ext = best_url.split(".")[-1].split("?")[0]
            filename = f"{target_folder}/{project_slug}_image_{count}.{ext}"
            r = requests.get(best_url)
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"✔ Скачано: {filename}")
            downloaded.add(best_url)
            count += 1
        except Exception as e:
            print(f"⚠ Ошибка при скачивании {best_url}: {e}")

driver.quit()
print(f"\n✅ Скачано {count} изображений в папку '{target_folder}'!")
