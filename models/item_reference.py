# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sharepoint_ids import SharepointIds
from ..one_drive_object_base import OneDriveObjectBase


class ItemReference(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def drive_id(self):
        """Gets and sets the driveId
        
        Returns: 
            str:
                The driveId
        """
        if "driveId" in self._prop_dict:
            return self._prop_dict["driveId"]
        else:
            return None

    @drive_id.setter
    def drive_id(self, val):
        self._prop_dict["driveId"] = val

    @property
    def drive_type(self):
        """Gets and sets the driveType
        
        Returns: 
            str:
                The driveType
        """
        if "driveType" in self._prop_dict:
            return self._prop_dict["driveType"]
        else:
            return None

    @drive_type.setter
    def drive_type(self, val):
        self._prop_dict["driveType"] = val

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def parent(self):
        """
        Gets and sets the parent
        
        Returns: 
            :class:`ItemReference<onedrivesdk.model.item_reference.ItemReference>`:
                The parent
        """
        if "parent" in self._prop_dict:
            if isinstance(self._prop_dict["parent"], OneDriveObjectBase):
                return self._prop_dict["parent"]
            else :
                self._prop_dict["parent"] = ItemReference(self._prop_dict["parent"])
                return self._prop_dict["parent"]

        return None

    @parent.setter
    def parent(self, val):
        self._prop_dict["parent"] = val
    @property
    def path(self):
        """Gets and sets the path
        
        Returns: 
            str:
                The path
        """
        if "path" in self._prop_dict:
            return self._prop_dict["path"]
        else:
            return None

    @path.setter
    def path(self, val):
        self._prop_dict["path"] = val

    @property
    def share_id(self):
        """Gets and sets the shareId
        
        Returns: 
            str:
                The shareId
        """
        if "shareId" in self._prop_dict:
            return self._prop_dict["shareId"]
        else:
            return None

    @share_id.setter
    def share_id(self, val):
        self._prop_dict["shareId"] = val

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
