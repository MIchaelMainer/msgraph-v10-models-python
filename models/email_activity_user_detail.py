# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class EmailActivityUserDetail(OneDriveObjectBase):

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
    def send_count(self):
        """
        Gets and sets the sendCount
        
        Returns:
            int:
                The sendCount
        """
        if "sendCount" in self._prop_dict:
            return self._prop_dict["sendCount"]
        else:
            return None

    @send_count.setter
    def send_count(self, val):
        self._prop_dict["sendCount"] = val

    @property
    def receive_count(self):
        """
        Gets and sets the receiveCount
        
        Returns:
            int:
                The receiveCount
        """
        if "receiveCount" in self._prop_dict:
            return self._prop_dict["receiveCount"]
        else:
            return None

    @receive_count.setter
    def receive_count(self, val):
        self._prop_dict["receiveCount"] = val

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

