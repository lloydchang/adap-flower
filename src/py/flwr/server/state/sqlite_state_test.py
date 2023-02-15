# Copyright 2020 Adap GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Test for utility functions."""
# pylint: disable=no-self-use, invalid-name, disable=R0904

import unittest

from flwr.proto.node_pb2 import Node
from flwr.proto.task_pb2 import Task, TaskIns, TaskRes

from .sqlite_state import task_ins_to_dict
from .state_test import create_task_ins, create_task_res

INS_KEYS = [
    "task_id",
    "group_id",
    "workload_id",
    "producer_anonymous",
    "producer_node_id",
    "consumer_anonymous",
    "consumer_node_id",
    "created_at",
    "delivered_at",
    "ttl",
    "ancestry",
    "legacy_server_message",
    "legacy_client_message",
]

class SqliteStateTest(unittest.TestCase):
    """Test utilitiy functions."""

    def test_ins_res_to_dict(self) -> None:
        """Validate that a new state has no TaskIns."""

        # Prepare
        ins_res = create_task_ins(consumer_node_id=1, anonymous=True)

        # Execute
        result = task_ins_to_dict(ins_res)

        # Assert
        for key in INS_KEYS:
            assert key in result.keys()

if __name__ == "__main__":
    unittest.main(verbosity=2)
