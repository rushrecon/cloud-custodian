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


class ProtocolCustomSettingsFormat(Model):
    """DDoS custom policy properties.

    :param protocol: The protocol for which the DDoS protection policy is
     being customized. Possible values include: 'Tcp', 'Udp', 'Syn'
    :type protocol: str or
     ~azure.mgmt.network.v2018_12_01.models.DdosCustomPolicyProtocol
    :param trigger_rate_override: The customized DDoS protection trigger rate.
    :type trigger_rate_override: str
    :param source_rate_override: The customized DDoS protection source rate.
    :type source_rate_override: str
    :param trigger_sensitivity_override: The customized DDoS protection
     trigger rate sensitivity degrees. High: Trigger rate set with most
     sensitivity w.r.t. normal traffic. Default: Trigger rate set with moderate
     sensitivity w.r.t. normal traffic. Low: Trigger rate set with less
     sensitivity w.r.t. normal traffic. Relaxed: Trigger rate set with least
     sensitivity w.r.t. normal traffic. Possible values include: 'Relaxed',
     'Low', 'Default', 'High'
    :type trigger_sensitivity_override: str or
     ~azure.mgmt.network.v2018_12_01.models.DdosCustomPolicyTriggerSensitivityOverride
    """

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'str'},
        'trigger_rate_override': {'key': 'triggerRateOverride', 'type': 'str'},
        'source_rate_override': {'key': 'sourceRateOverride', 'type': 'str'},
        'trigger_sensitivity_override': {'key': 'triggerSensitivityOverride', 'type': 'str'},
    }

    def __init__(self, *, protocol=None, trigger_rate_override: str=None, source_rate_override: str=None, trigger_sensitivity_override=None, **kwargs) -> None:
        super(ProtocolCustomSettingsFormat, self).__init__(**kwargs)
        self.protocol = protocol
        self.trigger_rate_override = trigger_rate_override
        self.source_rate_override = source_rate_override
        self.trigger_sensitivity_override = trigger_sensitivity_override
