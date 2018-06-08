# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.image_info import ImageInfo
from ..model.json import Json
from ..one_drive_object_base import OneDriveObjectBase


class VisualInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def attribution(self):
        """
        Gets and sets the attribution
        
        Returns: 
            :class:`ImageInfo<onedrivesdk.model.image_info.ImageInfo>`:
                The attribution
        """
        if "attribution" in self._prop_dict:
            if isinstance(self._prop_dict["attribution"], OneDriveObjectBase):
                return self._prop_dict["attribution"]
            else :
                self._prop_dict["attribution"] = ImageInfo(self._prop_dict["attribution"])
                return self._prop_dict["attribution"]

        return None

    @attribution.setter
    def attribution(self, val):
        self._prop_dict["attribution"] = val
    @property
    def background_color(self):
        """Gets and sets the backgroundColor
        
        Returns: 
            str:
                The backgroundColor
        """
        if "backgroundColor" in self._prop_dict:
            return self._prop_dict["backgroundColor"]
        else:
            return None

    @background_color.setter
    def background_color(self, val):
        self._prop_dict["backgroundColor"] = val

    @property
    def description(self):
        """Gets and sets the description
        
        Returns: 
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def display_text(self):
        """Gets and sets the displayText
        
        Returns: 
            str:
                The displayText
        """
        if "displayText" in self._prop_dict:
            return self._prop_dict["displayText"]
        else:
            return None

    @display_text.setter
    def display_text(self, val):
        self._prop_dict["displayText"] = val

    @property
    def content(self):
        """
        Gets and sets the content
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The content
        """
        if "content" in self._prop_dict:
            if isinstance(self._prop_dict["content"], OneDriveObjectBase):
                return self._prop_dict["content"]
            else :
                self._prop_dict["content"] = Json(self._prop_dict["content"])
                return self._prop_dict["content"]

        return None

    @content.setter
    def content(self, val):
        self._prop_dict["content"] = val
