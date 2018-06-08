# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppStatusRaw(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def content(self):
        """
        Gets and sets the content
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The content
        """
        if "content" in self._prop_dict:
            if isinstance(self._prop_dict["content"], OneDriveObjectBase):
                return self._prop_dict["content"]
            else :
                self._prop_dict["content"] = Json(self._prop_dict["content"])
                return self._prop_dict["content"]

        return None

    @content.setter
    def content(self, val):
        self._prop_dict["content"] = val

