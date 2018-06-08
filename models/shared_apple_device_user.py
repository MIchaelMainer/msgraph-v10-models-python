# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SharedAppleDeviceUser(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_principal_name(self):
        """Gets and sets the userPrincipalName
        
        Returns: 
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def data_to_sync(self):
        """Gets and sets the dataToSync
        
        Returns: 
            bool:
                The dataToSync
        """
        if "dataToSync" in self._prop_dict:
            return self._prop_dict["dataToSync"]
        else:
            return None

    @data_to_sync.setter
    def data_to_sync(self, val):
        self._prop_dict["dataToSync"] = val

    @property
    def data_quota(self):
        """Gets and sets the dataQuota
        
        Returns: 
            int:
                The dataQuota
        """
        if "dataQuota" in self._prop_dict:
            return self._prop_dict["dataQuota"]
        else:
            return None

    @data_quota.setter
    def data_quota(self, val):
        self._prop_dict["dataQuota"] = val

    @property
    def data_used(self):
        """Gets and sets the dataUsed
        
        Returns: 
            int:
                The dataUsed
        """
        if "dataUsed" in self._prop_dict:
            return self._prop_dict["dataUsed"]
        else:
            return None

    @data_used.setter
    def data_used(self, val):
        self._prop_dict["dataUsed"] = val

