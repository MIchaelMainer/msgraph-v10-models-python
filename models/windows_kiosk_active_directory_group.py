# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskActiveDirectoryGroup(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def group_name(self):
        """Gets and sets the groupName
        
        Returns: 
            str:
                The groupName
        """
        if "groupName" in self._prop_dict:
            return self._prop_dict["groupName"]
        else:
            return None

    @group_name.setter
    def group_name(self, val):
        self._prop_dict["groupName"] = val
