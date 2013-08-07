#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from psutil import Process
try:
    from psutil import _error
except ImportError:
    from psutil import error as _error
from copy import deepcopy
import re


class ControlDaemon(object):

    __slots__ = ["daemon_name", "actions", "pid", "process", "regex"]
    pattern = r'\d{3,7}'

    def __init__(self, daemon_name):
        self.actions = ["start", "restart", "stop", "status"]
        self.daemon_name = daemon_name
        self.regex = re.compile(self.pattern)
        self.process = list()

    def __repr__(self):
        return self.daemon_name

    def exec_service(self, action_string):
        """
        Execute the command services
        """
        if action_string is 'pid':
            command = ['pgrep', str(self.daemon_name)]
        else:
            command = ['sudo', 'service', str(self.daemon_name),
                       str(action_string)]
        action = sub.Popen(' '.join(command), stdout=sub.PIPE, shell=True)
        (output, error) = action.communicate()
        return error or output

    def know_pid(self):
        """
        Return the pid numbers of the service.
        """
        result_service = self.exec_service('pid')

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
        """
        Do a action, with a action number than
        correspond a index in self.actions list.

        Return the status service
        """
        self.exec_service(self.actions[action])
        self.pid = self.know_pid()
        return self.get_status()

    def start(self):
        """
        Start the service
        """
        return self.do_action(0)

    def restart(self):
        """
        Restart the service
        """
        return self.do_action(1)

    def stop(self):
        """
        Stop the service
        """
        return not self.do_action(2)

    def get_status(self):
        status_dict = {'running': True, 'stopped': False, 'dead': False}
        pattern = r'\b(?:%s)\b' % '|'.join(status_dict.keys())
        regex = re.compile(pattern)
        # Get status from service command
        status_service = self.exec_service(self.actions[3])
        result = regex.search(status_service)
        if result:
            return status_dict[result.group()]
        return False

    def get_memory_usage(self):
        """
        Return memory rss usage
        """
        if self.get_status():
            # Research process thread
            self.pid = self.know_pid()
            mem = 0
            for p in self.process:
                mem += p.get_memory_info()[0] / (1024 ** 2)
            return mem
        return False
