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


class AzureFirewallNatRCAction(Model):
    """AzureFirewall NAT Rule Collection Action.

    :param type: The type of action. Possible values include: 'Snat', 'Dnat'
    :type type: str or
     ~azure.mgmt.network.v2018_08_01.models.AzureFirewallNatRCActionType
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureFirewallNatRCAction, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
