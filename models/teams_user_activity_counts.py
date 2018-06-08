# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class TeamsUserActivityCounts(OneDriveObjectBase):

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
    def team_chat_messages(self):
        """
        Gets and sets the teamChatMessages
        
        Returns:
            int:
                The teamChatMessages
        """
        if "teamChatMessages" in self._prop_dict:
            return self._prop_dict["teamChatMessages"]
        else:
            return None

    @team_chat_messages.setter
    def team_chat_messages(self, val):
        self._prop_dict["teamChatMessages"] = val

    @property
    def private_chat_messages(self):
        """
        Gets and sets the privateChatMessages
        
        Returns:
            int:
                The privateChatMessages
        """
        if "privateChatMessages" in self._prop_dict:
            return self._prop_dict["privateChatMessages"]
        else:
            return None

    @private_chat_messages.setter
    def private_chat_messages(self, val):
        self._prop_dict["privateChatMessages"] = val

    @property
    def calls(self):
        """
        Gets and sets the calls
        
        Returns:
            int:
                The calls
        """
        if "calls" in self._prop_dict:
            return self._prop_dict["calls"]
        else:
            return None

    @calls.setter
    def calls(self, val):
        self._prop_dict["calls"] = val

    @property
    def meetings(self):
        """
        Gets and sets the meetings
        
        Returns:
            int:
                The meetings
        """
        if "meetings" in self._prop_dict:
            return self._prop_dict["meetings"]
        else:
            return None

    @meetings.setter
    def meetings(self, val):
        self._prop_dict["meetings"] = val

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

