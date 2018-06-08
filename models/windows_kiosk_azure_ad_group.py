# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskAzureADGroup(OneDriveObjectBase):

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
    def group_id(self):
        """Gets and sets the groupId
        
        Returns: 
            str:
                The groupId
        """
        if "groupId" in self._prop_dict:
            return self._prop_dict["groupId"]
        else:
            return None

    @group_id.setter
    def group_id(self, val):
        self._prop_dict["groupId"] = val

