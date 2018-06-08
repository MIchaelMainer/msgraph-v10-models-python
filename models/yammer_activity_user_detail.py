# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class YammerActivityUserDetail(OneDriveObjectBase):

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
    def user_state(self):
        """
        Gets and sets the userState
        
        Returns:
            str:
                The userState
        """
        if "userState" in self._prop_dict:
            return self._prop_dict["userState"]
        else:
            return None

    @user_state.setter
    def user_state(self, val):
        self._prop_dict["userState"] = val

    @property
    def state_change_date(self):
        """
        Gets and sets the stateChangeDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The stateChangeDate
        """
        if "stateChangeDate" in self._prop_dict:
            if isinstance(self._prop_dict["stateChangeDate"], OneDriveObjectBase):
                return self._prop_dict["stateChangeDate"]
            else :
                self._prop_dict["stateChangeDate"] = Date(self._prop_dict["stateChangeDate"])
                return self._prop_dict["stateChangeDate"]

        return None

    @state_change_date.setter
    def state_change_date(self, val):
        self._prop_dict["stateChangeDate"] = val

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

