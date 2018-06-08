# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.folder_view import FolderView
from ..one_drive_object_base import OneDriveObjectBase


class Folder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def child_count(self):
        """Gets and sets the childCount
        
        Returns: 
            int:
                The childCount
        """
        if "childCount" in self._prop_dict:
            return self._prop_dict["childCount"]
        else:
            return None

    @child_count.setter
    def child_count(self, val):
        self._prop_dict["childCount"] = val

    @property
    def view(self):
        """
        Gets and sets the view
        
        Returns: 
            :class:`FolderView<onedrivesdk.model.folder_view.FolderView>`:
                The view
        """
        if "view" in self._prop_dict:
            if isinstance(self._prop_dict["view"], OneDriveObjectBase):
                return self._prop_dict["view"]
            else :
                self._prop_dict["view"] = FolderView(self._prop_dict["view"])
                return self._prop_dict["view"]

        return None

    @view.setter
    def view(self, val):
        self._prop_dict["view"] = val
