# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.health_state import HealthState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class WindowsManagementAppHealthState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def health_state(self):
        """
        Gets and sets the healthState
        
        Returns: 
            :class:`HealthState<onedrivesdk.model.health_state.HealthState>`:
                The healthState
        """
        if "healthState" in self._prop_dict:
            if isinstance(self._prop_dict["healthState"], OneDriveObjectBase):
                return self._prop_dict["healthState"]
            else :
                self._prop_dict["healthState"] = HealthState(self._prop_dict["healthState"])
                return self._prop_dict["healthState"]

        return None

    @health_state.setter
    def health_state(self, val):
        self._prop_dict["healthState"] = val

    @property
    def installed_version(self):
        """
        Gets and sets the installedVersion
        
        Returns:
            str:
                The installedVersion
        """
        if "installedVersion" in self._prop_dict:
            return self._prop_dict["installedVersion"]
        else:
            return None

    @installed_version.setter
    def installed_version(self, val):
        self._prop_dict["installedVersion"] = val

    @property
    def last_check_in_date_time(self):
        """
        Gets and sets the lastCheckInDateTime
        
        Returns:
            datetime:
                The lastCheckInDateTime
        """
        if "lastCheckInDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastCheckInDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_check_in_date_time.setter
    def last_check_in_date_time(self, val):
        self._prop_dict["lastCheckInDateTime"] = val.isoformat()+"Z"

    @property
    def device_name(self):
        """
        Gets and sets the deviceName
        
        Returns:
            str:
                The deviceName
        """
        if "deviceName" in self._prop_dict:
            return self._prop_dict["deviceName"]
        else:
            return None

    @device_name.setter
    def device_name(self, val):
        self._prop_dict["deviceName"] = val

    @property
    def device_os_version(self):
        """
        Gets and sets the deviceOSVersion
        
        Returns:
            str:
                The deviceOSVersion
        """
        if "deviceOSVersion" in self._prop_dict:
            return self._prop_dict["deviceOSVersion"]
        else:
            return None

    @device_os_version.setter
    def device_os_version(self, val):
        self._prop_dict["deviceOSVersion"] = val

