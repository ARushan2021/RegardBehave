import time

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from features.locators import regard_locators
from features.utils import *


@step('открываем сайт "{site}"')
def open_site(context, site):
    context.drv.get(site)
    context.drv.maximize_window()
    time.sleep(2)
    title_site = context.drv.title[0:25]
    title = 'Регард - интернет магазин'
    get_assert_screenshot(context, title_site, title)
    assert title_site == title, f'Заглавие сайта не совпадает: {title_site}'


@step('открываем каталог {section} и {sub_section}')
def submenu(context, section, sub_section):
    context.drv.find_element(By.XPATH, regard_locators.get("button_catalog")).click()
    time.sleep(3)
    catalog_name = regard_locators.get("catalog_name").replace('section_old', section)
    context.drv.find_element(By.XPATH, catalog_name).click()
    time.sleep(3)
    sub_catalog_name = regard_locators.get("sub_catalog_name").replace('sub_section_old', sub_section)
    context.drv.find_element(By.XPATH, sub_catalog_name).click()
    time.sleep(3)


@step('устанавливаем фильтр цена: {min_max_price} значение цены: {price} и производитель: {company}')
def input_filter(context, min_max_price, price, company):
    min_or_max = regard_locators.get("min_or_max_price").replace('min_max', min_max_price)
    context.drv.find_element(By.XPATH, min_or_max).send_keys(price)
    time.sleep(5)
    context.drv.find_element(By.XPATH, regard_locators.get("all_company")).click()
    time.sleep(5)
    company_name = regard_locators.get("company_name").replace('company_old', company)
    context.drv.find_element(By.XPATH, company_name).click()
    time.sleep(5)


@step('проверяем кол.во найденных товаров на странице')
def prod_on_page(context):
    products_on_page = context.drv.find_element(By.XPATH, regard_locators.get("prod_on_page")).text
    products_of_page = "по 24"
    get_assert_screenshot(context, products_on_page, products_of_page)
    assert products_on_page == products_of_page,\
        f'На странице отображается: *{products_on_page}* , а должно: *{products_of_page}*!'
    time.sleep(2)


@step('копируем название первого товара и вставляем его в строку поиска')
def search_first_product(context):
    first_product = context.drv.find_element(By.XPATH, regard_locators.get("first_product_name")).text
    context.drv.find_element(By.XPATH, regard_locators.get("search_input")).send_keys(first_product)
    context.drv.find_element(By.XPATH, regard_locators.get("search_input")).send_keys(Keys.ENTER)
    time.sleep(8)


@step('снова проверяем кол.во найденных товаров на странице')
def accert_amount_priduct(context):
    amount_product_seach = context.drv.find_element(By.XPATH, regard_locators.get("amount_prod_seach")).text
    products_of_page = "1 товар"
    get_assert_screenshot(context, amount_product_seach, products_of_page)
    assert amount_product_seach == products_of_page, \
        f'На странице отображается: {amount_product_seach}, а должен: {products_of_page}!'
    time.sleep(2)


@step('проверяем, что найденный товар соответствует товару, вставленному в строку поиска')
def accert_seach_priduct(context):
    name_first_value = context.drv.find_element(By.XPATH, regard_locators.get("name_first_value")).text
    search_product = context.drv.find_element(By.XPATH, regard_locators.get("search_input")).get_attribute('value')
    get_assert_screenshot(context, search_product, name_first_value)
    assert search_product == name_first_value, \
        f'Найденный товар *{name_first_value}* не соответствует товару, вставленному в поиск *{search_product}*!'
    get_screenshot(context)
    time.sleep(2)
