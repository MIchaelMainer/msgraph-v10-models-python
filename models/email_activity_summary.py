# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class EmailActivitySummary(OneDriveObjectBase):

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
    def send(self):
        """
        Gets and sets the send
        
        Returns:
            int:
                The send
        """
        if "send" in self._prop_dict:
            return self._prop_dict["send"]
        else:
            return None

    @send.setter
    def send(self, val):
        self._prop_dict["send"] = val

    @property
    def receive(self):
        """
        Gets and sets the receive
        
        Returns:
            int:
                The receive
        """
        if "receive" in self._prop_dict:
            return self._prop_dict["receive"]
        else:
            return None

    @receive.setter
    def receive(self, val):
        self._prop_dict["receive"] = val

    @property
    def read(self):
        """
        Gets and sets the read
        
        Returns:
            int:
                The read
        """
        if "read" in self._prop_dict:
            return self._prop_dict["read"]
        else:
            return None

    @read.setter
    def read(self, val):
        self._prop_dict["read"] = val

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

