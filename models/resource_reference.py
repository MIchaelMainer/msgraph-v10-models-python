# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ResourceReference(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def web_url(self):
        """Gets and sets the webUrl
        
        Returns: 
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

