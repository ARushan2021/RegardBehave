import allure
from allure_commons.types import AttachmentType


def get_assert_screenshot(context, argument1, argument2):
    if argument1 != argument2:
        allure.attach(context.drv.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def get_screenshot(context):
    allure.attach(context.drv.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
