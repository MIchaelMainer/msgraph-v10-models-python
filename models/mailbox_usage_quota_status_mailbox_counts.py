# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class MailboxUsageQuotaStatusMailboxCounts(OneDriveObjectBase):

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
    def under_limit(self):
        """
        Gets and sets the underLimit
        
        Returns:
            int:
                The underLimit
        """
        if "underLimit" in self._prop_dict:
            return self._prop_dict["underLimit"]
        else:
            return None

    @under_limit.setter
    def under_limit(self, val):
        self._prop_dict["underLimit"] = val

    @property
    def warning_issued(self):
        """
        Gets and sets the warningIssued
        
        Returns:
            int:
                The warningIssued
        """
        if "warningIssued" in self._prop_dict:
            return self._prop_dict["warningIssued"]
        else:
            return None

    @warning_issued.setter
    def warning_issued(self, val):
        self._prop_dict["warningIssued"] = val

    @property
    def send_prohibited(self):
        """
        Gets and sets the sendProhibited
        
        Returns:
            int:
                The sendProhibited
        """
        if "sendProhibited" in self._prop_dict:
            return self._prop_dict["sendProhibited"]
        else:
            return None

    @send_prohibited.setter
    def send_prohibited(self, val):
        self._prop_dict["sendProhibited"] = val

    @property
    def send_receive_prohibited(self):
        """
        Gets and sets the sendReceiveProhibited
        
        Returns:
            int:
                The sendReceiveProhibited
        """
        if "sendReceiveProhibited" in self._prop_dict:
            return self._prop_dict["sendReceiveProhibited"]
        else:
            return None

    @send_receive_prohibited.setter
    def send_receive_prohibited(self, val):
        self._prop_dict["sendReceiveProhibited"] = val

    @property
    def indeterminate(self):
        """
        Gets and sets the indeterminate
        
        Returns:
            int:
                The indeterminate
        """
        if "indeterminate" in self._prop_dict:
            return self._prop_dict["indeterminate"]
        else:
            return None

    @indeterminate.setter
    def indeterminate(self, val):
        self._prop_dict["indeterminate"] = val

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

