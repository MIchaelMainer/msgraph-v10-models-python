# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class VpnDnsRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def servers(self):
        """Gets and sets the servers
        
        Returns: 
            str:
                The servers
        """
        if "servers" in self._prop_dict:
            return self._prop_dict["servers"]
        else:
            return None

    @servers.setter
    def servers(self, val):
        self._prop_dict["servers"] = val

    @property
    def proxy_server_uri(self):
        """Gets and sets the proxyServerUri
        
        Returns: 
            str:
                The proxyServerUri
        """
        if "proxyServerUri" in self._prop_dict:
            return self._prop_dict["proxyServerUri"]
        else:
            return None

    @proxy_server_uri.setter
    def proxy_server_uri(self, val):
        self._prop_dict["proxyServerUri"] = val

