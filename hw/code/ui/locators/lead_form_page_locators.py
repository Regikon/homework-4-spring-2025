from selenium.webdriver.common.by import By

class LeadFormDecorPageLocators:
    INPUT__NAME = (By.XPATH, "//input[@placeholder='Название лид-формы']")
    INPUT__NAME_ALERT_TOO_LONG = (By.XPATH, "//span[@role='alert' and contains(., 'Сократите текст')]")
    INPUT__NAME_ALERT_EMPTY = (By.XPATH, "//span[@role='alert' and contains(., 'Нужно заполнить')]")

    INPUT__COMPANY = (By.XPATH, "//input[@placeholder='Название компании']")
    INPUT__COMPANY_ALERT_EMPTY = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Название компании')]]//div[contains(., 'Нужно заполнить')]"
    )
    INPUT__COMPANY_ALERT_TOO_LONG = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Название компании')]]//div[contains(., 'Сократите')]"
    )

    INPUT__HEADER = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    INPUT__HEADER_ALERT_EMPTY = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Заголовок')]]//div[contains(., 'Нужно заполнить')]"
    )
    INPUT__HEADER_ALERT_TOO_LONG = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Заголовок')]]//div[contains(., 'Сократите')]"
    )

    INPUT__DESCRIPTION = (By.XPATH, "//input[@placeholder='Введите описание']")
    INPUT__DESCRIPTION_ALERT_EMPTY = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Описание')]]//div[contains(., 'Нужно заполнить')]"
    )
    INPUT__DESCRIPTION_ALERT_TOO_LONG = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Описание')]]//div[contains(., 'Сократите')]"
    )

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

    BUTTON__SELECT_LEAD_MAGNET = (
        By.XPATH,
        "//label[contains(@class, 'vkuiSegmentedControlOption')][.//span[text()='Лид-магнит']]"
    )
    INPUT__SALE = (
        By.XPATH,
        "//input[@value='500']"
    )
    BUTTON__SWITCH_RUBLE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSegmentedControlOption')][.//*[contains(.,'₽')]]"
    )
    BUTTON__SWITCH_PERCENT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSegmentedControlOption')][.//*[contains(.,'%')]]"
    )
    INPUT__SALE_ALERT_ZERO = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Размер скидки')]]//div[contains(., 'больше нуля')]"
    )
    INPUT__SALE_ALERT_TOO_BIG = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Размер скидки')]]//div[contains(., '100%')]"
    )
    SWITCH__BONUS = (
        By.XPATH,
        "//label[contains(@class, 'vkuiRadio')][.//input[@value='bonus']]"
    )
    INPUT__BONUS = (By.XPATH, "//input[@placeholder='Бонус']")
    INPUT__BONUS_ALERT_EMPTY = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Описание бонуса')]]//div[contains(., 'Нужно заполнить')]"
    )
    INPUT__BONUS_ALERT_TOO_LONG = (
        By.XPATH,
        "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Описание бонуса')]]//div[contains(., 'Сократите')]"
    )

    INPUT__COVER_UPLOAD = (
        By.XPATH,
        "//span[contains(@class, 'vkuiButton__in')][.//span[contains(., 'Выбрать из медиатеки')]]"
    )
    HAS_COVER = (By.XPATH, "//div[contains(@class, 'AdMediaPreview_item')]")

    BUTTON__CONTINUE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Продолжить')]"
    )

    STATUS_BAR_QUESTIONS_ACTIVE = (By.XPATH, "//div[contains(@class, 'CreateLeadFormModal_activeStep') and contains(., 'Вопросы')]")

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

    @staticmethod
    def LEAD_FORM_NAME(name):
        return (By.XPATH, f"//h5[@data-testid='lead_form_name__{name}']")

    @staticmethod
    def REMOVE_BUTTON(name):
        return (
            By.XPATH,
            f"//div[contains(@class, 'ContextMenuWrapper_wrapper')]\
            [.//h5[@data-testid='lead_form_name__{name}']]//span[text()='Архивировать']"
        )
    
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//span[@class='vkuiButton__in'][.//*[contains(., 'Архивировать')]]")
