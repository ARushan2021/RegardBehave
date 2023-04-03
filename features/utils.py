import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.locators import regard_locators


def get_screenshot(context):
    allure.attach(context.drv.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def find_element(context, xpath, time=10):
    return WebDriverWait(context.drv, time).until(EC.visibility_of_element_located((By.XPATH, xpath)),
                                                  message=f"Не удается найти элемент по локатору {xpath}")


def visibility_of(context, xpath, time=10):
    WebDriverWait(context.drv, time).until(EC.visibility_of_element_located((By.XPATH, xpath)))


def loading(context, times=10):
    WebDriverWait(context.drv, times).until(EC.invisibility_of_element_located
                                            ((By.XPATH, regard_locators.get("loading"))))

    time.sleep(2)
