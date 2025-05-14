from selenium.webdriver.common.by import By

class CPMSettingsLocators:
    GENERAL_LIMIT_INPUT = (By.XPATH, "//*[contains(@class, 'CpmSettings_input')]/input")

    @staticmethod
    def REGION_DROPDOWN(region: str):
        return (By.XPATH, f'//div[@role="button"][contains(., "{region}")]')

    @staticmethod
    def CPM_INPUT(region_or_country: str):
        return (By.XPATH, f'//div[@role="button"][contains(., "{region_or_country}")]//*[contains(@class, "editableCpmInput_textCpm")]')

    @staticmethod
    def CPM_INPUT_FIELD(region_or_country: str):
        return (By.XPATH, f'//div[@role="button"][contains(., "{region_or_country}")]//input')

    NO_CPM_LABEL = (By.XPATH, '//*[contains(text(), "CPM не задан")]')

    SEARCH_INPUT = (By.XPATH, '//*[contains(@class, "CpmSettings_search__")]//input')

    ONLY_SET_CPMS_CHECKBOX = (By.XPATH, '//*[contains(@class,"CpmSettings_edited_")]')
