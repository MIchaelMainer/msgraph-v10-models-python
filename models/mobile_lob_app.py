# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_content import MobileAppContent
from ..one_drive_object_base import OneDriveObjectBase


class MobileLobApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def committed_content_version(self):
        """
        Gets and sets the committedContentVersion
        
        Returns:
            str:
                The committedContentVersion
        """
        if "committedContentVersion" in self._prop_dict:
            return self._prop_dict["committedContentVersion"]
        else:
            return None

    @committed_content_version.setter
    def committed_content_version(self, val):
        self._prop_dict["committedContentVersion"] = val

    @property
    def file_name(self):
        """
        Gets and sets the fileName
        
        Returns:
            str:
                The fileName
        """
        if "fileName" in self._prop_dict:
            return self._prop_dict["fileName"]
        else:
            return None

    @file_name.setter
    def file_name(self, val):
        self._prop_dict["fileName"] = val

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
    def content_versions(self):
        """Gets and sets the contentVersions
        
        Returns: 
            :class:`ContentVersionsCollectionPage<onedrivesdk.request.content_versions_collection.ContentVersionsCollectionPage>`:
                The contentVersions
        """
        if "contentVersions" in self._prop_dict:
            return ContentVersionsCollectionPage(self._prop_dict["contentVersions"])
        else:
            return None

