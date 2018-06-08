# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Windows10NetworkProxyServer(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def address(self):
        """Gets and sets the address
        
        Returns: 
            str:
                The address
        """
        if "address" in self._prop_dict:
            return self._prop_dict["address"]
        else:
            return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def exceptions(self):
        """Gets and sets the exceptions
        
        Returns: 
            str:
                The exceptions
        """
        if "exceptions" in self._prop_dict:
            return self._prop_dict["exceptions"]
        else:
            return None

    @exceptions.setter
    def exceptions(self, val):
        self._prop_dict["exceptions"] = val

    @property
    def use_for_local_addresses(self):
        """Gets and sets the useForLocalAddresses
        
        Returns: 
            bool:
                The useForLocalAddresses
        """
        if "useForLocalAddresses" in self._prop_dict:
            return self._prop_dict["useForLocalAddresses"]
        else:
            return None

    @use_for_local_addresses.setter
    def use_for_local_addresses(self, val):
        self._prop_dict["useForLocalAddresses"] = val

