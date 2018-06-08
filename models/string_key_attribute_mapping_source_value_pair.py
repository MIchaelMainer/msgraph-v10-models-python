# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attribute_mapping_source import AttributeMappingSource
from ..one_drive_object_base import OneDriveObjectBase


class StringKeyAttributeMappingSourceValuePair(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def key(self):
        """Gets and sets the key
        
        Returns: 
            str:
                The key
        """
        if "key" in self._prop_dict:
            return self._prop_dict["key"]
        else:
            return None

    @key.setter
    def key(self, val):
        self._prop_dict["key"] = val

    @property
    def value(self):
        """
        Gets and sets the value
        
        Returns: 
            :class:`AttributeMappingSource<onedrivesdk.model.attribute_mapping_source.AttributeMappingSource>`:
                The value
        """
        if "value" in self._prop_dict:
            if isinstance(self._prop_dict["value"], OneDriveObjectBase):
                return self._prop_dict["value"]
            else :
                self._prop_dict["value"] = AttributeMappingSource(self._prop_dict["value"])
                return self._prop_dict["value"]

        return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val
