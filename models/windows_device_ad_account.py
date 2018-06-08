# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsDeviceADAccount(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def domain_name(self):
        """Gets and sets the domainName
        
        Returns: 
            str:
                The domainName
        """
        if "domainName" in self._prop_dict:
            return self._prop_dict["domainName"]
        else:
            return None

    @domain_name.setter
    def domain_name(self, val):
        self._prop_dict["domainName"] = val

    @property
    def user_name(self):
        """Gets and sets the userName
        
        Returns: 
            str:
                The userName
        """
        if "userName" in self._prop_dict:
            return self._prop_dict["userName"]
        else:
            return None

    @user_name.setter
    def user_name(self, val):
        self._prop_dict["userName"] = val

