# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.string_key_string_value_pair import StringKeyStringValuePair
from ..model.metadata_entry import MetadataEntry
from ..model.mutability import Mutability
from ..model.referenced_object import ReferencedObject
from ..model.attribute_type import AttributeType
from ..one_drive_object_base import OneDriveObjectBase


class AttributeDefinition(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def anchor(self):
        """Gets and sets the anchor
        
        Returns: 
            bool:
                The anchor
        """
        if "anchor" in self._prop_dict:
            return self._prop_dict["anchor"]
        else:
            return None

    @anchor.setter
    def anchor(self, val):
        self._prop_dict["anchor"] = val

    @property
    def api_expressions(self):
        """
        Gets and sets the apiExpressions
        
        Returns: 
            :class:`StringKeyStringValuePair<onedrivesdk.model.string_key_string_value_pair.StringKeyStringValuePair>`:
                The apiExpressions
        """
        if "apiExpressions" in self._prop_dict:
            if isinstance(self._prop_dict["apiExpressions"], OneDriveObjectBase):
                return self._prop_dict["apiExpressions"]
            else :
                self._prop_dict["apiExpressions"] = StringKeyStringValuePair(self._prop_dict["apiExpressions"])
                return self._prop_dict["apiExpressions"]

        return None

    @api_expressions.setter
    def api_expressions(self, val):
        self._prop_dict["apiExpressions"] = val
    @property
    def case_exact(self):
        """Gets and sets the caseExact
        
        Returns: 
            bool:
                The caseExact
        """
        if "caseExact" in self._prop_dict:
            return self._prop_dict["caseExact"]
        else:
            return None

    @case_exact.setter
    def case_exact(self, val):
        self._prop_dict["caseExact"] = val

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
    def multivalued(self):
        """Gets and sets the multivalued
        
        Returns: 
            bool:
                The multivalued
        """
        if "multivalued" in self._prop_dict:
            return self._prop_dict["multivalued"]
        else:
            return None

    @multivalued.setter
    def multivalued(self, val):
        self._prop_dict["multivalued"] = val

    @property
    def mutability(self):
        """
        Gets and sets the mutability
        
        Returns: 
            :class:`Mutability<onedrivesdk.model.mutability.Mutability>`:
                The mutability
        """
        if "mutability" in self._prop_dict:
            if isinstance(self._prop_dict["mutability"], OneDriveObjectBase):
                return self._prop_dict["mutability"]
            else :
                self._prop_dict["mutability"] = Mutability(self._prop_dict["mutability"])
                return self._prop_dict["mutability"]

        return None

    @mutability.setter
    def mutability(self, val):
        self._prop_dict["mutability"] = val
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
    def required(self):
        """Gets and sets the required
        
        Returns: 
            bool:
                The required
        """
        if "required" in self._prop_dict:
            return self._prop_dict["required"]
        else:
            return None

    @required.setter
    def required(self, val):
        self._prop_dict["required"] = val

    @property
    def referenced_objects(self):
        """
        Gets and sets the referencedObjects
        
        Returns: 
            :class:`ReferencedObject<onedrivesdk.model.referenced_object.ReferencedObject>`:
                The referencedObjects
        """
        if "referencedObjects" in self._prop_dict:
            if isinstance(self._prop_dict["referencedObjects"], OneDriveObjectBase):
                return self._prop_dict["referencedObjects"]
            else :
                self._prop_dict["referencedObjects"] = ReferencedObject(self._prop_dict["referencedObjects"])
                return self._prop_dict["referencedObjects"]

        return None

    @referenced_objects.setter
    def referenced_objects(self, val):
        self._prop_dict["referencedObjects"] = val
    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`AttributeType<onedrivesdk.model.attribute_type.AttributeType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = AttributeType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val
