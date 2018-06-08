# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class YammerDeviceUsageDistributionUserCounts(OneDriveObjectBase):

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
    def i_phone(self):
        """
        Gets and sets the iPhone
        
        Returns:
            int:
                The iPhone
        """
        if "iPhone" in self._prop_dict:
            return self._prop_dict["iPhone"]
        else:
            return None

    @i_phone.setter
    def i_phone(self, val):
        self._prop_dict["iPhone"] = val

    @property
    def i_pad(self):
        """
        Gets and sets the iPad
        
        Returns:
            int:
                The iPad
        """
        if "iPad" in self._prop_dict:
            return self._prop_dict["iPad"]
        else:
            return None

    @i_pad.setter
    def i_pad(self, val):
        self._prop_dict["iPad"] = val

    @property
    def other(self):
        """
        Gets and sets the other
        
        Returns:
            int:
                The other
        """
        if "other" in self._prop_dict:
            return self._prop_dict["other"]
        else:
            return None

    @other.setter
    def other(self, val):
        self._prop_dict["other"] = val

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

