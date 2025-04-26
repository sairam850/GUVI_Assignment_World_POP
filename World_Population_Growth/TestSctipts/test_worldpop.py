"""
Extract the dynamically updated world population
https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live

1. launch the website
2. fetch the current world population
"""

# Import all necessary Dependencies
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Import Explicitly Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Use Page Object Model Import Data and Locators
from TestData.data import WorldPopulationData
from TestLocators.Locators import WorldPopulationLocators


class TestWorldPopulationCount:

    def test_world_population_growth(self):
        try:
            # create the driver Object
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.wait = WebDriverWait(self.driver, 15)

            # Fetch the World Population URL
            self.driver.get(WorldPopulationData.world_population_url)

            self.driver.maximize_window()
            # create an empty list to store web elements
            world_total_population = []

            # using while loop for continuous iteration
            while True:
                total_population_count = self.wait.until(EC.presence_of_element_located((By.XPATH,WorldPopulationLocators.world_population_locators)))

                # append the elements into list
                world_total_population.append(total_population_count)

                # Iterate to print the text present in the element
                for data in world_total_population:
                    print(f"Current World Population: {data.text}")

        # Exception Handiling
        except (NoSuchElementException,ElementNotVisibleException) as Error:
                print("ERROR: Problem fetching the data!", Error)

        self.driver.quit()
