# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class EmailAppUsageAppsUserCounts(OneDriveObjectBase):

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
    def mail_for_mac(self):
        """
        Gets and sets the mailForMac
        
        Returns:
            int:
                The mailForMac
        """
        if "mailForMac" in self._prop_dict:
            return self._prop_dict["mailForMac"]
        else:
            return None

    @mail_for_mac.setter
    def mail_for_mac(self, val):
        self._prop_dict["mailForMac"] = val

    @property
    def outlook_for_mac(self):
        """
        Gets and sets the outlookForMac
        
        Returns:
            int:
                The outlookForMac
        """
        if "outlookForMac" in self._prop_dict:
            return self._prop_dict["outlookForMac"]
        else:
            return None

    @outlook_for_mac.setter
    def outlook_for_mac(self, val):
        self._prop_dict["outlookForMac"] = val

    @property
    def outlook_for_windows(self):
        """
        Gets and sets the outlookForWindows
        
        Returns:
            int:
                The outlookForWindows
        """
        if "outlookForWindows" in self._prop_dict:
            return self._prop_dict["outlookForWindows"]
        else:
            return None

    @outlook_for_windows.setter
    def outlook_for_windows(self, val):
        self._prop_dict["outlookForWindows"] = val

    @property
    def outlook_for_mobile(self):
        """
        Gets and sets the outlookForMobile
        
        Returns:
            int:
                The outlookForMobile
        """
        if "outlookForMobile" in self._prop_dict:
            return self._prop_dict["outlookForMobile"]
        else:
            return None

    @outlook_for_mobile.setter
    def outlook_for_mobile(self, val):
        self._prop_dict["outlookForMobile"] = val

    @property
    def other_for_mobile(self):
        """
        Gets and sets the otherForMobile
        
        Returns:
            int:
                The otherForMobile
        """
        if "otherForMobile" in self._prop_dict:
            return self._prop_dict["otherForMobile"]
        else:
            return None

    @other_for_mobile.setter
    def other_for_mobile(self, val):
        self._prop_dict["otherForMobile"] = val

    @property
    def outlook_for_web(self):
        """
        Gets and sets the outlookForWeb
        
        Returns:
            int:
                The outlookForWeb
        """
        if "outlookForWeb" in self._prop_dict:
            return self._prop_dict["outlookForWeb"]
        else:
            return None

    @outlook_for_web.setter
    def outlook_for_web(self, val):
        self._prop_dict["outlookForWeb"] = val

    @property
    def pop3_app(self):
        """
        Gets and sets the pop3App
        
        Returns:
            int:
                The pop3App
        """
        if "pop3App" in self._prop_dict:
            return self._prop_dict["pop3App"]
        else:
            return None

    @pop3_app.setter
    def pop3_app(self, val):
        self._prop_dict["pop3App"] = val

    @property
    def imap4_app(self):
        """
        Gets and sets the imap4App
        
        Returns:
            int:
                The imap4App
        """
        if "imap4App" in self._prop_dict:
            return self._prop_dict["imap4App"]
        else:
            return None

    @imap4_app.setter
    def imap4_app(self, val):
        self._prop_dict["imap4App"] = val

    @property
    def smtp_app(self):
        """
        Gets and sets the smtpApp
        
        Returns:
            int:
                The smtpApp
        """
        if "smtpApp" in self._prop_dict:
            return self._prop_dict["smtpApp"]
        else:
            return None

    @smtp_app.setter
    def smtp_app(self, val):
        self._prop_dict["smtpApp"] = val

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

