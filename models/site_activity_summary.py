# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class SiteActivitySummary(OneDriveObjectBase):

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
    def viewed_or_edited(self):
        """
        Gets and sets the viewedOrEdited
        
        Returns:
            int:
                The viewedOrEdited
        """
        if "viewedOrEdited" in self._prop_dict:
            return self._prop_dict["viewedOrEdited"]
        else:
            return None

    @viewed_or_edited.setter
    def viewed_or_edited(self, val):
        self._prop_dict["viewedOrEdited"] = val

    @property
    def synced(self):
        """
        Gets and sets the synced
        
        Returns:
            int:
                The synced
        """
        if "synced" in self._prop_dict:
            return self._prop_dict["synced"]
        else:
            return None

    @synced.setter
    def synced(self, val):
        self._prop_dict["synced"] = val

    @property
    def shared_internally(self):
        """
        Gets and sets the sharedInternally
        
        Returns:
            int:
                The sharedInternally
        """
        if "sharedInternally" in self._prop_dict:
            return self._prop_dict["sharedInternally"]
        else:
            return None

    @shared_internally.setter
    def shared_internally(self, val):
        self._prop_dict["sharedInternally"] = val

    @property
    def shared_externally(self):
        """
        Gets and sets the sharedExternally
        
        Returns:
            int:
                The sharedExternally
        """
        if "sharedExternally" in self._prop_dict:
            return self._prop_dict["sharedExternally"]
        else:
            return None

    @shared_externally.setter
    def shared_externally(self, val):
        self._prop_dict["sharedExternally"] = val

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

