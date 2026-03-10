
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
class TestAuthentication_signup_partial:
    @pytest.mark.sanity 
    def test_authentication_signup_partial(self, driver):
        appium_driver = BaseTest(driver)

        # Attente initiale pour le chargement de l'app
        appium_driver = BaseTest(driver)
        time.sleep(3)

        # Page 1

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='Europe' and @type='XCUIElementTypeOther']')
        appium_driver.click_element_by_name("//*[@name='Europe' and @type='XCUIElementTypeOther']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Page 2

        # Clic on the button
        appium_driver.wait_for_element('//*[@type='XCUIElementTypeCell'][10]')
        appium_driver.click_element_by_name("//*[@type='XCUIElementTypeCell'][10]")

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_continent_text"), "Error: dispatchCountry_continent_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("dispatchCountry_country_text"), "Error: dispatchCountry_country_text is not visible on the page."

        # Page 3
        appium_driver.clear_and_type_on_element_by_name("cbdt_description_text", "En plus des cookies strictement nécessaires au fonctionnement, Louis Vuitton Malletier utilise des cookies, y compris de tiers, à des fins d’analyse statistique ou de personnalisation de votre expérience, afin de vous proposer des contenus ciblés adaptés à vos centres d’intérêts et analyser la performance de ses campagnes publicitaires. Vous pouvez accepter ou refuser les cookies liés aux finalités mentionnées ci-dessus en utilisant les cases à cocher prévues à cet effet. Vous pouvez à tout moment modifier ")

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='cbdt_rejectAll_button' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='cbdt_rejectAll_button' and @type='XCUIElementTypeButton']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("cbdt_title_text"), "Error: cbdt_title_text is not visible on the page."

        # Text checking
        assert appium_driver.is_element_visible_with_name("cbdt_description_text"), "Error: cbdt_description_text is not visible on the page."

        # Page 4

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='Continuer en tant qu'invité' and @type='XCUIElementTypeStaticText']')
        appium_driver.click_element_by_name("//*[@name='Continuer en tant qu'invité' and @type='XCUIElementTypeStaticText']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("authentificationSelection_description_text"), "Error: authentificationSelection_description_text is not visible on the page."

        # Page 5

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='Continuer en tant qu'invité' and @type='XCUIElementTypeStaticText']')
        appium_driver.click_element_by_name("//*[@name='Continuer en tant qu'invité' and @type='XCUIElementTypeStaticText']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("authentificationSelection_description_text"), "Error: authentificationSelection_description_text is not visible on the page."

        # Page 6

        # Clic on the button
        appium_driver.wait_for_element('//*[@name='authentificationSelection_signUp_button' and @type='XCUIElementTypeButton']')
        appium_driver.click_element_by_name("//*[@name='authentificationSelection_signUp_button' and @type='XCUIElementTypeButton']")

        # Text checking
        assert appium_driver.is_element_visible_with_name("authentificationSelection_description_text"), "Error: authentificationSelection_description_text is not visible on the page."
