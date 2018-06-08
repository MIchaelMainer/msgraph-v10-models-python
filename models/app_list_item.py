# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AppListItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def publisher(self):
        """Gets and sets the publisher
        
        Returns: 
            str:
                The publisher
        """
        if "publisher" in self._prop_dict:
            return self._prop_dict["publisher"]
        else:
            return None

    @publisher.setter
    def publisher(self, val):
        self._prop_dict["publisher"] = val

    @property
    def app_store_url(self):
        """Gets and sets the appStoreUrl
        
        Returns: 
            str:
                The appStoreUrl
        """
        if "appStoreUrl" in self._prop_dict:
            return self._prop_dict["appStoreUrl"]
        else:
            return None

    @app_store_url.setter
    def app_store_url(self, val):
        self._prop_dict["appStoreUrl"] = val

    @property
    def app_id(self):
        """Gets and sets the appId
        
        Returns: 
            str:
                The appId
        """
        if "appId" in self._prop_dict:
            return self._prop_dict["appId"]
        else:
            return None

    @app_id.setter
    def app_id(self, val):
        self._prop_dict["appId"] = val

