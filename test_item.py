link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, "Button not found"

