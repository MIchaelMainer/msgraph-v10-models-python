# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class TeamsDeviceUsageUserCounts(OneDriveObjectBase):

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
    def web(self):
        """
        Gets and sets the web
        
        Returns:
            int:
                The web
        """
        if "web" in self._prop_dict:
            return self._prop_dict["web"]
        else:
            return None

    @web.setter
    def web(self, val):
        self._prop_dict["web"] = val

    @property
    def windows_phone(self):
        """
        Gets and sets the windowsPhone
        
        Returns:
            int:
                The windowsPhone
        """
        if "windowsPhone" in self._prop_dict:
            return self._prop_dict["windowsPhone"]
        else:
            return None

    @windows_phone.setter
    def windows_phone(self, val):
        self._prop_dict["windowsPhone"] = val

    @property
    def android_phone(self):
        """
        Gets and sets the androidPhone
        
        Returns:
            int:
                The androidPhone
        """
        if "androidPhone" in self._prop_dict:
            return self._prop_dict["androidPhone"]
        else:
            return None

    @android_phone.setter
    def android_phone(self, val):
        self._prop_dict["androidPhone"] = val

    @property
    def ios(self):
        """
        Gets and sets the ios
        
        Returns:
            int:
                The ios
        """
        if "ios" in self._prop_dict:
            return self._prop_dict["ios"]
        else:
            return None

    @ios.setter
    def ios(self, val):
        self._prop_dict["ios"] = val

    @property
    def mac(self):
        """
        Gets and sets the mac
        
        Returns:
            int:
                The mac
        """
        if "mac" in self._prop_dict:
            return self._prop_dict["mac"]
        else:
            return None

    @mac.setter
    def mac(self, val):
        self._prop_dict["mac"] = val

    @property
    def windows(self):
        """
        Gets and sets the windows
        
        Returns:
            int:
                The windows
        """
        if "windows" in self._prop_dict:
            return self._prop_dict["windows"]
        else:
            return None

    @windows.setter
    def windows(self, val):
        self._prop_dict["windows"] = val

    @property
    def report_date(self):
        """
        Gets and sets the reportDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The reportDate
        """
        if "reportDate" in self._prop_dict:
            if isinstance(self._prop_dict["reportDate"], OneDriveObjectBase):
                return self._prop_dict["reportDate"]
            else :
                self._prop_dict["reportDate"] = Date(self._prop_dict["reportDate"])
                return self._prop_dict["reportDate"]

        return None

    @report_date.setter
    def report_date(self, val):
        self._prop_dict["reportDate"] = val

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

