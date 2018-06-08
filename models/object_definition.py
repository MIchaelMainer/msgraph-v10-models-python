# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attribute_definition import AttributeDefinition
from ..model.metadata_entry import MetadataEntry
from ..one_drive_object_base import OneDriveObjectBase


class ObjectDefinition(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def attributes(self):
        """
        Gets and sets the attributes
        
        Returns: 
            :class:`AttributeDefinition<onedrivesdk.model.attribute_definition.AttributeDefinition>`:
                The attributes
        """
        if "attributes" in self._prop_dict:
            if isinstance(self._prop_dict["attributes"], OneDriveObjectBase):
                return self._prop_dict["attributes"]
            else :
                self._prop_dict["attributes"] = AttributeDefinition(self._prop_dict["attributes"])
                return self._prop_dict["attributes"]

        return None

    @attributes.setter
    def attributes(self, val):
        self._prop_dict["attributes"] = val
    @property
    def metadata(self):
        """
        Gets and sets the metadata
        
        Returns: 
            :class:`MetadataEntry<onedrivesdk.model.metadata_entry.MetadataEntry>`:
                The metadata
        """
        if "metadata" in self._prop_dict:
            if isinstance(self._prop_dict["metadata"], OneDriveObjectBase):
                return self._prop_dict["metadata"]
            else :
                self._prop_dict["metadata"] = MetadataEntry(self._prop_dict["metadata"])
                return self._prop_dict["metadata"]

        return None

    @metadata.setter
    def metadata(self, val):
        self._prop_dict["metadata"] = val
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
    def supported_apis(self):
        """Gets and sets the supportedApis
        
        Returns: 
            str:
                The supportedApis
        """
        if "supportedApis" in self._prop_dict:
            return self._prop_dict["supportedApis"]
        else:
            return None

    @supported_apis.setter
    def supported_apis(self, val):
        self._prop_dict["supportedApis"] = val

