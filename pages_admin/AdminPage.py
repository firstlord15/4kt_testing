from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *
import time


class AdminPage(BasePage):
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")

    # CATEGORIES
    LI_CATEGORIES = (By.XPATH, "//a[contains(text(),'Categories')]")
    
    # _GENERAL
    LI_GENERAL = (By.LINK_TEXT, "General")
    BUTTON_ADD_NEW_CATEGORIES = (By.CSS_SELECTOR, "a.btn.btn-primary:nth-child(2)")
    INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, "#input-name-1")
    INPUT_DESCRIPTION = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/iframe[1]")
    INPUT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title-1")
    INPUT_META_TAG_DESCRIPTION = (By.CSS_SELECTOR, "#input-meta-description-1")
    INPUT_META_TAG_KEYWORDS = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    BUTTON_SAVE_CATEGORY = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-child(1)")

    # _DATA
    LI_DATA = (By.LINK_TEXT, "Data")
    SELECT_PARENT = (By.CSS_SELECTOR, "#input-parent")
    INPUT_FILTER = (By.CSS_SELECTOR, "#input-filter")
    INPUT_COLUMNS = (By.CSS_SELECTOR, "#input-column")
    INPUT_SORT_ORDER = (By.CSS_SELECTOR, "#input-sort-order")
    INPUT_STATUS = (By.CSS_SELECTOR, "#input-status")

    # _SEO
    LI_SEO = (By.LINK_TEXT, "SEO")
    INPUT_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")

    # _DESIGN
    LI_DESIGN = (By.LINK_TEXT, "Design")
    SELECT_LAYOUT_OVERRIDE = (By.XPATH, "//tbody/tr[1]/td[2]/select[1]")
    OPTION_LAYOUT_OVERRIDE = (By.XPATH, "//option[contains(text(),'Default')]")

    