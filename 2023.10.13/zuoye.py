# -*-coding:utf-8-*-
# @Time    :2023/10/2016:04
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :zuoye.py
# @Software:PyCharm
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.username_input = (By.NAME, 'username')
    self.password_input = (By.NAME, 'password')
    self.login_button = (By.XPATH, '//button[@type="submit"]')
    self.error_message = (By.XPATH, '//div[@class="alert alert-danger"]')

  def login(self, username, password):
    self.driver.find_element(*self.username_input).send_keys(username)
    self.driver.find_element(*self.password_input).send_keys(password)
    self.driver.find_element(*self.login_button).click()

  def get_error_message(self):
    return self.driver.find_element(*self.error_message).text


class AddEventPage:
  def __init__(self, driver):
    self.driver = driver
    self.date_input = (By.ID, 'date')
    self.add_button = (By.XPATH, '//button[@type="submit"]')

  def add_event(self, date):
    self.driver.find_element(*self.date_input).send_keys(date)
    self.driver.find_element(*self.add_button).click()


class AddGuestPage:
  def __init__(self, driver):
    self.driver = driver
    self.add_button = (By.XPATH, '//button[@type="submit"]')

  def add_guest(self):
    self.driver.find_element(*self.add_button).click()


@pytest.fixture(scope="class")
def setup(request):
  driver = webdriver.Chrome()
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.quit()


@pytest.mark.usefixtures("setup")
class TestProject:
  def test_login_success(self):
    login_page = LoginPage(self.driver)
    login_page.login("admin", "admin123456")
    assert self.driver.current_url.endswith('/home/')

  def test_login_failure(self):
    login_page = LoginPage(self.driver)
    login_page.login("admin", "wrongpassword")
    error_message = login_page.get_error_message()
    assert error_message == "Invalid username or password"

  def test_add_event(self):
    add_event_page = AddEventPage(self.driver)
    add_event_page.add_event("2023-10-21")
    # Add event assertion

  def test_add_guest(self):
    add_guest_page = AddGuestPage(self.driver)
    add_guest_page.add_guest()
    # Add guest assertion


if __name__ == '__main__':
  pytest.main(['-v', '--html=report.html'])

