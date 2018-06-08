# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ProxiedDomain(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def ip_address_or_fqdn(self):
        """Gets and sets the ipAddressOrFQDN
        
        Returns: 
            str:
                The ipAddressOrFQDN
        """
        if "ipAddressOrFQDN" in self._prop_dict:
            return self._prop_dict["ipAddressOrFQDN"]
        else:
            return None

    @ip_address_or_fqdn.setter
    def ip_address_or_fqdn(self, val):
        self._prop_dict["ipAddressOrFQDN"] = val

    @property
    def proxy(self):
        """Gets and sets the proxy
        
        Returns: 
            str:
                The proxy
        """
        if "proxy" in self._prop_dict:
            return self._prop_dict["proxy"]
        else:
            return None

    @proxy.setter
    def proxy(self, val):
        self._prop_dict["proxy"] = val

