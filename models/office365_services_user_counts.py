# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365ServicesUserCounts(OneDriveObjectBase):

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
    def exchange_active(self):
        """
        Gets and sets the exchangeActive
        
        Returns:
            int:
                The exchangeActive
        """
        if "exchangeActive" in self._prop_dict:
            return self._prop_dict["exchangeActive"]
        else:
            return None

    @exchange_active.setter
    def exchange_active(self, val):
        self._prop_dict["exchangeActive"] = val

    @property
    def exchange_inactive(self):
        """
        Gets and sets the exchangeInactive
        
        Returns:
            int:
                The exchangeInactive
        """
        if "exchangeInactive" in self._prop_dict:
            return self._prop_dict["exchangeInactive"]
        else:
            return None

    @exchange_inactive.setter
    def exchange_inactive(self, val):
        self._prop_dict["exchangeInactive"] = val

    @property
    def one_drive_active(self):
        """
        Gets and sets the oneDriveActive
        
        Returns:
            int:
                The oneDriveActive
        """
        if "oneDriveActive" in self._prop_dict:
            return self._prop_dict["oneDriveActive"]
        else:
            return None

    @one_drive_active.setter
    def one_drive_active(self, val):
        self._prop_dict["oneDriveActive"] = val

    @property
    def one_drive_inactive(self):
        """
        Gets and sets the oneDriveInactive
        
        Returns:
            int:
                The oneDriveInactive
        """
        if "oneDriveInactive" in self._prop_dict:
            return self._prop_dict["oneDriveInactive"]
        else:
            return None

    @one_drive_inactive.setter
    def one_drive_inactive(self, val):
        self._prop_dict["oneDriveInactive"] = val

    @property
    def share_point_active(self):
        """
        Gets and sets the sharePointActive
        
        Returns:
            int:
                The sharePointActive
        """
        if "sharePointActive" in self._prop_dict:
            return self._prop_dict["sharePointActive"]
        else:
            return None

    @share_point_active.setter
    def share_point_active(self, val):
        self._prop_dict["sharePointActive"] = val

    @property
    def share_point_inactive(self):
        """
        Gets and sets the sharePointInactive
        
        Returns:
            int:
                The sharePointInactive
        """
        if "sharePointInactive" in self._prop_dict:
            return self._prop_dict["sharePointInactive"]
        else:
            return None

    @share_point_inactive.setter
    def share_point_inactive(self, val):
        self._prop_dict["sharePointInactive"] = val

    @property
    def skype_for_business_active(self):
        """
        Gets and sets the skypeForBusinessActive
        
        Returns:
            int:
                The skypeForBusinessActive
        """
        if "skypeForBusinessActive" in self._prop_dict:
            return self._prop_dict["skypeForBusinessActive"]
        else:
            return None

    @skype_for_business_active.setter
    def skype_for_business_active(self, val):
        self._prop_dict["skypeForBusinessActive"] = val

    @property
    def skype_for_business_inactive(self):
        """
        Gets and sets the skypeForBusinessInactive
        
        Returns:
            int:
                The skypeForBusinessInactive
        """
        if "skypeForBusinessInactive" in self._prop_dict:
            return self._prop_dict["skypeForBusinessInactive"]
        else:
            return None

    @skype_for_business_inactive.setter
    def skype_for_business_inactive(self, val):
        self._prop_dict["skypeForBusinessInactive"] = val

    @property
    def yammer_active(self):
        """
        Gets and sets the yammerActive
        
        Returns:
            int:
                The yammerActive
        """
        if "yammerActive" in self._prop_dict:
            return self._prop_dict["yammerActive"]
        else:
            return None

    @yammer_active.setter
    def yammer_active(self, val):
        self._prop_dict["yammerActive"] = val

    @property
    def yammer_inactive(self):
        """
        Gets and sets the yammerInactive
        
        Returns:
            int:
                The yammerInactive
        """
        if "yammerInactive" in self._prop_dict:
            return self._prop_dict["yammerInactive"]
        else:
            return None

    @yammer_inactive.setter
    def yammer_inactive(self, val):
        self._prop_dict["yammerInactive"] = val

    @property
    def teams_active(self):
        """
        Gets and sets the teamsActive
        
        Returns:
            int:
                The teamsActive
        """
        if "teamsActive" in self._prop_dict:
            return self._prop_dict["teamsActive"]
        else:
            return None

    @teams_active.setter
    def teams_active(self, val):
        self._prop_dict["teamsActive"] = val

    @property
    def teams_inactive(self):
        """
        Gets and sets the teamsInactive
        
        Returns:
            int:
                The teamsInactive
        """
        if "teamsInactive" in self._prop_dict:
            return self._prop_dict["teamsInactive"]
        else:
            return None

    @teams_inactive.setter
    def teams_inactive(self, val):
        self._prop_dict["teamsInactive"] = val

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

