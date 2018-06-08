# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.object_definition import ObjectDefinition
from ..model.string_key_object_value_pair import StringKeyObjectValuePair
from ..one_drive_object_base import OneDriveObjectBase


class ExpressionInputObject(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def definition(self):
        """
        Gets and sets the definition
        
        Returns: 
            :class:`ObjectDefinition<onedrivesdk.model.object_definition.ObjectDefinition>`:
                The definition
        """
        if "definition" in self._prop_dict:
            if isinstance(self._prop_dict["definition"], OneDriveObjectBase):
                return self._prop_dict["definition"]
            else :
                self._prop_dict["definition"] = ObjectDefinition(self._prop_dict["definition"])
                return self._prop_dict["definition"]

        return None

    @definition.setter
    def definition(self, val):
        self._prop_dict["definition"] = val
    @property
    def properties(self):
        """
        Gets and sets the properties
        
        Returns: 
            :class:`StringKeyObjectValuePair<onedrivesdk.model.string_key_object_value_pair.StringKeyObjectValuePair>`:
                The properties
        """
        if "properties" in self._prop_dict:
            if isinstance(self._prop_dict["properties"], OneDriveObjectBase):
                return self._prop_dict["properties"]
            else :
                self._prop_dict["properties"] = StringKeyObjectValuePair(self._prop_dict["properties"])
                return self._prop_dict["properties"]

        return None

    @properties.setter
    def properties(self, val):
        self._prop_dict["properties"] = val
