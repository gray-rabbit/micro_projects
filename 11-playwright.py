from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.clien.net/service/board/sold")
    rows = page.query_selector_all("#div_content > div.list_content > div")
    rows = rows[:]
    for el in rows:
        t = el.query_selector(".list_title")
        t.click()
        time.sleep(5)
        page.go_back()
        time.sleep(5)
    time.sleep(10)
    browser.close()
