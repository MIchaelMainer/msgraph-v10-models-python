# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_identifier import MobileAppIdentifier
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppPolicyDeploymentSummaryPerApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def mobile_app_identifier(self):
        """
        Gets and sets the mobileAppIdentifier
        
        Returns: 
            :class:`MobileAppIdentifier<onedrivesdk.model.mobile_app_identifier.MobileAppIdentifier>`:
                The mobileAppIdentifier
        """
        if "mobileAppIdentifier" in self._prop_dict:
            if isinstance(self._prop_dict["mobileAppIdentifier"], OneDriveObjectBase):
                return self._prop_dict["mobileAppIdentifier"]
            else :
                self._prop_dict["mobileAppIdentifier"] = MobileAppIdentifier(self._prop_dict["mobileAppIdentifier"])
                return self._prop_dict["mobileAppIdentifier"]

        return None

    @mobile_app_identifier.setter
    def mobile_app_identifier(self, val):
        self._prop_dict["mobileAppIdentifier"] = val
    @property
    def configuration_applied_user_count(self):
        """Gets and sets the configurationAppliedUserCount
        
        Returns: 
            int:
                The configurationAppliedUserCount
        """
        if "configurationAppliedUserCount" in self._prop_dict:
            return self._prop_dict["configurationAppliedUserCount"]
        else:
            return None

    @configuration_applied_user_count.setter
    def configuration_applied_user_count(self, val):
        self._prop_dict["configurationAppliedUserCount"] = val

