from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import time, datetime, timedelta
from selenium.webdriver.chrome.options import Options
import time

class TestRentCar():
    def setup_method(self, method):
        options = Options()
        options.add_argument('--headless=new')

        # Use headless mode
        self.driver = webdriver.Chrome(options=options)

        # Use normal mode
        # self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 20)

        # Fungsi input start date & end date
        today = datetime.today()
        future_date_start = today + timedelta(days=2)
        future_date_end = today + timedelta(days=5)
        future_date_formatted_start = f"{future_date_start.day}-{future_date_start.month}-{future_date_start.year}"
        future_date_formatted_end = f"{future_date_end.day}-{future_date_end.month}-{future_date_end.year}"
        self.vars['css_selector_start'] = f"[data-testid='date-cell-{future_date_formatted_start}']"
        self.vars['css_selector_end'] = f"[data-testid='date-cell-{future_date_formatted_end}']"

    def teardown_method(self, method):
        self.driver.quit()

    def test_rent(self):

        # Access url
        self.driver.get("https://www.traveloka.com/id-id")

        # Select menu Rental Mobil
        self.driver.find_element(By.CSS_SELECTOR, ".r-kdyh1x[href='/id-id/car-rental']").click()

        # Search - Input location
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Cari kota atau wilayah']"))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Cari kota atau wilayah']"))).send_keys("jakarta")
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Jakarta']"))).click()

        # Search - Input Date & Time Start
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='rental-search-form-date-input-start']").click()
        time.sleep(5)
        modal1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".r-1d2f490.r-14lw9ot > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n")))
        time.sleep(5)
        modal1.find_element(By.CSS_SELECTOR, self.vars['css_selector_start']).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='rental-search-form-time-input-start']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".r-xyw6el div:nth-of-type(10)").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".r-xyw6el.r-18u37iz > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1)").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".r-173mn98.css-18t94o4").click()
        time.sleep(5)

        # Search - Input Date & Time End
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='rental-search-form-date-input-end']").click()
        time.sleep(5)
        modal2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.r-zchlnj.r-1udh08x')))
        time.sleep(5)
        modal2.find_element(By.CSS_SELECTOR, self.vars['css_selector_end']).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='rental-search-form-time-input-end']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".r-xyw6el div:nth-of-type(12)").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".r-xyw6el.r-18u37iz > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1)").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".r-173mn98.css-18t94o4").click()
        time.sleep(5)

        # Click Button Search
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='rental-search-form-cta']").click()
        time.sleep(15)

        # Select Car
        self.driver.find_element(By.CSS_SELECTOR, ".r-1q2s4rl > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(3) > div:nth-of-type(3) > div:nth-of-type(1)").click()
        time.sleep(5)

        # Select Provider
        self.driver.find_element(By.CSS_SELECTOR, ".r-169s5xo.r-1kihuf0 div:nth-of-type(2) > .css-1dbjc4n > .css-1dbjc4n > .css-18t94o4").click()
        time.sleep(5)

        # Select Pick-up Location in “Rental Office”
        self.driver.find_element(By.CSS_SELECTOR, ".r-136ojw6.r-14lw9ot div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".r-136ojw6.r-14lw9ot > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n > .r-1loqt21").click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[tabindex="0"]').click()
        time.sleep(5)

        # Select Drop-off Location in “Other Location”
        self.driver.find_element(By.CSS_SELECTOR, ".r-184en5c.r-kdyh1x div:nth-of-type(5) [aria-labelledby='0.257c17eb34f13']").click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Cari lokasi atau alamat"]'))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Cari lokasi atau alamat"]'))).send_keys("jakarta barat")
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='West Jakarta']"))).click()
        time.sleep(5)

        # Notes opsional
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="Catatan tambahan (opsional)"]'))).send_keys("Ini catatan")
        time.sleep(5)

        # Click continue
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-173mn98'))).send_keys("Ini catatan")
        time.sleep(5)

        # Input full name
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="contact-detail"] [aria-labelledby="name.full"]'))).send_keys("Nur Ahmad F")
        time.sleep(5)

        # Input no handphone
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='contact-detail'] [aria-label='Phone Number']"))).send_keys("085155311257")
        time.sleep(5)

        # Input email
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-labelledby='emailAddress']"))).send_keys("nurahmadf09@gmail.com")
        time.sleep(5)

        # Save contact detail
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='contact-detail'] .css-18t94o4"))).click()
        time.sleep(5)

        # Input detail driver
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-30o5oe"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[value='MR']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'aria-labelledby="name.full"'))).send_keys("Nur Ahmad F")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'aria-label="Phone Number"'))).send_keys("085155311257")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-mhe3cw .css-18t94o4'))).click()
        time.sleep(5)

        # Continue next step
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'placeholder="Plat ganjil atau genap, charger mobil, kursi bayi dll."'))).send_keys("Ini notes")
        time.sleep(5)

        # Check all rental requirements
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-1wtj0ep.r-14lw9ot'))).click()
        time.sleep(5)
        # modal
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-633pao.r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-150rngu div:nth-of-type(3) > .r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-150rngu div:nth-of-type(4) > .r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-150rngu div:nth-of-type(5) > .r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-150rngu div:nth-of-type(6) > .r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-150rngu div:nth-of-type(7) > .r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.r-150rngu div:nth-of-type(8) > .r-1awozwy'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[.='SimpanSimpan']"))).click()
        time.sleep(5)

        # Continue next step
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-1dbjc4n r-14l27qf']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[.='LanjutkanLanjutkan']"))).click()
        time.sleep(5)

        # Select payment
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='paymentScopeOption-Mandiri Virtual Account']"))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'data-testid="paymentPayButton"'))).click()
        time.sleep(5)