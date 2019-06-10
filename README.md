# Ubiquiti Rocket M5 Signal Scraper
A Selenium-powered signal strength scraper module for the Rocket M5.

To use, you will need to get the ChromeDriver executable: [ChromeDriver.exe](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Then, in your Python environment, install Selenium:
```
python -m pip install selenium
```

And that's it!

# Example Usage

This script starts the scraper and then updates every second.
The first variable passed is the location of your driver.
```python
import signalscraper as scraper
import time


scraper.begin('C://chromedriver.exe', password='ground')

while True:
    print(scraper.fetch_signal())
    time.sleep(1)
```