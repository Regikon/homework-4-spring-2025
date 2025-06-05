from selenium.webdriver.common.by import By


class LeadFormQuestionsLocators:
    ADD_QUESTION = (By.XPATH, "//span[contains(@class, 'vkuiButton')][.//*[contains(., 'Добавить вопрос')]]")
    REMOVE_QUESTION = (By.XPATH, "//button[@aria-label='Remove']")
    QUESTION_EXISTS = (By.XPATH, "//div[contains(@class, 'Question_question__')]")
    QUESTION_TEXT = (By.XPATH, "//textarea[@placeholder='Напишите вопрос']")

    @staticmethod
    def HAS_QUESTION_TEXT_ON_PREVIEW(text: str):
        return (By.XPATH, f"//div[contains(@class, 'OnePageContentBlock')]//*[text()='{text}']")

    @staticmethod
    def ANSWER(index: int):
        return (By.XPATH, f"(//input[@placeholder='Введите ответ'])[{index}]")
    
    @staticmethod
    def HAS_ANSWER_ON_PREVIEW(text: str):
        return (By.XPATH, f"//div[contains(@class, 'OnePageContentBlock')]//div[text()='{text}']")
    
    QUESTION_TYPE = (By.XPATH, "//span[contains(., 'Тип вопроса')]//div[contains(@class, 'HintSelector')]")
    QUESTION_TYPE_MANY_ANSWERS = (By.XPATH, "//div[@role='button'][.//*[contains(., 'Выбор нескольких ответов')]]")
    HAS_QUESTION_TYPE_MANY_ANSWERS_ON_PREVIEW = (By.XPATH, "//div[contains(@class, 'OnePageContentBlock')]//input[@type='checkbox']")

    ADD_ANSWER = (By.XPATH, "//span[@class='vkuiButton__in'][.//span[text()='Добавить ответ']]")

    ADD_CONTACTS = (By.XPATH, "//span[@class='vkuiButton__in'][.//span[text()='Добавить контактные данные']]")
    
    @staticmethod
    def SELECT_CONTACT(text: str):
        return (By.XPATH, f"//label[contains(@class, 'vkuiCheckbox')][.//span[text()='{text}']]")
    CONFIRM_CONTACTS = (By.XPATH, "//span[@class='vkuiButton__in'][.//span[text()='Добавить']]")
    HAS_CONTACTS_NAME_ON_PREVIEW = (By.XPATH, "//input[@placeholder='Введите имя']")
    HAS_CONTACTS_CITY_ON_PREVIEW = (By.XPATH, "//input[@placeholder='Введите город']")
    HAS_CONTACTS_TELEPHONE_ON_PREVIEW = (By.XPATH, "//input[@placeholder='+7']")

    CONTINUE = (By.XPATH, "//span[@class='vkuiButton__in'][.//span[text()='Продолжить']]")    
