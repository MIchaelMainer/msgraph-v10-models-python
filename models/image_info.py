# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ImageInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def icon_url(self):
        """Gets and sets the iconUrl
        
        Returns: 
            str:
                The iconUrl
        """
        if "iconUrl" in self._prop_dict:
            return self._prop_dict["iconUrl"]
        else:
            return None

    @icon_url.setter
    def icon_url(self, val):
        self._prop_dict["iconUrl"] = val

    @property
    def alternative_text(self):
        """Gets and sets the alternativeText
        
        Returns: 
            str:
                The alternativeText
        """
        if "alternativeText" in self._prop_dict:
            return self._prop_dict["alternativeText"]
        else:
            return None

    @alternative_text.setter
    def alternative_text(self, val):
        self._prop_dict["alternativeText"] = val

    @property
    def alternate_text(self):
        """Gets and sets the alternateText
        
        Returns: 
            str:
                The alternateText
        """
        if "alternateText" in self._prop_dict:
            return self._prop_dict["alternateText"]
        else:
            return None

    @alternate_text.setter
    def alternate_text(self, val):
        self._prop_dict["alternateText"] = val

    @property
    def add_image_query(self):
        """Gets and sets the addImageQuery
        
        Returns: 
            bool:
                The addImageQuery
        """
        if "addImageQuery" in self._prop_dict:
            return self._prop_dict["addImageQuery"]
        else:
            return None

    @add_image_query.setter
    def add_image_query(self, val):
        self._prop_dict["addImageQuery"] = val

