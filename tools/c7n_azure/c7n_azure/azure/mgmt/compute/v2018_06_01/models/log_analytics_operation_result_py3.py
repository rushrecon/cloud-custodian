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


class LogAnalyticsOperationResult(Model):
    """LogAnalytics operation status response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar properties: LogAnalyticsOutput
    :vartype properties:
     ~azure.mgmt.compute.v2018_06_01.models.LogAnalyticsOutput
    """

    _validation = {
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'LogAnalyticsOutput'},
    }

    def __init__(self, **kwargs) -> None:
        super(LogAnalyticsOperationResult, self).__init__(**kwargs)
        self.properties = None
