# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_home_screen_folder_page import IosHomeScreenFolderPage
from ..one_drive_object_base import OneDriveObjectBase


class IosHomeScreenFolder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def pages(self):
        """
        Gets and sets the pages
        
        Returns: 
            :class:`IosHomeScreenFolderPage<onedrivesdk.model.ios_home_screen_folder_page.IosHomeScreenFolderPage>`:
                The pages
        """
        if "pages" in self._prop_dict:
            if isinstance(self._prop_dict["pages"], OneDriveObjectBase):
                return self._prop_dict["pages"]
            else :
                self._prop_dict["pages"] = IosHomeScreenFolderPage(self._prop_dict["pages"])
                return self._prop_dict["pages"]

        return None

    @pages.setter
    def pages(self, val):
        self._prop_dict["pages"] = val
