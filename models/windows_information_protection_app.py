# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionApp(OneDriveObjectBase):

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
    def description(self):
        """Gets and sets the description
        
        Returns: 
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def publisher_name(self):
        """Gets and sets the publisherName
        
        Returns: 
            str:
                The publisherName
        """
        if "publisherName" in self._prop_dict:
            return self._prop_dict["publisherName"]
        else:
            return None

    @publisher_name.setter
    def publisher_name(self, val):
        self._prop_dict["publisherName"] = val

    @property
    def product_name(self):
        """Gets and sets the productName
        
        Returns: 
            str:
                The productName
        """
        if "productName" in self._prop_dict:
            return self._prop_dict["productName"]
        else:
            return None

    @product_name.setter
    def product_name(self, val):
        self._prop_dict["productName"] = val

    @property
    def denied(self):
        """Gets and sets the denied
        
        Returns: 
            bool:
                The denied
        """
        if "denied" in self._prop_dict:
            return self._prop_dict["denied"]
        else:
            return None

    @denied.setter
    def denied(self, val):
        self._prop_dict["denied"] = val

