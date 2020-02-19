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


class ApplicationPackageReference(Model):
    """A reference to an application package to be deployed to compute nodes.

    :param application_id: The ID of the application to deploy.
    :type application_id: str
    :param version: The version of the application to deploy. If omitted, the
     default version is deployed. If this is omitted on a pool, and no default
     version is specified for this application, the request fails with the
     error code InvalidApplicationPackageReferences and HTTP status code 409.
     If this is omitted on a task, and no default version is specified for this
     application, the task fails with a pre-processing error.
    :type version: str
    """

    _validation = {
        'application_id': {'required': True},
    }

    _attribute_map = {
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, application_id, version=None):
        super(ApplicationPackageReference, self).__init__()
        self.application_id = application_id
        self.version = version
