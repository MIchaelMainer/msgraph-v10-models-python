# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceConfigurationUserStateSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

