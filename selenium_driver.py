from selenium import webdriver

# Подключение
driver = webdriver.Chrome()
driver.get("https://passport.yandex.ru/auth/")
# объекты на сайте
login_field = driver.find_element_by_name('login')
button_login = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button')