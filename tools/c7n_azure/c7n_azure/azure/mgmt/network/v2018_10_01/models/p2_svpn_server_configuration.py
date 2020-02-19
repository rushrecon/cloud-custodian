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


class P2SVpnServerConfiguration(SubResource):
    """P2SVpnServerConfiguration Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param p2_svpn_server_configuration_properties_name: The name of the
     P2SVpnServerConfiguration that is unique within a VirtualWan in a resource
     group. This name can be used to access the resource along with Parent
     VirtualWan resource name.
    :type p2_svpn_server_configuration_properties_name: str
    :param vpn_protocols: vpnProtocols for the P2SVpnServerConfiguration.
    :type vpn_protocols: list[str or
     ~azure.mgmt.network.v2018_10_01.models.VpnGatewayTunnelingProtocol]
    :param p2_svpn_server_config_vpn_client_root_certificates: VPN client root
     certificate of P2SVpnServerConfiguration.
    :type p2_svpn_server_config_vpn_client_root_certificates:
     list[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfigVpnClientRootCertificate]
    :param p2_svpn_server_config_vpn_client_revoked_certificates: VPN client
     revoked certificate of P2SVpnServerConfiguration.
    :type p2_svpn_server_config_vpn_client_revoked_certificates:
     list[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfigVpnClientRevokedCertificate]
    :param p2_svpn_server_config_radius_server_root_certificates: Radius
     Server root certificate of P2SVpnServerConfiguration.
    :type p2_svpn_server_config_radius_server_root_certificates:
     list[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfigRadiusServerRootCertificate]
    :param p2_svpn_server_config_radius_client_root_certificates: Radius
     client root certificate of P2SVpnServerConfiguration.
    :type p2_svpn_server_config_radius_client_root_certificates:
     list[~azure.mgmt.network.v2018_10_01.models.P2SVpnServerConfigRadiusClientRootCertificate]
    :param vpn_client_ipsec_policies: VpnClientIpsecPolicies for
     P2SVpnServerConfiguration.
    :type vpn_client_ipsec_policies:
     list[~azure.mgmt.network.v2018_10_01.models.IpsecPolicy]
    :param radius_server_address: The radius server address property of the
     P2SVpnServerConfiguration resource for point to site client connection.
    :type radius_server_address: str
    :param radius_server_secret: The radius secret property of the
     P2SVpnServerConfiguration resource for point to site client connection.
    :type radius_server_secret: str
    :ivar provisioning_state: The provisioning state of the
     P2SVpnServerConfiguration resource. Possible values are: 'Updating',
     'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :ivar p2_svpn_gateways:
    :vartype p2_svpn_gateways:
     list[~azure.mgmt.network.v2018_10_01.models.SubResource]
    :param p2_svpn_server_configuration_properties_etag: A unique read-only
     string that changes whenever the resource is updated.
    :type p2_svpn_server_configuration_properties_etag: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'p2_svpn_gateways': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'p2_svpn_server_configuration_properties_name': {'key': 'properties.name', 'type': 'str'},
        'vpn_protocols': {'key': 'properties.vpnProtocols', 'type': '[str]'},
        'p2_svpn_server_config_vpn_client_root_certificates': {'key': 'properties.p2SVpnServerConfigVpnClientRootCertificates', 'type': '[P2SVpnServerConfigVpnClientRootCertificate]'},
        'p2_svpn_server_config_vpn_client_revoked_certificates': {'key': 'properties.p2SVpnServerConfigVpnClientRevokedCertificates', 'type': '[P2SVpnServerConfigVpnClientRevokedCertificate]'},
        'p2_svpn_server_config_radius_server_root_certificates': {'key': 'properties.p2SVpnServerConfigRadiusServerRootCertificates', 'type': '[P2SVpnServerConfigRadiusServerRootCertificate]'},
        'p2_svpn_server_config_radius_client_root_certificates': {'key': 'properties.p2SVpnServerConfigRadiusClientRootCertificates', 'type': '[P2SVpnServerConfigRadiusClientRootCertificate]'},
        'vpn_client_ipsec_policies': {'key': 'properties.vpnClientIpsecPolicies', 'type': '[IpsecPolicy]'},
        'radius_server_address': {'key': 'properties.radiusServerAddress', 'type': 'str'},
        'radius_server_secret': {'key': 'properties.radiusServerSecret', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'p2_svpn_gateways': {'key': 'properties.p2SVpnGateways', 'type': '[SubResource]'},
        'p2_svpn_server_configuration_properties_etag': {'key': 'properties.etag', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(P2SVpnServerConfiguration, self).__init__(**kwargs)
        self.p2_svpn_server_configuration_properties_name = kwargs.get('p2_svpn_server_configuration_properties_name', None)
        self.vpn_protocols = kwargs.get('vpn_protocols', None)
        self.p2_svpn_server_config_vpn_client_root_certificates = kwargs.get('p2_svpn_server_config_vpn_client_root_certificates', None)
        self.p2_svpn_server_config_vpn_client_revoked_certificates = kwargs.get('p2_svpn_server_config_vpn_client_revoked_certificates', None)
        self.p2_svpn_server_config_radius_server_root_certificates = kwargs.get('p2_svpn_server_config_radius_server_root_certificates', None)
        self.p2_svpn_server_config_radius_client_root_certificates = kwargs.get('p2_svpn_server_config_radius_client_root_certificates', None)
        self.vpn_client_ipsec_policies = kwargs.get('vpn_client_ipsec_policies', None)
        self.radius_server_address = kwargs.get('radius_server_address', None)
        self.radius_server_secret = kwargs.get('radius_server_secret', None)
        self.provisioning_state = None
        self.p2_svpn_gateways = None
        self.p2_svpn_server_configuration_properties_etag = kwargs.get('p2_svpn_server_configuration_properties_etag', None)
        self.name = kwargs.get('name', None)
        self.etag = None
