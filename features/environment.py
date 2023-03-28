from selenium import webdriver


def before_all(context):
    context.drv = webdriver.Chrome('driver/chromedriver.exe')


def after_all(context):
    context.drv.quit()
