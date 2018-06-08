# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceOperatingSystemSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def android_count(self):
        """Gets and sets the androidCount
        
        Returns: 
            int:
                The androidCount
        """
        if "androidCount" in self._prop_dict:
            return self._prop_dict["androidCount"]
        else:
            return None

    @android_count.setter
    def android_count(self, val):
        self._prop_dict["androidCount"] = val

    @property
    def ios_count(self):
        """Gets and sets the iosCount
        
        Returns: 
            int:
                The iosCount
        """
        if "iosCount" in self._prop_dict:
            return self._prop_dict["iosCount"]
        else:
            return None

    @ios_count.setter
    def ios_count(self, val):
        self._prop_dict["iosCount"] = val

    @property
    def mac_os_count(self):
        """Gets and sets the macOSCount
        
        Returns: 
            int:
                The macOSCount
        """
        if "macOSCount" in self._prop_dict:
            return self._prop_dict["macOSCount"]
        else:
            return None

    @mac_os_count.setter
    def mac_os_count(self, val):
        self._prop_dict["macOSCount"] = val

    @property
    def windows_mobile_count(self):
        """Gets and sets the windowsMobileCount
        
        Returns: 
            int:
                The windowsMobileCount
        """
        if "windowsMobileCount" in self._prop_dict:
            return self._prop_dict["windowsMobileCount"]
        else:
            return None

    @windows_mobile_count.setter
    def windows_mobile_count(self, val):
        self._prop_dict["windowsMobileCount"] = val

    @property
    def windows_count(self):
        """Gets and sets the windowsCount
        
        Returns: 
            int:
                The windowsCount
        """
        if "windowsCount" in self._prop_dict:
            return self._prop_dict["windowsCount"]
        else:
            return None

    @windows_count.setter
    def windows_count(self, val):
        self._prop_dict["windowsCount"] = val

    @property
    def unknown_count(self):
        """Gets and sets the unknownCount
        
        Returns: 
            int:
                The unknownCount
        """
        if "unknownCount" in self._prop_dict:
            return self._prop_dict["unknownCount"]
        else:
            return None

    @unknown_count.setter
    def unknown_count(self, val):
        self._prop_dict["unknownCount"] = val

