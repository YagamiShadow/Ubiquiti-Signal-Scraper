import time
import signalscraper as scraper


scraper.begin('C://chromedriver.exe', password='ground')

while True:
    print(scraper.fetch_signal())
    time.sleep(1)
