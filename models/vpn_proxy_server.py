# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class VpnProxyServer(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def automatic_configuration_script_url(self):
        """Gets and sets the automaticConfigurationScriptUrl
        
        Returns: 
            str:
                The automaticConfigurationScriptUrl
        """
        if "automaticConfigurationScriptUrl" in self._prop_dict:
            return self._prop_dict["automaticConfigurationScriptUrl"]
        else:
            return None

    @automatic_configuration_script_url.setter
    def automatic_configuration_script_url(self, val):
        self._prop_dict["automaticConfigurationScriptUrl"] = val

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

