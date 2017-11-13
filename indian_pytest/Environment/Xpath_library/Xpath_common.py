"""
File list Xpath locators:
"""

"""
File List
"""

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

"""
Action panel (Save/Print):
"""

cancel_button_Xpath = ".//button[@class='button-back']/span"
main_action_button_Xpath = ".//button[@class='button-apply']/span"

"""
Preview:
"""

"""
- Tab
"""
preview_icon_Xpath = ".//span[@class='i i-page-preview document-viewer-tabs-item__icon']"

"""
- Navigation
"""
previous_page_arrow_button_Xpath = ".//div[@class='document-preview-nav']/div[1]"
next_page_arrow_button_Xpath = ".//div[@class='document-preview-nav']/div[2]"

"""
- Page position
"""
current_preview_page_position_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[2]/span[1]"
count_of_pages_preview_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[2]/span[2]"

"""
Select Pages:
"""

"""
- Tab
"""
select_pages_icon_Xpath = ".//span[@class='i i-select-pages document-viewer-tabs-item__icon']"

"""
- Canvases
"""

positionable_canvas_without_hover_Xpath = "(.//div[@class='page-preview-content'])[position]"
positionable_canvas_check_mark_Xpath = "(.//button[@class='button-page-selection'])[position]"
positionable_canvas_excluded_mark_Xpath = "(.//div[@class='page-preview-selection-indicator'])[position]"

"""
- Count of pages with(out) selection
"""

selected_pages_count_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[1]/span[1]"
count_of_pages_select_pages_text_Xpath = "(.//div[@class='document-viewer-info-container__body'])[1]/span[2]"

"""
- (Un)Select all
"""

select_all_button_Xpath = ".//button[@class='button-filter-pages button-filter-pages-select']"
unselect_all_button_Xpath = ".//button[@class='button-filter-pages button-filter-pages-unselect']"

"""
Sub header:
"""

help_icon_Xpath = "(.//span[@class='button-help-bar__icon-container'])[1]"
feedback_icon_Xpath = "(.//span[@class='button-help-bar__icon-container'])[2]"

"""
Modals
"""

"""
- Max documents modal
"""

ok__max_files_modal_button_Xpath = ".//button[@class='g-btn g-btn-primary g-btn-auto-width']"
x__max_files_modal_icon_Xpath = ".//i[@class='i i-close cm__close']"

"""
- Report a Problem
"""

faq__report_modal_tab_icon_Xpath = ".//span[@class='i i-help feedback-module-tab__icon']"
suggestion__report_modal_tab_icon_Xpath = ".//span[@class='i i-suggested-docs feedback-module-tab__icon']"
problem__report_modal_tab_icon_Xpath = ".//span[@class='i i-error feedback-module-tab__icon']"
