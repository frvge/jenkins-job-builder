#!/usr/bin/env python
#
# Copyright 2013 Darragh Bailey
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
from testtools import TestCase
from testscenarios.testcase import TestWithScenarios
from tests.base import get_scenarios, JsonTestCase


class TestCaseLocalYamlInclude(TestWithScenarios, TestCase, JsonTestCase):
    """
    Verify application specific tags independently of any changes to
    modules XML parsing behaviour
    """
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    scenarios = get_scenarios(fixtures_path, 'yaml', 'json')
