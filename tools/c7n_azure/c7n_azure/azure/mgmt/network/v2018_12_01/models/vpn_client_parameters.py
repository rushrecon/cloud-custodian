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


class VpnClientParameters(Model):
    """Vpn Client Parameters for package generation.

    :param processor_architecture: VPN client Processor Architecture. Possible
     values are: 'AMD64' and 'X86'. Possible values include: 'Amd64', 'X86'
    :type processor_architecture: str or
     ~azure.mgmt.network.v2018_12_01.models.ProcessorArchitecture
    :param authentication_method: VPN client Authentication Method. Possible
     values are: 'EAPTLS' and 'EAPMSCHAPv2'. Possible values include: 'EAPTLS',
     'EAPMSCHAPv2'
    :type authentication_method: str or
     ~azure.mgmt.network.v2018_12_01.models.AuthenticationMethod
    :param radius_server_auth_certificate: The public certificate data for the
     radius server authentication certificate as a Base-64 encoded string.
     Required only if external radius authentication has been configured with
     EAPTLS authentication.
    :type radius_server_auth_certificate: str
    :param client_root_certificates: A list of client root certificates public
     certificate data encoded as Base-64 strings. Optional parameter for
     external radius based authentication with EAPTLS.
    :type client_root_certificates: list[str]
    """

    _attribute_map = {
        'processor_architecture': {'key': 'processorArchitecture', 'type': 'str'},
        'authentication_method': {'key': 'authenticationMethod', 'type': 'str'},
        'radius_server_auth_certificate': {'key': 'radiusServerAuthCertificate', 'type': 'str'},
        'client_root_certificates': {'key': 'clientRootCertificates', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(VpnClientParameters, self).__init__(**kwargs)
        self.processor_architecture = kwargs.get('processor_architecture', None)
        self.authentication_method = kwargs.get('authentication_method', None)
        self.radius_server_auth_certificate = kwargs.get('radius_server_auth_certificate', None)
        self.client_root_certificates = kwargs.get('client_root_certificates', None)
