# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.drive_item import DriveItem
from ..model.list import List
from ..model.list_item import ListItem
from ..model.site import Site
from ..one_drive_object_base import OneDriveObjectBase


class SharedDriveItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def list_item(self):
        """
        Gets and sets the listItem
        
        Returns: 
            :class:`ListItem<onedrivesdk.model.list_item.ListItem>`:
                The listItem
        """
        if "listItem" in self._prop_dict:
            if isinstance(self._prop_dict["listItem"], OneDriveObjectBase):
                return self._prop_dict["listItem"]
            else :
                self._prop_dict["listItem"] = ListItem(self._prop_dict["listItem"])
                return self._prop_dict["listItem"]

        return None

    @list_item.setter
    def list_item(self, val):
        self._prop_dict["listItem"] = val

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
    def site(self):
        """
        Gets and sets the site
        
        Returns: 
            :class:`Site<onedrivesdk.model.site.Site>`:
                The site
        """
        if "site" in self._prop_dict:
            if isinstance(self._prop_dict["site"], OneDriveObjectBase):
                return self._prop_dict["site"]
            else :
                self._prop_dict["site"] = Site(self._prop_dict["site"])
                return self._prop_dict["site"]

        return None

    @site.setter
    def site(self, val):
        self._prop_dict["site"] = val

