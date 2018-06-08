# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_operating_system_summary import DeviceOperatingSystemSummary
from ..model.device_exchange_access_state_summary import DeviceExchangeAccessStateSummary
from ..model.managed_device_models_and_manufacturers import ManagedDeviceModelsAndManufacturers
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDeviceOverview(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def enrolled_device_count(self):
        """
        Gets and sets the enrolledDeviceCount
        
        Returns:
            int:
                The enrolledDeviceCount
        """
        if "enrolledDeviceCount" in self._prop_dict:
            return self._prop_dict["enrolledDeviceCount"]
        else:
            return None

    @enrolled_device_count.setter
    def enrolled_device_count(self, val):
        self._prop_dict["enrolledDeviceCount"] = val

    @property
    def mdm_enrolled_count(self):
        """
        Gets and sets the mdmEnrolledCount
        
        Returns:
            int:
                The mdmEnrolledCount
        """
        if "mdmEnrolledCount" in self._prop_dict:
            return self._prop_dict["mdmEnrolledCount"]
        else:
            return None

    @mdm_enrolled_count.setter
    def mdm_enrolled_count(self, val):
        self._prop_dict["mdmEnrolledCount"] = val

    @property
    def dual_enrolled_device_count(self):
        """
        Gets and sets the dualEnrolledDeviceCount
        
        Returns:
            int:
                The dualEnrolledDeviceCount
        """
        if "dualEnrolledDeviceCount" in self._prop_dict:
            return self._prop_dict["dualEnrolledDeviceCount"]
        else:
            return None

    @dual_enrolled_device_count.setter
    def dual_enrolled_device_count(self, val):
        self._prop_dict["dualEnrolledDeviceCount"] = val

    @property
    def device_operating_system_summary(self):
        """
        Gets and sets the deviceOperatingSystemSummary
        
        Returns: 
            :class:`DeviceOperatingSystemSummary<onedrivesdk.model.device_operating_system_summary.DeviceOperatingSystemSummary>`:
                The deviceOperatingSystemSummary
        """
        if "deviceOperatingSystemSummary" in self._prop_dict:
            if isinstance(self._prop_dict["deviceOperatingSystemSummary"], OneDriveObjectBase):
                return self._prop_dict["deviceOperatingSystemSummary"]
            else :
                self._prop_dict["deviceOperatingSystemSummary"] = DeviceOperatingSystemSummary(self._prop_dict["deviceOperatingSystemSummary"])
                return self._prop_dict["deviceOperatingSystemSummary"]

        return None

    @device_operating_system_summary.setter
    def device_operating_system_summary(self, val):
        self._prop_dict["deviceOperatingSystemSummary"] = val

    @property
    def device_exchange_access_state_summary(self):
        """
        Gets and sets the deviceExchangeAccessStateSummary
        
        Returns: 
            :class:`DeviceExchangeAccessStateSummary<onedrivesdk.model.device_exchange_access_state_summary.DeviceExchangeAccessStateSummary>`:
                The deviceExchangeAccessStateSummary
        """
        if "deviceExchangeAccessStateSummary" in self._prop_dict:
            if isinstance(self._prop_dict["deviceExchangeAccessStateSummary"], OneDriveObjectBase):
                return self._prop_dict["deviceExchangeAccessStateSummary"]
            else :
                self._prop_dict["deviceExchangeAccessStateSummary"] = DeviceExchangeAccessStateSummary(self._prop_dict["deviceExchangeAccessStateSummary"])
                return self._prop_dict["deviceExchangeAccessStateSummary"]

        return None

    @device_exchange_access_state_summary.setter
    def device_exchange_access_state_summary(self, val):
        self._prop_dict["deviceExchangeAccessStateSummary"] = val

    @property
    def managed_device_models_and_manufacturers(self):
        """
        Gets and sets the managedDeviceModelsAndManufacturers
        
        Returns: 
            :class:`ManagedDeviceModelsAndManufacturers<onedrivesdk.model.managed_device_models_and_manufacturers.ManagedDeviceModelsAndManufacturers>`:
                The managedDeviceModelsAndManufacturers
        """
        if "managedDeviceModelsAndManufacturers" in self._prop_dict:
            if isinstance(self._prop_dict["managedDeviceModelsAndManufacturers"], OneDriveObjectBase):
                return self._prop_dict["managedDeviceModelsAndManufacturers"]
            else :
                self._prop_dict["managedDeviceModelsAndManufacturers"] = ManagedDeviceModelsAndManufacturers(self._prop_dict["managedDeviceModelsAndManufacturers"])
                return self._prop_dict["managedDeviceModelsAndManufacturers"]

        return None

    @managed_device_models_and_manufacturers.setter
    def managed_device_models_and_manufacturers(self, val):
        self._prop_dict["managedDeviceModelsAndManufacturers"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

