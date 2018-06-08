# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.content_type_info import ContentTypeInfo
from ..model.sharepoint_ids import SharepointIds
from ..model.drive_item import DriveItem
from ..model.field_value_set import FieldValueSet
from ..model.list_item_version import ListItemVersion
from ..one_drive_object_base import OneDriveObjectBase


class ListItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def content_type(self):
        """
        Gets and sets the contentType
        
        Returns: 
            :class:`ContentTypeInfo<onedrivesdk.model.content_type_info.ContentTypeInfo>`:
                The contentType
        """
        if "contentType" in self._prop_dict:
            if isinstance(self._prop_dict["contentType"], OneDriveObjectBase):
                return self._prop_dict["contentType"]
            else :
                self._prop_dict["contentType"] = ContentTypeInfo(self._prop_dict["contentType"])
                return self._prop_dict["contentType"]

        return None

    @content_type.setter
    def content_type(self, val):
        self._prop_dict["contentType"] = val

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
    def drive_item(self):
        """
        Gets and sets the driveItem
        
        Returns: 
            :class:`DriveItem<onedrivesdk.model.drive_item.DriveItem>`:
                The driveItem
        """
        if "driveItem" in self._prop_dict:
            if isinstance(self._prop_dict["driveItem"], OneDriveObjectBase):
                return self._prop_dict["driveItem"]
            else :
                self._prop_dict["driveItem"] = DriveItem(self._prop_dict["driveItem"])
                return self._prop_dict["driveItem"]

        return None

    @drive_item.setter
    def drive_item(self, val):
        self._prop_dict["driveItem"] = val

    @property
    def fields(self):
        """
        Gets and sets the fields
        
        Returns: 
            :class:`FieldValueSet<onedrivesdk.model.field_value_set.FieldValueSet>`:
                The fields
        """
        if "fields" in self._prop_dict:
            if isinstance(self._prop_dict["fields"], OneDriveObjectBase):
                return self._prop_dict["fields"]
            else :
                self._prop_dict["fields"] = FieldValueSet(self._prop_dict["fields"])
                return self._prop_dict["fields"]

        return None

    @fields.setter
    def fields(self, val):
        self._prop_dict["fields"] = val

    @property
    def versions(self):
        """Gets and sets the versions
        
        Returns: 
            :class:`VersionsCollectionPage<onedrivesdk.request.versions_collection.VersionsCollectionPage>`:
                The versions
        """
        if "versions" in self._prop_dict:
            return VersionsCollectionPage(self._prop_dict["versions"])
        else:
            return None

