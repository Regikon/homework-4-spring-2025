from selenium.webdriver.common.by import By

class CompaniesPageLocators:
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Создать")]]')
    CREATE_CAMPAIGN_BUTTON_ALT = (By.XPATH, '//a[.//span[contains(text(), "Создать")]]')

    EDIT_MAIN_NAME = (By.XPATH, '//div[contains(@class, "EditableTitle_container")]')
    EDIT_MAIN_NAME_INPUT = (By.XPATH, '//textarea[contains(@class, "EditableTitle_input")]')

    @staticmethod
    def COMPANY_NAME(new_name):
        return By.XPATH,  '//span[contains(text(), "{new_name}")]'

    DELL_CHAPTER_BUTTON = (By.XPATH, '//label[@data-testid="dropdown-item" and .//span[contains(text(), "Удалить")]]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//button[.//span[text()="Удалить"]]')
    WAIT_FOR_DELETE = (By.XPATH, '//span[text()="Изменения не сохранятся"]]')

    DELETE_COMPANY = (By.XPATH, '//button[.//span[text()="Не сохранять"]]')

    CHOOSE_SITE_BUTTON = (By.XPATH, '//div[@data-id="site_conversions"]')
    ADVERTISING_SITE_URL_INPUT = (By.XPATH, '//input[@placeholder="Вставьте ссылку или выберите из списка"]')
    GOAL_INPUT = (By.XPATH, '//input[@data-testid="priced-goal"]')
    PRICE_INPUT = (By.XPATH, '//input[@placeholder="Не задан"]')
    #CHOOSE_LID_FORMS_BUTTON = (By.XPATH, '//div[@data-id="leadads"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[.//span[text()="Продолжить"]]')
    

    REGION_INPUT = (By.XPATH, '//input[@placeholder="Страна, регион или город"]')

    @staticmethod
    def REGION_CHECKBOX(region_name):
        return By.XPATH, f'//label[contains(@class, "vkuiCheckbox") and .//span[text()="{region_name}"]]'

    INTERESTS_AND_BEHAVIOR_DIV = (By.XPATH, '//div[@type="button" and .//h3[text()="Интересы и поведение"]]')
    INTERESTS_DIV = (By.XPATH, '//div[@role="button" and .//span[text()="Подбор пользователей на основе их интересов, привычек и увлечений"]]')
    INTEREST_INPUT_MENU = (By.XPATH, '//button[@aria-label="Развернуть"]')

    @staticmethod
    def ONE_INTEREST(interest_name):
        return By.XPATH, '//div[@role="option" and @title="{interest_name}"]'
    
    @staticmethod
    def SHOW_DELETE_BUTTON(chapter_name):
        return By.XPATH, '//div[@role="option" and .//span[text()="{chapter_name}"]]//button[@aria-label="More"]'

    @staticmethod
    def SPAN_TEXT(text):
        return By.XPATH, '//span[text()="{text}"]'

    INVALID_SITE_LINK_ERROR = (By.XPATH, '//div[text()="Не удалось подгрузить данные ссылки"]')
    INVALID_BUDGET_ERROR = (By.XPATH, '//div[text()="Укажите бюджет не меньше 100₽"]')

    WAIT_FOR_ERROR_DIV = (By.XPATH, '//div[text()="Не удалось сгенерировать текст. Попробуйте ещё раз"]')

    CLOSE_SOME_ADS = (By.XPATH, '//div[@role="button" and contains(@class, "vkuiModalDismissButton ")]')

    @staticmethod
    def WAIT_BUDGET(budget):#budget<=999!
        return By.XPATH, '//h4[contains(@value, "{budget}")]'

    @staticmethod
    def TEXT_INPUT_OF_ANNOUNCEMENT(text):
        return By.XPATH, '//div[.//span[text()="{text}"]]//dib[contains(@class, "EditableTextField__textField")]'

    PUBLISH_BUTTON = (By.XPATH, '//button[.//span[text()="Опубликовать"]]')
    ADD_MORE_FORMATS = (By.XPATH, '//button[.//span[text()="Добавить ещё формат"]]')
    MEDIA_FILES_GALLERY = (By.XPATH, '//div[@role="button" and .//span[text()="Галерея медиафайлов"]]')
    MEDIA_FILES_UPLOAD_BUTTON = (By.XPATH, '//button[contains(@class, "UploadMediaButton_button")]')

    @staticmethod
    def CREATED_ROW(name_of_company):
        return By.XPATH, '//div[@role="button" and .//button[text()="{name_of_company}"]]]'
    
    @staticmethod
    def CREATED_ROW_MORE(name_of_company):
        return By.XPATH, '//button[@aria-label="More"]'


