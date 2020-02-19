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


class OperationPropertiesFormatServiceSpecification(Model):
    """Specification of the service.

    :param metric_specifications: Operation service specification.
    :type metric_specifications:
     list[~azure.mgmt.network.v2018_08_01.models.MetricSpecification]
    :param log_specifications: Operation log specification.
    :type log_specifications:
     list[~azure.mgmt.network.v2018_08_01.models.LogSpecification]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecification]'},
        'log_specifications': {'key': 'logSpecifications', 'type': '[LogSpecification]'},
    }

    def __init__(self, *, metric_specifications=None, log_specifications=None, **kwargs) -> None:
        super(OperationPropertiesFormatServiceSpecification, self).__init__(**kwargs)
        self.metric_specifications = metric_specifications
        self.log_specifications = log_specifications
