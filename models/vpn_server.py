# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class VpnServer(OneDriveObjectBase):

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
    def is_default_server(self):
        """Gets and sets the isDefaultServer
        
        Returns: 
            bool:
                The isDefaultServer
        """
        if "isDefaultServer" in self._prop_dict:
            return self._prop_dict["isDefaultServer"]
        else:
            return None

    @is_default_server.setter
    def is_default_server(self, val):
        self._prop_dict["isDefaultServer"] = val

