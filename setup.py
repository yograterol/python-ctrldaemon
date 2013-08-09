"""
Copyright (c) 2013, Yohan Graterol
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

  Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

  Neither the name of the Yohan Graterol  nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from setuptools import setup, find_packages

f = open('README.md')
try:
    README = f.read()
finally:
    f.close()

setup (name='ctrldaemon',
       version="0.2",
       description="Service command wrapper for Python.",
       long_description=README,
       packages=find_packages(exclude=['tests']),
       include_package_data=True,
       test_suite='nose.collector',
       author="Yohan Graterol",
       author_email="yograterol@fedoraproject.org",
       download_url="https://github.com/yograterol/python-ctrldaemon",
       license="BSD License",
       url="http://www.yograterol.me",
       zip_safe=False,
       package_data={
                 'ctrldaemon': ['LICENSE', 'README.md'],
              },
       tests_require=['nose',],
       install_requires=['psutil'],
       )

