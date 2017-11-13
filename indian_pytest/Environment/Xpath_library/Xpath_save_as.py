"""
Save as export page
"""

"""
Select Format and Destination:
"""

format_destination_tab_Xpath = "(.//div[@class='react-panel__header'])[2]"
format_destination_tab_icon_Xpath = ".//div[@class='i i-format large-panel-header__icon']"

"""
- Formats
"""

format_pdf_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[1]"
format_word_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[2]"
format_excel_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[3]"
format_presentation_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[4]"

"""
- Destinations
"""

destination_desktop_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[5]"
destination_dropbox_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[6]"
destination_google_drive_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[7]"
destination_box_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[8]"
destination_oneDrive_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[9]"

"""
- Instructions page link
"""

where_will_my_document_be_saved_link_text_Xpath = ".//a[@class='save-configurator-info-link']"

"""
- Positionable xpath for formats & destinations
"""

positionable_format_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[position]"

"""
Set Export Options
"""

set_export_options_tab_Xpath = "(.//div[@class='react-panel__header'])[3]"
set_export_options_tab_icon_Xpath = ".//div[@class='i i-outline-settings large-panel-header__icon']"

save_with_fillable_fields_switch_Xpath = ".//div[@class='settings-panel']/div/div/div/div[1]/div[2]/div"
save_content_only_switch_Xpath = ".//div[@class='settings-panel']/div/div/div/div[2]/div[2]/div"
add_suffix_to_file_name_Xpath = ".//div[@class='settings-panel']/div/div/div/div[3]/div[2]/div"

"""
Set Document Security:
"""

set_document_access_security_icon_Xpath = ".//div[@class='i i-security large-panel-header__icon']"

password_input_field_Xpath = ".//div[@class='security-configuration-table-access-control']/input"
eye_password_button_Xpath = ".//button[@class='security-configuration-button']/span"

"""
Modals
"""

"""
- Timeout modal
"""

timeout_modal_icon_Xpath = ".//div[@class='cm__icon cm__icon--connection-lost']"
timeout_modal_title_Xpath = ".//div[@class='cm__title']"
timeout_modal_description_Xpath = ".//div[@class='cm__text']"
timeout_modal_refresh_button_Xpath = ".//button[@class='g-btn g-btn--sm g-btn--primary g-btn--auto-width']"

"""
- Multi save modal
"""

positionable_name_of_file__multi_save_modal_text_Xpath = "(.//div[@class='file-download-item-main__title']/strong)[position]"
positionable_size_of_file__multi_save_text_Xpath = "(.//span[@class='item-size'])[position]"
positionable_status_of_file__multi_save_text_Xpath = "(.//span[@class='item-status'])[position]"

download_zip__multi_save_button_Xpath = ".//button[@class='g-btn g-btn--primary g-btn--white g-btn--sm']"
positionable_download_single_file__multi_save_button_Xpath = "(.//button[@class='file-action-control'])[position]"

report_a_problem__multi_save_button_Xpath = ".//button[@class='g-btn g-btn--secondary g-btn--auto-width']"
done_go_to_mydocs__multi_save_button_Xpath = ".//button[@class='g-btn g-btn--empty-primary g-btn--auto-width']"
cant_find_your_document__multi_save_text_Xpath = ".//div[@class='download-instruction-link']"
x__multi_save_modal_icon_Xpath = ".//i[@class='i i-close cm__close']"



