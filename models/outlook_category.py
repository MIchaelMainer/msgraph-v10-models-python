# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.category_color import CategoryColor
from ..one_drive_object_base import OneDriveObjectBase


class OutlookCategory(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def color(self):
        """
        Gets and sets the color
        
        Returns: 
            :class:`CategoryColor<onedrivesdk.model.category_color.CategoryColor>`:
                The color
        """
        if "color" in self._prop_dict:
            if isinstance(self._prop_dict["color"], OneDriveObjectBase):
                return self._prop_dict["color"]
            else :
                self._prop_dict["color"] = CategoryColor(self._prop_dict["color"])
                return self._prop_dict["color"]

        return None

    @color.setter
    def color(self, val):
        self._prop_dict["color"] = val

