# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class EmailAppUsageUserDetail(OneDriveObjectBase):

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
    def is_deleted(self):
        """
        Gets and sets the isDeleted
        
        Returns:
            bool:
                The isDeleted
        """
        if "isDeleted" in self._prop_dict:
            return self._prop_dict["isDeleted"]
        else:
            return None

    @is_deleted.setter
    def is_deleted(self, val):
        self._prop_dict["isDeleted"] = val

    @property
    def deleted_date(self):
        """
        Gets and sets the deletedDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The deletedDate
        """
        if "deletedDate" in self._prop_dict:
            if isinstance(self._prop_dict["deletedDate"], OneDriveObjectBase):
                return self._prop_dict["deletedDate"]
            else :
                self._prop_dict["deletedDate"] = Date(self._prop_dict["deletedDate"])
                return self._prop_dict["deletedDate"]

        return None

    @deleted_date.setter
    def deleted_date(self, val):
        self._prop_dict["deletedDate"] = val

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
    def mail_for_mac(self):
        """
        Gets and sets the mailForMac
        
        Returns:
            str:
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
            str:
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
            str:
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
            str:
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
            str:
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
            str:
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
            str:
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
            str:
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
            str:
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

