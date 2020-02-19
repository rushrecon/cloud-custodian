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

try:
    from .resource_py3 import Resource
    from .disk_sku_py3 import DiskSku
    from .image_disk_reference_py3 import ImageDiskReference
    from .creation_data_py3 import CreationData
    from .source_vault_py3 import SourceVault
    from .key_vault_and_secret_reference_py3 import KeyVaultAndSecretReference
    from .key_vault_and_key_reference_py3 import KeyVaultAndKeyReference
    from .encryption_settings_element_py3 import EncryptionSettingsElement
    from .encryption_settings_collection_py3 import EncryptionSettingsCollection
    from .disk_py3 import Disk
    from .disk_update_py3 import DiskUpdate
    from .snapshot_sku_py3 import SnapshotSku
    from .grant_access_data_py3 import GrantAccessData
    from .access_uri_py3 import AccessUri
    from .snapshot_py3 import Snapshot
    from .snapshot_update_py3 import SnapshotUpdate
except (SyntaxError, ImportError):
    from .resource import Resource
    from .disk_sku import DiskSku
    from .image_disk_reference import ImageDiskReference
    from .creation_data import CreationData
    from .source_vault import SourceVault
    from .key_vault_and_secret_reference import KeyVaultAndSecretReference
    from .key_vault_and_key_reference import KeyVaultAndKeyReference
    from .encryption_settings_element import EncryptionSettingsElement
    from .encryption_settings_collection import EncryptionSettingsCollection
    from .disk import Disk
    from .disk_update import DiskUpdate
    from .snapshot_sku import SnapshotSku
    from .grant_access_data import GrantAccessData
    from .access_uri import AccessUri
    from .snapshot import Snapshot
    from .snapshot_update import SnapshotUpdate
from .disk_paged import DiskPaged
from .snapshot_paged import SnapshotPaged
from .compute_management_client_enums import (
    DiskStorageAccountTypes,
    OperatingSystemTypes,
    HyperVGeneration,
    DiskCreateOption,
    DiskState,
    SnapshotStorageAccountTypes,
    AccessLevel,
    StorageAccountTypes,
)

__all__ = [
    'Resource',
    'DiskSku',
    'ImageDiskReference',
    'CreationData',
    'SourceVault',
    'KeyVaultAndSecretReference',
    'KeyVaultAndKeyReference',
    'EncryptionSettingsElement',
    'EncryptionSettingsCollection',
    'Disk',
    'DiskUpdate',
    'SnapshotSku',
    'GrantAccessData',
    'AccessUri',
    'Snapshot',
    'SnapshotUpdate',
    'DiskPaged',
    'SnapshotPaged',
    'DiskStorageAccountTypes',
    'StorageAccountTypes',
    'OperatingSystemTypes',
    'HyperVGeneration',
    'DiskCreateOption',
    'DiskState',
    'SnapshotStorageAccountTypes',
    'AccessLevel',
]
