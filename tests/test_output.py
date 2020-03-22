# Copyright 2015-2018 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function, unicode_literals

import datetime
import gzip
import logging
import mock
import shutil
import os

from dateutil.parser import parse as date_parse

from c7n.ctx import ExecutionContext
from c7n.config import Config
from c7n.output import DirectoryOutput, LogFile, metrics_outputs
from c7n.resources.aws import S3Output, MetricsOutput
from c7n.testing import mock_datetime_now, TestUtils

from .common import Bag, BaseTest


class S3OutputTest(TestUtils):

    def test_join_leave_log(self):
        temp_dir = self.get_temp_dir()
        output = LogFile(Bag(log_dir=temp_dir), {})
        output.join_log()

        l = logging.getLogger("custodian.s3") # NOQA

        # recent versions of nose mess with the logging manager
        v = l.manager.disable
        l.manager.disable = 0

        l.info("hello world")
        output.leave_log()
        logging.getLogger("c7n.s3").info("byebye")

        # Reset logging.manager back to nose configured value
        l.manager.disable = v

        with open(os.path.join(temp_dir, "custodian-run.log")) as fh:
            content = fh.read().strip()
            self.assertTrue(content.endswith("hello world"))
