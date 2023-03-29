import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.locators import regard_locators


def get_screenshot(context):
    allure.attach(context.drv.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def visibility_of(context, xpath):
    WebDriverWait(context.drv, 5).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))


def loading(context):
    WebDriverWait(context.drv, 5).until(
        EC.invisibility_of_element_located((By.XPATH, regard_locators.get("loading"))))
