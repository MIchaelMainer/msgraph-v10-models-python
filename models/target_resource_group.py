# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.group_type import GroupType
from ..one_drive_object_base import OneDriveObjectBase


class TargetResourceGroup(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def group_type(self):
        """
        Gets and sets the groupType
        
        Returns: 
            :class:`GroupType<onedrivesdk.model.group_type.GroupType>`:
                The groupType
        """
        if "groupType" in self._prop_dict:
            if isinstance(self._prop_dict["groupType"], OneDriveObjectBase):
                return self._prop_dict["groupType"]
            else :
                self._prop_dict["groupType"] = GroupType(self._prop_dict["groupType"])
                return self._prop_dict["groupType"]

        return None

    @group_type.setter
    def group_type(self, val):
        self._prop_dict["groupType"] = val
