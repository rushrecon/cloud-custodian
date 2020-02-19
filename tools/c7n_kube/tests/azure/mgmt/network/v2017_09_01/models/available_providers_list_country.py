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


class AvailableProvidersListCountry(Model):
    """Country details.

    :param country_name: The country name.
    :type country_name: str
    :param providers: A list of Internet service providers.
    :type providers: list[str]
    :param states: List of available states in the country.
    :type states:
     list[~azure.mgmt.network.v2017_09_01.models.AvailableProvidersListState]
    """

    _attribute_map = {
        'country_name': {'key': 'countryName', 'type': 'str'},
        'providers': {'key': 'providers', 'type': '[str]'},
        'states': {'key': 'states', 'type': '[AvailableProvidersListState]'},
    }

    def __init__(self, **kwargs):
        super(AvailableProvidersListCountry, self).__init__(**kwargs)
        self.country_name = kwargs.get('country_name', None)
        self.providers = kwargs.get('providers', None)
        self.states = kwargs.get('states', None)
