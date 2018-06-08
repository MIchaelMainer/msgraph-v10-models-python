# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationOAuth2ClientCredentialsConnectionSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def token_url(self):
        """Gets and sets the tokenUrl
        
        Returns: 
            str:
                The tokenUrl
        """
        if "tokenUrl" in self._prop_dict:
            return self._prop_dict["tokenUrl"]
        else:
            return None

    @token_url.setter
    def token_url(self, val):
        self._prop_dict["tokenUrl"] = val

    @property
    def scope(self):
        """Gets and sets the scope
        
        Returns: 
            str:
                The scope
        """
        if "scope" in self._prop_dict:
            return self._prop_dict["scope"]
        else:
            return None

    @scope.setter
    def scope(self, val):
        self._prop_dict["scope"] = val

