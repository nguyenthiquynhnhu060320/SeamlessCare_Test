from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path='venv/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://portal.seamlesscare.ca/login')
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("oanhoanh@testing.com")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Hpc1000!")
driver.find_element(By.XPATH, "//ion-row[4]/ion-col/ion-button")

driver.quit()