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


class Error(Model):
    """Error object properties.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~azure.mgmt.network.v2015_06_15.models.ErrorDetails]
    :param inner_error:
    :type inner_error: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetails]'},
        'inner_error': {'key': 'innerError', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, target: str=None, details=None, inner_error: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.inner_error = inner_error
