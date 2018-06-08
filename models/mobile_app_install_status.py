# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.resultant_app_state import ResultantAppState
from ..model.mobile_app import MobileApp
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppInstallStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def last_sync_date_time(self):
        """
        Gets and sets the lastSyncDateTime
        
        Returns:
            datetime:
                The lastSyncDateTime
        """
        if "lastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_sync_date_time.setter
    def last_sync_date_time(self, val):
        self._prop_dict["lastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def mobile_app_install_status_value(self):
        """
        Gets and sets the mobileAppInstallStatusValue
        
        Returns: 
            :class:`ResultantAppState<onedrivesdk.model.resultant_app_state.ResultantAppState>`:
                The mobileAppInstallStatusValue
        """
        if "mobileAppInstallStatusValue" in self._prop_dict:
            if isinstance(self._prop_dict["mobileAppInstallStatusValue"], OneDriveObjectBase):
                return self._prop_dict["mobileAppInstallStatusValue"]
            else :
                self._prop_dict["mobileAppInstallStatusValue"] = ResultantAppState(self._prop_dict["mobileAppInstallStatusValue"])
                return self._prop_dict["mobileAppInstallStatusValue"]

        return None

    @mobile_app_install_status_value.setter
    def mobile_app_install_status_value(self, val):
        self._prop_dict["mobileAppInstallStatusValue"] = val

    @property
    def install_state(self):
        """
        Gets and sets the installState
        
        Returns: 
            :class:`ResultantAppState<onedrivesdk.model.resultant_app_state.ResultantAppState>`:
                The installState
        """
        if "installState" in self._prop_dict:
            if isinstance(self._prop_dict["installState"], OneDriveObjectBase):
                return self._prop_dict["installState"]
            else :
                self._prop_dict["installState"] = ResultantAppState(self._prop_dict["installState"])
                return self._prop_dict["installState"]

        return None

    @install_state.setter
    def install_state(self, val):
        self._prop_dict["installState"] = val

    @property
    def error_code(self):
        """
        Gets and sets the errorCode
        
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
    def os_version(self):
        """
        Gets and sets the osVersion
        
        Returns:
            str:
                The osVersion
        """
        if "osVersion" in self._prop_dict:
            return self._prop_dict["osVersion"]
        else:
            return None

    @os_version.setter
    def os_version(self, val):
        self._prop_dict["osVersion"] = val

    @property
    def os_description(self):
        """
        Gets and sets the osDescription
        
        Returns:
            str:
                The osDescription
        """
        if "osDescription" in self._prop_dict:
            return self._prop_dict["osDescription"]
        else:
            return None

    @os_description.setter
    def os_description(self, val):
        self._prop_dict["osDescription"] = val

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
    def display_version(self):
        """
        Gets and sets the displayVersion
        
        Returns:
            str:
                The displayVersion
        """
        if "displayVersion" in self._prop_dict:
            return self._prop_dict["displayVersion"]
        else:
            return None

    @display_version.setter
    def display_version(self, val):
        self._prop_dict["displayVersion"] = val

    @property
    def app(self):
        """
        Gets and sets the app
        
        Returns: 
            :class:`MobileApp<onedrivesdk.model.mobile_app.MobileApp>`:
                The app
        """
        if "app" in self._prop_dict:
            if isinstance(self._prop_dict["app"], OneDriveObjectBase):
                return self._prop_dict["app"]
            else :
                self._prop_dict["app"] = MobileApp(self._prop_dict["app"])
                return self._prop_dict["app"]

        return None

    @app.setter
    def app(self, val):
        self._prop_dict["app"] = val

