# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SecurityVendorInformation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def provider(self):
        """Gets and sets the provider
        
        Returns: 
            str:
                The provider
        """
        if "provider" in self._prop_dict:
            return self._prop_dict["provider"]
        else:
            return None

    @provider.setter
    def provider(self, val):
        self._prop_dict["provider"] = val

    @property
    def provider_version(self):
        """Gets and sets the providerVersion
        
        Returns: 
            str:
                The providerVersion
        """
        if "providerVersion" in self._prop_dict:
            return self._prop_dict["providerVersion"]
        else:
            return None

    @provider_version.setter
    def provider_version(self, val):
        self._prop_dict["providerVersion"] = val

    @property
    def sub_provider(self):
        """Gets and sets the subProvider
        
        Returns: 
            str:
                The subProvider
        """
        if "subProvider" in self._prop_dict:
            return self._prop_dict["subProvider"]
        else:
            return None

    @sub_provider.setter
    def sub_provider(self, val):
        self._prop_dict["subProvider"] = val

    @property
    def vendor(self):
        """Gets and sets the vendor
        
        Returns: 
            str:
                The vendor
        """
        if "vendor" in self._prop_dict:
            return self._prop_dict["vendor"]
        else:
            return None

    @vendor.setter
    def vendor(self, val):
        self._prop_dict["vendor"] = val

