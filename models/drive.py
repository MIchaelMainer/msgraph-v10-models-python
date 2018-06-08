# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.quota import Quota
from ..model.sharepoint_ids import SharepointIds
from ..model.system_facet import SystemFacet
from ..model.item_activity import ItemActivity
from ..model.drive_item import DriveItem
from ..model.list import List
from ..one_drive_object_base import OneDriveObjectBase


class Drive(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def drive_type(self):
        """
        Gets and sets the driveType
        
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
    def owner(self):
        """
        Gets and sets the owner
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The owner
        """
        if "owner" in self._prop_dict:
            if isinstance(self._prop_dict["owner"], OneDriveObjectBase):
                return self._prop_dict["owner"]
            else :
                self._prop_dict["owner"] = IdentitySet(self._prop_dict["owner"])
                return self._prop_dict["owner"]

        return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

    @property
    def quota(self):
        """
        Gets and sets the quota
        
        Returns: 
            :class:`Quota<onedrivesdk.model.quota.Quota>`:
                The quota
        """
        if "quota" in self._prop_dict:
            if isinstance(self._prop_dict["quota"], OneDriveObjectBase):
                return self._prop_dict["quota"]
            else :
                self._prop_dict["quota"] = Quota(self._prop_dict["quota"])
                return self._prop_dict["quota"]

        return None

    @quota.setter
    def quota(self, val):
        self._prop_dict["quota"] = val

    @property
    def share_point_ids(self):
        """
        Gets and sets the sharePointIds
        
        Returns: 
            :class:`SharepointIds<onedrivesdk.model.sharepoint_ids.SharepointIds>`:
                The sharePointIds
        """
        if "sharePointIds" in self._prop_dict:
            if isinstance(self._prop_dict["sharePointIds"], OneDriveObjectBase):
                return self._prop_dict["sharePointIds"]
            else :
                self._prop_dict["sharePointIds"] = SharepointIds(self._prop_dict["sharePointIds"])
                return self._prop_dict["sharePointIds"]

        return None

    @share_point_ids.setter
    def share_point_ids(self, val):
        self._prop_dict["sharePointIds"] = val

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

    @property
    def list(self):
        """
        Gets and sets the list
        
        Returns: 
            :class:`List<onedrivesdk.model.list.List>`:
                The list
        """
        if "list" in self._prop_dict:
            if isinstance(self._prop_dict["list"], OneDriveObjectBase):
                return self._prop_dict["list"]
            else :
                self._prop_dict["list"] = List(self._prop_dict["list"])
                return self._prop_dict["list"]

        return None

    @list.setter
    def list(self, val):
        self._prop_dict["list"] = val

    @property
    def root(self):
        """
        Gets and sets the root
        
        Returns: 
            :class:`DriveItem<onedrivesdk.model.drive_item.DriveItem>`:
                The root
        """
        if "root" in self._prop_dict:
            if isinstance(self._prop_dict["root"], OneDriveObjectBase):
                return self._prop_dict["root"]
            else :
                self._prop_dict["root"] = DriveItem(self._prop_dict["root"])
                return self._prop_dict["root"]

        return None

    @root.setter
    def root(self, val):
        self._prop_dict["root"] = val

    @property
    def special(self):
        """Gets and sets the special
        
        Returns: 
            :class:`SpecialCollectionPage<onedrivesdk.request.special_collection.SpecialCollectionPage>`:
                The special
        """
        if "special" in self._prop_dict:
            return SpecialCollectionPage(self._prop_dict["special"])
        else:
            return None

