# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_content_file import MobileAppContentFile
from ..model.mobile_contained_app import MobileContainedApp
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppContent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def files(self):
        """Gets and sets the files
        
        Returns: 
            :class:`FilesCollectionPage<onedrivesdk.request.files_collection.FilesCollectionPage>`:
                The files
        """
        if "files" in self._prop_dict:
            return FilesCollectionPage(self._prop_dict["files"])
        else:
            return None

    @property
    def contained_apps(self):
        """Gets and sets the containedApps
        
        Returns: 
            :class:`ContainedAppsCollectionPage<onedrivesdk.request.contained_apps_collection.ContainedAppsCollectionPage>`:
                The containedApps
        """
        if "containedApps" in self._prop_dict:
            return ContainedAppsCollectionPage(self._prop_dict["containedApps"])
        else:
            return None

