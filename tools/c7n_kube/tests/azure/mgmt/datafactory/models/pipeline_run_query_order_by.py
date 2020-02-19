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


class PipelineRunQueryOrderBy(Model):
    """An object to provide order by options for listing pipeline runs.

    :param order_by: Parameter name to be used for order by. Possible values
     include: 'RunStart', 'RunEnd'
    :type order_by: str or
     ~azure.mgmt.datafactory.models.PipelineRunQueryOrderByField
    :param order: Sorting order of the parameter. Possible values include:
     'ASC', 'DESC'
    :type order: str or ~azure.mgmt.datafactory.models.PipelineRunQueryOrder
    """

    _validation = {
        'order_by': {'required': True},
        'order': {'required': True},
    }

    _attribute_map = {
        'order_by': {'key': 'orderBy', 'type': 'str'},
        'order': {'key': 'order', 'type': 'str'},
    }

    def __init__(self, order_by, order):
        super(PipelineRunQueryOrderBy, self).__init__()
        self.order_by = order_by
        self.order = order
