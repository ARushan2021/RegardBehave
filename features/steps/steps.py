import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@step('open website {website}')
def step_one(self, website):
    self.drv = webdriver.Chrome('chromedriver.exe')
    self.drv.get(website)
    self.drv.maximize_window()
    time.sleep(2)
    titlesite = self.drv.title
    title = 'Регард - интернет магазин компьютеров и комплектующих, техники для офиса и электроники. Сборка ПК. Доставка по России'
    assert titlesite in title
    time.sleep(2)

@step('open subsection {section} and subsection {sub_section}')
def submenu(self, section, sub_section):
    # Нажимаем кнопку каталог
    self.drv.find_element(By.XPATH, "//button[contains(@class, 'NavigationBar_burgerButton')]").click()
    time.sleep(2)
    # Нажимаем на раздел в каталоге
    self.drv.find_element(By.XPATH, "//div[text()='" + section + "']/ancestor::a").click()
    time.sleep(2)
    # Нажимем на нужный раздел
    self.drv.find_element(By.XPATH, "//div/p[contains(text(),'" + sub_section + "')]").click()
    time.sleep(2)

@step('put the filter on min price: {min_price} and company: {company}')
def input_filter(self, min_price, company):
    # Ставим фильтр по минимальной цене
    self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div[1]/section/div[2]/div/div/div/div/input[@name='min']").send_keys(min_price)
    # Разворачиваем список всех производителей
    self.drv.find_element(By.XPATH, "//li[33]/span[@class='ListingFilters_showMore__btn__dw-Xb']").click()
    # Выбираем нужного производителя
    self.drv.find_element(By.XPATH, "//label[text()='" + company + "']").click()
    time.sleep(2)

@step('the first product found in the search')
def seach_first_priduct(self):
    products_on_page = self.drv.find_element(By.XPATH, "//span[@class='Pagination_countSetter__count__3f3n_']").get_text()
    assert products_on_page == "по 24"
    time.sleep(7)





