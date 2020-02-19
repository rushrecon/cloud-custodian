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


class CheckAvailabilityParameters(Model):
    """Parameters supplied to the Check Name Availability for Namespace and
    NotificationHubs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Required. Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The sku of the created namespace
    :type sku: ~azure.mgmt.notificationhubs.models.Sku
    :param is_availiable: True if the name is available and can be used to
     create new Namespace/NotificationHub. Otherwise false.
    :type is_availiable: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'is_availiable': {'key': 'isAvailiable', 'type': 'bool'},
    }

    def __init__(self, *, name: str, location: str=None, tags=None, sku=None, is_availiable: bool=None, **kwargs) -> None:
        super(CheckAvailabilityParameters, self).__init__(**kwargs)
        self.id = None
        self.name = name
        self.type = None
        self.location = location
        self.tags = tags
        self.sku = sku
        self.is_availiable = is_availiable
