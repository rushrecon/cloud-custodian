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


class EffectiveRouteListResult(Model):
    """Response for list effective route API service call.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param value: A list of effective routes.
    :type value: list[~azure.mgmt.network.v2018_11_01.models.EffectiveRoute]
    :ivar next_link: The URL to get the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EffectiveRoute]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EffectiveRouteListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None
