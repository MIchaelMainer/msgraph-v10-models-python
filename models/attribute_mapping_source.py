# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.string_key_attribute_mapping_source_value_pair import StringKeyAttributeMappingSourceValuePair
from ..model.attribute_mapping_source_type import AttributeMappingSourceType
from ..one_drive_object_base import OneDriveObjectBase


class AttributeMappingSource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def expression(self):
        """Gets and sets the expression
        
        Returns: 
            str:
                The expression
        """
        if "expression" in self._prop_dict:
            return self._prop_dict["expression"]
        else:
            return None

    @expression.setter
    def expression(self, val):
        self._prop_dict["expression"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def parameters(self):
        """
        Gets and sets the parameters
        
        Returns: 
            :class:`StringKeyAttributeMappingSourceValuePair<onedrivesdk.model.string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair>`:
                The parameters
        """
        if "parameters" in self._prop_dict:
            if isinstance(self._prop_dict["parameters"], OneDriveObjectBase):
                return self._prop_dict["parameters"]
            else :
                self._prop_dict["parameters"] = StringKeyAttributeMappingSourceValuePair(self._prop_dict["parameters"])
                return self._prop_dict["parameters"]

        return None

    @parameters.setter
    def parameters(self, val):
        self._prop_dict["parameters"] = val
    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`AttributeMappingSourceType<onedrivesdk.model.attribute_mapping_source_type.AttributeMappingSourceType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = AttributeMappingSourceType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
