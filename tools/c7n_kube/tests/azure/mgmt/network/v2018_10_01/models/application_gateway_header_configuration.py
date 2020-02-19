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


class ApplicationGatewayHeaderConfiguration(Model):
    """Header configuration of the Actions set in Application Gateway.

    :param header_name: Header name of the header configuration
    :type header_name: str
    :param header_value: Header value of the header configuration
    :type header_value: str
    """

    _attribute_map = {
        'header_name': {'key': 'headerName', 'type': 'str'},
        'header_value': {'key': 'headerValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayHeaderConfiguration, self).__init__(**kwargs)
        self.header_name = kwargs.get('header_name', None)
        self.header_value = kwargs.get('header_value', None)
