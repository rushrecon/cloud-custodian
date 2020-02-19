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


class ImmutabilityPolicyProperties(Model):
    """The properties of an ImmutabilityPolicy of a blob container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param immutability_period_since_creation_in_days: Required. The
     immutability period for the blobs in the container since the policy
     creation, in days.
    :type immutability_period_since_creation_in_days: int
    :ivar state: The ImmutabilityPolicy state of a blob container, possible
     values include: Locked and Unlocked. Possible values include: 'Locked',
     'Unlocked'
    :vartype state: str or
     ~azure.mgmt.storage.v2018_03_01_preview.models.ImmutabilityPolicyState
    :ivar etag: ImmutabilityPolicy Etag.
    :vartype etag: str
    :ivar update_history: The ImmutabilityPolicy update history of the blob
     container.
    :vartype update_history:
     list[~azure.mgmt.storage.v2018_03_01_preview.models.UpdateHistoryProperty]
    """

    _validation = {
        'immutability_period_since_creation_in_days': {'required': True},
        'state': {'readonly': True},
        'etag': {'readonly': True},
        'update_history': {'readonly': True},
    }

    _attribute_map = {
        'immutability_period_since_creation_in_days': {'key': 'properties.immutabilityPeriodSinceCreationInDays', 'type': 'int'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'update_history': {'key': 'updateHistory', 'type': '[UpdateHistoryProperty]'},
    }

    def __init__(self, **kwargs):
        super(ImmutabilityPolicyProperties, self).__init__(**kwargs)
        self.immutability_period_since_creation_in_days = kwargs.get('immutability_period_since_creation_in_days', None)
        self.state = None
        self.etag = None
        self.update_history = None
