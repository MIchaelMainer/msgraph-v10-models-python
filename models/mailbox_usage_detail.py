# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class MailboxUsageDetail(OneDriveObjectBase):

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
    def created_date(self):
        """
        Gets and sets the createdDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The createdDate
        """
        if "createdDate" in self._prop_dict:
            if isinstance(self._prop_dict["createdDate"], OneDriveObjectBase):
                return self._prop_dict["createdDate"]
            else :
                self._prop_dict["createdDate"] = Date(self._prop_dict["createdDate"])
                return self._prop_dict["createdDate"]

        return None

    @created_date.setter
    def created_date(self, val):
        self._prop_dict["createdDate"] = val

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
    def item_count(self):
        """
        Gets and sets the itemCount
        
        Returns:
            int:
                The itemCount
        """
        if "itemCount" in self._prop_dict:
            return self._prop_dict["itemCount"]
        else:
            return None

    @item_count.setter
    def item_count(self, val):
        self._prop_dict["itemCount"] = val

    @property
    def storage_used_in_bytes(self):
        """
        Gets and sets the storageUsedInBytes
        
        Returns:
            int:
                The storageUsedInBytes
        """
        if "storageUsedInBytes" in self._prop_dict:
            return self._prop_dict["storageUsedInBytes"]
        else:
            return None

    @storage_used_in_bytes.setter
    def storage_used_in_bytes(self, val):
        self._prop_dict["storageUsedInBytes"] = val

    @property
    def issue_warning_quota_in_bytes(self):
        """
        Gets and sets the issueWarningQuotaInBytes
        
        Returns:
            int:
                The issueWarningQuotaInBytes
        """
        if "issueWarningQuotaInBytes" in self._prop_dict:
            return self._prop_dict["issueWarningQuotaInBytes"]
        else:
            return None

    @issue_warning_quota_in_bytes.setter
    def issue_warning_quota_in_bytes(self, val):
        self._prop_dict["issueWarningQuotaInBytes"] = val

    @property
    def prohibit_send_quota_in_bytes(self):
        """
        Gets and sets the prohibitSendQuotaInBytes
        
        Returns:
            int:
                The prohibitSendQuotaInBytes
        """
        if "prohibitSendQuotaInBytes" in self._prop_dict:
            return self._prop_dict["prohibitSendQuotaInBytes"]
        else:
            return None

    @prohibit_send_quota_in_bytes.setter
    def prohibit_send_quota_in_bytes(self, val):
        self._prop_dict["prohibitSendQuotaInBytes"] = val

    @property
    def prohibit_send_receive_quota_in_bytes(self):
        """
        Gets and sets the prohibitSendReceiveQuotaInBytes
        
        Returns:
            int:
                The prohibitSendReceiveQuotaInBytes
        """
        if "prohibitSendReceiveQuotaInBytes" in self._prop_dict:
            return self._prop_dict["prohibitSendReceiveQuotaInBytes"]
        else:
            return None

    @prohibit_send_receive_quota_in_bytes.setter
    def prohibit_send_receive_quota_in_bytes(self, val):
        self._prop_dict["prohibitSendReceiveQuotaInBytes"] = val

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

