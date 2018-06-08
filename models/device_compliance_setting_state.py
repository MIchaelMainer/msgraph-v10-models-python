# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_type import DeviceType
from ..model.compliance_status import ComplianceStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceComplianceSettingState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def platform_type(self):
        """
        Gets and sets the platformType
        
        Returns: 
            :class:`DeviceType<onedrivesdk.model.device_type.DeviceType>`:
                The platformType
        """
        if "platformType" in self._prop_dict:
            if isinstance(self._prop_dict["platformType"], OneDriveObjectBase):
                return self._prop_dict["platformType"]
            else :
                self._prop_dict["platformType"] = DeviceType(self._prop_dict["platformType"])
                return self._prop_dict["platformType"]

        return None

    @platform_type.setter
    def platform_type(self, val):
        self._prop_dict["platformType"] = val

    @property
    def setting(self):
        """
        Gets and sets the setting
        
        Returns:
            str:
                The setting
        """
        if "setting" in self._prop_dict:
            return self._prop_dict["setting"]
        else:
            return None

    @setting.setter
    def setting(self, val):
        self._prop_dict["setting"] = val

    @property
    def setting_name(self):
        """
        Gets and sets the settingName
        
        Returns:
            str:
                The settingName
        """
        if "settingName" in self._prop_dict:
            return self._prop_dict["settingName"]
        else:
            return None

    @setting_name.setter
    def setting_name(self, val):
        self._prop_dict["settingName"] = val

    @property
    def device_id(self):
        """
        Gets and sets the deviceId
        
        Returns:
            str:
                The deviceId
        """
        if "deviceId" in self._prop_dict:
            return self._prop_dict["deviceId"]
        else:
            return None

    @device_id.setter
    def device_id(self, val):
        self._prop_dict["deviceId"] = val

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
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def user_email(self):
        """
        Gets and sets the userEmail
        
        Returns:
            str:
                The userEmail
        """
        if "userEmail" in self._prop_dict:
            return self._prop_dict["userEmail"]
        else:
            return None

    @user_email.setter
    def user_email(self, val):
        self._prop_dict["userEmail"] = val

    @property
    def user_name(self):
        """
        Gets and sets the userName
        
        Returns:
            str:
                The userName
        """
        if "userName" in self._prop_dict:
            return self._prop_dict["userName"]
        else:
            return None

    @user_name.setter
    def user_name(self, val):
        self._prop_dict["userName"] = val

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def device_model(self):
        """
        Gets and sets the deviceModel
        
        Returns:
            str:
                The deviceModel
        """
        if "deviceModel" in self._prop_dict:
            return self._prop_dict["deviceModel"]
        else:
            return None

    @device_model.setter
    def device_model(self, val):
        self._prop_dict["deviceModel"] = val

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
    def compliance_grace_period_expiration_date_time(self):
        """
        Gets and sets the complianceGracePeriodExpirationDateTime
        
        Returns:
            datetime:
                The complianceGracePeriodExpirationDateTime
        """
        if "complianceGracePeriodExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["complianceGracePeriodExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self, val):
        self._prop_dict["complianceGracePeriodExpirationDateTime"] = val.isoformat()+"Z"

