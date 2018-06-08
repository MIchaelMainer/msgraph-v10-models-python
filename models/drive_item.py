# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.audio import Audio
from ..model.deleted import Deleted
from ..model.file import File
from ..model.file_system_info import FileSystemInfo
from ..model.folder import Folder
from ..model.image import Image
from ..model.geo_coordinates import GeoCoordinates
from ..model.package import Package
from ..model.photo import Photo
from ..model.publication_facet import PublicationFacet
from ..model.remote_item import RemoteItem
from ..model.root import Root
from ..model.search_result import SearchResult
from ..model.shared import Shared
from ..model.sharepoint_ids import SharepointIds
from ..model.special_folder import SpecialFolder
from ..model.video import Video
from ..model.list_item import ListItem
from ..model.permission import Permission
from ..model.thumbnail_set import ThumbnailSet
from ..model.drive_item_version import DriveItemVersion
from ..model.workbook import Workbook
from ..one_drive_object_base import OneDriveObjectBase


class DriveItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def audio(self):
        """
        Gets and sets the audio
        
        Returns: 
            :class:`Audio<onedrivesdk.model.audio.Audio>`:
                The audio
        """
        if "audio" in self._prop_dict:
            if isinstance(self._prop_dict["audio"], OneDriveObjectBase):
                return self._prop_dict["audio"]
            else :
                self._prop_dict["audio"] = Audio(self._prop_dict["audio"])
                return self._prop_dict["audio"]

        return None

    @audio.setter
    def audio(self, val):
        self._prop_dict["audio"] = val

    @property
    def c_tag(self):
        """
        Gets and sets the cTag
        
        Returns:
            str:
                The cTag
        """
        if "cTag" in self._prop_dict:
            return self._prop_dict["cTag"]
        else:
            return None

    @c_tag.setter
    def c_tag(self, val):
        self._prop_dict["cTag"] = val

    @property
    def deleted(self):
        """
        Gets and sets the deleted
        
        Returns: 
            :class:`Deleted<onedrivesdk.model.deleted.Deleted>`:
                The deleted
        """
        if "deleted" in self._prop_dict:
            if isinstance(self._prop_dict["deleted"], OneDriveObjectBase):
                return self._prop_dict["deleted"]
            else :
                self._prop_dict["deleted"] = Deleted(self._prop_dict["deleted"])
                return self._prop_dict["deleted"]

        return None

    @deleted.setter
    def deleted(self, val):
        self._prop_dict["deleted"] = val

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
    def image(self):
        """
        Gets and sets the image
        
        Returns: 
            :class:`Image<onedrivesdk.model.image.Image>`:
                The image
        """
        if "image" in self._prop_dict:
            if isinstance(self._prop_dict["image"], OneDriveObjectBase):
                return self._prop_dict["image"]
            else :
                self._prop_dict["image"] = Image(self._prop_dict["image"])
                return self._prop_dict["image"]

        return None

    @image.setter
    def image(self, val):
        self._prop_dict["image"] = val

    @property
    def location(self):
        """
        Gets and sets the location
        
        Returns: 
            :class:`GeoCoordinates<onedrivesdk.model.geo_coordinates.GeoCoordinates>`:
                The location
        """
        if "location" in self._prop_dict:
            if isinstance(self._prop_dict["location"], OneDriveObjectBase):
                return self._prop_dict["location"]
            else :
                self._prop_dict["location"] = GeoCoordinates(self._prop_dict["location"])
                return self._prop_dict["location"]

        return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

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
    def photo(self):
        """
        Gets and sets the photo
        
        Returns: 
            :class:`Photo<onedrivesdk.model.photo.Photo>`:
                The photo
        """
        if "photo" in self._prop_dict:
            if isinstance(self._prop_dict["photo"], OneDriveObjectBase):
                return self._prop_dict["photo"]
            else :
                self._prop_dict["photo"] = Photo(self._prop_dict["photo"])
                return self._prop_dict["photo"]

        return None

    @photo.setter
    def photo(self, val):
        self._prop_dict["photo"] = val

    @property
    def publication(self):
        """
        Gets and sets the publication
        
        Returns: 
            :class:`PublicationFacet<onedrivesdk.model.publication_facet.PublicationFacet>`:
                The publication
        """
        if "publication" in self._prop_dict:
            if isinstance(self._prop_dict["publication"], OneDriveObjectBase):
                return self._prop_dict["publication"]
            else :
                self._prop_dict["publication"] = PublicationFacet(self._prop_dict["publication"])
                return self._prop_dict["publication"]

        return None

    @publication.setter
    def publication(self, val):
        self._prop_dict["publication"] = val

    @property
    def remote_item(self):
        """
        Gets and sets the remoteItem
        
        Returns: 
            :class:`RemoteItem<onedrivesdk.model.remote_item.RemoteItem>`:
                The remoteItem
        """
        if "remoteItem" in self._prop_dict:
            if isinstance(self._prop_dict["remoteItem"], OneDriveObjectBase):
                return self._prop_dict["remoteItem"]
            else :
                self._prop_dict["remoteItem"] = RemoteItem(self._prop_dict["remoteItem"])
                return self._prop_dict["remoteItem"]

        return None

    @remote_item.setter
    def remote_item(self, val):
        self._prop_dict["remoteItem"] = val

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
    def search_result(self):
        """
        Gets and sets the searchResult
        
        Returns: 
            :class:`SearchResult<onedrivesdk.model.search_result.SearchResult>`:
                The searchResult
        """
        if "searchResult" in self._prop_dict:
            if isinstance(self._prop_dict["searchResult"], OneDriveObjectBase):
                return self._prop_dict["searchResult"]
            else :
                self._prop_dict["searchResult"] = SearchResult(self._prop_dict["searchResult"])
                return self._prop_dict["searchResult"]

        return None

    @search_result.setter
    def search_result(self, val):
        self._prop_dict["searchResult"] = val

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
        """
        Gets and sets the size
        
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
    def video(self):
        """
        Gets and sets the video
        
        Returns: 
            :class:`Video<onedrivesdk.model.video.Video>`:
                The video
        """
        if "video" in self._prop_dict:
            if isinstance(self._prop_dict["video"], OneDriveObjectBase):
                return self._prop_dict["video"]
            else :
                self._prop_dict["video"] = Video(self._prop_dict["video"])
                return self._prop_dict["video"]

        return None

    @video.setter
    def video(self, val):
        self._prop_dict["video"] = val

    @property
    def web_dav_url(self):
        """
        Gets and sets the webDavUrl
        
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
    def children(self):
        """Gets and sets the children
        
        Returns: 
            :class:`ChildrenCollectionPage<onedrivesdk.request.children_collection.ChildrenCollectionPage>`:
                The children
        """
        if "children" in self._prop_dict:
            return ChildrenCollectionPage(self._prop_dict["children"])
        else:
            return None

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
    def permissions(self):
        """Gets and sets the permissions
        
        Returns: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The permissions
        """
        if "permissions" in self._prop_dict:
            return PermissionsCollectionPage(self._prop_dict["permissions"])
        else:
            return None

    @property
    def thumbnails(self):
        """Gets and sets the thumbnails
        
        Returns: 
            :class:`ThumbnailsCollectionPage<onedrivesdk.request.thumbnails_collection.ThumbnailsCollectionPage>`:
                The thumbnails
        """
        if "thumbnails" in self._prop_dict:
            return ThumbnailsCollectionPage(self._prop_dict["thumbnails"])
        else:
            return None

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

    @property
    def workbook(self):
        """
        Gets and sets the workbook
        
        Returns: 
            :class:`Workbook<onedrivesdk.model.workbook.Workbook>`:
                The workbook
        """
        if "workbook" in self._prop_dict:
            if isinstance(self._prop_dict["workbook"], OneDriveObjectBase):
                return self._prop_dict["workbook"]
            else :
                self._prop_dict["workbook"] = Workbook(self._prop_dict["workbook"])
                return self._prop_dict["workbook"]

        return None

    @workbook.setter
    def workbook(self, val):
        self._prop_dict["workbook"] = val

