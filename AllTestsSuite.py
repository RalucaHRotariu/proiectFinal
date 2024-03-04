import unittest

from HtmlTestRunner import HTMLTestRunner

from TestCart import TestCart
from TestFavorites import TestsFavorites
from TestLogin import TestsLogin


def test_suite():
    suite = unittest.TestSuite()
    # Add Login tests
    suite.addTest(TestsLogin('test_login_incorrect_password'))
    suite.addTest(TestsLogin('test_login_confirm_button_not_available'))
    suite.addTest(TestsLogin('test_login_ok'))
    # Add Favorites tests
    suite.addTest(TestsFavorites('test_favorites_empty'))
    suite.addTest(TestsFavorites('test_add_item_to_favorites'))
    suite.addTest(TestsFavorites('test_remove_item_from_favorites'))
    suite.addTest(TestsFavorites('test_move_from_favorites_to_Cart'))
    # # Add Cart tests
    suite.addTest(TestCart('test_cart_empty'))
    suite.addTest(TestCart('test_add_item_to_cart'))
    suite.addTest(TestCart('test_remove_from_cart'))
    return suite


class AllTestsSuite:
    if __name__ == '__main__':

        runner = HTMLTestRunner(output='report',
                                combine_reports=True,
                                report_title='Test Results',
                                report_name='Automated Test Results')
        suite = test_suite()
        runner.run(suite)
