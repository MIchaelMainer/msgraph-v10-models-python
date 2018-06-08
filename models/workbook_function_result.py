# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookFunctionResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns:
            str:
                The error
        """
        if "error" in self._prop_dict:
            return self._prop_dict["error"]
        else:
            return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val

    @property
    def value(self):
        """
        Gets and sets the value
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The value
        """
        if "value" in self._prop_dict:
            if isinstance(self._prop_dict["value"], OneDriveObjectBase):
                return self._prop_dict["value"]
            else :
                self._prop_dict["value"] = Json(self._prop_dict["value"])
                return self._prop_dict["value"]

        return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val

