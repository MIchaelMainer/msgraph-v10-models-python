# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ReferencedObject(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def referenced_object_name(self):
        """Gets and sets the referencedObjectName
        
        Returns: 
            str:
                The referencedObjectName
        """
        if "referencedObjectName" in self._prop_dict:
            return self._prop_dict["referencedObjectName"]
        else:
            return None

    @referenced_object_name.setter
    def referenced_object_name(self, val):
        self._prop_dict["referencedObjectName"] = val

    @property
    def referenced_property(self):
        """Gets and sets the referencedProperty
        
        Returns: 
            str:
                The referencedProperty
        """
        if "referencedProperty" in self._prop_dict:
            return self._prop_dict["referencedProperty"]
        else:
            return None

    @referenced_property.setter
    def referenced_property(self, val):
        self._prop_dict["referencedProperty"] = val

