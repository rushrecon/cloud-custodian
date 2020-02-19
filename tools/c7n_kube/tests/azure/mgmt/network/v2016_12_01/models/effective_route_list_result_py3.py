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

    :param value: A list of effective routes.
    :type value: list[~azure.mgmt.network.v2016_12_01.models.EffectiveRoute]
    :param next_link: The URL to get the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EffectiveRoute]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value=None, next_link: str=None, **kwargs) -> None:
        super(EffectiveRouteListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
