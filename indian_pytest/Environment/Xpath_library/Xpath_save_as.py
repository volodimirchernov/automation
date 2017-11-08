# Save as export page


# File list:

positionable_delete_file_button_Xpath = "(.//i[@class='i i-close'])[position]"
# - check count of documents in file list count(xpath)
positionable_view_file_button_Xpath = "(.//i[@class='i i-page-preview'])[position]"
# - check color of element by css selector
positionable_file_list_canvas_Xpath = "(.//div[@class='document-preview__canvas'])[position]"
# - check by equal with icon / check is unknown icon
add_another_document_button_Xpath = ".//div[@class='doc-collaboration-action-btn']"
# - modal is open
positionable_name_of_file__file_list_text_Xpath = "(.//div[@class='doc-collab-list-item__name'])[position]"
# - check by name
positionable_date_of_last_update__file_list_text_Xpath = "(.//div[@class='doc-collab-list-item__date'])[position]"
# - save date and equal

# Select Format and Destination:

format_destination_tab_Xpath = "(.//div[@class='react-panel__header'])[2]"
format_destination_tab_icon_Xpath = ".//div[@class='i i-format large-panel-header__icon']"

# -- Formats

format_pdf_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[1]"
format_word_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[2]"
format_excel_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[3]"
format_presentation_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[4]"

# -- Destinations

destination_desktop_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[5]"
destination_dropbox_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[6]"
destination_google_drive_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[7]"
destination_box_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[8]"
destination_oneDrive_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[9]"

# -- Instructions page link

where_will_my_document_be_saved_Xpath = ".//a[@class='save-configurator-info-link']"

# -- Positionable xpath for formats & destinations

positionable_format_item_Xpath = "(.//label[@class='save-configuration-list-item__content'])[position]"

# Set Export Options

set_export_options_tab_Xpath = "(.//div[@class='react-panel__header'])[3]"
set_export_options_tab_icon_Xpath = ".//div[@class='i i-outline-settings large-panel-header__icon']"

save_with_fillable_fields_switch_Xpath = ".//div[@class='settings-panel']/div/div/div/div[1]/div[2]/div"
save_content_only_switch_Xpath = ".//div[@class='settings-panel']/div/div/div/div[2]/div[2]/div"
add_suffix_to_file_name_Xpath = ".//div[@class='settings-panel']/div/div/div/div[3]/div[2]/div"

# Set Document Security:

set_document_access_security_icon_Xpath = ".//div[@class='i i-security large-panel-header__icon']"

password_input_field_Xpath = ".//div[@class='security-configuration-table-access-control']/input"
eye_password_button_Xpath = ".//button[@class='security-configuration-button']/span"

# Action panel:

cancel_button_Xpath = ".//button[@class='button-back']/span"
save_as_button_Xpath = ".//button[@class='button-apply']/span"

# Preview:

# -- Tab
preview_icon_Xpath = ".//span[@class='i i-page-preview document-viewer-tabs-item__icon']"

# -- Navigation
previous_page_arrow_button_Xpath = ".//div[@class='document-preview-nav']/div[1]"
next_page_arrow_button_Xpath = ".//div[@class='document-preview-nav']/div[2]"

# -- Page position
current_preview_page_position_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[2]/span[1]"
count_of_pages_preview_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[2]/span[2]"

# Select Pages:

# -- Tab
select_pages_icon_Xpath = ".//span[@class='i i-select-pages document-viewer-tabs-item__icon']"

# -- Canvases
positionable_canvas_without_hover_Xpath = "(.//div[@class='page-preview-content'])[position]"
positionable_canvas_check_mark_Xpath = "(.//button[@class='button-page-selection'])[position]"
positionable_canvas_excluded_mark_Xpath = "(.//div[@class='page-preview-selection-indicator'])[position]"

# -- Count of pages with(out) selection
selected_pages_count_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[1]/span[1]"
count_of_pages_select_pages_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[1]/span[2]"

