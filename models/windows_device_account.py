# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsDeviceAccount(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def password(self):
        """Gets and sets the password
        
        Returns: 
            str:
                The password
        """
        if "password" in self._prop_dict:
            return self._prop_dict["password"]
        else:
            return None

    @password.setter
    def password(self, val):
        self._prop_dict["password"] = val

