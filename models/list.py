# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.list_info import ListInfo
from ..model.sharepoint_ids import SharepointIds
from ..model.system_facet import SystemFacet
from ..model.item_activity import ItemActivity
from ..model.column_definition import ColumnDefinition
from ..model.content_type import ContentType
from ..model.drive import Drive
from ..model.list_item import ListItem
from ..one_drive_object_base import OneDriveObjectBase


class List(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def list(self):
        """
        Gets and sets the list
        
        Returns: 
            :class:`ListInfo<onedrivesdk.model.list_info.ListInfo>`:
                The list
        """
        if "list" in self._prop_dict:
            if isinstance(self._prop_dict["list"], OneDriveObjectBase):
                return self._prop_dict["list"]
            else :
                self._prop_dict["list"] = ListInfo(self._prop_dict["list"])
                return self._prop_dict["list"]

        return None

    @list.setter
    def list(self, val):
        self._prop_dict["list"] = val

    @property
    def sharepoint_ids(self):
        """
        Gets and sets the sharepointIds
        
        Returns: 
            :class:`SharepointIds<onedrivesdk.model.sharepoint_ids.SharepointIds>`:
                The sharepointIds
        """
        if "sharepointIds" in self._prop_dict:
            if isinstance(self._prop_dict["sharepointIds"], OneDriveObjectBase):
                return self._prop_dict["sharepointIds"]
            else :
                self._prop_dict["sharepointIds"] = SharepointIds(self._prop_dict["sharepointIds"])
                return self._prop_dict["sharepointIds"]

        return None

    @sharepoint_ids.setter
    def sharepoint_ids(self, val):
        self._prop_dict["sharepointIds"] = val

    @property
    def system(self):
        """
        Gets and sets the system
        
        Returns: 
            :class:`SystemFacet<onedrivesdk.model.system_facet.SystemFacet>`:
                The system
        """
        if "system" in self._prop_dict:
            if isinstance(self._prop_dict["system"], OneDriveObjectBase):
                return self._prop_dict["system"]
            else :
                self._prop_dict["system"] = SystemFacet(self._prop_dict["system"])
                return self._prop_dict["system"]

        return None

    @system.setter
    def system(self, val):
        self._prop_dict["system"] = val

    @property
    def activities(self):
        """Gets and sets the activities
        
        Returns: 
            :class:`ActivitiesCollectionPage<onedrivesdk.request.activities_collection.ActivitiesCollectionPage>`:
                The activities
        """
        if "activities" in self._prop_dict:
            return ActivitiesCollectionPage(self._prop_dict["activities"])
        else:
            return None

    @property
    def columns(self):
        """Gets and sets the columns
        
        Returns: 
            :class:`ColumnsCollectionPage<onedrivesdk.request.columns_collection.ColumnsCollectionPage>`:
                The columns
        """
        if "columns" in self._prop_dict:
            return ColumnsCollectionPage(self._prop_dict["columns"])
        else:
            return None

    @property
    def content_types(self):
        """Gets and sets the contentTypes
        
        Returns: 
            :class:`ContentTypesCollectionPage<onedrivesdk.request.content_types_collection.ContentTypesCollectionPage>`:
                The contentTypes
        """
        if "contentTypes" in self._prop_dict:
            return ContentTypesCollectionPage(self._prop_dict["contentTypes"])
        else:
            return None

    @property
    def drive(self):
        """
        Gets and sets the drive
        
        Returns: 
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The drive
        """
        if "drive" in self._prop_dict:
            if isinstance(self._prop_dict["drive"], OneDriveObjectBase):
                return self._prop_dict["drive"]
            else :
                self._prop_dict["drive"] = Drive(self._prop_dict["drive"])
                return self._prop_dict["drive"]

        return None

    @drive.setter
    def drive(self, val):
        self._prop_dict["drive"] = val

    @property
    def items(self):
        """Gets and sets the items
        
        Returns: 
            :class:`ItemsCollectionPage<onedrivesdk.request.items_collection.ItemsCollectionPage>`:
                The items
        """
        if "items" in self._prop_dict:
            return ItemsCollectionPage(self._prop_dict["items"])
        else:
            return None

