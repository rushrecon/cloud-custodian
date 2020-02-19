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


class VpnClientIPsecParameters(Model):
    """An IPSec parameters for a virtual network gateway P2S connection.

    All required parameters must be populated in order to send to Azure.

    :param sa_life_time_seconds: Required. The IPSec Security Association
     (also called Quick Mode or Phase 2 SA) lifetime in seconds for P2S client.
    :type sa_life_time_seconds: int
    :param sa_data_size_kilobytes: Required. The IPSec Security Association
     (also called Quick Mode or Phase 2 SA) payload size in KB for P2S client..
    :type sa_data_size_kilobytes: int
    :param ipsec_encryption: Required. The IPSec encryption algorithm (IKE
     phase 1). Possible values include: 'None', 'DES', 'DES3', 'AES128',
     'AES192', 'AES256', 'GCMAES128', 'GCMAES192', 'GCMAES256'
    :type ipsec_encryption: str or
     ~azure.mgmt.network.v2018_06_01.models.IpsecEncryption
    :param ipsec_integrity: Required. The IPSec integrity algorithm (IKE phase
     1). Possible values include: 'MD5', 'SHA1', 'SHA256', 'GCMAES128',
     'GCMAES192', 'GCMAES256'
    :type ipsec_integrity: str or
     ~azure.mgmt.network.v2018_06_01.models.IpsecIntegrity
    :param ike_encryption: Required. The IKE encryption algorithm (IKE phase
     2). Possible values include: 'DES', 'DES3', 'AES128', 'AES192', 'AES256',
     'GCMAES256', 'GCMAES128'
    :type ike_encryption: str or
     ~azure.mgmt.network.v2018_06_01.models.IkeEncryption
    :param ike_integrity: Required. The IKE integrity algorithm (IKE phase 2).
     Possible values include: 'MD5', 'SHA1', 'SHA256', 'SHA384', 'GCMAES256',
     'GCMAES128'
    :type ike_integrity: str or
     ~azure.mgmt.network.v2018_06_01.models.IkeIntegrity
    :param dh_group: Required. The DH Groups used in IKE Phase 1 for initial
     SA. Possible values include: 'None', 'DHGroup1', 'DHGroup2', 'DHGroup14',
     'DHGroup2048', 'ECP256', 'ECP384', 'DHGroup24'
    :type dh_group: str or ~azure.mgmt.network.v2018_06_01.models.DhGroup
    :param pfs_group: Required. The Pfs Groups used in IKE Phase 2 for new
     child SA. Possible values include: 'None', 'PFS1', 'PFS2', 'PFS2048',
     'ECP256', 'ECP384', 'PFS24', 'PFS14', 'PFSMM'
    :type pfs_group: str or ~azure.mgmt.network.v2018_06_01.models.PfsGroup
    """

    _validation = {
        'sa_life_time_seconds': {'required': True},
        'sa_data_size_kilobytes': {'required': True},
        'ipsec_encryption': {'required': True},
        'ipsec_integrity': {'required': True},
        'ike_encryption': {'required': True},
        'ike_integrity': {'required': True},
        'dh_group': {'required': True},
        'pfs_group': {'required': True},
    }

    _attribute_map = {
        'sa_life_time_seconds': {'key': 'saLifeTimeSeconds', 'type': 'int'},
        'sa_data_size_kilobytes': {'key': 'saDataSizeKilobytes', 'type': 'int'},
        'ipsec_encryption': {'key': 'ipsecEncryption', 'type': 'str'},
        'ipsec_integrity': {'key': 'ipsecIntegrity', 'type': 'str'},
        'ike_encryption': {'key': 'ikeEncryption', 'type': 'str'},
        'ike_integrity': {'key': 'ikeIntegrity', 'type': 'str'},
        'dh_group': {'key': 'dhGroup', 'type': 'str'},
        'pfs_group': {'key': 'pfsGroup', 'type': 'str'},
    }

    def __init__(self, *, sa_life_time_seconds: int, sa_data_size_kilobytes: int, ipsec_encryption, ipsec_integrity, ike_encryption, ike_integrity, dh_group, pfs_group, **kwargs) -> None:
        super(VpnClientIPsecParameters, self).__init__(**kwargs)
        self.sa_life_time_seconds = sa_life_time_seconds
        self.sa_data_size_kilobytes = sa_data_size_kilobytes
        self.ipsec_encryption = ipsec_encryption
        self.ipsec_integrity = ipsec_integrity
        self.ike_encryption = ike_encryption
        self.ike_integrity = ike_integrity
        self.dh_group = dh_group
        self.pfs_group = pfs_group
