# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_bookmark import IosBookmark
from ..one_drive_object_base import OneDriveObjectBase


class IosWebContentFilterSpecificWebsitesAccess(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def specific_websites_only(self):
        """
        Gets and sets the specificWebsitesOnly
        
        Returns: 
            :class:`IosBookmark<onedrivesdk.model.ios_bookmark.IosBookmark>`:
                The specificWebsitesOnly
        """
        if "specificWebsitesOnly" in self._prop_dict:
            if isinstance(self._prop_dict["specificWebsitesOnly"], OneDriveObjectBase):
                return self._prop_dict["specificWebsitesOnly"]
            else :
                self._prop_dict["specificWebsitesOnly"] = IosBookmark(self._prop_dict["specificWebsitesOnly"])
                return self._prop_dict["specificWebsitesOnly"]

        return None

    @specific_websites_only.setter
    def specific_websites_only(self, val):
        self._prop_dict["specificWebsitesOnly"] = val
