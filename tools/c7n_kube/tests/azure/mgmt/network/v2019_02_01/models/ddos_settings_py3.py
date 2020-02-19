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


class DdosSettings(Model):
    """Contains the DDoS protection settings of the public IP.

    :param ddos_custom_policy: The DDoS custom policy associated with the
     public IP.
    :type ddos_custom_policy:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param protection_coverage: The DDoS protection policy customizability of
     the public IP. Only standard coverage will have the ability to be
     customized. Possible values include: 'Basic', 'Standard'
    :type protection_coverage: str or
     ~azure.mgmt.network.v2019_02_01.models.DdosSettingsProtectionCoverage
    """

    _attribute_map = {
        'ddos_custom_policy': {'key': 'ddosCustomPolicy', 'type': 'SubResource'},
        'protection_coverage': {'key': 'protectionCoverage', 'type': 'str'},
    }

    def __init__(self, *, ddos_custom_policy=None, protection_coverage=None, **kwargs) -> None:
        super(DdosSettings, self).__init__(**kwargs)
        self.ddos_custom_policy = ddos_custom_policy
        self.protection_coverage = protection_coverage
