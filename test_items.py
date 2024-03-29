import time

"""
pytest -s --language=es test_items.py
pytest -s --language=fr test_items.py
"""


def test_user_should_see_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_cart_button = browser.find_element_by_css_selector('button[class*="btn-add-to-basket"]')
    print(f'\nText on add_to_cart_button = "{add_to_cart_button.text}"')
    time.sleep(30)
