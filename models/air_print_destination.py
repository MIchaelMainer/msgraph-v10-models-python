# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AirPrintDestination(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def ip_address(self):
        """Gets and sets the ipAddress
        
        Returns: 
            str:
                The ipAddress
        """
        if "ipAddress" in self._prop_dict:
            return self._prop_dict["ipAddress"]
        else:
            return None

    @ip_address.setter
    def ip_address(self, val):
        self._prop_dict["ipAddress"] = val

    @property
    def resource_path(self):
        """Gets and sets the resourcePath
        
        Returns: 
            str:
                The resourcePath
        """
        if "resourcePath" in self._prop_dict:
            return self._prop_dict["resourcePath"]
        else:
            return None

    @resource_path.setter
    def resource_path(self, val):
        self._prop_dict["resourcePath"] = val

    @property
    def port(self):
        """Gets and sets the port
        
        Returns: 
            int:
                The port
        """
        if "port" in self._prop_dict:
            return self._prop_dict["port"]
        else:
            return None

    @port.setter
    def port(self, val):
        self._prop_dict["port"] = val

    @property
    def force_tls(self):
        """Gets and sets the forceTls
        
        Returns: 
            bool:
                The forceTls
        """
        if "forceTls" in self._prop_dict:
            return self._prop_dict["forceTls"]
        else:
            return None

    @force_tls.setter
    def force_tls(self, val):
        self._prop_dict["forceTls"] = val

