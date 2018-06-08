# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ResourceVisualization(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def title(self):
        """Gets and sets the title
        
        Returns: 
            str:
                The title
        """
        if "title" in self._prop_dict:
            return self._prop_dict["title"]
        else:
            return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def media_type(self):
        """Gets and sets the mediaType
        
        Returns: 
            str:
                The mediaType
        """
        if "mediaType" in self._prop_dict:
            return self._prop_dict["mediaType"]
        else:
            return None

    @media_type.setter
    def media_type(self, val):
        self._prop_dict["mediaType"] = val

    @property
    def preview_image_url(self):
        """Gets and sets the previewImageUrl
        
        Returns: 
            str:
                The previewImageUrl
        """
        if "previewImageUrl" in self._prop_dict:
            return self._prop_dict["previewImageUrl"]
        else:
            return None

    @preview_image_url.setter
    def preview_image_url(self, val):
        self._prop_dict["previewImageUrl"] = val

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
    def container_web_url(self):
        """Gets and sets the containerWebUrl
        
        Returns: 
            str:
                The containerWebUrl
        """
        if "containerWebUrl" in self._prop_dict:
            return self._prop_dict["containerWebUrl"]
        else:
            return None

    @container_web_url.setter
    def container_web_url(self, val):
        self._prop_dict["containerWebUrl"] = val

    @property
    def container_display_name(self):
        """Gets and sets the containerDisplayName
        
        Returns: 
            str:
                The containerDisplayName
        """
        if "containerDisplayName" in self._prop_dict:
            return self._prop_dict["containerDisplayName"]
        else:
            return None

    @container_display_name.setter
    def container_display_name(self, val):
        self._prop_dict["containerDisplayName"] = val

    @property
    def container_type(self):
        """Gets and sets the containerType
        
        Returns: 
            str:
                The containerType
        """
        if "containerType" in self._prop_dict:
            return self._prop_dict["containerType"]
        else:
            return None

    @container_type.setter
    def container_type(self, val):
        self._prop_dict["containerType"] = val

