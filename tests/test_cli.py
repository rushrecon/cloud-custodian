# Copyright 2016-2017 Capital One Services, LLC
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

import json
import os
import sys

from argparse import ArgumentTypeError
from datetime import datetime, timedelta

from c7n import cli, version, commands
from c7n.resolver import ValuesFrom
from c7n.resources import aws
from c7n.schema import ElementSchema, generate
from c7n.utils import yaml_dump

from .common import BaseTest, TextTestIO


class CliTest(BaseTest):
    """ A subclass of BaseTest with some handy functions for CLI related tests. """

    def patch_account_id(self):

        def test_account_id(options):
            options.account_id = self.account_id

        self.patch(aws, "_default_account_id", test_account_id)

    def get_output(self, argv):
        """ Run cli.main with the supplied argv and return the output. """
        out, err = self.run_and_expect_success(argv)
        return out

    def capture_output(self):
        out = TextTestIO()
        err = TextTestIO()
        self.patch(sys, "stdout", out)
        self.patch(sys, "stderr", err)
        return out, err

    def run_and_expect_success(self, argv):
        """ Run cli.main() with supplied argv and expect normal execution. """
        self.patch_account_id()
        self.patch(sys, "argv", argv)
        out, err = self.capture_output()
        try:
            cli.main()
        except SystemExit as e:
            self.fail(
                "Expected sys.exit would not be called. Exit code was ({})".format(
                    e.code
                )
            )
        return out.getvalue(), err.getvalue()

    def run_and_expect_failure(self, argv, exit_code):
        """ Run cli.main() with supplied argv and expect exit_code. """
        self.patch_account_id()
        self.patch(sys, "argv", argv)
        out, err = self.capture_output()
        # clear_resources()
        with self.assertRaises(SystemExit) as cm:
            cli.main()
        self.assertEqual(cm.exception.code, exit_code)
        return out.getvalue(), err.getvalue()

    def run_and_expect_exception(self, argv, exception):
        """ Run cli.main() with supplied argv and expect supplied exception. """
        self.patch_account_id()
        self.patch(sys, "argv", argv)
        # clear_resources()
        try:
            cli.main()
        except exception:
            return
        self.fail("Error: did not raise {}.".format(exception))


class SchemaTest(CliTest):

    def test_schema(self):
        pass

    def test_invalid_options(self):
        self.run_and_expect_failure(["custodian", "schema", "ec2.filters.and.foo"], 1)


class ReportTest(CliTest):

    def test_report(self):
        policy_name = "ec2-running-instances"
        valid_policies = {
            "policies": [
                {
                    "name": policy_name,
                    "resource": "ec2",
                    "query": [{"instance-state-name": "running"}],
                }
            ]
        }
        yaml_file = self.write_policy_file(valid_policies)

        output = self.get_output(
            ["custodian", "report", "-s", self.output_dir, yaml_file]
        )
        self.assertIn("InstanceId", output)
        self.assertIn("i-014296505597bf519", output)

        # ASCII formatted test
        output = self.get_output(
            [
                "custodian",
                "report",
                "--format",
                "grid",
                "-s",
                self.output_dir,
                yaml_file,
            ]
        )
        self.assertIn("InstanceId", output)
        self.assertIn("i-014296505597bf519", output)

        # json format
        output = self.get_output(
            ["custodian", "report", "--format", "json", "-s", self.output_dir, yaml_file]
        )
        self.assertTrue("i-014296505597bf519", json.loads(output)[0]['InstanceId'])

        # empty file
        temp_dir = self.get_temp_dir()
        empty_policies = {"policies": []}
        yaml_file = self.write_policy_file(empty_policies)
        self.run_and_expect_failure(
            ["custodian", "report", "-s", temp_dir, yaml_file], 1
        )

        # more than 1 policy
        policies = {
            "policies": [
                {"name": "foo", "resource": "s3"}, {"name": "bar", "resource": "ec2"}
            ]
        }
        yaml_file = self.write_policy_file(policies)
        self.run_and_expect_failure(
            ["custodian", "report", "-s", temp_dir, yaml_file], 1
        )

    def test_warning_on_empty_policy_filter(self):
        # This test is to examine the warning output supplied when -p is used and
        # the resulting policy set is empty.  It is not specific to the `report`
        # subcommand - it is also used by `run` and a few other subcommands.

        policy_name = "test-policy"
        valid_policies = {
            "policies": [
                {
                    "name": policy_name,
                    "resource": "s3",
                    "filters": [{"tag:custodian_tagging": "not-null"}],
                }
            ]
        }
        yaml_file = self.write_policy_file(valid_policies)
        temp_dir = self.get_temp_dir()

        bad_policy_name = policy_name + "-nonexistent"
        log_output = self.capture_logging("custodian.commands")
        self.run_and_expect_failure(
            ["custodian", "report", "-s", temp_dir, "-p", bad_policy_name, yaml_file], 1
        )
        self.assertIn(policy_name, log_output.getvalue())

        bad_resource_name = "foo"
        self.run_and_expect_failure(
            ["custodian", "report", "-s", temp_dir, "-t", bad_resource_name, yaml_file],
            1,
        )


class LogsTest(CliTest):

    def test_logs(self):
        temp_dir = self.get_temp_dir()

        # Test 1 - empty file
        empty_policies = {"policies": []}
        yaml_file = self.write_policy_file(empty_policies)
        self.run_and_expect_failure(["custodian", "logs", "-s", temp_dir, yaml_file], 1)

        # Test 2 - more than one policy
        policies = {
            "policies": [
                {"name": "foo", "resource": "s3"}, {"name": "bar", "resource": "ec2"}
            ]
        }
        yaml_file = self.write_policy_file(policies)
        self.run_and_expect_failure(["custodian", "logs", "-s", temp_dir, yaml_file], 1)

        # Test 3 - successful test
        p_data = {
            "name": "test-policy",
            "resource": "rds",
            "filters": [
                {"key": "GroupName", "type": "security-group", "value": "default"}
            ],
            "actions": [{"days": 10, "type": "retention"}],
        }
        yaml_file = self.write_policy_file({"policies": [p_data]})
        output_dir = os.path.join(os.path.dirname(__file__), "data", "logs")
        self.run_and_expect_success(["custodian", "logs", "-s", output_dir, yaml_file])
