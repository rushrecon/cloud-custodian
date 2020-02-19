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

from .backup_configuration_info_py3 import BackupConfigurationInfo


class PartitionBackupConfigurationInfo(BackupConfigurationInfo):
    """Backup configuration information, for a specific partition, specifying what
    backup policy is being applied and suspend description, if any.

    All required parameters must be populated in order to send to Azure.

    :param policy_name: The name of the backup policy which is applicable to
     this Service Fabric application or service or partition.
    :type policy_name: str
    :param policy_inherited_from: Specifies the scope at which the backup
     policy is applied. Possible values include: 'Invalid', 'Partition',
     'Service', 'Application'
    :type policy_inherited_from: str or
     ~azure.servicefabric.models.BackupPolicyScope
    :param suspension_info: Describes the backup suspension details.
    :type suspension_info: ~azure.servicefabric.models.BackupSuspensionInfo
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param service_name: The full name of the service with 'fabric:' URI
     scheme.
    :type service_name: str
    :param partition_id: An internal ID used by Service Fabric to uniquely
     identify a partition. This is a randomly generated GUID when the service
     was created. The partition ID is unique and does not change for the
     lifetime of the service. If the same service was deleted and recreated the
     IDs of its partitions would be different.
    :type partition_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'policy_name': {'key': 'PolicyName', 'type': 'str'},
        'policy_inherited_from': {'key': 'PolicyInheritedFrom', 'type': 'str'},
        'suspension_info': {'key': 'SuspensionInfo', 'type': 'BackupSuspensionInfo'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
    }

    def __init__(self, *, policy_name: str=None, policy_inherited_from=None, suspension_info=None, service_name: str=None, partition_id: str=None, **kwargs) -> None:
        super(PartitionBackupConfigurationInfo, self).__init__(policy_name=policy_name, policy_inherited_from=policy_inherited_from, suspension_info=suspension_info, **kwargs)
        self.service_name = service_name
        self.partition_id = partition_id
        self.kind = 'Partition'
