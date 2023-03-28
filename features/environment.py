from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    context.drv = webdriver.Chrome('driver/chromedriver.exe')


def after_all(context):
    context.drv.quit()


# def get_screenshot(context, argument1, argument2):
#     if argument1 != argument2:
#         allure.attach(context.drv.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
