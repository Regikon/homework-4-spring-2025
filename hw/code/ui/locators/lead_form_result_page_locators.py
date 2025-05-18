from selenium.webdriver.common.by import By


class LeadFormResultPageLocators:
    ADD_SITE  = (By.XPATH, "//div[@role='button'][.//*[contains(., 'сайт')]]")
    SITE = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Ссылка на сайт']]//input")
    HAS_SITE = (By.XPATH, "//span[text()='Перейти на сайт']")

    ADD_TEL   = (By.XPATH, "//div[@role='button'][.//*[contains(., 'телефон')]]")
    TEL = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Телефон для заказа']]//input")
    HAS_TEL = (By.XPATH, "//span[@class='vkuiButton__in'][.//*[contains(@class, 'phone')]]")
    TEL_INCORRECT = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Телефон для заказа']]//*[contains(., 'Телефон должен')]")

    ADD_PROMO = (By.XPATH, "//div[@role='button'][.//*[contains(., 'промокод')]]")
    PROMO = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Промокод']]//input")
    HAS_PROMO = (By.XPATH, "//span[contains(@class, 'vkuiFormField')][.//*[@aria-label='Скопировать']]")
    PROMO_TOO_LONG = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Промокод']]//*[text()='Сократите текст']")

    HEADER  = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Заголовок']]//input")
    HEADER_EMPTY = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Заголовок']]//*[text()='Нужно заполнить']")
    HEADER_TOO_LONG = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Заголовок']]//*[text()='Сократите текст']")
    
    DESCRIPTION  = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Описание']]//input")
    DESCRIPTION_TOO_LONG = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[text()='Описание']]//*[text()='Сократите текст']")

    CONTINUE = (By.XPATH, "//span[@class='vkuiButton__in'][.//span[text()='Продолжить']]")

    STATUS_BAR_SETTINGS_PAGE_ACTIVE = (By.XPATH, "//div[contains(@class, 'CreateLeadFormModal_activeStep') and contains(., 'Настройки')]")
