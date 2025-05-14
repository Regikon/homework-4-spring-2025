from selenium.webdriver.common.by import By

class AdvertiserSitesLocators:
    ADD_PIXEL = (By.XPATH, '//button[.//span[text()="Добавить пиксель"]]')
    ADD_PIXEL_IN_MODAL = (By.XPATH, '//div[contains(@class, "vkuiModalCard")]//button[.//span[text()="Добавить пиксель"]]')
    BACK_TO_SITES = (By.XPATH, '//a[@href="/hq/pixels"]')
    DOMAIN = (By.XPATH, '//input[@placeholder="Домен сайта"]')
    DISMISS_RENAME = (By.XPATH, '//div[@role="button" and contains(@class, "vkuiModalDismissButton")]')

    IGNORE_AND_CREATE_NEW = (By.XPATH, '//div[@role="button" and .//span[text()="Создать новый пиксель"]]')
    DISMISS_BY_DOMAIN = (By.XPATH, '//div[@role="button" and contains(@class, "vkuiModalDismissButton")]')
    PIXEL_ROWS = (By.XPATH, '//div[contains(@class, "PixelsList__row")]')

    DELETE_PIXEL_H2 = (By.XPATH, '//h2[text()="Удаление пикселя"]')
    CONFIRM_DELETE = (By.XPATH, '//button[.//span[text()="Удалить"]]')

    INPUT_URL_CONTAINS = (By.XPATH, '//input[@placeholder="Введите значение"]')
    INPUT_CATEGORY = (By.XPATH, '//div[contains(@id, "purchase")]')
    INPUT_CONDITION = (By.XPATH, '//div[contains(@id, "uss")]')

    DIV_ERROR = (By.XPATH, '//div[text()="Внутренняя ошибка сервера"]')

    SETTINGS_PIXEL = (By.XPATH, '//a[text()="Настройка"]')
    MORE_BUTTON = (By.XPATH, '//button[contains(@class, "PixelMoreCell_moreButton")]')
    DELL_PIXEL_DROPDOWN = (By.XPATH, '//label[.//span[text()="Удалить пиксель"]]')
    RENAME_PIXEL_DROPDOWN = (By.XPATH, '//label[.//span[text()="Переименовать"]]')
    RENAME_INPUT = (By.XPATH, '//input[contains(@class, "vkuiInput__el")]')
    CONFIRM_RENAME = (By.XPATH, '//button[.//span[text()="Изменить"]]')

    ADD_EVENT_TO_PIXEL = (By.XPATH, '//button[.//span[text()="Добавить событие"]]')
    ADD_EVENT_TO_PIXEL_CONFIRM = (By.XPATH, '//div[contains(@class, "Footer_footer")]//button[.//span[text()="Добавить событие"]]')
    INPUT_EVENT_NAME = (By.XPATH, '//input[@placeholder="Введите название"]')
    INPUT_EVENT_CATEGORY = (By.XPATH, '//input[@placeholder="Выберите категорию"]')
    INPUT_EVENT_CONDITION = (By.XPATH, '//input[@placeholder="Выберите условие"]')

    CODE_PIXEL_MENU = (By.XPATH, '//div[@role="tab" and .//span[text()="Код пикселя"]]')
    DATA_LAYER_SWITCH = (By.XPATH, '//label[.//div[contains(text(), "data-layer")]]')
    DATA_LAYER_INPUT = (By.XPATH, '//input[@placeholder="Введите название слоя"]')

    TAGS_PIXEL_MENU = (By.XPATH, '//div[@role="tab" and .//span[text()="Аудиторные теги"]]') 
    CREATE_TAG_BUTTON = (By.XPATH, '//button[.//span[text()="Создать аудиторный тег"]]')
    TAG_INPUT = (By.XPATH, '//input[@placeholder="Введите название тега"]')
    TAG_INPUT_BUTTON = (By.XPATH, '//button[.//span[text()="Создать"]]')
    TAG_ROW = (By.XPATH, '//div[contains(@class, "TagsList_row")]')
    SHOW_TAG_BUTTON = (By.XPATH, '//button[contains(@class, "TagsList_button")]')#'//button[.//svg[contains(@class, "vkuiIcon--brackets_slash_outline")]]')
    TAG_CLOSE_BUTTON = (By.XPATH, '//button[.//span[text()="Закрыть"]]')

    ACCESS_PIXEL_MENU = (By.XPATH, '//div[@role="tab" and .//span[text()="Доступы"]]')
    GIVE_ACCESS_BUTTON = (By.XPATH, '//button[.//span[text()="Выдать доступ"]]')
    ACCESS_INPUT = (By.XPATH, '//input[@placeholder="Введите ID аккаунта VK Рекламы"]')
    ACCESS_GIVE_BUTTON = (By.XPATH, '//div[contains(@class, "ModalManagerPage_footer")]//button[.//span[text()="Выдать доступ"]]')
    ACCESS_CLOSE_BUTTON = (By.XPATH, '//button[.//span[text()="Закрыть"]]')
    ACCESS_ROW = (By.XPATH, '//div[contains(@class, "AccessKeysList_row")]')
    REVOKE_ACCESS_BUTTON = (By.XPATH, '//button[contains(@class, "RevokeSharingKeyCell")]')
    REVOKE_ACCESS_CONFIRM_BUTTON = (By.XPATH, '//button[.//span[text()="Закрыть доступ"]]')


    

