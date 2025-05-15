from selenium.webdriver.common.by import By

class AudienceAddAudiencePageLocators:
    ADD_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить источник")]')
    EXCLUDE_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Исключить источник")]')

    AUDIENCE_NAME_INPUT = (By.XPATH, '//section[contains(@class, "CreateSegmentModal_form")]//input[@class[contains(., "vkuiInput__el")]]')

    USERLIST_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Список пользователей")]]')
    CREATE_NEW_LIST = (By.XPATH, '//div[@id="tab-create-from-user-list-new"]')
    LIST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название списка"]')
    LIST_TYPE_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][.//h5[text()="Тип списка"]]//input')
    UPLOAD_FILE = (By.XPATH, '//label[contains(@class, "LocalFileSelector_file__")]//input[@type="file"]')

    AUDIENCE_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Уже созданная аудитория")]]')
    AUDIENCE_TO_ADD_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][.//h5[text()="Аудитория"]]//input')
    OPTION = (By.XPATH, '//div[contains(@class, "Segment_option")]')

    EVENTS_FROM_ANNOUNCEMENTS_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "События в моих объявлениях")]]')

    MOBILE_CATEGORIES_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Категории мобильного приложения")]]')

    EVENTS_FROM_LEAD_FORMS_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "События в лид-форме")]]')

    KEY_PHRASES_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Вводили ключевые фразы")]]')
    KEY_PHRASES_INPUT = (By.XPATH, '//h5[contains(., "Ключевые фразы")]/following::textarea[1]')

    COMMUNITY_SUBSCRIBERS_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Подписчики сообществ")]]')
    COMMUNITY_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название сообщества"]')
    SELECT_ALL_COMMUNTIES_BUTTON = (By.XPATH, '//div[@id="react-collapsed-toggle-:r3v:"]//div[@class="GroupHeader_selectAll__kkZtN"]')
    MODAL_SECTION = (By.XPATH, '//section[contains(@class, "SelectSourceModal_groupSourceWrapper")]')
    ADD_BY_LIST_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Добавить списком")]]')
    VK_COMMUNITIES_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiActionSheetItem")]//span[text()="Сообщества ВКонтакте"]')
    TEXTAREA = (By.XPATH, '//div[contains(@class, "AddGroupsListModal_content")]//textarea[contains(@class, "vkuiTextarea__el")]')
    ADD_BUTTON = (By.XPATH, '//form//div[contains(@class, "AddTextListCard_footerContent")]//button')
    CLOSE_MODAL = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton")]')
    ADDED_COMMUNITY = (By.XPATH, '//div[contains(@class, "Selected_item") and contains(.., "Авторская керамика | Сон Совы")]')

    LISTENERS_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Слушатели музыкантов")]]')
    MUSICIAN_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название музыканта"]')
    CHOSEN_MUSICIAN = (By.XPATH, '//div[contains(@class, "VariantsListItem_name") and contains(.., "Lizer")]')
    COMPLETE_BUTTON = (By.XPATH, '//button[contains(@class, "SearchInputDropdown_dropdownActionLink")]')

    VK_MINI_APPS_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Пользуются VK Mini Apps")]]')
    LOAD_BY_LIST_BUTTON = (By.XPATH, '//button[.//span[contains(text(), "Загрузить списком")]]')
    APPS_TEXTAREA = (By.XPATH, '//div[contains(@class, "AddTextListCard_fieldWrapper")]//textarea')

    SAVE_IN_MODAL_BUTTON = (By.XPATH, '//div[contains(@class, "ModalSidebarPage_container")]//button[.//span[text()="Сохранить"]]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(.,"Сохранить")]')