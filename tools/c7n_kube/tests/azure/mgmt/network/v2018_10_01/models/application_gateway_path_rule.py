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


class ApplicationGatewayPathRule(SubResource):
    """Path rule of URL path map of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param paths: Path rules of URL path map.
    :type paths: list[str]
    :param backend_address_pool: Backend address pool resource of URL path map
     path rule.
    :type backend_address_pool:
     ~azure.mgmt.network.v2018_10_01.models.SubResource
    :param backend_http_settings: Backend http settings resource of URL path
     map path rule.
    :type backend_http_settings:
     ~azure.mgmt.network.v2018_10_01.models.SubResource
    :param redirect_configuration: Redirect configuration resource of URL path
     map path rule.
    :type redirect_configuration:
     ~azure.mgmt.network.v2018_10_01.models.SubResource
    :param rewrite_rule_set: Rewrite rule set resource of URL path map path
     rule.
    :type rewrite_rule_set: ~azure.mgmt.network.v2018_10_01.models.SubResource
    :param provisioning_state: Path rule of URL path map resource. Possible
     values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the path rule that is unique within an Application
     Gateway.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'paths': {'key': 'properties.paths', 'type': '[str]'},
        'backend_address_pool': {'key': 'properties.backendAddressPool', 'type': 'SubResource'},
        'backend_http_settings': {'key': 'properties.backendHttpSettings', 'type': 'SubResource'},
        'redirect_configuration': {'key': 'properties.redirectConfiguration', 'type': 'SubResource'},
        'rewrite_rule_set': {'key': 'properties.rewriteRuleSet', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayPathRule, self).__init__(**kwargs)
        self.paths = kwargs.get('paths', None)
        self.backend_address_pool = kwargs.get('backend_address_pool', None)
        self.backend_http_settings = kwargs.get('backend_http_settings', None)
        self.redirect_configuration = kwargs.get('redirect_configuration', None)
        self.rewrite_rule_set = kwargs.get('rewrite_rule_set', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
        self.type = kwargs.get('type', None)
