from selenium.webdriver.common.by import By

class AudienceAddAudiencePageLocators:
    @staticmethod
    def DROPDOWN_BY_LABEL(label_text: str):
        return (By.XPATH, f'//div[contains(@class, "vkuiFormItem")][.//*[contains(text(), "{label_text}")]]//input')
    
    @staticmethod
    def SOURCE_BUTTON_BY_LABEL(label_text: str):
        return (By.XPATH, f'//div[contains(@class, "SourceType_button")][.//*[contains(., "{label_text}")]]')
    
    ADD_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить источник")]')
    EXCLUDE_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Исключить источник")]')

    AUDIENCE_NAME_INPUT = (By.XPATH, '//section[contains(@class, "CreateSegmentModal_form")]//input[@class[contains(., "vkuiInput__el")]]')

    CREATE_NEW_LIST = (By.XPATH, '//div[@id="tab-create-from-user-list-new"]') 
    LIST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название списка"]')
    UPLOAD_FILE = (By.XPATH, '//label[contains(@class, "LocalFileSelector_file__")]//input[@type="file"]')

    OPTION = (By.XPATH, '//div[contains(@class, "Segment_option")]')
    KEY_PHRASES_INPUT = (By.XPATH, '//*[contains(text(), "Ключевые фразы")]/ancestor::div[contains(@class, "vkuiFormItem")]//textarea')

    COMMUNITY_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название сообщества"]')
    SELECT_ALL_COMMUNTIES_BUTTON = (By.XPATH, '//div[@id="react-collapsed-toggle-:r3v:"]//div[@class="GroupHeader_selectAll__kkZtN"]')
    MODAL_SECTION = (By.XPATH, '//section[contains(@class, "SelectSourceModal_groupSourceWrapper")]')
    ADD_BY_LIST_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Добавить списком")]]')
    VK_COMMUNITIES_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiActionSheetItem")]//span[text()="Сообщества ВКонтакте"]')
    TEXTAREA = (By.XPATH, '//div[contains(@class, "AddGroupsListModal_content")]//textarea[contains(@class, "vkuiTextarea__el")]')
    ADD_BUTTON = (By.XPATH, '//form//div[contains(@class, "AddTextListCard_footerContent")]//button')
    CLOSE_MODAL = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton")]')
    ADDED_COMMUNITY = (By.XPATH, '//div[contains(@class, "Selected_item") and contains(.., "Авторская керамика | Сон Совы")]')

    MUSICIAN_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название музыканта"]')
    CHOSEN_MUSICIAN = (By.XPATH, '//div[contains(@class, "VariantsListItem_name") and contains(.., "Lizer")]')
    COMPLETE_BUTTON = (By.XPATH, '//button[contains(@class, "SearchInputDropdown_dropdownActionLink")]')

    LOAD_BY_LIST_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Загрузить списком")]]')
    APPS_TEXTAREA = (By.XPATH, '//div[contains(@class, "AddTextListCard_fieldWrapper")]//textarea')

    SAVE_IN_MODAL_BUTTON = (By.XPATH, '//div[contains(@class, "ModalSidebarPage_container")]//button[.//span[text()="Сохранить"]]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(.,"Сохранить")]')

    OK_DIV = (By.XPATH, '//div[contains(.,"Список успешно загружен")]')