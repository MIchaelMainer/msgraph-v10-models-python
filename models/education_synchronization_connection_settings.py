# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationConnectionSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def client_id(self):
        """Gets and sets the clientId
        
        Returns: 
            str:
                The clientId
        """
        if "clientId" in self._prop_dict:
            return self._prop_dict["clientId"]
        else:
            return None

    @client_id.setter
    def client_id(self, val):
        self._prop_dict["clientId"] = val

    @property
    def client_secret(self):
        """Gets and sets the clientSecret
        
        Returns: 
            str:
                The clientSecret
        """
        if "clientSecret" in self._prop_dict:
            return self._prop_dict["clientSecret"]
        else:
            return None

    @client_secret.setter
    def client_secret(self, val):
        self._prop_dict["clientSecret"] = val

