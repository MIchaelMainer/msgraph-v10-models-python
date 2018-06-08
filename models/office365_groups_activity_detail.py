# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365GroupsActivityDetail(OneDriveObjectBase):

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
    def external_member_count(self):
        """
        Gets and sets the externalMemberCount
        
        Returns:
            int:
                The externalMemberCount
        """
        if "externalMemberCount" in self._prop_dict:
            return self._prop_dict["externalMemberCount"]
        else:
            return None

    @external_member_count.setter
    def external_member_count(self, val):
        self._prop_dict["externalMemberCount"] = val

    @property
    def exchange_received_email_count(self):
        """
        Gets and sets the exchangeReceivedEmailCount
        
        Returns:
            int:
                The exchangeReceivedEmailCount
        """
        if "exchangeReceivedEmailCount" in self._prop_dict:
            return self._prop_dict["exchangeReceivedEmailCount"]
        else:
            return None

    @exchange_received_email_count.setter
    def exchange_received_email_count(self, val):
        self._prop_dict["exchangeReceivedEmailCount"] = val

    @property
    def share_point_active_file_count(self):
        """
        Gets and sets the sharePointActiveFileCount
        
        Returns:
            int:
                The sharePointActiveFileCount
        """
        if "sharePointActiveFileCount" in self._prop_dict:
            return self._prop_dict["sharePointActiveFileCount"]
        else:
            return None

    @share_point_active_file_count.setter
    def share_point_active_file_count(self, val):
        self._prop_dict["sharePointActiveFileCount"] = val

    @property
    def yammer_posted_message_count(self):
        """
        Gets and sets the yammerPostedMessageCount
        
        Returns:
            int:
                The yammerPostedMessageCount
        """
        if "yammerPostedMessageCount" in self._prop_dict:
            return self._prop_dict["yammerPostedMessageCount"]
        else:
            return None

    @yammer_posted_message_count.setter
    def yammer_posted_message_count(self, val):
        self._prop_dict["yammerPostedMessageCount"] = val

    @property
    def yammer_read_message_count(self):
        """
        Gets and sets the yammerReadMessageCount
        
        Returns:
            int:
                The yammerReadMessageCount
        """
        if "yammerReadMessageCount" in self._prop_dict:
            return self._prop_dict["yammerReadMessageCount"]
        else:
            return None

    @yammer_read_message_count.setter
    def yammer_read_message_count(self, val):
        self._prop_dict["yammerReadMessageCount"] = val

    @property
    def yammer_liked_message_count(self):
        """
        Gets and sets the yammerLikedMessageCount
        
        Returns:
            int:
                The yammerLikedMessageCount
        """
        if "yammerLikedMessageCount" in self._prop_dict:
            return self._prop_dict["yammerLikedMessageCount"]
        else:
            return None

    @yammer_liked_message_count.setter
    def yammer_liked_message_count(self, val):
        self._prop_dict["yammerLikedMessageCount"] = val

    @property
    def exchange_mailbox_total_item_count(self):
        """
        Gets and sets the exchangeMailboxTotalItemCount
        
        Returns:
            int:
                The exchangeMailboxTotalItemCount
        """
        if "exchangeMailboxTotalItemCount" in self._prop_dict:
            return self._prop_dict["exchangeMailboxTotalItemCount"]
        else:
            return None

    @exchange_mailbox_total_item_count.setter
    def exchange_mailbox_total_item_count(self, val):
        self._prop_dict["exchangeMailboxTotalItemCount"] = val

    @property
    def exchange_mailbox_storage_used_in_bytes(self):
        """
        Gets and sets the exchangeMailboxStorageUsedInBytes
        
        Returns:
            int:
                The exchangeMailboxStorageUsedInBytes
        """
        if "exchangeMailboxStorageUsedInBytes" in self._prop_dict:
            return self._prop_dict["exchangeMailboxStorageUsedInBytes"]
        else:
            return None

    @exchange_mailbox_storage_used_in_bytes.setter
    def exchange_mailbox_storage_used_in_bytes(self, val):
        self._prop_dict["exchangeMailboxStorageUsedInBytes"] = val

    @property
    def share_point_total_file_count(self):
        """
        Gets and sets the sharePointTotalFileCount
        
        Returns:
            int:
                The sharePointTotalFileCount
        """
        if "sharePointTotalFileCount" in self._prop_dict:
            return self._prop_dict["sharePointTotalFileCount"]
        else:
            return None

    @share_point_total_file_count.setter
    def share_point_total_file_count(self, val):
        self._prop_dict["sharePointTotalFileCount"] = val

    @property
    def share_point_site_storage_used_in_bytes(self):
        """
        Gets and sets the sharePointSiteStorageUsedInBytes
        
        Returns:
            int:
                The sharePointSiteStorageUsedInBytes
        """
        if "sharePointSiteStorageUsedInBytes" in self._prop_dict:
            return self._prop_dict["sharePointSiteStorageUsedInBytes"]
        else:
            return None

    @share_point_site_storage_used_in_bytes.setter
    def share_point_site_storage_used_in_bytes(self, val):
        self._prop_dict["sharePointSiteStorageUsedInBytes"] = val

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

