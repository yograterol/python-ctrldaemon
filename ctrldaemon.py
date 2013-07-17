"""
Copyright (c) 2013 Yohan Graterol <yograterol@fedoraproject.org>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""
import subprocess as sub
from psutil import (Process, _error)
from copy import deepcopy
import re


class ControlDaemon(object):

    __slots__ = ["daemon_name", "actions", "pid", "process", "regex"]
    pattern = r'\d{3,7}'

    def __init__(self, daemon_name):
        self.actions = ["start", "restart", "stop", "status"]
        self.daemon_name = daemon_name
        self.regex = re.compile(self.pattern)

    def exec_service(self, action_string):
        """
        Execute the command services
        """
        action = sub.Popen("sudo service {} {}".format(str(self.daemon_name),
                                                       str(action_string)),
                           stdout=sub.PIPE, shell=True)
        (output, error) = action.communicate()
        return error or output

    def know_pid(self):
        """
        Return the pid numbers of the service.
        """
        result_service = self.exec_service(self.actions[3])
        pid = self.regex.findall(result_service)
        if pid:
            tmp_pid = deepcopy(pid)
            self.process = list()
            for p in tmp_pid:
                try:
                    proc = Process(int(p))
                    self.process.append(proc)
                except _error.NoSuchProcess:
                    pid.remove(p)
        return pid

    def do_action(self, action):
        self.exec_service(self.actions[action])
        self.pid = self.know_pid()

        if self.process:
            return True
        elif not self.process and action == 2:
            return True
        else:
            return False

    def start(self):
        return self.do_action(0)

    def restart(self):
        return self.do_action(1)

    def stop(self):
        return self.do_action(2)
