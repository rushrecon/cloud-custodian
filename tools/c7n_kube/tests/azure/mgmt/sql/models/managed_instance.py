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

from .tracked_resource import TrackedResource


class ManagedInstance(TrackedResource):
    """An Azure SQL managed instance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. Resource location.
    :type location: str
    :param identity: The Azure Active Directory identity of the managed
     instance.
    :type identity: ~azure.mgmt.sql.models.ResourceIdentity
    :param sku: Managed instance sku
    :type sku: ~azure.mgmt.sql.models.Sku
    :ivar fully_qualified_domain_name: The fully qualified domain name of the
     managed instance.
    :vartype fully_qualified_domain_name: str
    :param administrator_login: Administrator username for the managed
     instance. Can only be specified when the managed instance is being created
     (and is required for creation).
    :type administrator_login: str
    :param administrator_login_password: The administrator login password
     (required for managed instance creation).
    :type administrator_login_password: str
    :param subnet_id: Subnet resource ID for the managed instance.
    :type subnet_id: str
    :ivar state: The state of the managed instance.
    :vartype state: str
    :param license_type: The license type. Possible values are
     'LicenseIncluded' and 'BasePrice'.
    :type license_type: str
    :param v_cores: The number of VCores.
    :type v_cores: int
    :param storage_size_in_gb: The maximum storage size in GB.
    :type storage_size_in_gb: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'fully_qualified_domain_name': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ResourceIdentity'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'fully_qualified_domain_name': {'key': 'properties.fullyQualifiedDomainName', 'type': 'str'},
        'administrator_login': {'key': 'properties.administratorLogin', 'type': 'str'},
        'administrator_login_password': {'key': 'properties.administratorLoginPassword', 'type': 'str'},
        'subnet_id': {'key': 'properties.subnetId', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'license_type': {'key': 'properties.licenseType', 'type': 'str'},
        'v_cores': {'key': 'properties.vCores', 'type': 'int'},
        'storage_size_in_gb': {'key': 'properties.storageSizeInGB', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ManagedInstance, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.sku = kwargs.get('sku', None)
        self.fully_qualified_domain_name = None
        self.administrator_login = kwargs.get('administrator_login', None)
        self.administrator_login_password = kwargs.get('administrator_login_password', None)
        self.subnet_id = kwargs.get('subnet_id', None)
        self.state = None
        self.license_type = kwargs.get('license_type', None)
        self.v_cores = kwargs.get('v_cores', None)
        self.storage_size_in_gb = kwargs.get('storage_size_in_gb', None)
