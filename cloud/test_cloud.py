import time

from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)  # ✅ store in variable
    context = browser.new_context() #opening browser incognito mode
    page = context.new_page()
    page.goto("https://cc.dev.fastraxpos.com/")
    #browser.close()

def test_coreLocators(page: Page):
    page.goto("https://cc.dev.fastraxpos.com/")
    page.get_by_placeholder("Username").fill("test")
    page.get_by_placeholder("password").fill("1")
    page.get_by_role("button", name="Sign-in").click()
    #page.locator("input[name='password']").fill("test123") #second way to enter password
    # dropdown selector, basically asjking toi identify a role based component on page
    #page.get_by_role("combobox").select_option("teach")
    time.sleep(5)

