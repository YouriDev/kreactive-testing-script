
import pytest
from base_test import BaseTest
import time
import os
from selenium.webdriver.common.by import By
import datetime
from utils import get_currency_symbol
from utils import get_country_info
from conftest import email_guest

local_name = os.environ["TEST_LOCAL"]

@pytest.mark.usefixtures("driver")
class TestProduct_partial:
    @pytest.mark.sanity 
    def test_product_partial(self, driver):
        appium_driver = BaseTest(driver)

        # Attente initiale pour le chargement de l'app
        appium_driver = BaseTest(driver)
        time.sleep(3)

        # Page 1
        appium_driver.clear_and_type_on_element_by_name("cbdt_description_text", "In addition to the cookies strictly necessary for operation of this app, Louis Vuitton Malletier uses cookies, including third-party cookies, for statistical analysis or to personalize your experience, to offer you targeted content adapted to your interests and to analyse the performance of its advertising campaigns. You can accept or refuse cookies for the above-mentioned purposes by using the checkboxes provided. You can modify your preferences at any time by going to your profile if you have a Louis Vuit")

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='Reject all' and @type='XCUIElementTypeStaticText']')
        appium_driver.click_element_by_name("//*[@name='Reject all' and @type='XCUIElementTypeStaticText']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("cbdt_title_text"), "Error: cbdt_title_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("cbdt_description_text"), "Error: cbdt_description_text is not visible on the page."

        # Page 2

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='Continue as guest' and @type='XCUIElementTypeStaticText']')
        appium_driver.click_element_by_name("//*[@name='Continue as guest' and @type='XCUIElementTypeStaticText']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("authentificationSelection_description_text"), "Error: authentificationSelection_description_text is not visible on the page."

        # Page 3

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='onboarding_consentNext_button' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='onboarding_consentNext_button' and @type='XCUIElementTypeButton']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("onboarding_consentDescription_text"), "Error: onboarding_consentDescription_text is not visible on the page."

        # Page 4

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='onboarding_consentNext_button' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='onboarding_consentNext_button' and @type='XCUIElementTypeButton']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("onboarding_consentDescription_text"), "Error: onboarding_consentDescription_text is not visible on the page."

        # Page 5

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='bottomBar_shop_button' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='bottomBar_shop_button' and @type='XCUIElementTypeButton']")

        # Page 6

        # Clic on the button
        appium_driver.wait_for_element('//*[@type='XCUIElementTypeCell'][9]')
        appium_driver.click_element_by_name("//*[@type='XCUIElementTypeCell'][9]")

        # Page 7

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='Search for product' and @type='XCUIElementTypeSearchField']')
        appium_driver.click_element_by_name("//*[@name='Search for product' and @type='XCUIElementTypeSearchField']")

        # Page 9
        appium_driver.clear_and_type_on_element_by_name("search_searchedTitle_text", " watches")

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='watches for men' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='watches for men' and @type='XCUIElementTypeButton']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("search_searchedTitle_text"), "Error: search_searchedTitle_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("searchSuggestions_title_text"), "Error: searchSuggestions_title_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("productCarouselItem_title_text"), "Error: productCarouselItem_title_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("productCarouselItem_title_text"), "Error: productCarouselItem_title_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("productCarouselItem_title_text"), "Error: productCarouselItem_title_text is not visible on the page."

        # Page 10
        appium_driver.clear_and_type_on_element_by_name("XCUIElementTypeSearchField", "watches for men")

        # Clic on the button
        appium_driver.wait_for_element('//*[@type='XCUIElementTypeSearchField']')
        appium_driver.click_element_by_name("//*[@type='XCUIElementTypeSearchField']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productName_text"), "Error: plp_productName_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productPrice_text"), "Error: plp_productPrice_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productName_text"), "Error: plp_productName_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productPrice_text"), "Error: plp_productPrice_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productName_text"), "Error: plp_productName_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productPrice_text"), "Error: plp_productPrice_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productName_text"), "Error: plp_productName_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("plp_productPrice_text"), "Error: plp_productPrice_text is not visible on the page."

        # Page 11
        appium_driver.clear_and_type_on_element_by_name("productDescription_description_text", "Fine jewellery orders may take up to 2 weeks for delivery due to UK hallmarking regulations.&amp;#10; &amp;#10; &amp;#10;Part of the LV Volt One Collection, a tribute to the energy and rhythm of the LV Initials, this dazzling pendant is crafted from 18-karat yellow gold set with pavé diamonds and suspended from an adjustable chain. The large L holds a small V within which is a brilliant diamond, whose setting perfectly respects the V shape. Pieces from this range can be mixed and matched at will.")

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='pdp_findInStore_button' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='pdp_findInStore_button' and @type='XCUIElementTypeButton']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("pdp_price_text"), "Error: pdp_price_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("pdp_priceValue_text"), "Error: pdp_priceValue_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("productDescription_description_text"), "Error: productDescription_description_text is not visible on the page."
