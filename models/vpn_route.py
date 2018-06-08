# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class VpnRoute(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def destination_prefix(self):
        """Gets and sets the destinationPrefix
        
        Returns: 
            str:
                The destinationPrefix
        """
        if "destinationPrefix" in self._prop_dict:
            return self._prop_dict["destinationPrefix"]
        else:
            return None

    @destination_prefix.setter
    def destination_prefix(self, val):
        self._prop_dict["destinationPrefix"] = val

    @property
    def prefix_size(self):
        """Gets and sets the prefixSize
        
        Returns: 
            int:
                The prefixSize
        """
        if "prefixSize" in self._prop_dict:
            return self._prop_dict["prefixSize"]
        else:
            return None

    @prefix_size.setter
    def prefix_size(self, val):
        self._prop_dict["prefixSize"] = val

