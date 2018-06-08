# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_compliance_checkin_threshold_days(self):
        """Gets and sets the deviceComplianceCheckinThresholdDays
        
        Returns: 
            int:
                The deviceComplianceCheckinThresholdDays
        """
        if "deviceComplianceCheckinThresholdDays" in self._prop_dict:
            return self._prop_dict["deviceComplianceCheckinThresholdDays"]
        else:
            return None

    @device_compliance_checkin_threshold_days.setter
    def device_compliance_checkin_threshold_days(self, val):
        self._prop_dict["deviceComplianceCheckinThresholdDays"] = val

    @property
    def is_scheduled_action_enabled(self):
        """Gets and sets the isScheduledActionEnabled
        
        Returns: 
            bool:
                The isScheduledActionEnabled
        """
        if "isScheduledActionEnabled" in self._prop_dict:
            return self._prop_dict["isScheduledActionEnabled"]
        else:
            return None

    @is_scheduled_action_enabled.setter
    def is_scheduled_action_enabled(self, val):
        self._prop_dict["isScheduledActionEnabled"] = val

    @property
    def secure_by_default(self):
        """Gets and sets the secureByDefault
        
        Returns: 
            bool:
                The secureByDefault
        """
        if "secureByDefault" in self._prop_dict:
            return self._prop_dict["secureByDefault"]
        else:
            return None

    @secure_by_default.setter
    def secure_by_default(self, val):
        self._prop_dict["secureByDefault"] = val

