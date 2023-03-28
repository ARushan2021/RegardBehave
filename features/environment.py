from selenium import webdriver


def before_tag(context, tag):
    pass


def before_all(context):
    context.drv = webdriver.Chrome('chromedriver.exe')


def after_all(context):
    context.drv.quit()
