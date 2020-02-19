# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RunFilter(Model):
    """Properties that are enabled for Odata querying on runs.

    :param run_id: The unique identifier for the run.
    :type run_id: str
    :param run_type: The type of run. Possible values include: 'QuickBuild',
     'QuickRun', 'AutoBuild', 'AutoRun'
    :type run_type: str or
     ~azure.mgmt.containerregistry.v2019_04_01.models.RunType
    :param status: The current status of the run. Possible values include:
     'Queued', 'Started', 'Running', 'Succeeded', 'Failed', 'Canceled',
     'Error', 'Timeout'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_04_01.models.RunStatus
    :param create_time: The create time for a run.
    :type create_time: datetime
    :param finish_time: The time the run finished.
    :type finish_time: datetime
    :param output_image_manifests: The list of comma-separated image manifests
     that were generated from the run. This is applicable if the run is of
     build type.
    :type output_image_manifests: str
    :param is_archive_enabled: The value that indicates whether archiving is
     enabled or not.
    :type is_archive_enabled: bool
    :param task_name: The name of the task that the run corresponds to.
    :type task_name: str
    """

    _attribute_map = {
        'run_id': {'key': 'runId', 'type': 'str'},
        'run_type': {'key': 'runType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'create_time': {'key': 'createTime', 'type': 'iso-8601'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'output_image_manifests': {'key': 'outputImageManifests', 'type': 'str'},
        'is_archive_enabled': {'key': 'isArchiveEnabled', 'type': 'bool'},
        'task_name': {'key': 'taskName', 'type': 'str'},
    }

    def __init__(self, *, run_id: str=None, run_type=None, status=None, create_time=None, finish_time=None, output_image_manifests: str=None, is_archive_enabled: bool=None, task_name: str=None, **kwargs) -> None:
        super(RunFilter, self).__init__(**kwargs)
        self.run_id = run_id
        self.run_type = run_type
        self.status = status
        self.create_time = create_time
        self.finish_time = finish_time
        self.output_image_manifests = output_image_manifests
        self.is_archive_enabled = is_archive_enabled
        self.task_name = task_name
