# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Contract(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def contract_type(self):
        """
        Gets and sets the contractType
        
        Returns:
            str:
                The contractType
        """
        if "contractType" in self._prop_dict:
            return self._prop_dict["contractType"]
        else:
            return None

    @contract_type.setter
    def contract_type(self, val):
        self._prop_dict["contractType"] = val

    @property
    def customer_id(self):
        """
        Gets and sets the customerId
        
        Returns:
            UUID:
                The customerId
        """
        if "customerId" in self._prop_dict:
            return self._prop_dict["customerId"]
        else:
            return None

    @customer_id.setter
    def customer_id(self, val):
        self._prop_dict["customerId"] = val

    @property
    def default_domain_name(self):
        """
        Gets and sets the defaultDomainName
        
        Returns:
            str:
                The defaultDomainName
        """
        if "defaultDomainName" in self._prop_dict:
            return self._prop_dict["defaultDomainName"]
        else:
            return None

    @default_domain_name.setter
    def default_domain_name(self, val):
        self._prop_dict["defaultDomainName"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
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

