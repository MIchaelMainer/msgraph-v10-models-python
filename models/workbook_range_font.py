# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookRangeFont(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bold(self):
        """
        Gets and sets the bold
        
        Returns:
            bool:
                The bold
        """
        if "bold" in self._prop_dict:
            return self._prop_dict["bold"]
        else:
            return None

    @bold.setter
    def bold(self, val):
        self._prop_dict["bold"] = val

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
    def italic(self):
        """
        Gets and sets the italic
        
        Returns:
            bool:
                The italic
        """
        if "italic" in self._prop_dict:
            return self._prop_dict["italic"]
        else:
            return None

    @italic.setter
    def italic(self, val):
        self._prop_dict["italic"] = val

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def size(self):
        """
        Gets and sets the size
        
        Returns:
            float:
                The size
        """
        if "size" in self._prop_dict:
            return self._prop_dict["size"]
        else:
            return None

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

    @property
    def underline(self):
        """
        Gets and sets the underline
        
        Returns:
            str:
                The underline
        """
        if "underline" in self._prop_dict:
            return self._prop_dict["underline"]
        else:
            return None

    @underline.setter
    def underline(self, val):
        self._prop_dict["underline"] = val

