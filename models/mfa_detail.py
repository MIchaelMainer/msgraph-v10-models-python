# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MfaDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def auth_method(self):
        """Gets and sets the authMethod
        
        Returns: 
            str:
                The authMethod
        """
        if "authMethod" in self._prop_dict:
            return self._prop_dict["authMethod"]
        else:
            return None

    @auth_method.setter
    def auth_method(self, val):
        self._prop_dict["authMethod"] = val

    @property
    def auth_detail(self):
        """Gets and sets the authDetail
        
        Returns: 
            str:
                The authDetail
        """
        if "authDetail" in self._prop_dict:
            return self._prop_dict["authDetail"]
        else:
            return None

    @auth_detail.setter
    def auth_detail(self, val):
        self._prop_dict["authDetail"] = val

