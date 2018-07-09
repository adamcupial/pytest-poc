# Local imports
from .page_object import HomepagePageObject


class TestHomepage(object):

    URL = 'http://www.goal.com/en'
    PAGE_OBJECT_CLASS = HomepagePageObject

    def test_title(self):
        """ check if title matches """

        assert self.page_object.title == \
            'Football News, Live Scores, Results & Transfers | Goal.com'

    def test_description(self):
        """ check if meta description matches """
        assert self.page_object.description == '''The latest football news, live scores, results, rumours, transfers, fixtures, tables and player profiles from around the world, including World Cup.'''
