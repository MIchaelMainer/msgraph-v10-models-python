# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.resource_action import ResourceAction
from ..one_drive_object_base import OneDriveObjectBase


class RolePermission(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def actions(self):
        """Gets and sets the actions
        
        Returns: 
            str:
                The actions
        """
        if "actions" in self._prop_dict:
            return self._prop_dict["actions"]
        else:
            return None

    @actions.setter
    def actions(self, val):
        self._prop_dict["actions"] = val

    @property
    def resource_actions(self):
        """
        Gets and sets the resourceActions
        
        Returns: 
            :class:`ResourceAction<onedrivesdk.model.resource_action.ResourceAction>`:
                The resourceActions
        """
        if "resourceActions" in self._prop_dict:
            if isinstance(self._prop_dict["resourceActions"], OneDriveObjectBase):
                return self._prop_dict["resourceActions"]
            else :
                self._prop_dict["resourceActions"] = ResourceAction(self._prop_dict["resourceActions"])
                return self._prop_dict["resourceActions"]

        return None

    @resource_actions.setter
    def resource_actions(self, val):
        self._prop_dict["resourceActions"] = val
