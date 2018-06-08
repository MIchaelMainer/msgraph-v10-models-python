# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.attribute_flow_behavior import AttributeFlowBehavior
from ..model.attribute_flow_type import AttributeFlowType
from ..model.attribute_mapping_source import AttributeMappingSource
from ..one_drive_object_base import OneDriveObjectBase


class AttributeMapping(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def default_value(self):
        """Gets and sets the defaultValue
        
        Returns: 
            str:
                The defaultValue
        """
        if "defaultValue" in self._prop_dict:
            return self._prop_dict["defaultValue"]
        else:
            return None

    @default_value.setter
    def default_value(self, val):
        self._prop_dict["defaultValue"] = val

    @property
    def export_missing_references(self):
        """Gets and sets the exportMissingReferences
        
        Returns: 
            bool:
                The exportMissingReferences
        """
        if "exportMissingReferences" in self._prop_dict:
            return self._prop_dict["exportMissingReferences"]
        else:
            return None

    @export_missing_references.setter
    def export_missing_references(self, val):
        self._prop_dict["exportMissingReferences"] = val

    @property
    def flow_behavior(self):
        """
        Gets and sets the flowBehavior
        
        Returns: 
            :class:`AttributeFlowBehavior<onedrivesdk.model.attribute_flow_behavior.AttributeFlowBehavior>`:
                The flowBehavior
        """
        if "flowBehavior" in self._prop_dict:
            if isinstance(self._prop_dict["flowBehavior"], OneDriveObjectBase):
                return self._prop_dict["flowBehavior"]
            else :
                self._prop_dict["flowBehavior"] = AttributeFlowBehavior(self._prop_dict["flowBehavior"])
                return self._prop_dict["flowBehavior"]

        return None

    @flow_behavior.setter
    def flow_behavior(self, val):
        self._prop_dict["flowBehavior"] = val
    @property
    def flow_type(self):
        """
        Gets and sets the flowType
        
        Returns: 
            :class:`AttributeFlowType<onedrivesdk.model.attribute_flow_type.AttributeFlowType>`:
                The flowType
        """
        if "flowType" in self._prop_dict:
            if isinstance(self._prop_dict["flowType"], OneDriveObjectBase):
                return self._prop_dict["flowType"]
            else :
                self._prop_dict["flowType"] = AttributeFlowType(self._prop_dict["flowType"])
                return self._prop_dict["flowType"]

        return None

    @flow_type.setter
    def flow_type(self, val):
        self._prop_dict["flowType"] = val
    @property
    def matching_priority(self):
        """Gets and sets the matchingPriority
        
        Returns: 
            int:
                The matchingPriority
        """
        if "matchingPriority" in self._prop_dict:
            return self._prop_dict["matchingPriority"]
        else:
            return None

    @matching_priority.setter
    def matching_priority(self, val):
        self._prop_dict["matchingPriority"] = val

    @property
    def source(self):
        """
        Gets and sets the source
        
        Returns: 
            :class:`AttributeMappingSource<onedrivesdk.model.attribute_mapping_source.AttributeMappingSource>`:
                The source
        """
        if "source" in self._prop_dict:
            if isinstance(self._prop_dict["source"], OneDriveObjectBase):
                return self._prop_dict["source"]
            else :
                self._prop_dict["source"] = AttributeMappingSource(self._prop_dict["source"])
                return self._prop_dict["source"]

        return None

    @source.setter
    def source(self, val):
        self._prop_dict["source"] = val
    @property
    def target_attribute_name(self):
        """Gets and sets the targetAttributeName
        
        Returns: 
            str:
                The targetAttributeName
        """
        if "targetAttributeName" in self._prop_dict:
            return self._prop_dict["targetAttributeName"]
        else:
            return None

    @target_attribute_name.setter
    def target_attribute_name(self, val):
        self._prop_dict["targetAttributeName"] = val

