from api.dependency import *


@test(groups=['ip_api', 'test_ip_api_json'])
class TestIpApiJson(unittest.TestCase):
    """
    Verify JSON API for ip-api.com
    """
    def setUp(self):
        self.step = Steps(self.__class__.__doc__)
        self.data = drive_data(os.path.dirname(sys.modules[self.__class__.__module__].__file__)+"/drivedata.csv")

    def test_ip_api_json(self):
        self.step.step('Verify JSON API')
        for ip in self.data['ip']:
            r = rest_get('http://ip-api.com/json/' + ip)
            self.step.info(r)
            assert_equal(r['status'], 'success')

    def tearDown(self):
        self.step.step('Tear Down')
