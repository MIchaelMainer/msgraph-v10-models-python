# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.onenote_page_preview_links import OnenotePagePreviewLinks
from ..one_drive_object_base import OneDriveObjectBase


class OnenotePagePreview(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def preview_text(self):
        """Gets and sets the previewText
        
        Returns: 
            str:
                The previewText
        """
        if "previewText" in self._prop_dict:
            return self._prop_dict["previewText"]
        else:
            return None

    @preview_text.setter
    def preview_text(self, val):
        self._prop_dict["previewText"] = val

    @property
    def links(self):
        """
        Gets and sets the links
        
        Returns: 
            :class:`OnenotePagePreviewLinks<onedrivesdk.model.onenote_page_preview_links.OnenotePagePreviewLinks>`:
                The links
        """
        if "links" in self._prop_dict:
            if isinstance(self._prop_dict["links"], OneDriveObjectBase):
                return self._prop_dict["links"]
            else :
                self._prop_dict["links"] = OnenotePagePreviewLinks(self._prop_dict["links"])
                return self._prop_dict["links"]

        return None

    @links.setter
    def links(self, val):
        self._prop_dict["links"] = val
