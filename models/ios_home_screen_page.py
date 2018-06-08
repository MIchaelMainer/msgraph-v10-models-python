# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_home_screen_item import IosHomeScreenItem
from ..one_drive_object_base import OneDriveObjectBase


class IosHomeScreenPage(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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
    def icons(self):
        """
        Gets and sets the icons
        
        Returns: 
            :class:`IosHomeScreenItem<onedrivesdk.model.ios_home_screen_item.IosHomeScreenItem>`:
                The icons
        """
        if "icons" in self._prop_dict:
            if isinstance(self._prop_dict["icons"], OneDriveObjectBase):
                return self._prop_dict["icons"]
            else :
                self._prop_dict["icons"] = IosHomeScreenItem(self._prop_dict["icons"])
                return self._prop_dict["icons"]

        return None

    @icons.setter
    def icons(self, val):
        self._prop_dict["icons"] = val
