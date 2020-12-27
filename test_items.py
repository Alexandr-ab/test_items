import time

def test_user_should_find_the_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(5)
    cart = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert cart, 'Button "Add to cart" doesn\'t exist'