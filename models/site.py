# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.root import Root
from ..model.sharepoint_ids import SharepointIds
from ..model.site_collection import SiteCollection
from ..model.column_definition import ColumnDefinition
from ..model.content_type import ContentType
from ..model.drive import Drive
from ..model.base_item import BaseItem
from ..model.list import List
from ..model.onenote import Onenote
from ..one_drive_object_base import OneDriveObjectBase


class Site(OneDriveObjectBase):

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
    def root(self):
        """
        Gets and sets the root
        
        Returns: 
            :class:`Root<onedrivesdk.model.root.Root>`:
                The root
        """
        if "root" in self._prop_dict:
            if isinstance(self._prop_dict["root"], OneDriveObjectBase):
                return self._prop_dict["root"]
            else :
                self._prop_dict["root"] = Root(self._prop_dict["root"])
                return self._prop_dict["root"]

        return None

    @root.setter
    def root(self, val):
        self._prop_dict["root"] = val

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
    def site_collection(self):
        """
        Gets and sets the siteCollection
        
        Returns: 
            :class:`SiteCollection<onedrivesdk.model.site_collection.SiteCollection>`:
                The siteCollection
        """
        if "siteCollection" in self._prop_dict:
            if isinstance(self._prop_dict["siteCollection"], OneDriveObjectBase):
                return self._prop_dict["siteCollection"]
            else :
                self._prop_dict["siteCollection"] = SiteCollection(self._prop_dict["siteCollection"])
                return self._prop_dict["siteCollection"]

        return None

    @site_collection.setter
    def site_collection(self, val):
        self._prop_dict["siteCollection"] = val

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
    def drives(self):
        """Gets and sets the drives
        
        Returns: 
            :class:`DrivesCollectionPage<onedrivesdk.request.drives_collection.DrivesCollectionPage>`:
                The drives
        """
        if "drives" in self._prop_dict:
            return DrivesCollectionPage(self._prop_dict["drives"])
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
    def lists(self):
        """Gets and sets the lists
        
        Returns: 
            :class:`ListsCollectionPage<onedrivesdk.request.lists_collection.ListsCollectionPage>`:
                The lists
        """
        if "lists" in self._prop_dict:
            return ListsCollectionPage(self._prop_dict["lists"])
        else:
            return None

    @property
    def sites(self):
        """Gets and sets the sites
        
        Returns: 
            :class:`SitesCollectionPage<onedrivesdk.request.sites_collection.SitesCollectionPage>`:
                The sites
        """
        if "sites" in self._prop_dict:
            return SitesCollectionPage(self._prop_dict["sites"])
        else:
            return None

    @property
    def onenote(self):
        """
        Gets and sets the onenote
        
        Returns: 
            :class:`Onenote<onedrivesdk.model.onenote.Onenote>`:
                The onenote
        """
        if "onenote" in self._prop_dict:
            if isinstance(self._prop_dict["onenote"], OneDriveObjectBase):
                return self._prop_dict["onenote"]
            else :
                self._prop_dict["onenote"] = Onenote(self._prop_dict["onenote"])
                return self._prop_dict["onenote"]

        return None

    @onenote.setter
    def onenote(self, val):
        self._prop_dict["onenote"] = val

