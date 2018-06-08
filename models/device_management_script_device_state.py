# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.run_state import RunState
from ..model.managed_device import ManagedDevice
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementScriptDeviceState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def run_state(self):
        """
        Gets and sets the runState
        
        Returns: 
            :class:`RunState<onedrivesdk.model.run_state.RunState>`:
                The runState
        """
        if "runState" in self._prop_dict:
            if isinstance(self._prop_dict["runState"], OneDriveObjectBase):
                return self._prop_dict["runState"]
            else :
                self._prop_dict["runState"] = RunState(self._prop_dict["runState"])
                return self._prop_dict["runState"]

        return None

    @run_state.setter
    def run_state(self, val):
        self._prop_dict["runState"] = val

    @property
    def result_message(self):
        """
        Gets and sets the resultMessage
        
        Returns:
            str:
                The resultMessage
        """
        if "resultMessage" in self._prop_dict:
            return self._prop_dict["resultMessage"]
        else:
            return None

    @result_message.setter
    def result_message(self, val):
        self._prop_dict["resultMessage"] = val

    @property
    def last_state_update_date_time(self):
        """
        Gets and sets the lastStateUpdateDateTime
        
        Returns:
            datetime:
                The lastStateUpdateDateTime
        """
        if "lastStateUpdateDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastStateUpdateDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_state_update_date_time.setter
    def last_state_update_date_time(self, val):
        self._prop_dict["lastStateUpdateDateTime"] = val.isoformat()+"Z"

    @property
    def error_code(self):
        """
        Gets and sets the errorCode
        
        Returns:
            int:
                The errorCode
        """
        if "errorCode" in self._prop_dict:
            return self._prop_dict["errorCode"]
        else:
            return None

    @error_code.setter
    def error_code(self, val):
        self._prop_dict["errorCode"] = val

    @property
    def error_description(self):
        """
        Gets and sets the errorDescription
        
        Returns:
            str:
                The errorDescription
        """
        if "errorDescription" in self._prop_dict:
            return self._prop_dict["errorDescription"]
        else:
            return None

    @error_description.setter
    def error_description(self, val):
        self._prop_dict["errorDescription"] = val

    @property
    def managed_device(self):
        """
        Gets and sets the managedDevice
        
        Returns: 
            :class:`ManagedDevice<onedrivesdk.model.managed_device.ManagedDevice>`:
                The managedDevice
        """
        if "managedDevice" in self._prop_dict:
            if isinstance(self._prop_dict["managedDevice"], OneDriveObjectBase):
                return self._prop_dict["managedDevice"]
            else :
                self._prop_dict["managedDevice"] = ManagedDevice(self._prop_dict["managedDevice"])
                return self._prop_dict["managedDevice"]

        return None

    @managed_device.setter
    def managed_device(self, val):
        self._prop_dict["managedDevice"] = val

