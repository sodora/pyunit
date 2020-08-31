from api.dependency import *


@test(groups=['ip_api', 'test_ip_api_batch'])
class TestIpApiBatch(unittest.TestCase):
    """
    Verify BATCH API for ip-api.com
    """
    def setUp(self):
        self.step = Steps(self.__class__.__doc__)
        self.data = drive_data(os.path.dirname(sys.modules[self.__class__.__module__].__file__) + "/drivedata.csv")

    def test_ip_api_batch(self):
        self.step.step('Verify BATCH API')
        rs = rest_post('http://ip-api.com/batch', self.data['ip'])
        for r in rs:
            self.step.info(r)
            assert_equal(r['status'], 'success')

    def tearDown(self):
        self.step.step('Tear Down')
