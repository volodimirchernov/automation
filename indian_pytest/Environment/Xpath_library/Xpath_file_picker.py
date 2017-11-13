"""
File Picker
"""

"""
- Common
"""

x__file_picker_icon_Xpath = ".//i[@class='i i-close cm__close']"
title__file_picker_icon_Xpath = ".//div[@class='cm-header__title']"

"""
- Tabs
"""

file_picker_active_tab_Xpath = ".//div[@class='g-tabs-list__item g-tabs-list__item--icon is-active']"

"""
-- Upload document Tab (is active by default)
"""

upload_document__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[1]"
upload_document__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-upload']"
upload_document__file_picker_tab_text_Xpath = "(.//div[@class='g-tabs-list__item-title'])[1]"

"""
--- In Upload Document Tab
"""

drag_drop__file_picker__upload_document_zone_Xpath = ".//div[@class='crop-body-upload__inner']"
drag_drop__file_picker__upload_document_title_Xpath = ".//div[@class='crop-body__title']"
drag_drop__file_picker__upload_document_description_Xpath = ".//div[@class='crop-body__small-title']"
drag_drop__file_picker__upload_document_button_Xpath = ".//div[@class='js-fileapi-wrapper g-btn g-btn-primary g-btn-auto-width']"

active_source__file_picker__upload_document_item_Xpath = ".//div[@class='docs-manage-upload-tabs__item is-active']"

desktop_source__file_picker__upload_document_icon_Xpath = ".//div[@class='docs-manage-sprite-laptop docs-manage-upload-tabs-icon-desktop']"
dropbox_source__file_picker__upload_document_icon_Xpath = ".//div[@class='docs-manage-sprite-dropbox docs-manage-upload-tabs-icon-desktop']"

"""
--- Get From MYBOX Tab
"""

get_from_mybox__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[2]"
get_from_mybox__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-mybox']"
get_from_mybox__file_picker_tab_title_Xpath = "(.//div[@class='g-tabs-list__item-title'])[2]"

"""
-- Get From INBOX Tab
"""

get_from_inbox__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[3]"
get_from_inbox__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-inbox']"
get_from_inbox__file_picker_tab_title_Xpath = "(.//div[@class='g-tabs-list__item-title'])[3]"

"""
-- Search for Documents Tab
"""

search_for_documents__file_picker_tab_item_Xpath = "(.//div[@class='g-tabs-list__item g-tabs-list__item--icon'])[4]"
search_for_documents__file_picker_tab_icon_Xpath = ".//div[@class='g-tabs-list__item-icon docs-manage-tab-icon-search']"
search_for_documents__file_picker_tab_title_Xpath = "(.//div[@class='g-tabs-list__item-title'])[4]"

"""
--- In Get From "Source" Tab
"""

"""
---- Common & Universal
"""

positionable_source__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[position]"
positionable_source__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[position]"
positionable_source__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[position]"

active__file_picker__get_from_source_item_Xpath = ".//div[@class='mf-menuItem is-active']"

"""
---- All Documents
"""

all_documents__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[1]"
all_documents__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-mybox']"
all_documents__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[1]"
all_documents__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[1]"

"""
---- Unsorted
"""

unsorted__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item']])[2]"
unsorted__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-unsorted']"
unsorted__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[2]"
unsorted__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[2]"

"""
---- Other
"""

custom_folder__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-folder']"

"""
--- In Get From INBOX Tab
"""

"""
---- Received Email
"""

received_email__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[1]"
received_email__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-email']"
received_email__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[1]"
received_email__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[1]"

"""
---- Received Faxes
"""

received_faxes__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[2]"
received_faxes__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-fax']"
received_faxes__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[2]"
received_faxes__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[2]"

"""
---- Received LinkToFill
"""

link_to_fill__file_picker__get_from_source_item_Xpath = "(.//div[@class='mf-doc__item'])[3]"
link_to_fill__file_picker__get_from_source_icon_Xpath = ".//i[@class='i i-linktofill']"
link_to_fill__file_picker__get_from_source_title_Xpath = "(.//div[@class='mf-menuItem__title'])[3]"
link_to_fill__file_picker__get_from_source_count_Xpath = "(.//div[@class='mf-counter'])[3]"

"""
--- Search for Documents
"""

title__file_picker__search_for_documents_text_Xpath = ".//div[@class='docs-manage-page__title']"
description__file_picker__search_for_documents_text_Xpath = ".//div[@class='docs-manage-page__description']"
document_name__file_picker__search_for_documents_input_field_Xpath = ".//input[@class='g-form-control']"
search_disabled__file_picker__search_for_documents_button_Xpath = ".//button[@class='g-btn g-btn--primary disabled']"
search_enabled__file_picker__search_for_documents_button_Xpath = ".//button[@class='g-btn g-btn--primary']"

"""
---- Search results
"""

# Search Results (count)
results_title__file_picker__search_for_documents_text_Xpath = ".//div[@class='docs-manage-search-result-header__title']"
results_back__file_picker__search_for_documents_button_Xpath = ".//button[@class='g-btn g-btn--link']"
results_back__file_picker__search_for_documents_button_icon_Xpath = "(.//i[@class='i i-prev'])[3]"
no_results__file_picker__search_for_documents_icon_Xpath = ".//div[@class='docs-manage-sprite-no-result']"

"""
----- List of documents
"""

"""
------ Common & Universal
"""

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
