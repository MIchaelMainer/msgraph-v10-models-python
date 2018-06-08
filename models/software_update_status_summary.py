# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SoftwareUpdateStatusSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def compliant_device_count(self):
        """
        Gets and sets the compliantDeviceCount
        
        Returns:
            int:
                The compliantDeviceCount
        """
        if "compliantDeviceCount" in self._prop_dict:
            return self._prop_dict["compliantDeviceCount"]
        else:
            return None

    @compliant_device_count.setter
    def compliant_device_count(self, val):
        self._prop_dict["compliantDeviceCount"] = val

    @property
    def non_compliant_device_count(self):
        """
        Gets and sets the nonCompliantDeviceCount
        
        Returns:
            int:
                The nonCompliantDeviceCount
        """
        if "nonCompliantDeviceCount" in self._prop_dict:
            return self._prop_dict["nonCompliantDeviceCount"]
        else:
            return None

    @non_compliant_device_count.setter
    def non_compliant_device_count(self, val):
        self._prop_dict["nonCompliantDeviceCount"] = val

    @property
    def remediated_device_count(self):
        """
        Gets and sets the remediatedDeviceCount
        
        Returns:
            int:
                The remediatedDeviceCount
        """
        if "remediatedDeviceCount" in self._prop_dict:
            return self._prop_dict["remediatedDeviceCount"]
        else:
            return None

    @remediated_device_count.setter
    def remediated_device_count(self, val):
        self._prop_dict["remediatedDeviceCount"] = val

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
    def unknown_device_count(self):
        """
        Gets and sets the unknownDeviceCount
        
        Returns:
            int:
                The unknownDeviceCount
        """
        if "unknownDeviceCount" in self._prop_dict:
            return self._prop_dict["unknownDeviceCount"]
        else:
            return None

    @unknown_device_count.setter
    def unknown_device_count(self, val):
        self._prop_dict["unknownDeviceCount"] = val

    @property
    def conflict_device_count(self):
        """
        Gets and sets the conflictDeviceCount
        
        Returns:
            int:
                The conflictDeviceCount
        """
        if "conflictDeviceCount" in self._prop_dict:
            return self._prop_dict["conflictDeviceCount"]
        else:
            return None

    @conflict_device_count.setter
    def conflict_device_count(self, val):
        self._prop_dict["conflictDeviceCount"] = val

    @property
    def not_applicable_device_count(self):
        """
        Gets and sets the notApplicableDeviceCount
        
        Returns:
            int:
                The notApplicableDeviceCount
        """
        if "notApplicableDeviceCount" in self._prop_dict:
            return self._prop_dict["notApplicableDeviceCount"]
        else:
            return None

    @not_applicable_device_count.setter
    def not_applicable_device_count(self, val):
        self._prop_dict["notApplicableDeviceCount"] = val

    @property
    def compliant_user_count(self):
        """
        Gets and sets the compliantUserCount
        
        Returns:
            int:
                The compliantUserCount
        """
        if "compliantUserCount" in self._prop_dict:
            return self._prop_dict["compliantUserCount"]
        else:
            return None

    @compliant_user_count.setter
    def compliant_user_count(self, val):
        self._prop_dict["compliantUserCount"] = val

    @property
    def non_compliant_user_count(self):
        """
        Gets and sets the nonCompliantUserCount
        
        Returns:
            int:
                The nonCompliantUserCount
        """
        if "nonCompliantUserCount" in self._prop_dict:
            return self._prop_dict["nonCompliantUserCount"]
        else:
            return None

    @non_compliant_user_count.setter
    def non_compliant_user_count(self, val):
        self._prop_dict["nonCompliantUserCount"] = val

    @property
    def remediated_user_count(self):
        """
        Gets and sets the remediatedUserCount
        
        Returns:
            int:
                The remediatedUserCount
        """
        if "remediatedUserCount" in self._prop_dict:
            return self._prop_dict["remediatedUserCount"]
        else:
            return None

    @remediated_user_count.setter
    def remediated_user_count(self, val):
        self._prop_dict["remediatedUserCount"] = val

    @property
    def error_user_count(self):
        """
        Gets and sets the errorUserCount
        
        Returns:
            int:
                The errorUserCount
        """
        if "errorUserCount" in self._prop_dict:
            return self._prop_dict["errorUserCount"]
        else:
            return None

    @error_user_count.setter
    def error_user_count(self, val):
        self._prop_dict["errorUserCount"] = val

    @property
    def unknown_user_count(self):
        """
        Gets and sets the unknownUserCount
        
        Returns:
            int:
                The unknownUserCount
        """
        if "unknownUserCount" in self._prop_dict:
            return self._prop_dict["unknownUserCount"]
        else:
            return None

    @unknown_user_count.setter
    def unknown_user_count(self, val):
        self._prop_dict["unknownUserCount"] = val

    @property
    def conflict_user_count(self):
        """
        Gets and sets the conflictUserCount
        
        Returns:
            int:
                The conflictUserCount
        """
        if "conflictUserCount" in self._prop_dict:
            return self._prop_dict["conflictUserCount"]
        else:
            return None

    @conflict_user_count.setter
    def conflict_user_count(self, val):
        self._prop_dict["conflictUserCount"] = val

    @property
    def not_applicable_user_count(self):
        """
        Gets and sets the notApplicableUserCount
        
        Returns:
            int:
                The notApplicableUserCount
        """
        if "notApplicableUserCount" in self._prop_dict:
            return self._prop_dict["notApplicableUserCount"]
        else:
            return None

    @not_applicable_user_count.setter
    def not_applicable_user_count(self, val):
        self._prop_dict["notApplicableUserCount"] = val

