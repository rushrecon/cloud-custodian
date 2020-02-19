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

from .resource_py3 import Resource


class VaultExtendedInfoResource(Resource):
    """Vault extended information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id represents the complete path to the resource.
    :vartype id: str
    :ivar name: Resource name associated with the resource.
    :vartype name: str
    :ivar type: Resource type represents the complete path of the form
     Namespace/ResourceType/ResourceType/...
    :vartype type: str
    :param e_tag: Optional ETag.
    :type e_tag: str
    :param integrity_key: Integrity key.
    :type integrity_key: str
    :param encryption_key: Encryption key.
    :type encryption_key: str
    :param encryption_key_thumbprint: Encryption key thumbprint.
    :type encryption_key_thumbprint: str
    :param algorithm: Algorithm for Vault ExtendedInfo
    :type algorithm: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'integrity_key': {'key': 'properties.integrityKey', 'type': 'str'},
        'encryption_key': {'key': 'properties.encryptionKey', 'type': 'str'},
        'encryption_key_thumbprint': {'key': 'properties.encryptionKeyThumbprint', 'type': 'str'},
        'algorithm': {'key': 'properties.algorithm', 'type': 'str'},
    }

    def __init__(self, *, e_tag: str=None, integrity_key: str=None, encryption_key: str=None, encryption_key_thumbprint: str=None, algorithm: str=None, **kwargs) -> None:
        super(VaultExtendedInfoResource, self).__init__(e_tag=e_tag, **kwargs)
        self.integrity_key = integrity_key
        self.encryption_key = encryption_key
        self.encryption_key_thumbprint = encryption_key_thumbprint
        self.algorithm = algorithm
