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

from .sub_resource_py3 import SubResource


class P2SVpnServerConfigRadiusClientRootCertificate(SubResource):
    """Radius client root certificate of P2SVpnServerConfiguration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param thumbprint: The Radius client root certificate thumbprint.
    :type thumbprint: str
    :ivar provisioning_state: The provisioning state of the Radius client root
     certificate resource. Possible values are: 'Updating', 'Deleting', and
     'Failed'.
    :vartype provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, thumbprint: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(P2SVpnServerConfigRadiusClientRootCertificate, self).__init__(id=id, **kwargs)
        self.thumbprint = thumbprint
        self.provisioning_state = None
        self.name = name
        self.etag = etag
