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


class AS2MessageConnectionSettings(Model):
    """The AS2 agreement message connection settings.

    All required parameters must be populated in order to send to Azure.

    :param ignore_certificate_name_mismatch: Required. The value indicating
     whether to ignore mismatch in certificate name.
    :type ignore_certificate_name_mismatch: bool
    :param support_http_status_code_continue: Required. The value indicating
     whether to support HTTP status code 'CONTINUE'.
    :type support_http_status_code_continue: bool
    :param keep_http_connection_alive: Required. The value indicating whether
     to keep the connection alive.
    :type keep_http_connection_alive: bool
    :param unfold_http_headers: Required. The value indicating whether to
     unfold the HTTP headers.
    :type unfold_http_headers: bool
    """

    _validation = {
        'ignore_certificate_name_mismatch': {'required': True},
        'support_http_status_code_continue': {'required': True},
        'keep_http_connection_alive': {'required': True},
        'unfold_http_headers': {'required': True},
    }

    _attribute_map = {
        'ignore_certificate_name_mismatch': {'key': 'ignoreCertificateNameMismatch', 'type': 'bool'},
        'support_http_status_code_continue': {'key': 'supportHttpStatusCodeContinue', 'type': 'bool'},
        'keep_http_connection_alive': {'key': 'keepHttpConnectionAlive', 'type': 'bool'},
        'unfold_http_headers': {'key': 'unfoldHttpHeaders', 'type': 'bool'},
    }

    def __init__(self, *, ignore_certificate_name_mismatch: bool, support_http_status_code_continue: bool, keep_http_connection_alive: bool, unfold_http_headers: bool, **kwargs) -> None:
        super(AS2MessageConnectionSettings, self).__init__(**kwargs)
        self.ignore_certificate_name_mismatch = ignore_certificate_name_mismatch
        self.support_http_status_code_continue = support_http_status_code_continue
        self.keep_http_connection_alive = keep_http_connection_alive
        self.unfold_http_headers = unfold_http_headers
