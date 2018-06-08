# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.string_key_string_value_pair import StringKeyStringValuePair
from ..model.object_mapping import ObjectMapping
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def editable(self):
        """Gets and sets the editable
        
        Returns: 
            bool:
                The editable
        """
        if "editable" in self._prop_dict:
            return self._prop_dict["editable"]
        else:
            return None

    @editable.setter
    def editable(self, val):
        self._prop_dict["editable"] = val

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def metadata(self):
        """
        Gets and sets the metadata
        
        Returns: 
            :class:`StringKeyStringValuePair<onedrivesdk.model.string_key_string_value_pair.StringKeyStringValuePair>`:
                The metadata
        """
        if "metadata" in self._prop_dict:
            if isinstance(self._prop_dict["metadata"], OneDriveObjectBase):
                return self._prop_dict["metadata"]
            else :
                self._prop_dict["metadata"] = StringKeyStringValuePair(self._prop_dict["metadata"])
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
    def object_mappings(self):
        """
        Gets and sets the objectMappings
        
        Returns: 
            :class:`ObjectMapping<onedrivesdk.model.object_mapping.ObjectMapping>`:
                The objectMappings
        """
        if "objectMappings" in self._prop_dict:
            if isinstance(self._prop_dict["objectMappings"], OneDriveObjectBase):
                return self._prop_dict["objectMappings"]
            else :
                self._prop_dict["objectMappings"] = ObjectMapping(self._prop_dict["objectMappings"])
                return self._prop_dict["objectMappings"]

        return None

    @object_mappings.setter
    def object_mappings(self, val):
        self._prop_dict["objectMappings"] = val
    @property
    def priority(self):
        """Gets and sets the priority
        
        Returns: 
            int:
                The priority
        """
        if "priority" in self._prop_dict:
            return self._prop_dict["priority"]
        else:
            return None

    @priority.setter
    def priority(self, val):
        self._prop_dict["priority"] = val

    @property
    def source_directory_name(self):
        """Gets and sets the sourceDirectoryName
        
        Returns: 
            str:
                The sourceDirectoryName
        """
        if "sourceDirectoryName" in self._prop_dict:
            return self._prop_dict["sourceDirectoryName"]
        else:
            return None

    @source_directory_name.setter
    def source_directory_name(self, val):
        self._prop_dict["sourceDirectoryName"] = val

    @property
    def target_directory_name(self):
        """Gets and sets the targetDirectoryName
        
        Returns: 
            str:
                The targetDirectoryName
        """
        if "targetDirectoryName" in self._prop_dict:
            return self._prop_dict["targetDirectoryName"]
        else:
            return None

    @target_directory_name.setter
    def target_directory_name(self, val):
        self._prop_dict["targetDirectoryName"] = val

