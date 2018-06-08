# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.external_link import ExternalLink
from ..one_drive_object_base import OneDriveObjectBase


class OnenotePagePreviewLinks(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def preview_image_url(self):
        """
        Gets and sets the previewImageUrl
        
        Returns: 
            :class:`ExternalLink<onedrivesdk.model.external_link.ExternalLink>`:
                The previewImageUrl
        """
        if "previewImageUrl" in self._prop_dict:
            if isinstance(self._prop_dict["previewImageUrl"], OneDriveObjectBase):
                return self._prop_dict["previewImageUrl"]
            else :
                self._prop_dict["previewImageUrl"] = ExternalLink(self._prop_dict["previewImageUrl"])
                return self._prop_dict["previewImageUrl"]

        return None

    @preview_image_url.setter
    def preview_image_url(self, val):
        self._prop_dict["previewImageUrl"] = val
