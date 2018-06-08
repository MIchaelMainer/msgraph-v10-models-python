# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attribute_mapping import AttributeMapping
from ..model.object_flow_types import ObjectFlowTypes
from ..model.metadata_entry import MetadataEntry
from ..model.filter import Filter
from ..one_drive_object_base import OneDriveObjectBase


class ObjectMapping(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def attribute_mappings(self):
        """
        Gets and sets the attributeMappings
        
        Returns: 
            :class:`AttributeMapping<onedrivesdk.model.attribute_mapping.AttributeMapping>`:
                The attributeMappings
        """
        if "attributeMappings" in self._prop_dict:
            if isinstance(self._prop_dict["attributeMappings"], OneDriveObjectBase):
                return self._prop_dict["attributeMappings"]
            else :
                self._prop_dict["attributeMappings"] = AttributeMapping(self._prop_dict["attributeMappings"])
                return self._prop_dict["attributeMappings"]

        return None

    @attribute_mappings.setter
    def attribute_mappings(self, val):
        self._prop_dict["attributeMappings"] = val
    @property
    def enabled(self):
        """Gets and sets the enabled
        
        Returns: 
            bool:
                The enabled
        """
        if "enabled" in self._prop_dict:
            return self._prop_dict["enabled"]
        else:
            return None

    @enabled.setter
    def enabled(self, val):
        self._prop_dict["enabled"] = val

    @property
    def flow_types(self):
        """
        Gets and sets the flowTypes
        
        Returns: 
            :class:`ObjectFlowTypes<onedrivesdk.model.object_flow_types.ObjectFlowTypes>`:
                The flowTypes
        """
        if "flowTypes" in self._prop_dict:
            if isinstance(self._prop_dict["flowTypes"], OneDriveObjectBase):
                return self._prop_dict["flowTypes"]
            else :
                self._prop_dict["flowTypes"] = ObjectFlowTypes(self._prop_dict["flowTypes"])
                return self._prop_dict["flowTypes"]

        return None

    @flow_types.setter
    def flow_types(self, val):
        self._prop_dict["flowTypes"] = val
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
    def scope(self):
        """
        Gets and sets the scope
        
        Returns: 
            :class:`Filter<onedrivesdk.model.filter.Filter>`:
                The scope
        """
        if "scope" in self._prop_dict:
            if isinstance(self._prop_dict["scope"], OneDriveObjectBase):
                return self._prop_dict["scope"]
            else :
                self._prop_dict["scope"] = Filter(self._prop_dict["scope"])
                return self._prop_dict["scope"]

        return None

    @scope.setter
    def scope(self, val):
        self._prop_dict["scope"] = val
    @property
    def source_object_name(self):
        """Gets and sets the sourceObjectName
        
        Returns: 
            str:
                The sourceObjectName
        """
        if "sourceObjectName" in self._prop_dict:
            return self._prop_dict["sourceObjectName"]
        else:
            return None

    @source_object_name.setter
    def source_object_name(self, val):
        self._prop_dict["sourceObjectName"] = val

    @property
    def target_object_name(self):
        """Gets and sets the targetObjectName
        
        Returns: 
            str:
                The targetObjectName
        """
        if "targetObjectName" in self._prop_dict:
            return self._prop_dict["targetObjectName"]
        else:
            return None

    @target_object_name.setter
    def target_object_name(self, val):
        self._prop_dict["targetObjectName"] = val