# -- (Un)Select all
select_all_button_Xpath = ".//button[@class='button-filter-pages button-filter-pages-select']"
unselect_all_button_Xpath = ".//button[@class='button-filter-pages button-filter-pages-unselect']"

# Sub header:

help_icon_Xpath = "(.//span[@class='button-help-bar__icon-container'])[1]"
feedback_icon_Xpath = "(.//span[@class='button-help-bar__icon-container'])[2]"

# Timeout modal

refresh_button_Xpath = ".//button[@class='g-btn g-btn--sm g-btn--primary g-btn--auto-width']"

# Max documents modal

ok__max_files_modal_button_Xpath = ".//button[@class='g-btn g-btn-primary g-btn-auto-width']"
x__max_files_modal_icon_Xpath = ".//i[@class='i i-close cm__close']"

# Multi save modal

positionable_name_of_file__multi_save_modal_text_Xpath = "(.//div[@class='file-download-item-main__title']/strong)[position]"
positionable_size_of_file__multi_save_text_Xpath = "(.//span[@class='item-size'])[position]"
positionable_status_of_file__multi_save_text_Xpath = "(.//span[@class='item-status'])[position]"

download_zip__multi_save_button_Xpath = ".//button[@class='g-btn g-btn--primary g-btn--white g-btn--sm']"
positionable_download_single_file__multi_save_button_Xpath = "(.//button[@class='file-action-control'])[position]"

report_a_problem__multi_save_button_Xpath = ".//button[@class='g-btn g-btn--secondary g-btn--auto-width']"
done_go_to_mydocs__multi_save_button_Xpath = ".//button[@class='g-btn g-btn--empty-primary g-btn--auto-width']"
cant_find_your_document__multi_save_text_Xpath = ".//div[@class='download-instruction-link']"
x__multi_save_modal_icon_Xpath = ".//i[@class='i i-close cm__close']"

# Report a Problem

faq__report_modal_tab_icon_Xpath = ".//span[@class='i i-help feedback-module-tab__icon']"
suggestion__report_modal_tab_icon_Xpath = ".//span[@class='i i-suggested-docs feedback-module-tab__icon']"
problem__report_modal_tab_icon_Xpath = ".//span[@class='i i-error feedback-module-tab__icon']"

# File Picker

# -- Common

x__file_picker_icon_Xpath = ".//i[@class='i i-close cm__close']"
title__file_picker_icon_Xpath = ".//div[@class='cm-header__title']"

# -- Tabs

file_picker_active_tab_Xpath = ".//div[@class='g-tabs-list__item g-tabs-list__item--icon is-active']"

# --- Upload document Tab (is active by default)

upload_document__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[1]"
upload_document__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-upload']"
upload_document__file_picker_tab_text_Xpath = "(.//div[@class='g-tabs-list__item-title'])[1]"

# ---- In Upload Document Tab

drag_drop__file_picker__upload_document_zone_Xpath = ".//div[@class='crop-body-upload__inner']"
drag_drop__file_picker__upload_document_title_Xpath = ".//div[@class='crop-body__title']"
drag_drop__file_picker__upload_document_description_Xpath = ".//div[@class='crop-body__small-title']"
drag_drop__file_picker__upload_document_button_Xpath = ".//div[@class='js-fileapi-wrapper g-btn g-btn-primary g-btn-auto-width']"

active_source__file_picker__upload_document_item_Xpath = ".//div[@class='docs-manage-upload-tabs__item is-active']"

desktop_source__file_picker__upload_document_icon_Xpath = ".//div[@class='docs-manage-sprite-laptop docs-manage-upload-tabs-icon-desktop']"
dropbox_source__file_picker__upload_document_icon_Xpath = ".//div[@class='docs-manage-sprite-dropbox docs-manage-upload-tabs-icon-desktop']"

# --- Get From MYBOX Tab

get_from_mybox__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[2]"
get_from_mybox__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-mybox']"
get_from_mybox__file_picker_tab_title_Xpath = "(.//div[@class='g-tabs-list__item-title'])[2]"

