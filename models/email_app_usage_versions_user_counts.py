# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class EmailAppUsageVersionsUserCounts(OneDriveObjectBase):

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
    def outlook2016(self):
        """
        Gets and sets the outlook2016
        
        Returns:
            int:
                The outlook2016
        """
        if "outlook2016" in self._prop_dict:
            return self._prop_dict["outlook2016"]
        else:
            return None

    @outlook2016.setter
    def outlook2016(self, val):
        self._prop_dict["outlook2016"] = val

    @property
    def outlook2013(self):
        """
        Gets and sets the outlook2013
        
        Returns:
            int:
                The outlook2013
        """
        if "outlook2013" in self._prop_dict:
            return self._prop_dict["outlook2013"]
        else:
            return None

    @outlook2013.setter
    def outlook2013(self, val):
        self._prop_dict["outlook2013"] = val

    @property
    def outlook2010(self):
        """
        Gets and sets the outlook2010
        
        Returns:
            int:
                The outlook2010
        """
        if "outlook2010" in self._prop_dict:
            return self._prop_dict["outlook2010"]
        else:
            return None

    @outlook2010.setter
    def outlook2010(self, val):
        self._prop_dict["outlook2010"] = val

    @property
    def outlook2007(self):
        """
        Gets and sets the outlook2007
        
        Returns:
            int:
                The outlook2007
        """
        if "outlook2007" in self._prop_dict:
            return self._prop_dict["outlook2007"]
        else:
            return None

    @outlook2007.setter
    def outlook2007(self, val):
        self._prop_dict["outlook2007"] = val

    @property
    def undetermined(self):
        """
        Gets and sets the undetermined
        
        Returns:
            int:
                The undetermined
        """
        if "undetermined" in self._prop_dict:
            return self._prop_dict["undetermined"]
        else:
            return None

    @undetermined.setter
    def undetermined(self, val):
        self._prop_dict["undetermined"] = val

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

