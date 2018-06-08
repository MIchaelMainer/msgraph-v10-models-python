# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.file import File
from ..model.file_system_info import FileSystemInfo
from ..model.folder import Folder
from ..model.package import Package
from ..model.item_reference import ItemReference
from ..model.shared import Shared
from ..model.sharepoint_ids import SharepointIds
from ..model.special_folder import SpecialFolder
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class RemoteItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val
    @property
    def created_date_time(self):
        """Gets and sets the createdDateTime
        
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
    def file(self):
        """
        Gets and sets the file
        
        Returns: 
            :class:`File<onedrivesdk.model.file.File>`:
                The file
        """
        if "file" in self._prop_dict:
            if isinstance(self._prop_dict["file"], OneDriveObjectBase):
                return self._prop_dict["file"]
            else :
                self._prop_dict["file"] = File(self._prop_dict["file"])
                return self._prop_dict["file"]

        return None

    @file.setter
    def file(self, val):
        self._prop_dict["file"] = val
    @property
    def file_system_info(self):
        """
        Gets and sets the fileSystemInfo
        
        Returns: 
            :class:`FileSystemInfo<onedrivesdk.model.file_system_info.FileSystemInfo>`:
                The fileSystemInfo
        """
        if "fileSystemInfo" in self._prop_dict:
            if isinstance(self._prop_dict["fileSystemInfo"], OneDriveObjectBase):
                return self._prop_dict["fileSystemInfo"]
            else :
                self._prop_dict["fileSystemInfo"] = FileSystemInfo(self._prop_dict["fileSystemInfo"])
                return self._prop_dict["fileSystemInfo"]

        return None

    @file_system_info.setter
    def file_system_info(self, val):
        self._prop_dict["fileSystemInfo"] = val
    @property
    def folder(self):
        """
        Gets and sets the folder
        
        Returns: 
            :class:`Folder<onedrivesdk.model.folder.Folder>`:
                The folder
        """
        if "folder" in self._prop_dict:
            if isinstance(self._prop_dict["folder"], OneDriveObjectBase):
                return self._prop_dict["folder"]
            else :
                self._prop_dict["folder"] = Folder(self._prop_dict["folder"])
                return self._prop_dict["folder"]

        return None

    @folder.setter
    def folder(self, val):
        self._prop_dict["folder"] = val
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
    def last_modified_by(self):
        """
        Gets and sets the lastModifiedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The lastModifiedBy
        """
        if "lastModifiedBy" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedBy"], OneDriveObjectBase):
                return self._prop_dict["lastModifiedBy"]
            else :
                self._prop_dict["lastModifiedBy"] = IdentitySet(self._prop_dict["lastModifiedBy"])
                return self._prop_dict["lastModifiedBy"]

        return None

    @last_modified_by.setter
    def last_modified_by(self, val):
        self._prop_dict["lastModifiedBy"] = val
    @property
    def last_modified_date_time(self):
        """Gets and sets the lastModifiedDateTime
        
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
    def package(self):
        """
        Gets and sets the package
        
        Returns: 
            :class:`Package<onedrivesdk.model.package.Package>`:
                The package
        """
        if "package" in self._prop_dict:
            if isinstance(self._prop_dict["package"], OneDriveObjectBase):
                return self._prop_dict["package"]
            else :
                self._prop_dict["package"] = Package(self._prop_dict["package"])
                return self._prop_dict["package"]

        return None

    @package.setter
    def package(self, val):
        self._prop_dict["package"] = val
    @property
    def parent_reference(self):
        """
        Gets and sets the parentReference
        
        Returns: 
            :class:`ItemReference<onedrivesdk.model.item_reference.ItemReference>`:
                The parentReference
        """
        if "parentReference" in self._prop_dict:
            if isinstance(self._prop_dict["parentReference"], OneDriveObjectBase):
                return self._prop_dict["parentReference"]
            else :
                self._prop_dict["parentReference"] = ItemReference(self._prop_dict["parentReference"])
                return self._prop_dict["parentReference"]

        return None

    @parent_reference.setter
    def parent_reference(self, val):
        self._prop_dict["parentReference"] = val
    @property
    def shared(self):
        """
        Gets and sets the shared
        
        Returns: 
            :class:`Shared<onedrivesdk.model.shared.Shared>`:
                The shared
        """
        if "shared" in self._prop_dict:
            if isinstance(self._prop_dict["shared"], OneDriveObjectBase):
                return self._prop_dict["shared"]
            else :
                self._prop_dict["shared"] = Shared(self._prop_dict["shared"])
                return self._prop_dict["shared"]

        return None

    @shared.setter
    def shared(self, val):
        self._prop_dict["shared"] = val
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
    def size(self):
        """Gets and sets the size
        
        Returns: 
            int:
                The size
        """
        if "size" in self._prop_dict:
            return self._prop_dict["size"]
        else:
            return None

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

    @property
    def special_folder(self):
        """
        Gets and sets the specialFolder
        
        Returns: 
            :class:`SpecialFolder<onedrivesdk.model.special_folder.SpecialFolder>`:
                The specialFolder
        """
        if "specialFolder" in self._prop_dict:
            if isinstance(self._prop_dict["specialFolder"], OneDriveObjectBase):
                return self._prop_dict["specialFolder"]
            else :
                self._prop_dict["specialFolder"] = SpecialFolder(self._prop_dict["specialFolder"])
                return self._prop_dict["specialFolder"]

        return None

    @special_folder.setter
    def special_folder(self, val):
        self._prop_dict["specialFolder"] = val
    @property
    def web_dav_url(self):
        """Gets and sets the webDavUrl
        
        Returns: 
            str:
                The webDavUrl
        """
        if "webDavUrl" in self._prop_dict:
            return self._prop_dict["webDavUrl"]
        else:
            return None

    @web_dav_url.setter
    def web_dav_url(self, val):
        self._prop_dict["webDavUrl"] = val

    @property
    def web_url(self):
        """Gets and sets the webUrl
        
        Returns: 
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

