# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Windows10VpnProxyServer(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bypass_proxy_server_for_local_address(self):
        """Gets and sets the bypassProxyServerForLocalAddress
        
        Returns: 
            bool:
                The bypassProxyServerForLocalAddress
        """
        if "bypassProxyServerForLocalAddress" in self._prop_dict:
            return self._prop_dict["bypassProxyServerForLocalAddress"]
        else:
            return None

    @bypass_proxy_server_for_local_address.setter
    def bypass_proxy_server_for_local_address(self, val):
        self._prop_dict["bypassProxyServerForLocalAddress"] = val
