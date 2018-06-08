# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_compliance_policy_setting_state import DeviceCompliancePolicySettingState
from ..model.policy_platform_type import PolicyPlatformType
from ..model.compliance_status import ComplianceStatus
from ..one_drive_object_base import OneDriveObjectBase


class DeviceCompliancePolicyState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def setting_states(self):
        """Gets and sets the settingStates
        
        Returns: 
            :class:`SettingStatesCollectionPage<onedrivesdk.request.setting_states_collection.SettingStatesCollectionPage>`:
                The settingStates
        """
        if "settingStates" in self._prop_dict:
            return SettingStatesCollectionPage(self._prop_dict["settingStates"])
        else:
            return None

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
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            int:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

    @property
    def platform_type(self):
        """
        Gets and sets the platformType
        
        Returns: 
            :class:`PolicyPlatformType<onedrivesdk.model.policy_platform_type.PolicyPlatformType>`:
                The platformType
        """
        if "platformType" in self._prop_dict:
            if isinstance(self._prop_dict["platformType"], OneDriveObjectBase):
                return self._prop_dict["platformType"]
            else :
                self._prop_dict["platformType"] = PolicyPlatformType(self._prop_dict["platformType"])
                return self._prop_dict["platformType"]

        return None

    @platform_type.setter
    def platform_type(self, val):
        self._prop_dict["platformType"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`ComplianceStatus<onedrivesdk.model.compliance_status.ComplianceStatus>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = ComplianceStatus(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def setting_count(self):
        """
        Gets and sets the settingCount
        
        Returns:
            int:
                The settingCount
        """
        if "settingCount" in self._prop_dict:
            return self._prop_dict["settingCount"]
        else:
            return None

    @setting_count.setter
    def setting_count(self, val):
        self._prop_dict["settingCount"] = val

