# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class NetworkInterface(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def ip_v4_address(self):
        """Gets and sets the ipV4Address
        
        Returns: 
            str:
                The ipV4Address
        """
        if "ipV4Address" in self._prop_dict:
            return self._prop_dict["ipV4Address"]
        else:
            return None

    @ip_v4_address.setter
    def ip_v4_address(self, val):
        self._prop_dict["ipV4Address"] = val

    @property
    def ip_v6_address(self):
        """Gets and sets the ipV6Address
        
        Returns: 
            str:
                The ipV6Address
        """
        if "ipV6Address" in self._prop_dict:
            return self._prop_dict["ipV6Address"]
        else:
            return None

    @ip_v6_address.setter
    def ip_v6_address(self, val):
        self._prop_dict["ipV6Address"] = val

    @property
    def local_ip_v6_address(self):
        """Gets and sets the localIpV6Address
        
        Returns: 
            str:
                The localIpV6Address
        """
        if "localIpV6Address" in self._prop_dict:
            return self._prop_dict["localIpV6Address"]
        else:
            return None

    @local_ip_v6_address.setter
    def local_ip_v6_address(self, val):
        self._prop_dict["localIpV6Address"] = val

    @property
    def mac_address(self):
        """Gets and sets the macAddress
        
        Returns: 
            str:
                The macAddress
        """
        if "macAddress" in self._prop_dict:
            return self._prop_dict["macAddress"]
        else:
            return None

    @mac_address.setter
    def mac_address(self, val):
        self._prop_dict["macAddress"] = val

