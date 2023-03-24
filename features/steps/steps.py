import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from allure_behave.hooks import allure_report



@step('открываем сайт {website}')
def step_one(self, website):
    self.drv = webdriver.Chrome('chromedriver.exe')
    self.drv.get(website)
    self.drv.maximize_window()
    time.sleep(2)
    titlesite = self.drv.title
    title = 'Регард - интернет магазин компьютеров и комплектующих, техники для офиса и электроники. Сборка ПК. Доставка по России'
    assert titlesite == title

    time.sleep(2)

@step('открываем каталог, в каталоге {section} и {sub_section}')
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

@step('устанавливаем фильтр минимальная цена: {min_price} и производитель: {company}')
def input_filter(self, min_price, company):
    # Ставим фильтр по минимальной цене
    self.drv.find_element(By.XPATH, "//input[@name='min']").send_keys(min_price)
    time.sleep(2)
    # Разворачиваем список всех производителей
    self.drv.find_element(By.XPATH, "//li/span[@class='ListingFilters_showMore__btn__mNrGe']").click()
    # Выбираем нужного производителя
    self.drv.find_element(By.XPATH, "//label[text()='" + company + "']").click()
    time.sleep(2)

@step('проверяем кол.во найденных товаров на странице')
def prod_on_page(self):
    products_on_page = self.drv.find_element(By.XPATH, "//span[@class='Pagination_countSetter__count__Ml6rE']").text
    assert products_on_page == "по 24"
    time.sleep(2)

@step('копируем название первого товара и вставляем его в строку поиска')
def seach_first_priduct(self):
    self.first_priduct = self.drv.find_element(By.XPATH, "//div[contains(@class,'CardText_wrap__YYHuc')]/a/h6").text
    self.drv.find_element(By.XPATH, "//*[@id='searchInput']").send_keys(self.first_priduct)
    self.drv.find_element(By.XPATH, "//*[@id='searchInput']").send_keys(Keys.ENTER)
    time.sleep(2)

@step('снова проверяем кол.во найденных товаров на странице')
def accert_amount_priduct(self):
    amount_priduct_seach = self.drv.find_element(By.XPATH, "//span[contains(@class, 'ListingLayout_count')]").text
    assert amount_priduct_seach == "1 товар"
    time.sleep(2)
@step('проверяем, что найденный товар соответствует, товару вставили встроку поиска')
def accert_seach_priduct(self):
    name_first_value = self.drv.find_element(By.XPATH, "//div[contains(@class,'CardText_wrap__YYHuc')]/a/h6").text
    assert self.first_priduct == name_first_value
    time.sleep(2)

allure_report("path/to/result/dir")










