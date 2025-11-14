import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.wikipedia.org")

# try:
#    print(f"Page Title : {driver.title}")
#    search_input = driver.find_element(By.NAME, "searchinput")
#    print(search_input)
   
   
   
# except Exception as e:
#    print("Error : ", e)
   
# finally:
#    time.sleep(3)
#    driver.quit()


#---------------------------------------------
# driver = webdriver.Edge()
# driver.get("https://the-internet.hackerearth.com/javascript_alerts")

# alert_button = driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Alert')]")

# alert_button.click()
# time.sleep(1)
# alert = driver.switch_to.alert
# print("Alert message:", alert.text)
# alert.accept()

# print("Alert accepted.")
# time.sleep(2)
# driver.quit()

#---------------------------------------------
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.google.com")
# print(f"now on: {driver.title} ")
# time.sleep(2)

# driver.get("https://www.w3schools.com")
# print(f"now on : {driver.title}")
# time.sleep(2)

# driver.back()
# print(f"after going back : {driver.title}")
# time.sleep(2)

# driver.forward()
# print(f"after going forward : {driver.title}")
# time.sleep(2)

# driver.quit()

# -------------------------------------------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


   

driver.get("https://web-scraping.dev/login")

try:
   
   userEle = driver.find_element(By.NAME, "username")
   userEle.send_keys("user123")
   time.sleep(3)
   
   passEle = driver.find_element(By.NAME, "password")
   passEle.send_keys("password")
   time.sleep(3)
   passEle.submit()
   time.sleep(3)
   
   print("Logged in successfully.")
   
   element = driver.find_element(By.XPATH, "//div[contains(text(),'secret message')]")   
   print(f"secret message: {element.text}")
   time.sleep(3)
   
   print("Now logging out.")
   logout_btn = driver.find_element(By.CLASS_NAME, "btn")
   logout_btn.click()
   print("Logged out Successfully.")
   
except Exception as e:
   print("error : " ,e)
   


