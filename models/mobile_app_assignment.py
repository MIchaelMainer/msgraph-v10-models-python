# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.install_intent import InstallIntent
from ..model.device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
from ..model.mobile_app_assignment_settings import MobileAppAssignmentSettings
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def intent(self):
        """
        Gets and sets the intent
        
        Returns: 
            :class:`InstallIntent<onedrivesdk.model.install_intent.InstallIntent>`:
                The intent
        """
        if "intent" in self._prop_dict:
            if isinstance(self._prop_dict["intent"], OneDriveObjectBase):
                return self._prop_dict["intent"]
            else :
                self._prop_dict["intent"] = InstallIntent(self._prop_dict["intent"])
                return self._prop_dict["intent"]

        return None

    @intent.setter
    def intent(self, val):
        self._prop_dict["intent"] = val

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
    def settings(self):
        """
        Gets and sets the settings
        
        Returns: 
            :class:`MobileAppAssignmentSettings<onedrivesdk.model.mobile_app_assignment_settings.MobileAppAssignmentSettings>`:
                The settings
        """
        if "settings" in self._prop_dict:
            if isinstance(self._prop_dict["settings"], OneDriveObjectBase):
                return self._prop_dict["settings"]
            else :
                self._prop_dict["settings"] = MobileAppAssignmentSettings(self._prop_dict["settings"])
                return self._prop_dict["settings"]

        return None

    @settings.setter
    def settings(self, val):
        self._prop_dict["settings"] = val

