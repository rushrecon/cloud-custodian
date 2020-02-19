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


class ApplicationGatewayRedirectConfiguration(SubResource):
    """Redirect configuration of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param redirect_type: Supported http redirection types - Permanent,
     Temporary, Found, SeeOther. Possible values include: 'Permanent', 'Found',
     'SeeOther', 'Temporary'
    :type redirect_type: str or
     ~azure.mgmt.network.v2018_08_01.models.ApplicationGatewayRedirectType
    :param target_listener: Reference to a listener to redirect the request
     to.
    :type target_listener: ~azure.mgmt.network.v2018_08_01.models.SubResource
    :param target_url: Url to redirect the request to.
    :type target_url: str
    :param include_path: Include path in the redirected url.
    :type include_path: bool
    :param include_query_string: Include query string in the redirected url.
    :type include_query_string: bool
    :param request_routing_rules: Request routing specifying redirect
     configuration.
    :type request_routing_rules:
     list[~azure.mgmt.network.v2018_08_01.models.SubResource]
    :param url_path_maps: Url path maps specifying default redirect
     configuration.
    :type url_path_maps:
     list[~azure.mgmt.network.v2018_08_01.models.SubResource]
    :param path_rules: Path rules specifying redirect configuration.
    :type path_rules: list[~azure.mgmt.network.v2018_08_01.models.SubResource]
    :param name: Name of the redirect configuration that is unique within an
     Application Gateway.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'redirect_type': {'key': 'properties.redirectType', 'type': 'str'},
        'target_listener': {'key': 'properties.targetListener', 'type': 'SubResource'},
        'target_url': {'key': 'properties.targetUrl', 'type': 'str'},
        'include_path': {'key': 'properties.includePath', 'type': 'bool'},
        'include_query_string': {'key': 'properties.includeQueryString', 'type': 'bool'},
        'request_routing_rules': {'key': 'properties.requestRoutingRules', 'type': '[SubResource]'},
        'url_path_maps': {'key': 'properties.urlPathMaps', 'type': '[SubResource]'},
        'path_rules': {'key': 'properties.pathRules', 'type': '[SubResource]'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayRedirectConfiguration, self).__init__(**kwargs)
        self.redirect_type = kwargs.get('redirect_type', None)
        self.target_listener = kwargs.get('target_listener', None)
        self.target_url = kwargs.get('target_url', None)
        self.include_path = kwargs.get('include_path', None)
        self.include_query_string = kwargs.get('include_query_string', None)
        self.request_routing_rules = kwargs.get('request_routing_rules', None)
        self.url_path_maps = kwargs.get('url_path_maps', None)
        self.path_rules = kwargs.get('path_rules', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
        self.type = kwargs.get('type', None)
