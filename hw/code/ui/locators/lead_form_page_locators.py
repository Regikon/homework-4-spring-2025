from selenium.webdriver.common.by import By

class LeadFormDecorPageLocators:
    INPUT__NAME = (By.XPATH, "//input[@placeholder='Название лид-формы']")
    INPUT__NAME_ALERT_TOO_LONG = (By.XPATH, "//span[@role='alert' and contains(., 'Сократите текст')]")
    INPUT__NAME_ALERT_EMPTY = (By.XPATH, "//span[@role='alert' and contains(., 'Нужно заполнить')]")

    INPUT__COMPANY = (By.XPATH, "//input[@placeholder='Название компании']")
    INPUT__HEADER = (By.XPATH, "//input[@placeholder='Название компании']")

    INPUT__LOGO_UPLOAD = (By.XPATH, "//div[@data-testid='set-global-image']")
    INPUT__LOGO_CHANGE = (By.XPATH, "//button[@data-testid='change-image']")
    INPUT__LOGO_EMPTY_ALERT = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Логотип']]//div[contains(., 'Нужно заполнить')]"
    )

    SWITCH__CREATE_LENDING = (By.CSS_SELECTOR, ".vkuiSwitch")
    BUTTON__EDIT_LENDING = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Редактировать')]"
    )
    INPUT__LENDING_COMPANY = (By.XPATH, "//input[@placeholder='Введите название компании']")
    INPUT__LENDING_HEADER = (By.XPATH, "//textarea[@placeholder='Введите заголовок']")
    BUTTON__LENDING_ADD_BLOCK = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Добавить блок')]"
    )
    BUTTON__LENDING_ADD_TEXT = (
        By.XPATH,
        "//*[contains(@class, 'AddBlockTooltip_option') and contains(., 'Текст')]"
    )
    INPUT__LENDING_WRITE_TEXT = (
        By.XPATH,
        "//*[contains(@class, 'TextBlock_inputField')]"
    )
    BUTTON__SAVE_LANDING = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Сохранить')]"
    )
    BUTTON__SELECT_LEAD_MAGNIT = (
        By.XPATH,
        "//span[text()='Лид-магнит']"
    )
    INPUT__SALE = (
        By.XPATH,
        "//input[@value='500']"
    )
    BUTTON__SWITCH_PERCENT = (
        By.XPATH,
        "//*[@class='vkuiSegmentedControlOption'][.//*[text()='%']]"
    )
    INPUT__LOAD_COVER = (
        By.XPATH,
        "//*[contains(@class, 'LocalFileSelector_file')]"
    )

    BUTTON__CONTINUE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Продолжить')]"
    )

class LeadFormPageLocators:
    BUTTON__CREATE_NEW = (By.XPATH, "//button[contains(., 'Создать лид-форму')]")
    

    BUTTON__ADD_QUESTION = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Добавить вопрос')]"
    )
    INPUT__QUESTION_TEXT = (
        By.XPATH,
        "//textarea[@placeholder='Напишите вопрос']"
    )
    INPUT_QUESTION_ANSWER_1 = (
        By.XPATH,
        "(//input[@placeholder='Введите ответ'])[1]"
    )
    INPUT_QUESTION_ANSWER_2 = (
        By.XPATH,
        "(//input[@placeholder='Введите ответ'])[2]"
    )
    BUTTON_QUESTION_REMOVE = (
        By.XPATH,
        "//button[@aria-label='Remove']"
    )

