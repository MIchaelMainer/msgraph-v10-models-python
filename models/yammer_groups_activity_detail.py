# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class YammerGroupsActivityDetail(OneDriveObjectBase):

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
    def group_display_name(self):
        """
        Gets and sets the groupDisplayName
        
        Returns:
            str:
                The groupDisplayName
        """
        if "groupDisplayName" in self._prop_dict:
            return self._prop_dict["groupDisplayName"]
        else:
            return None

    @group_display_name.setter
    def group_display_name(self, val):
        self._prop_dict["groupDisplayName"] = val

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
    def owner_principal_name(self):
        """
        Gets and sets the ownerPrincipalName
        
        Returns:
            str:
                The ownerPrincipalName
        """
        if "ownerPrincipalName" in self._prop_dict:
            return self._prop_dict["ownerPrincipalName"]
        else:
            return None

    @owner_principal_name.setter
    def owner_principal_name(self, val):
        self._prop_dict["ownerPrincipalName"] = val

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
    def group_type(self):
        """
        Gets and sets the groupType
        
        Returns:
            str:
                The groupType
        """
        if "groupType" in self._prop_dict:
            return self._prop_dict["groupType"]
        else:
            return None

    @group_type.setter
    def group_type(self, val):
        self._prop_dict["groupType"] = val

    @property
    def office365_connected(self):
        """
        Gets and sets the office365Connected
        
        Returns:
            bool:
                The office365Connected
        """
        if "office365Connected" in self._prop_dict:
            return self._prop_dict["office365Connected"]
        else:
            return None

    @office365_connected.setter
    def office365_connected(self, val):
        self._prop_dict["office365Connected"] = val

    @property
    def member_count(self):
        """
        Gets and sets the memberCount
        
        Returns:
            int:
                The memberCount
        """
        if "memberCount" in self._prop_dict:
            return self._prop_dict["memberCount"]
        else:
            return None

    @member_count.setter
    def member_count(self, val):
        self._prop_dict["memberCount"] = val

    @property
    def posted_count(self):
        """
        Gets and sets the postedCount
        
        Returns:
            int:
                The postedCount
        """
        if "postedCount" in self._prop_dict:
            return self._prop_dict["postedCount"]
        else:
            return None

    @posted_count.setter
    def posted_count(self, val):
        self._prop_dict["postedCount"] = val

    @property
    def read_count(self):
        """
        Gets and sets the readCount
        
        Returns:
            int:
                The readCount
        """
        if "readCount" in self._prop_dict:
            return self._prop_dict["readCount"]
        else:
            return None

    @read_count.setter
    def read_count(self, val):
        self._prop_dict["readCount"] = val

    @property
    def liked_count(self):
        """
        Gets and sets the likedCount
        
        Returns:
            int:
                The likedCount
        """
        if "likedCount" in self._prop_dict:
            return self._prop_dict["likedCount"]
        else:
            return None

    @liked_count.setter
    def liked_count(self, val):
        self._prop_dict["likedCount"] = val

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

