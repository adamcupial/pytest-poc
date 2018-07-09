# Third party modules
from elementium.drivers.se import SeElements

# Own
import pytest


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = '{0} -> {1}'.format(pref, suf)


@pytest.fixture(scope='session', autouse=True)
def driver_get(request):
    from selenium import webdriver
    driver = SeElements(webdriver.Chrome())
    session = request.node

    def exit():
        driver.browser.close()
        driver.browser.quit()

    request.addfinalizer(exit)

    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, 'driver', driver)


@pytest.fixture(scope='class', autouse=True)
def get_page_object(request):
    if callable(getattr(request.cls, 'get_url', None)):
        request.cls.driver.navigate(request.cls.get_url())
    elif getattr(request.cls, 'URL', None):
        request.cls.driver.navigate(request.cls.URL)

    if getattr(request.cls, 'PAGE_OBJECT_CLASS', None):
        setattr(request.cls, 'page_object', request.cls.PAGE_OBJECT_CLASS(request.cls.driver))
