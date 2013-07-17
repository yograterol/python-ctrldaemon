import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import unittest
from ctrldaemon import ControlDaemon


class TestCtrlDaemon(unittest.TestCase):

    def setUp(self):
        self.ctrl_daemon = ControlDaemon("httpd")

    def test_start_service(self):
        self.assertTrue(self.ctrl_daemon.start())

    def test_stop_service(self):
        self.assertTrue(self.ctrl_daemon.stop())

    def test_restart_service(self):
        self.assertTrue(self.ctrl_daemon.restart())

if __name__ == "__main__":
    unittest.main()

