# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class IosBookmark(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def url(self):
        """Gets and sets the url
        
        Returns: 
            str:
                The url
        """
        if "url" in self._prop_dict:
            return self._prop_dict["url"]
        else:
            return None

    @url.setter
    def url(self, val):
        self._prop_dict["url"] = val

    @property
    def bookmark_folder(self):
        """Gets and sets the bookmarkFolder
        
        Returns: 
            str:
                The bookmarkFolder
        """
        if "bookmarkFolder" in self._prop_dict:
            return self._prop_dict["bookmarkFolder"]
        else:
            return None

    @bookmark_folder.setter
    def bookmark_folder(self, val):
        self._prop_dict["bookmarkFolder"] = val

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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

