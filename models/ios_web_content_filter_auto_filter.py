# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class IosWebContentFilterAutoFilter(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allowed_urls(self):
        """Gets and sets the allowedUrls
        
        Returns: 
            str:
                The allowedUrls
        """
        if "allowedUrls" in self._prop_dict:
            return self._prop_dict["allowedUrls"]
        else:
            return None

    @allowed_urls.setter
    def allowed_urls(self, val):
        self._prop_dict["allowedUrls"] = val

    @property
    def blocked_urls(self):
        """Gets and sets the blockedUrls
        
        Returns: 
            str:
                The blockedUrls
        """
        if "blockedUrls" in self._prop_dict:
            return self._prop_dict["blockedUrls"]
        else:
            return None

    @blocked_urls.setter
    def blocked_urls(self, val):
        self._prop_dict["blockedUrls"] = val

