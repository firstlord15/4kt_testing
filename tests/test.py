import time
from conftest import *
from config import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegistrationPage import RegistrationPage
from pages_admin.LoginPage import LoginPage
from pages_admin.AdminPage import AdminPage


def test(driver):
    driver.get("http:/localhost/administration/")
    LoginPage(driver).login()
    adminPage = AdminPage(driver)
    adminPage.click(AdminPage.MENU_CATALOG)
    adminPage.click(AdminPage.LI_CATEGORIES)
    adminPage.click(AdminPage.BUTTON_ADD_NEW_CATEGORIES)
    time.sleep(0.5)
    adminPage._input(AdminPage.INPUT_CATEGORY_NAME, new_categories)
    # adminPage._input(AdminPage.INPUT_DESCRIPTION, "Description", clear=False) # надо исправить
    adminPage._input(AdminPage.INPUT_META_TAG_TITLE, "meta tag title")
    adminPage._input(AdminPage.INPUT_META_TAG_DESCRIPTION, "meta tag description")
    adminPage._input(AdminPage.INPUT_META_TAG_KEYWORDS, "meta tag keywords")
    time.sleep(0.5)

    adminPage.click(AdminPage.LI_DATA)
    adminPage.click(AdminPage.SELECT_PARENT)
    adminPage.downArrow()
    adminPage.enter()
    time.sleep(0.5)

    adminPage.click(AdminPage.LI_SEO)
    adminPage._input(AdminPage.INPUT_KEYWORD, "device")
    time.sleep(0.5)
    
    adminPage.click(AdminPage.LI_DESIGN)
    adminPage.click(AdminPage.SELECT_LAYOUT_OVERRIDE)
    adminPage.click(AdminPage.OPTION_LAYOUT_OVERRIDE)
    time.sleep(0.5)

    adminPage.click(AdminPage.BUTTON_SAVE_CATEGORY)
    time.sleep(3)