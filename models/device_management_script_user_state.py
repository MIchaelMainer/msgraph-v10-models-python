# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_script_device_state import DeviceManagementScriptDeviceState
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementScriptUserState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def success_device_count(self):
        """
        Gets and sets the successDeviceCount
        
        Returns:
            int:
                The successDeviceCount
        """
        if "successDeviceCount" in self._prop_dict:
            return self._prop_dict["successDeviceCount"]
        else:
            return None

    @success_device_count.setter
    def success_device_count(self, val):
        self._prop_dict["successDeviceCount"] = val

    @property
    def error_device_count(self):
        """
        Gets and sets the errorDeviceCount
        
        Returns:
            int:
                The errorDeviceCount
        """
        if "errorDeviceCount" in self._prop_dict:
            return self._prop_dict["errorDeviceCount"]
        else:
            return None

    @error_device_count.setter
    def error_device_count(self, val):
        self._prop_dict["errorDeviceCount"] = val

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def device_run_states(self):
        """Gets and sets the deviceRunStates
        
        Returns: 
            :class:`DeviceRunStatesCollectionPage<onedrivesdk.request.device_run_states_collection.DeviceRunStatesCollectionPage>`:
                The deviceRunStates
        """
        if "deviceRunStates" in self._prop_dict:
            return DeviceRunStatesCollectionPage(self._prop_dict["deviceRunStates"])
        else:
            return None

