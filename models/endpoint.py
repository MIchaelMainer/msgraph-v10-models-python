# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Endpoint(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def capability(self):
        """
        Gets and sets the capability
        
        Returns:
            str:
                The capability
        """
        if "capability" in self._prop_dict:
            return self._prop_dict["capability"]
        else:
            return None

    @capability.setter
    def capability(self, val):
        self._prop_dict["capability"] = val

    @property
    def provider_id(self):
        """
        Gets and sets the providerId
        
        Returns:
            str:
                The providerId
        """
        if "providerId" in self._prop_dict:
            return self._prop_dict["providerId"]
        else:
            return None

    @provider_id.setter
    def provider_id(self, val):
        self._prop_dict["providerId"] = val

    @property
    def provider_name(self):
        """
        Gets and sets the providerName
        
        Returns:
            str:
                The providerName
        """
        if "providerName" in self._prop_dict:
            return self._prop_dict["providerName"]
        else:
            return None

    @provider_name.setter
    def provider_name(self, val):
        self._prop_dict["providerName"] = val

    @property
    def uri(self):
        """
        Gets and sets the uri
        
        Returns:
            str:
                The uri
        """
        if "uri" in self._prop_dict:
            return self._prop_dict["uri"]
        else:
            return None

    @uri.setter
    def uri(self, val):
        self._prop_dict["uri"] = val

    @property
    def provider_resource_id(self):
        """
        Gets and sets the providerResourceId
        
        Returns:
            str:
                The providerResourceId
        """
        if "providerResourceId" in self._prop_dict:
            return self._prop_dict["providerResourceId"]
        else:
            return None

    @provider_resource_id.setter
    def provider_resource_id(self, val):
        self._prop_dict["providerResourceId"] = val

