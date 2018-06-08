# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
from ..model.install_intent import InstallIntent
from ..one_drive_object_base import OneDriveObjectBase


class ManagedEBookAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def target(self):
        """
        Gets and sets the target
        
        Returns: 
            :class:`DeviceAndAppManagementAssignmentTarget<onedrivesdk.model.device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget>`:
                The target
        """
        if "target" in self._prop_dict:
            if isinstance(self._prop_dict["target"], OneDriveObjectBase):
                return self._prop_dict["target"]
            else :
                self._prop_dict["target"] = DeviceAndAppManagementAssignmentTarget(self._prop_dict["target"])
                return self._prop_dict["target"]

        return None

    @target.setter
    def target(self, val):
        self._prop_dict["target"] = val

    @property
    def install_intent(self):
        """
        Gets and sets the installIntent
        
        Returns: 
            :class:`InstallIntent<onedrivesdk.model.install_intent.InstallIntent>`:
                The installIntent
        """
        if "installIntent" in self._prop_dict:
            if isinstance(self._prop_dict["installIntent"], OneDriveObjectBase):
                return self._prop_dict["installIntent"]
            else :
                self._prop_dict["installIntent"] = InstallIntent(self._prop_dict["installIntent"])
                return self._prop_dict["installIntent"]

        return None

    @install_intent.setter
    def install_intent(self, val):
        self._prop_dict["installIntent"] = val

