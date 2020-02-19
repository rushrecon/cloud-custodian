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


class ExpressRouteCrossConnection(Resource):
    """ExpressRouteCrossConnection resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar primary_azure_port: The name of the primary  port.
    :vartype primary_azure_port: str
    :ivar secondary_azure_port: The name of the secondary  port.
    :vartype secondary_azure_port: str
    :ivar s_tag: The identifier of the circuit traffic.
    :vartype s_tag: int
    :param peering_location: The peering location of the ExpressRoute circuit.
    :type peering_location: str
    :param bandwidth_in_mbps: The circuit bandwidth In Mbps.
    :type bandwidth_in_mbps: int
    :param express_route_circuit: The ExpressRouteCircuit
    :type express_route_circuit:
     ~azure.mgmt.network.v2018_02_01.models.ExpressRouteCircuitReference
    :param service_provider_provisioning_state: The provisioning state of the
     circuit in the connectivity provider system. Possible values are
     'NotProvisioned', 'Provisioning', 'Provisioned'. Possible values include:
     'NotProvisioned', 'Provisioning', 'Provisioned', 'Deprovisioning'
    :type service_provider_provisioning_state: str or
     ~azure.mgmt.network.v2018_02_01.models.ServiceProviderProvisioningState
    :param service_provider_notes: Additional read only notes set by the
     connectivity provider.
    :type service_provider_notes: str
    :ivar provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :param peerings: The list of peerings.
    :type peerings:
     list[~azure.mgmt.network.v2018_02_01.models.ExpressRouteCrossConnectionPeering]
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'primary_azure_port': {'readonly': True},
        'secondary_azure_port': {'readonly': True},
        's_tag': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'primary_azure_port': {'key': 'properties.primaryAzurePort', 'type': 'str'},
        'secondary_azure_port': {'key': 'properties.secondaryAzurePort', 'type': 'str'},
        's_tag': {'key': 'properties.sTag', 'type': 'int'},
        'peering_location': {'key': 'properties.peeringLocation', 'type': 'str'},
        'bandwidth_in_mbps': {'key': 'properties.bandwidthInMbps', 'type': 'int'},
        'express_route_circuit': {'key': 'properties.expressRouteCircuit', 'type': 'ExpressRouteCircuitReference'},
        'service_provider_provisioning_state': {'key': 'properties.serviceProviderProvisioningState', 'type': 'str'},
        'service_provider_notes': {'key': 'properties.serviceProviderNotes', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'peerings': {'key': 'properties.peerings', 'type': '[ExpressRouteCrossConnectionPeering]'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, peering_location: str=None, bandwidth_in_mbps: int=None, express_route_circuit=None, service_provider_provisioning_state=None, service_provider_notes: str=None, peerings=None, **kwargs) -> None:
        super(ExpressRouteCrossConnection, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.primary_azure_port = None
        self.secondary_azure_port = None
        self.s_tag = None
        self.peering_location = peering_location
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.express_route_circuit = express_route_circuit
        self.service_provider_provisioning_state = service_provider_provisioning_state
        self.service_provider_notes = service_provider_notes
        self.provisioning_state = None
        self.peerings = peerings
        self.etag = None
