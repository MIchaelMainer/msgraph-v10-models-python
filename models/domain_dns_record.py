# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DomainDnsRecord(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_optional(self):
        """
        Gets and sets the isOptional
        
        Returns:
            bool:
                The isOptional
        """
        if "isOptional" in self._prop_dict:
            return self._prop_dict["isOptional"]
        else:
            return None

    @is_optional.setter
    def is_optional(self, val):
        self._prop_dict["isOptional"] = val

    @property
    def label(self):
        """
        Gets and sets the label
        
        Returns:
            str:
                The label
        """
        if "label" in self._prop_dict:
            return self._prop_dict["label"]
        else:
            return None

    @label.setter
    def label(self, val):
        self._prop_dict["label"] = val

    @property
    def record_type(self):
        """
        Gets and sets the recordType
        
        Returns:
            str:
                The recordType
        """
        if "recordType" in self._prop_dict:
            return self._prop_dict["recordType"]
        else:
            return None

    @record_type.setter
    def record_type(self, val):
        self._prop_dict["recordType"] = val

    @property
    def supported_service(self):
        """
        Gets and sets the supportedService
        
        Returns:
            str:
                The supportedService
        """
        if "supportedService" in self._prop_dict:
            return self._prop_dict["supportedService"]
        else:
            return None

    @supported_service.setter
    def supported_service(self, val):
        self._prop_dict["supportedService"] = val

    @property
    def ttl(self):
        """
        Gets and sets the ttl
        
        Returns:
            int:
                The ttl
        """
        if "ttl" in self._prop_dict:
            return self._prop_dict["ttl"]
        else:
            return None

    @ttl.setter
    def ttl(self, val):
        self._prop_dict["ttl"] = val

