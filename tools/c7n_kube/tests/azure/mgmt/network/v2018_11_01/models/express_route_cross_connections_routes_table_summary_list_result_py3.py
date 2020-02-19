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


class ExpressRouteCrossConnectionsRoutesTableSummaryListResult(Model):
    """Response for ListRoutesTable associated with the Express Route Cross
    Connections.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param value: A list of the routes table.
    :type value:
     list[~azure.mgmt.network.v2018_11_01.models.ExpressRouteCrossConnectionRoutesTableSummary]
    :ivar next_link: The URL to get the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ExpressRouteCrossConnectionRoutesTableSummary]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(ExpressRouteCrossConnectionsRoutesTableSummaryListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = None
