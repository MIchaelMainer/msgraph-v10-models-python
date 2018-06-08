# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class YammerDeviceUsageUserDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def report_refresh_date(self):
        """
        Gets and sets the reportRefreshDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The reportRefreshDate
        """
        if "reportRefreshDate" in self._prop_dict:
            if isinstance(self._prop_dict["reportRefreshDate"], OneDriveObjectBase):
                return self._prop_dict["reportRefreshDate"]
            else :
                self._prop_dict["reportRefreshDate"] = Date(self._prop_dict["reportRefreshDate"])
                return self._prop_dict["reportRefreshDate"]

        return None

    @report_refresh_date.setter
    def report_refresh_date(self, val):
        self._prop_dict["reportRefreshDate"] = val

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
    def user_state(self):
        """
        Gets and sets the userState
        
        Returns:
            str:
                The userState
        """
        if "userState" in self._prop_dict:
            return self._prop_dict["userState"]
        else:
            return None

    @user_state.setter
    def user_state(self, val):
        self._prop_dict["userState"] = val

    @property
    def state_change_date(self):
        """
        Gets and sets the stateChangeDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The stateChangeDate
        """
        if "stateChangeDate" in self._prop_dict:
            if isinstance(self._prop_dict["stateChangeDate"], OneDriveObjectBase):
                return self._prop_dict["stateChangeDate"]
            else :
                self._prop_dict["stateChangeDate"] = Date(self._prop_dict["stateChangeDate"])
                return self._prop_dict["stateChangeDate"]

        return None

    @state_change_date.setter
    def state_change_date(self, val):
        self._prop_dict["stateChangeDate"] = val

    @property
    def last_activity_date(self):
        """
        Gets and sets the lastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The lastActivityDate
        """
        if "lastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["lastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["lastActivityDate"]
            else :
                self._prop_dict["lastActivityDate"] = Date(self._prop_dict["lastActivityDate"])
                return self._prop_dict["lastActivityDate"]

        return None

    @last_activity_date.setter
    def last_activity_date(self, val):
        self._prop_dict["lastActivityDate"] = val

    @property
    def used_web(self):
        """
        Gets and sets the usedWeb
        
        Returns:
            bool:
                The usedWeb
        """
        if "usedWeb" in self._prop_dict:
            return self._prop_dict["usedWeb"]
        else:
            return None

    @used_web.setter
    def used_web(self, val):
        self._prop_dict["usedWeb"] = val

    @property
    def used_windows_phone(self):
        """
        Gets and sets the usedWindowsPhone
        
        Returns:
            bool:
                The usedWindowsPhone
        """
        if "usedWindowsPhone" in self._prop_dict:
            return self._prop_dict["usedWindowsPhone"]
        else:
            return None

    @used_windows_phone.setter
    def used_windows_phone(self, val):
        self._prop_dict["usedWindowsPhone"] = val

    @property
    def used_android_phone(self):
        """
        Gets and sets the usedAndroidPhone
        
        Returns:
            bool:
                The usedAndroidPhone
        """
        if "usedAndroidPhone" in self._prop_dict:
            return self._prop_dict["usedAndroidPhone"]
        else:
            return None

    @used_android_phone.setter
    def used_android_phone(self, val):
        self._prop_dict["usedAndroidPhone"] = val

    @property
    def usedi_phone(self):
        """
        Gets and sets the usediPhone
        
        Returns:
            bool:
                The usediPhone
        """
        if "usediPhone" in self._prop_dict:
            return self._prop_dict["usediPhone"]
        else:
            return None

    @usedi_phone.setter
    def usedi_phone(self, val):
        self._prop_dict["usediPhone"] = val

    @property
    def usedi_pad(self):
        """
        Gets and sets the usediPad
        
        Returns:
            bool:
                The usediPad
        """
        if "usediPad" in self._prop_dict:
            return self._prop_dict["usediPad"]
        else:
            return None

    @usedi_pad.setter
    def usedi_pad(self, val):
        self._prop_dict["usediPad"] = val

    @property
    def used_others(self):
        """
        Gets and sets the usedOthers
        
        Returns:
            bool:
                The usedOthers
        """
        if "usedOthers" in self._prop_dict:
            return self._prop_dict["usedOthers"]
        else:
            return None

    @used_others.setter
    def used_others(self, val):
        self._prop_dict["usedOthers"] = val

    @property
    def report_period(self):
        """
        Gets and sets the reportPeriod
        
        Returns:
            str:
                The reportPeriod
        """
        if "reportPeriod" in self._prop_dict:
            return self._prop_dict["reportPeriod"]
        else:
            return None

    @report_period.setter
    def report_period(self, val):
        self._prop_dict["reportPeriod"] = val

