# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookTableRow(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def index(self):
        """
        Gets and sets the index
        
        Returns:
            int:
                The index
        """
        if "index" in self._prop_dict:
            return self._prop_dict["index"]
        else:
            return None

    @index.setter
    def index(self, val):
        self._prop_dict["index"] = val

    @property
    def values(self):
        """
        Gets and sets the values
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The values
        """
        if "values" in self._prop_dict:
            if isinstance(self._prop_dict["values"], OneDriveObjectBase):
                return self._prop_dict["values"]
            else :
                self._prop_dict["values"] = Json(self._prop_dict["values"])
                return self._prop_dict["values"]

        return None

    @values.setter
    def values(self, val):
        self._prop_dict["values"] = val

