# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class LookupColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allow_multiple_values(self):
        """Gets and sets the allowMultipleValues
        
        Returns: 
            bool:
                The allowMultipleValues
        """
        if "allowMultipleValues" in self._prop_dict:
            return self._prop_dict["allowMultipleValues"]
        else:
            return None

    @allow_multiple_values.setter
    def allow_multiple_values(self, val):
        self._prop_dict["allowMultipleValues"] = val

    @property
    def allow_unlimited_length(self):
        """Gets and sets the allowUnlimitedLength
        
        Returns: 
            bool:
                The allowUnlimitedLength
        """
        if "allowUnlimitedLength" in self._prop_dict:
            return self._prop_dict["allowUnlimitedLength"]
        else:
            return None

    @allow_unlimited_length.setter
    def allow_unlimited_length(self, val):
        self._prop_dict["allowUnlimitedLength"] = val

    @property
    def column_name(self):
        """Gets and sets the columnName
        
        Returns: 
            str:
                The columnName
        """
        if "columnName" in self._prop_dict:
            return self._prop_dict["columnName"]
        else:
            return None

    @column_name.setter
    def column_name(self, val):
        self._prop_dict["columnName"] = val

    @property
    def list_id(self):
        """Gets and sets the listId
        
        Returns: 
            str:
                The listId
        """
        if "listId" in self._prop_dict:
            return self._prop_dict["listId"]
        else:
            return None

    @list_id.setter
    def list_id(self, val):
        self._prop_dict["listId"] = val

    @property
    def primary_lookup_column_id(self):
        """Gets and sets the primaryLookupColumnId
        
        Returns: 
            str:
                The primaryLookupColumnId
        """
        if "primaryLookupColumnId" in self._prop_dict:
            return self._prop_dict["primaryLookupColumnId"]
        else:
            return None

    @primary_lookup_column_id.setter
    def primary_lookup_column_id(self, val):
        self._prop_dict["primaryLookupColumnId"] = val

