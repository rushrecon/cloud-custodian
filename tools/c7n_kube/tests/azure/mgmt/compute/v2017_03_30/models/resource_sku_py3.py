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


class ResourceSku(Model):
    """Describes an available Compute SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar resource_type: The type of resource the SKU applies to.
    :vartype resource_type: str
    :ivar name: The name of SKU.
    :vartype name: str
    :ivar tier: Specifies the tier of virtual machines in a scale set.<br
     /><br /> Possible Values:<br /><br /> **Standard**<br /><br /> **Basic**
    :vartype tier: str
    :ivar size: The Size of the SKU.
    :vartype size: str
    :ivar family: The Family of this particular SKU.
    :vartype family: str
    :ivar kind: The Kind of resources that are supported in this SKU.
    :vartype kind: str
    :ivar capacity: Specifies the number of virtual machines in the scale set.
    :vartype capacity:
     ~azure.mgmt.compute.v2017_03_30.models.ResourceSkuCapacity
    :ivar locations: The set of locations that the SKU is available.
    :vartype locations: list[str]
    :ivar api_versions: The api versions that support this SKU.
    :vartype api_versions: list[str]
    :ivar costs: Metadata for retrieving price info.
    :vartype costs:
     list[~azure.mgmt.compute.v2017_03_30.models.ResourceSkuCosts]
    :ivar capabilities: A name value pair to describe the capability.
    :vartype capabilities:
     list[~azure.mgmt.compute.v2017_03_30.models.ResourceSkuCapabilities]
    :ivar restrictions: The restrictions because of which SKU cannot be used.
     This is empty if there are no restrictions.
    :vartype restrictions:
     list[~azure.mgmt.compute.v2017_03_30.models.ResourceSkuRestrictions]
    """

    _validation = {
        'resource_type': {'readonly': True},
        'name': {'readonly': True},
        'tier': {'readonly': True},
        'size': {'readonly': True},
        'family': {'readonly': True},
        'kind': {'readonly': True},
        'capacity': {'readonly': True},
        'locations': {'readonly': True},
        'api_versions': {'readonly': True},
        'costs': {'readonly': True},
        'capabilities': {'readonly': True},
        'restrictions': {'readonly': True},
    }

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'ResourceSkuCapacity'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'api_versions': {'key': 'apiVersions', 'type': '[str]'},
        'costs': {'key': 'costs', 'type': '[ResourceSkuCosts]'},
        'capabilities': {'key': 'capabilities', 'type': '[ResourceSkuCapabilities]'},
        'restrictions': {'key': 'restrictions', 'type': '[ResourceSkuRestrictions]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ResourceSku, self).__init__(**kwargs)
        self.resource_type = None
        self.name = None
        self.tier = None
        self.size = None
        self.family = None
        self.kind = None
        self.capacity = None
        self.locations = None
        self.api_versions = None
        self.costs = None
        self.capabilities = None
        self.restrictions = None
