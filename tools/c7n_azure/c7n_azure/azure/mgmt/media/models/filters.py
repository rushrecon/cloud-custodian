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


class Filters(Model):
    """Describes all the filtering operations, such as de-interlacing, rotation
    etc. that are to be applied to the input media before encoding.

    :param deinterlace: The de-interlacing settings.
    :type deinterlace: ~azure.mgmt.media.models.Deinterlace
    :param rotation: The rotation, if any, to be applied to the input video,
     before it is encoded. Default is Auto. Possible values include: 'Auto',
     'None', 'Rotate0', 'Rotate90', 'Rotate180', 'Rotate270'
    :type rotation: str or ~azure.mgmt.media.models.Rotation
    :param crop: The parameters for the rectangular window with which to crop
     the input video.
    :type crop: ~azure.mgmt.media.models.Rectangle
    :param overlays: The properties of overlays to be applied to the input
     video. These could be audio, image or video overlays.
    :type overlays: list[~azure.mgmt.media.models.Overlay]
    """

    _attribute_map = {
        'deinterlace': {'key': 'deinterlace', 'type': 'Deinterlace'},
        'rotation': {'key': 'rotation', 'type': 'Rotation'},
        'crop': {'key': 'crop', 'type': 'Rectangle'},
        'overlays': {'key': 'overlays', 'type': '[Overlay]'},
    }

    def __init__(self, **kwargs):
        super(Filters, self).__init__(**kwargs)
        self.deinterlace = kwargs.get('deinterlace', None)
        self.rotation = kwargs.get('rotation', None)
        self.crop = kwargs.get('crop', None)
        self.overlays = kwargs.get('overlays', None)
