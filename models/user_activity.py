# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.visual_info import VisualInfo
from ..model.json import Json
from ..model.status import Status
from ..model.activity_history_item import ActivityHistoryItem
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class UserActivity(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def visual_elements(self):
        """
        Gets and sets the visualElements
        
        Returns: 
            :class:`VisualInfo<onedrivesdk.model.visual_info.VisualInfo>`:
                The visualElements
        """
        if "visualElements" in self._prop_dict:
            if isinstance(self._prop_dict["visualElements"], OneDriveObjectBase):
                return self._prop_dict["visualElements"]
            else :
                self._prop_dict["visualElements"] = VisualInfo(self._prop_dict["visualElements"])
                return self._prop_dict["visualElements"]

        return None

    @visual_elements.setter
    def visual_elements(self, val):
        self._prop_dict["visualElements"] = val

    @property
    def activity_source_host(self):
        """
        Gets and sets the activitySourceHost
        
        Returns:
            str:
                The activitySourceHost
        """
        if "activitySourceHost" in self._prop_dict:
            return self._prop_dict["activitySourceHost"]
        else:
            return None

    @activity_source_host.setter
    def activity_source_host(self, val):
        self._prop_dict["activitySourceHost"] = val

    @property
    def activation_url(self):
        """
        Gets and sets the activationUrl
        
        Returns:
            str:
                The activationUrl
        """
        if "activationUrl" in self._prop_dict:
            return self._prop_dict["activationUrl"]
        else:
            return None

    @activation_url.setter
    def activation_url(self, val):
        self._prop_dict["activationUrl"] = val

    @property
    def app_activity_id(self):
        """
        Gets and sets the appActivityId
        
        Returns:
            str:
                The appActivityId
        """
        if "appActivityId" in self._prop_dict:
            return self._prop_dict["appActivityId"]
        else:
            return None

    @app_activity_id.setter
    def app_activity_id(self, val):
        self._prop_dict["appActivityId"] = val

    @property
    def app_display_name(self):
        """
        Gets and sets the appDisplayName
        
        Returns:
            str:
                The appDisplayName
        """
        if "appDisplayName" in self._prop_dict:
            return self._prop_dict["appDisplayName"]
        else:
            return None

    @app_display_name.setter
    def app_display_name(self, val):
        self._prop_dict["appDisplayName"] = val

    @property
    def content_url(self):
        """
        Gets and sets the contentUrl
        
        Returns:
            str:
                The contentUrl
        """
        if "contentUrl" in self._prop_dict:
            return self._prop_dict["contentUrl"]
        else:
            return None

    @content_url.setter
    def content_url(self, val):
        self._prop_dict["contentUrl"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

    @property
    def fallback_url(self):
        """
        Gets and sets the fallbackUrl
        
        Returns:
            str:
                The fallbackUrl
        """
        if "fallbackUrl" in self._prop_dict:
            return self._prop_dict["fallbackUrl"]
        else:
            return None

    @fallback_url.setter
    def fallback_url(self, val):
        self._prop_dict["fallbackUrl"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def user_timezone(self):
        """
        Gets and sets the userTimezone
        
        Returns:
            str:
                The userTimezone
        """
        if "userTimezone" in self._prop_dict:
            return self._prop_dict["userTimezone"]
        else:
            return None

    @user_timezone.setter
    def user_timezone(self, val):
        self._prop_dict["userTimezone"] = val

    @property
    def content_info(self):
        """
        Gets and sets the contentInfo
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The contentInfo
        """
        if "contentInfo" in self._prop_dict:
            if isinstance(self._prop_dict["contentInfo"], OneDriveObjectBase):
                return self._prop_dict["contentInfo"]
            else :
                self._prop_dict["contentInfo"] = Json(self._prop_dict["contentInfo"])
                return self._prop_dict["contentInfo"]

        return None

    @content_info.setter
    def content_info(self, val):
        self._prop_dict["contentInfo"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`Status<onedrivesdk.model.status.Status>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = Status(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def history_items(self):
        """Gets and sets the historyItems
        
        Returns: 
            :class:`HistoryItemsCollectionPage<onedrivesdk.request.history_items_collection.HistoryItemsCollectionPage>`:
                The historyItems
        """
        if "historyItems" in self._prop_dict:
            return HistoryItemsCollectionPage(self._prop_dict["historyItems"])
        else:
            return None

