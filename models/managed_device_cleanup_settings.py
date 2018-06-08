# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDeviceCleanupSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_inactivity_before_retirement_in_days(self):
        """Gets and sets the deviceInactivityBeforeRetirementInDays
        
        Returns: 
            str:
                The deviceInactivityBeforeRetirementInDays
        """
        if "deviceInactivityBeforeRetirementInDays" in self._prop_dict:
            return self._prop_dict["deviceInactivityBeforeRetirementInDays"]
        else:
            return None

    @device_inactivity_before_retirement_in_days.setter
    def device_inactivity_before_retirement_in_days(self, val):
        self._prop_dict["deviceInactivityBeforeRetirementInDays"] = val

