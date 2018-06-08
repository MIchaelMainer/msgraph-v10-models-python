# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class TeamsUserActivityUserDetail(OneDriveObjectBase):

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
    def assigned_products(self):
        """
        Gets and sets the assignedProducts
        
        Returns:
            str:
                The assignedProducts
        """
        if "assignedProducts" in self._prop_dict:
            return self._prop_dict["assignedProducts"]
        else:
            return None

    @assigned_products.setter
    def assigned_products(self, val):
        self._prop_dict["assignedProducts"] = val

    @property
    def team_chat_message_count(self):
        """
        Gets and sets the teamChatMessageCount
        
        Returns:
            int:
                The teamChatMessageCount
        """
        if "teamChatMessageCount" in self._prop_dict:
            return self._prop_dict["teamChatMessageCount"]
        else:
            return None

    @team_chat_message_count.setter
    def team_chat_message_count(self, val):
        self._prop_dict["teamChatMessageCount"] = val

    @property
    def private_chat_message_count(self):
        """
        Gets and sets the privateChatMessageCount
        
        Returns:
            int:
                The privateChatMessageCount
        """
        if "privateChatMessageCount" in self._prop_dict:
            return self._prop_dict["privateChatMessageCount"]
        else:
            return None

    @private_chat_message_count.setter
    def private_chat_message_count(self, val):
        self._prop_dict["privateChatMessageCount"] = val

    @property
    def call_count(self):
        """
        Gets and sets the callCount
        
        Returns:
            int:
                The callCount
        """
        if "callCount" in self._prop_dict:
            return self._prop_dict["callCount"]
        else:
            return None

    @call_count.setter
    def call_count(self, val):
        self._prop_dict["callCount"] = val

    @property
    def meeting_count(self):
        """
        Gets and sets the meetingCount
        
        Returns:
            int:
                The meetingCount
        """
        if "meetingCount" in self._prop_dict:
            return self._prop_dict["meetingCount"]
        else:
            return None

    @meeting_count.setter
    def meeting_count(self, val):
        self._prop_dict["meetingCount"] = val

    @property
    def has_other_action(self):
        """
        Gets and sets the hasOtherAction
        
        Returns:
            bool:
                The hasOtherAction
        """
        if "hasOtherAction" in self._prop_dict:
            return self._prop_dict["hasOtherAction"]
        else:
            return None

    @has_other_action.setter
    def has_other_action(self, val):
        self._prop_dict["hasOtherAction"] = val

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

