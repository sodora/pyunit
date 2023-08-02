from api.dependency import *


@test(groups=['baidu', 'test_baidu_input'])
class TestBaiduInput(unittest.TestCase):
    """
    Verify search result for baidu.com
    """
    def setUp(self):
        self.step = Steps(self.__class__.__doc__)
        self.data = drive_data(os.path.dirname(sys.modules[self.__class__.__module__].__file__) + "/drivedata.csv")
        self.selenium = Selenium()

    def test_baidu_input(self):
        self.step.step('Open baidu home page')
        self.selenium.open_url(self.data['url'][0])
        self.step.step('Input keyword')
        self.selenium.driver.find_element(self.data['search_input_id'][0],self.data['search_input_id'][1]).send_keys('selenium')
        self.step.step('Click search button')
        self.selenium.driver.find_element(self.data['search_button_id'][0], self.data['search_button_id'][1]).click()
        self.step.step('Wait for search result')
        self.selenium.wait_until(self.data['search_result_container_id'],10)
        self.step.step('Verify the title in search result page')
        title = self.selenium.title()
        self.step.info('Title: %s' % title)
        assert_true('selenium' in title)

    def tearDown(self):
        self.step.step('Tear Down')
        self.selenium.quit()
