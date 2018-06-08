# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_content_file import MobileAppContentFile
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

