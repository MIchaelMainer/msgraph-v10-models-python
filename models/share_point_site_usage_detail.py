# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class SharePointSiteUsageDetail(OneDriveObjectBase):

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
    def site_id(self):
        """
        Gets and sets the siteId
        
        Returns:
            UUID:
                The siteId
        """
        if "siteId" in self._prop_dict:
            return self._prop_dict["siteId"]
        else:
            return None

    @site_id.setter
    def site_id(self, val):
        self._prop_dict["siteId"] = val

    @property
    def site_url(self):
        """
        Gets and sets the siteUrl
        
        Returns:
            str:
                The siteUrl
        """
        if "siteUrl" in self._prop_dict:
            return self._prop_dict["siteUrl"]
        else:
            return None

    @site_url.setter
    def site_url(self, val):
        self._prop_dict["siteUrl"] = val

    @property
    def owner_display_name(self):
        """
        Gets and sets the ownerDisplayName
        
        Returns:
            str:
                The ownerDisplayName
        """
        if "ownerDisplayName" in self._prop_dict:
            return self._prop_dict["ownerDisplayName"]
        else:
            return None

    @owner_display_name.setter
    def owner_display_name(self, val):
        self._prop_dict["ownerDisplayName"] = val

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
    def file_count(self):
        """
        Gets and sets the fileCount
        
        Returns:
            int:
                The fileCount
        """
        if "fileCount" in self._prop_dict:
            return self._prop_dict["fileCount"]
        else:
            return None

    @file_count.setter
    def file_count(self, val):
        self._prop_dict["fileCount"] = val

    @property
    def active_file_count(self):
        """
        Gets and sets the activeFileCount
        
        Returns:
            int:
                The activeFileCount
        """
        if "activeFileCount" in self._prop_dict:
            return self._prop_dict["activeFileCount"]
        else:
            return None

    @active_file_count.setter
    def active_file_count(self, val):
        self._prop_dict["activeFileCount"] = val

    @property
    def page_view_count(self):
        """
        Gets and sets the pageViewCount
        
        Returns:
            int:
                The pageViewCount
        """
        if "pageViewCount" in self._prop_dict:
            return self._prop_dict["pageViewCount"]
        else:
            return None

    @page_view_count.setter
    def page_view_count(self, val):
        self._prop_dict["pageViewCount"] = val

    @property
    def visited_page_count(self):
        """
        Gets and sets the visitedPageCount
        
        Returns:
            int:
                The visitedPageCount
        """
        if "visitedPageCount" in self._prop_dict:
            return self._prop_dict["visitedPageCount"]
        else:
            return None

    @visited_page_count.setter
    def visited_page_count(self, val):
        self._prop_dict["visitedPageCount"] = val

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
    def storage_allocated_in_bytes(self):
        """
        Gets and sets the storageAllocatedInBytes
        
        Returns:
            int:
                The storageAllocatedInBytes
        """
        if "storageAllocatedInBytes" in self._prop_dict:
            return self._prop_dict["storageAllocatedInBytes"]
        else:
            return None

    @storage_allocated_in_bytes.setter
    def storage_allocated_in_bytes(self, val):
        self._prop_dict["storageAllocatedInBytes"] = val

    @property
    def root_web_template(self):
        """
        Gets and sets the rootWebTemplate
        
        Returns:
            str:
                The rootWebTemplate
        """
        if "rootWebTemplate" in self._prop_dict:
            return self._prop_dict["rootWebTemplate"]
        else:
            return None

    @root_web_template.setter
    def root_web_template(self, val):
        self._prop_dict["rootWebTemplate"] = val

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

