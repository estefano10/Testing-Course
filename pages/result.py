from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    #Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'searchbox_input__bEGm3')
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    #Initializer
    def __init__(self, browser):
        self.browser = browser

    #Interaction methods
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    def title(self):
        return self.browser.title
         