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

from .sub_resource import SubResource


class ExpressRouteLink(SubResource):
    """ExpressRouteLink.

    ExpressRouteLink child resource definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar router_name: Name of Azure router associated with physical port.
    :vartype router_name: str
    :ivar interface_name: Name of Azure router interface.
    :vartype interface_name: str
    :ivar patch_panel_id: Mapping between physical port to patch panel port.
    :vartype patch_panel_id: str
    :ivar rack_id: Mapping of physical patch panel to rack.
    :vartype rack_id: str
    :ivar connector_type: Physical fiber port type. Possible values include:
     'LC', 'SC'
    :vartype connector_type: str or
     ~azure.mgmt.network.v2018_11_01.models.ExpressRouteLinkConnectorType
    :param admin_state: Administrative state of the physical port. Possible
     values include: 'Enabled', 'Disabled'
    :type admin_state: str or
     ~azure.mgmt.network.v2018_11_01.models.ExpressRouteLinkAdminState
    :ivar provisioning_state: The provisioning state of the ExpressRouteLink
     resource. Possible values are: 'Succeeded', 'Updating', 'Deleting', and
     'Failed'.
    :vartype provisioning_state: str
    :param name: Name of child port resource that is unique among child port
     resources of the parent.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'router_name': {'readonly': True},
        'interface_name': {'readonly': True},
        'patch_panel_id': {'readonly': True},
        'rack_id': {'readonly': True},
        'connector_type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'router_name': {'key': 'properties.routerName', 'type': 'str'},
        'interface_name': {'key': 'properties.interfaceName', 'type': 'str'},
        'patch_panel_id': {'key': 'properties.patchPanelId', 'type': 'str'},
        'rack_id': {'key': 'properties.rackId', 'type': 'str'},
        'connector_type': {'key': 'properties.connectorType', 'type': 'str'},
        'admin_state': {'key': 'properties.adminState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteLink, self).__init__(**kwargs)
        self.router_name = None
        self.interface_name = None
        self.patch_panel_id = None
        self.rack_id = None
        self.connector_type = None
        self.admin_state = kwargs.get('admin_state', None)
        self.provisioning_state = None
        self.name = kwargs.get('name', None)
        self.etag = None
