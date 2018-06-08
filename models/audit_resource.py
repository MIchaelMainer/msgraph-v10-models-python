# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.audit_property import AuditProperty
from ..one_drive_object_base import OneDriveObjectBase


class AuditResource(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def modified_properties(self):
        """
        Gets and sets the modifiedProperties
        
        Returns: 
            :class:`AuditProperty<onedrivesdk.model.audit_property.AuditProperty>`:
                The modifiedProperties
        """
        if "modifiedProperties" in self._prop_dict:
            if isinstance(self._prop_dict["modifiedProperties"], OneDriveObjectBase):
                return self._prop_dict["modifiedProperties"]
            else :
                self._prop_dict["modifiedProperties"] = AuditProperty(self._prop_dict["modifiedProperties"])
                return self._prop_dict["modifiedProperties"]

        return None

    @modified_properties.setter
    def modified_properties(self, val):
        self._prop_dict["modifiedProperties"] = val
    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def resource_id(self):
        """Gets and sets the resourceId
        
        Returns: 
            str:
                The resourceId
        """
        if "resourceId" in self._prop_dict:
            return self._prop_dict["resourceId"]
        else:
            return None

    @resource_id.setter
    def resource_id(self, val):
        self._prop_dict["resourceId"] = val

