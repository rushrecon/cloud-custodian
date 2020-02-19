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


class KeyAndSecretDetails(Model):
    """BEK is bitlocker key.
    KEK is encryption key for BEK
    If the VM was encrypted then we will store follwing details :
    1. Secret(BEK) - Url + Backup Data + vaultId.
    2. Key(KEK) - Url + Backup Data + vaultId.
    3. EncryptionMechanism
    BEK and KEK can potentiallty have different vault ids.

    :param kek_details: KEK is encryption key for BEK.
    :type kek_details: ~azure.mgmt.recoveryservicesbackup.models.KEKDetails
    :param bek_details: BEK is bitlocker encrpytion key.
    :type bek_details: ~azure.mgmt.recoveryservicesbackup.models.BEKDetails
    :param encryption_mechanism: Encryption mechanism: None/ SinglePass/
     DoublePass
    :type encryption_mechanism: str
    """

    _attribute_map = {
        'kek_details': {'key': 'kekDetails', 'type': 'KEKDetails'},
        'bek_details': {'key': 'bekDetails', 'type': 'BEKDetails'},
        'encryption_mechanism': {'key': 'encryptionMechanism', 'type': 'str'},
    }

    def __init__(self, *, kek_details=None, bek_details=None, encryption_mechanism: str=None, **kwargs) -> None:
        super(KeyAndSecretDetails, self).__init__(**kwargs)
        self.kek_details = kek_details
        self.bek_details = bek_details
        self.encryption_mechanism = encryption_mechanism
