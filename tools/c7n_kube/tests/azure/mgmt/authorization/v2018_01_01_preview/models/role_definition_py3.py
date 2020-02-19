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


class RoleDefinition(Model):
    """Role definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The role definition ID.
    :vartype id: str
    :ivar name: The role definition name.
    :vartype name: str
    :ivar type: The role definition type.
    :vartype type: str
    :param role_name: The role name.
    :type role_name: str
    :param description: The role definition description.
    :type description: str
    :param role_type: The role type.
    :type role_type: str
    :param permissions: Role definition permissions.
    :type permissions:
     list[~azure.mgmt.authorization.v2018_01_01_preview.models.Permission]
    :param assignable_scopes: Role definition assignable scopes.
    :type assignable_scopes: list[str]
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
        'role_name': {'key': 'properties.roleName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'role_type': {'key': 'properties.type', 'type': 'str'},
        'permissions': {'key': 'properties.permissions', 'type': '[Permission]'},
        'assignable_scopes': {'key': 'properties.assignableScopes', 'type': '[str]'},
    }

    def __init__(self, *, role_name: str=None, description: str=None, role_type: str=None, permissions=None, assignable_scopes=None, **kwargs) -> None:
        super(RoleDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.role_name = role_name
        self.description = description
        self.role_type = role_type
        self.permissions = permissions
        self.assignable_scopes = assignable_scopes