# --- Get From INBOX Tab

get_from_inbox__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[3]"
get_from_inbox__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-inbox']"
get_from_inbox__file_picker_tab_title_Xpath = "(.//div[@class='g-tabs-list__item-title'])[3]"

# --- Search for Documents Tab

search_for_documents__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[4]"
search_for_documents__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-search']"
search_for_documents__file_picker_tab_title_Xpath = "(.//div[@class='g-tabs-list__item-title'])[4]"

# ---- In Get From "Source" Tab

# ----- Common & Universal

positionable_source__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[position]"
positionable_source__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[position]"
positionable_source__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[position]"

active__file_picker__get_from_source_item_Xpath = ".//div[@class='mf-menuItem is-active']"

# ----- All Documents

all_documents__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[1]"
all_documents__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-mybox']"
all_documents__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[1]"
all_documents__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[1]"

# ----- Unsorted

unsorted__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item']])[2]"
unsorted__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-unsorted']"
unsorted__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[2]"
unsorted__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[2]"

# ----- Other

custom_folder__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-folder']"

# ---- In Get From INBOX Tab

# ----- Received Email

received_email__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[1]"
received_email__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-email']"
received_email__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[1]"
received_email__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[1]"

# ----- Received Faxes

received_faxes__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[2]"
received_faxes__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-fax']"
received_faxes__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[2]"
received_faxes__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[2]"

# ----- Received LinkToFill

link_to_fill__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[3]"
link_to_fill__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-linktofill']"
link_to_fill__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[3]"
link_to_fill__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[3]"

# ---- Search for Documents

title__file_picker__search_for_documents_text_Xpath = ".//div[@class='docs-manage-page__title']"
description__file_picker__search_for_documents_text_Xpath = ".//div[@class='docs-manage-page__description']"
document_name__file_picker__search_for_documents_input_field_Xpath = ".//input[@class='g-form-control']"
search_disabled__file_picker__search_for_documents_button_Xpath = ".//button[@class='g-btn g-btn--primary disabled']"
search_enabled__file_picker__search_for_documents_button_Xpath = ".//button[@class='g-btn g-btn--primary']"

# ------ List of documents

# ------- Common & Universal

# scroll bar
scroll_bar_documents__file_picker__get_from_source_item_Xpath = "(.//div[@class='react-scrollbar__vertical-thumb'])[4]"

# pagination (first page is active by default)
active_pagination_documents__file_picker__get_from_source_item_Xpath = ".//li[@class='mf-pagination__numbersItem is-active']"
positionable_pagination_documents__file_picker__get_from_source_item_Xpath = "(.//li[@class='mf-pagination__numbersItem'])[position]"

# document list
positionable_pdf_document__file_picker__get_from_source_item_Xpath = ".//div[@class='mf-doc__name file-icon pdf']"
positionable_docx_document__file_picker__get_from_source_item_Xpath = ".//div[@class='mf-doc__name file-icon doc']"
positionable_pptx_document__file_picker__get_from_source_item_Xpath = ".//div[@class='mf-doc__name file-icon ppt']"
positionable_htm_document__file_picker__get_from_source_item_Xpath = ".//div[@class='mf-doc__name file-icon base']"
positionable_unavailable_document__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[position]"
positionable_disabled_document__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item is-disabled'])[position]"
positionable_document__file_picker__get_from_source_text_Xpath = "(.//div[@class='mf-doc__name file-icon doc'])[position]"
positionable_document__file_picker__get_from_source_date_Xpath = "(.//time[@class='mf-doc__date'])[position]"

# empty document list

empty_list__file_picker__get_from_source_icon_fax_Xpath = ".//div[@class='mf-info-banner__icon docs-manage-sprite-fax']"
empty_list__file_picker__get_from_source_title_Xpath = ".//div[@class='mf-info-banner__title']"
empty_list__file_picker__get_from_source_description_Xpath = ".//div[@class='mf-info-banner__desc']"


