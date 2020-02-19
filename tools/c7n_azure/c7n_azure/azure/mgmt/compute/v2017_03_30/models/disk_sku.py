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


class DiskSku(Model):
    """The disks and snapshots sku name. Can be Standard_LRS or Premium_LRS.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The sku name. Possible values include: 'Standard_LRS',
     'Premium_LRS'
    :type name: str or
     ~azure.mgmt.compute.v2017_03_30.models.StorageAccountTypes
    :ivar tier: The sku tier. Default value: "Standard" .
    :vartype tier: str
    """

    _validation = {
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'StorageAccountTypes'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DiskSku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = None
