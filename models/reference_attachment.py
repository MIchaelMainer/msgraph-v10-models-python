# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.reference_attachment_provider import ReferenceAttachmentProvider
from ..model.reference_attachment_permission import ReferenceAttachmentPermission
from ..one_drive_object_base import OneDriveObjectBase


class ReferenceAttachment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def source_url(self):
        """
        Gets and sets the sourceUrl
        
        Returns:
            str:
                The sourceUrl
        """
        if "sourceUrl" in self._prop_dict:
            return self._prop_dict["sourceUrl"]
        else:
            return None

    @source_url.setter
    def source_url(self, val):
        self._prop_dict["sourceUrl"] = val

    @property
    def provider_type(self):
        """
        Gets and sets the providerType
        
        Returns: 
            :class:`ReferenceAttachmentProvider<onedrivesdk.model.reference_attachment_provider.ReferenceAttachmentProvider>`:
                The providerType
        """
        if "providerType" in self._prop_dict:
            if isinstance(self._prop_dict["providerType"], OneDriveObjectBase):
                return self._prop_dict["providerType"]
            else :
                self._prop_dict["providerType"] = ReferenceAttachmentProvider(self._prop_dict["providerType"])
                return self._prop_dict["providerType"]

        return None

    @provider_type.setter
    def provider_type(self, val):
        self._prop_dict["providerType"] = val

    @property
    def thumbnail_url(self):
        """
        Gets and sets the thumbnailUrl
        
        Returns:
            str:
                The thumbnailUrl
        """
        if "thumbnailUrl" in self._prop_dict:
            return self._prop_dict["thumbnailUrl"]
        else:
            return None

    @thumbnail_url.setter
    def thumbnail_url(self, val):
        self._prop_dict["thumbnailUrl"] = val

    @property
    def preview_url(self):
        """
        Gets and sets the previewUrl
        
        Returns:
            str:
                The previewUrl
        """
        if "previewUrl" in self._prop_dict:
            return self._prop_dict["previewUrl"]
        else:
            return None

    @preview_url.setter
    def preview_url(self, val):
        self._prop_dict["previewUrl"] = val

    @property
    def permission(self):
        """
        Gets and sets the permission
        
        Returns: 
            :class:`ReferenceAttachmentPermission<onedrivesdk.model.reference_attachment_permission.ReferenceAttachmentPermission>`:
                The permission
        """
        if "permission" in self._prop_dict:
            if isinstance(self._prop_dict["permission"], OneDriveObjectBase):
                return self._prop_dict["permission"]
            else :
                self._prop_dict["permission"] = ReferenceAttachmentPermission(self._prop_dict["permission"])
                return self._prop_dict["permission"]

        return None

    @permission.setter
    def permission(self, val):
        self._prop_dict["permission"] = val

    @property
    def is_folder(self):
        """
        Gets and sets the isFolder
        
        Returns:
            bool:
                The isFolder
        """
        if "isFolder" in self._prop_dict:
            return self._prop_dict["isFolder"]
        else:
            return None

    @is_folder.setter
    def is_folder(self, val):
        self._prop_dict["isFolder"] = val

