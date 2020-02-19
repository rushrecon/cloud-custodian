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


class VpnClientConfiguration(Model):
    """VpnClientConfiguration for P2S client.

    :param vpn_client_address_pool: The reference of the address space
     resource which represents Address space for P2S VpnClient.
    :type vpn_client_address_pool:
     ~azure.mgmt.network.v2018_06_01.models.AddressSpace
    :param vpn_client_root_certificates: VpnClientRootCertificate for virtual
     network gateway.
    :type vpn_client_root_certificates:
     list[~azure.mgmt.network.v2018_06_01.models.VpnClientRootCertificate]
    :param vpn_client_revoked_certificates: VpnClientRevokedCertificate for
     Virtual network gateway.
    :type vpn_client_revoked_certificates:
     list[~azure.mgmt.network.v2018_06_01.models.VpnClientRevokedCertificate]
    :param vpn_client_protocols: VpnClientProtocols for Virtual network
     gateway.
    :type vpn_client_protocols: list[str or
     ~azure.mgmt.network.v2018_06_01.models.VpnClientProtocol]
    :param vpn_client_ipsec_policies: VpnClientIpsecPolicies for virtual
     network gateway P2S client.
    :type vpn_client_ipsec_policies:
     list[~azure.mgmt.network.v2018_06_01.models.IpsecPolicy]
    :param radius_server_address: The radius server address property of the
     VirtualNetworkGateway resource for vpn client connection.
    :type radius_server_address: str
    :param radius_server_secret: The radius secret property of the
     VirtualNetworkGateway resource for vpn client connection.
    :type radius_server_secret: str
    """

    _attribute_map = {
        'vpn_client_address_pool': {'key': 'vpnClientAddressPool', 'type': 'AddressSpace'},
        'vpn_client_root_certificates': {'key': 'vpnClientRootCertificates', 'type': '[VpnClientRootCertificate]'},
        'vpn_client_revoked_certificates': {'key': 'vpnClientRevokedCertificates', 'type': '[VpnClientRevokedCertificate]'},
        'vpn_client_protocols': {'key': 'vpnClientProtocols', 'type': '[str]'},
        'vpn_client_ipsec_policies': {'key': 'vpnClientIpsecPolicies', 'type': '[IpsecPolicy]'},
        'radius_server_address': {'key': 'radiusServerAddress', 'type': 'str'},
        'radius_server_secret': {'key': 'radiusServerSecret', 'type': 'str'},
    }

    def __init__(self, *, vpn_client_address_pool=None, vpn_client_root_certificates=None, vpn_client_revoked_certificates=None, vpn_client_protocols=None, vpn_client_ipsec_policies=None, radius_server_address: str=None, radius_server_secret: str=None, **kwargs) -> None:
        super(VpnClientConfiguration, self).__init__(**kwargs)
        self.vpn_client_address_pool = vpn_client_address_pool
        self.vpn_client_root_certificates = vpn_client_root_certificates
        self.vpn_client_revoked_certificates = vpn_client_revoked_certificates
        self.vpn_client_protocols = vpn_client_protocols
        self.vpn_client_ipsec_policies = vpn_client_ipsec_policies
        self.radius_server_address = radius_server_address
        self.radius_server_secret = radius_server_secret
