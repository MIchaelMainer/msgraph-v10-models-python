# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365ActiveUserCounts(OneDriveObjectBase):

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
    def office365(self):
        """
        Gets and sets the office365
        
        Returns:
            int:
                The office365
        """
        if "office365" in self._prop_dict:
            return self._prop_dict["office365"]
        else:
            return None

    @office365.setter
    def office365(self, val):
        self._prop_dict["office365"] = val

    @property
    def exchange(self):
        """
        Gets and sets the exchange
        
        Returns:
            int:
                The exchange
        """
        if "exchange" in self._prop_dict:
            return self._prop_dict["exchange"]
        else:
            return None

    @exchange.setter
    def exchange(self, val):
        self._prop_dict["exchange"] = val

    @property
    def one_drive(self):
        """
        Gets and sets the oneDrive
        
        Returns:
            int:
                The oneDrive
        """
        if "oneDrive" in self._prop_dict:
            return self._prop_dict["oneDrive"]
        else:
            return None

    @one_drive.setter
    def one_drive(self, val):
        self._prop_dict["oneDrive"] = val

    @property
    def share_point(self):
        """
        Gets and sets the sharePoint
        
        Returns:
            int:
                The sharePoint
        """
        if "sharePoint" in self._prop_dict:
            return self._prop_dict["sharePoint"]
        else:
            return None

    @share_point.setter
    def share_point(self, val):
        self._prop_dict["sharePoint"] = val

    @property
    def skype_for_business(self):
        """
        Gets and sets the skypeForBusiness
        
        Returns:
            int:
                The skypeForBusiness
        """
        if "skypeForBusiness" in self._prop_dict:
            return self._prop_dict["skypeForBusiness"]
        else:
            return None

    @skype_for_business.setter
    def skype_for_business(self, val):
        self._prop_dict["skypeForBusiness"] = val

    @property
    def yammer(self):
        """
        Gets and sets the yammer
        
        Returns:
            int:
                The yammer
        """
        if "yammer" in self._prop_dict:
            return self._prop_dict["yammer"]
        else:
            return None

    @yammer.setter
    def yammer(self, val):
        self._prop_dict["yammer"] = val

    @property
    def teams(self):
        """
        Gets and sets the teams
        
        Returns:
            int:
                The teams
        """
        if "teams" in self._prop_dict:
            return self._prop_dict["teams"]
        else:
            return None

    @teams.setter
    def teams(self, val):
        self._prop_dict["teams"] = val

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

