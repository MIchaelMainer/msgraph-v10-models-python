# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.scope_operator_type import ScopeOperatorType
from ..model.scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
from ..model.attribute_type import AttributeType
from ..one_drive_object_base import OneDriveObjectBase


class FilterOperatorSchema(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def arity(self):
        """
        Gets and sets the arity
        
        Returns: 
            :class:`ScopeOperatorType<onedrivesdk.model.scope_operator_type.ScopeOperatorType>`:
                The arity
        """
        if "arity" in self._prop_dict:
            if isinstance(self._prop_dict["arity"], OneDriveObjectBase):
                return self._prop_dict["arity"]
            else :
                self._prop_dict["arity"] = ScopeOperatorType(self._prop_dict["arity"])
                return self._prop_dict["arity"]

        return None

    @arity.setter
    def arity(self, val):
        self._prop_dict["arity"] = val

    @property
    def multivalued_comparison_type(self):
        """
        Gets and sets the multivaluedComparisonType
        
        Returns: 
            :class:`ScopeOperatorMultiValuedComparisonType<onedrivesdk.model.scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType>`:
                The multivaluedComparisonType
        """
        if "multivaluedComparisonType" in self._prop_dict:
            if isinstance(self._prop_dict["multivaluedComparisonType"], OneDriveObjectBase):
                return self._prop_dict["multivaluedComparisonType"]
            else :
                self._prop_dict["multivaluedComparisonType"] = ScopeOperatorMultiValuedComparisonType(self._prop_dict["multivaluedComparisonType"])
                return self._prop_dict["multivaluedComparisonType"]

        return None

    @multivalued_comparison_type.setter
    def multivalued_comparison_type(self, val):
        self._prop_dict["multivaluedComparisonType"] = val

    @property
    def supported_attribute_types(self):
        """Gets and sets the supportedAttributeTypes
        
        Returns: 
            :class:`SupportedAttributeTypesCollectionPage<onedrivesdk.request.supported_attribute_types_collection.SupportedAttributeTypesCollectionPage>`:
                The supportedAttributeTypes
        """
        if "supportedAttributeTypes" in self._prop_dict:
            return SupportedAttributeTypesCollectionPage(self._prop_dict["supportedAttributeTypes"])
        else:
            return None

