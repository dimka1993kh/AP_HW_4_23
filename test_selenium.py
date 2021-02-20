from selenium_driver import driver, login_field, button_login
import time
from data import true_login, true_password, wrong_login, wrong_password, space_login, space_password

class TestWithSelenium:
    def setup(self):
        print("method setup")   
    def teardown(self):
        print("method teardown")   

    def test_true_login_and_password(self):
        login_field.send_keys(true_login)
        button_login.submit()

        time.sleep(1)

        password_field = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
        password_field.send_keys(true_password)
        button_login_new = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
        button_login_new.submit()

        time.sleep(3)
        #Если найдет данный элемент, то загрузка прозошла успешно
        manage_acc = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/a[1]')

        time.sleep(3)

        driver.quit()
        assert manage_acc
    
    def test_wrong_login(self):
        login_field.send_keys(wrong_login)
        button_login.submit()
        time.sleep(1)
        result = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/h1')
        time.sleep(1)
        #driver.quit()
        assert result.text == f'Мы отправили письмо с кодом на {wrong_login}. Пожалуйста, введите его для завершения регистрации.'

    def test_wrong_password(self):
        login_field.send_keys(true_login)
        button_login.submit()

        time.sleep(1)

        password_field = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
        password_field.send_keys(wrong_password)
        button_login_new = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
        button_login_new.submit()

        time.sleep(3)
        wrong_answer = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[2]')
        assert wrong_answer.text == f'Неверный пароль'

    def test_space_login(self):
        login_field.send_keys(space_login)
        button_login.submit()
        time.sleep(1)
        result = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]')
        time.sleep(1)
        #driver.quit()
        assert result.text == f'Логин не указан'

    def test_space_password(self):

        login_field.send_keys(true_login)
        button_login.submit()

        time.sleep(1)

        password_field = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
        password_field.send_keys(space_password)
        button_login_new = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
        button_login_new.submit()

        time.sleep(3)
        result = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[2]')
        assert result.text == f'Пароль не указан'
