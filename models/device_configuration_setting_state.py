# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.compliance_status import ComplianceStatus
from ..model.setting_source import SettingSource
from ..one_drive_object_base import OneDriveObjectBase


class DeviceConfigurationSettingState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def setting(self):
        """Gets and sets the setting
        
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
        """Gets and sets the settingName
        
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
    def instance_display_name(self):
        """Gets and sets the instanceDisplayName
        
        Returns: 
            str:
                The instanceDisplayName
        """
        if "instanceDisplayName" in self._prop_dict:
            return self._prop_dict["instanceDisplayName"]
        else:
            return None

    @instance_display_name.setter
    def instance_display_name(self, val):
        self._prop_dict["instanceDisplayName"] = val

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
    def error_code(self):
        """Gets and sets the errorCode
        
        Returns: 
            int:
                The errorCode
        """
        if "errorCode" in self._prop_dict:
            return self._prop_dict["errorCode"]
        else:
            return None

    @error_code.setter
    def error_code(self, val):
        self._prop_dict["errorCode"] = val

    @property
    def error_description(self):
        """Gets and sets the errorDescription
        
        Returns: 
            str:
                The errorDescription
        """
        if "errorDescription" in self._prop_dict:
            return self._prop_dict["errorDescription"]
        else:
            return None

    @error_description.setter
    def error_description(self, val):
        self._prop_dict["errorDescription"] = val

    @property
    def user_id(self):
        """Gets and sets the userId
        
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
    def user_name(self):
        """Gets and sets the userName
        
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
    def user_email(self):
        """Gets and sets the userEmail
        
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
    def user_principal_name(self):
        """Gets and sets the userPrincipalName
        
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
    def sources(self):
        """
        Gets and sets the sources
        
        Returns: 
            :class:`SettingSource<onedrivesdk.model.setting_source.SettingSource>`:
                The sources
        """
        if "sources" in self._prop_dict:
            if isinstance(self._prop_dict["sources"], OneDriveObjectBase):
                return self._prop_dict["sources"]
            else :
                self._prop_dict["sources"] = SettingSource(self._prop_dict["sources"])
                return self._prop_dict["sources"]

        return None

    @sources.setter
    def sources(self, val):
        self._prop_dict["sources"] = val
    @property
    def current_value(self):
        """Gets and sets the currentValue
        
        Returns: 
            str:
                The currentValue
        """
        if "currentValue" in self._prop_dict:
            return self._prop_dict["currentValue"]
        else:
            return None

    @current_value.setter
    def current_value(self, val):
        self._prop_dict["currentValue"] = val

