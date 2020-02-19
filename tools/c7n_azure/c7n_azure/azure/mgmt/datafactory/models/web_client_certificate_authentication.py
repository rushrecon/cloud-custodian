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

from .web_linked_service_type_properties import WebLinkedServiceTypeProperties


class WebClientCertificateAuthentication(WebLinkedServiceTypeProperties):
    """A WebLinkedService that uses client certificate based authentication to
    communicate with an HTTP endpoint. This scheme follows mutual
    authentication; the server must also provide valid credentials to the
    client.

    :param url: The URL of the web service endpoint, e.g.
     http://www.microsoft.com . Type: string (or Expression with resultType
     string).
    :type url: object
    :param authentication_type: Constant filled by server.
    :type authentication_type: str
    :param pfx: Base64-encoded contents of a PFX file.
    :type pfx: ~azure.mgmt.datafactory.models.SecretBase
    :param password: Password for the PFX file.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    """

    _validation = {
        'url': {'required': True},
        'authentication_type': {'required': True},
        'pfx': {'required': True},
        'password': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'object'},
        'authentication_type': {'key': 'authenticationType', 'type': 'str'},
        'pfx': {'key': 'pfx', 'type': 'SecretBase'},
        'password': {'key': 'password', 'type': 'SecretBase'},
    }

    def __init__(self, url, pfx, password):
        super(WebClientCertificateAuthentication, self).__init__(url=url)
        self.pfx = pfx
        self.password = password
        self.authentication_type = 'ClientCertificate'
