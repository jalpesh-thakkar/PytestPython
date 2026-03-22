#from idlelib import browser
import time

from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)  # ✅ store in variable
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")
    #browser.close()
#another shortcut
#using page fixtures,only headed mode
def test_playwrightShortCut(page: Page):
    page.goto("https://www.rahulshettyacademy.com")

#ui functions


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulsheetyacademy")
    page.get_by_label("Password").fill("learning")
    # dropdown selector, basically asjking toi identify a role based component on page
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button",name="Sign In").click()
    time.sleep(5)

#get_by _label:label tag present that time label type used
#