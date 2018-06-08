# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_permission_action_type import AndroidPermissionActionType
from ..one_drive_object_base import OneDriveObjectBase


class AndroidPermissionAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def permission(self):
        """Gets and sets the permission
        
        Returns: 
            str:
                The permission
        """
        if "permission" in self._prop_dict:
            return self._prop_dict["permission"]
        else:
            return None

    @permission.setter
    def permission(self, val):
        self._prop_dict["permission"] = val

    @property
    def action(self):
        """
        Gets and sets the action
        
        Returns: 
            :class:`AndroidPermissionActionType<onedrivesdk.model.android_permission_action_type.AndroidPermissionActionType>`:
                The action
        """
        if "action" in self._prop_dict:
            if isinstance(self._prop_dict["action"], OneDriveObjectBase):
                return self._prop_dict["action"]
            else :
                self._prop_dict["action"] = AndroidPermissionActionType(self._prop_dict["action"])
                return self._prop_dict["action"]

        return None

    @action.setter
    def action(self, val):
        self._prop_dict["action"] = val
