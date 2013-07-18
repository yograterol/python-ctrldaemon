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

    def test_get_memory_usage(self):
        self.ctrl_daemon.start()
        self.assertGreater(self.ctrl_daemon.get_memory_usage(), 0)

    def test_get_status(self):
        self.ctrl_daemon.stop()
        # Is stop service?
        self.assertFalse(self.ctrl_daemon.get_status())

        self.ctrl_daemon.start()
        # Is running service?
        self.assertTrue(self.ctrl_daemon.get_status())

if __name__ == "__main__":
    unittest.main()

