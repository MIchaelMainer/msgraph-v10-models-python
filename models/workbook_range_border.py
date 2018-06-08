# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookRangeBorder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def color(self):
        """
        Gets and sets the color
        
        Returns:
            str:
                The color
        """
        if "color" in self._prop_dict:
            return self._prop_dict["color"]
        else:
            return None

    @color.setter
    def color(self, val):
        self._prop_dict["color"] = val

    @property
    def side_index(self):
        """
        Gets and sets the sideIndex
        
        Returns:
            str:
                The sideIndex
        """
        if "sideIndex" in self._prop_dict:
            return self._prop_dict["sideIndex"]
        else:
            return None

    @side_index.setter
    def side_index(self, val):
        self._prop_dict["sideIndex"] = val

    @property
    def style(self):
        """
        Gets and sets the style
        
        Returns:
            str:
                The style
        """
        if "style" in self._prop_dict:
            return self._prop_dict["style"]
        else:
            return None

    @style.setter
    def style(self, val):
        self._prop_dict["style"] = val

    @property
    def weight(self):
        """
        Gets and sets the weight
        
        Returns:
            str:
                The weight
        """
        if "weight" in self._prop_dict:
            return self._prop_dict["weight"]
        else:
            return None

    @weight.setter
    def weight(self, val):
        self._prop_dict["weight"] = val

