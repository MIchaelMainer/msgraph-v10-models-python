# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365GroupsActivityCounts(OneDriveObjectBase):

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
    def exchange_emails_received(self):
        """
        Gets and sets the exchangeEmailsReceived
        
        Returns:
            int:
                The exchangeEmailsReceived
        """
        if "exchangeEmailsReceived" in self._prop_dict:
            return self._prop_dict["exchangeEmailsReceived"]
        else:
            return None

    @exchange_emails_received.setter
    def exchange_emails_received(self, val):
        self._prop_dict["exchangeEmailsReceived"] = val

    @property
    def yammer_messages_posted(self):
        """
        Gets and sets the yammerMessagesPosted
        
        Returns:
            int:
                The yammerMessagesPosted
        """
        if "yammerMessagesPosted" in self._prop_dict:
            return self._prop_dict["yammerMessagesPosted"]
        else:
            return None

    @yammer_messages_posted.setter
    def yammer_messages_posted(self, val):
        self._prop_dict["yammerMessagesPosted"] = val

    @property
    def yammer_messages_read(self):
        """
        Gets and sets the yammerMessagesRead
        
        Returns:
            int:
                The yammerMessagesRead
        """
        if "yammerMessagesRead" in self._prop_dict:
            return self._prop_dict["yammerMessagesRead"]
        else:
            return None

    @yammer_messages_read.setter
    def yammer_messages_read(self, val):
        self._prop_dict["yammerMessagesRead"] = val

    @property
    def yammer_messages_liked(self):
        """
        Gets and sets the yammerMessagesLiked
        
        Returns:
            int:
                The yammerMessagesLiked
        """
        if "yammerMessagesLiked" in self._prop_dict:
            return self._prop_dict["yammerMessagesLiked"]
        else:
            return None

    @yammer_messages_liked.setter
    def yammer_messages_liked(self, val):
        self._prop_dict["yammerMessagesLiked"] = val

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

