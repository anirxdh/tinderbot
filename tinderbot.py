from selenium import webdriver
chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com")


