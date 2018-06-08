# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ItemPreviewInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def get_url(self):
        """Gets and sets the getUrl
        
        Returns: 
            str:
                The getUrl
        """
        if "getUrl" in self._prop_dict:
            return self._prop_dict["getUrl"]
        else:
            return None

    @get_url.setter
    def get_url(self, val):
        self._prop_dict["getUrl"] = val

    @property
    def post_parameters(self):
        """Gets and sets the postParameters
        
        Returns: 
            str:
                The postParameters
        """
        if "postParameters" in self._prop_dict:
            return self._prop_dict["postParameters"]
        else:
            return None

    @post_parameters.setter
    def post_parameters(self, val):
        self._prop_dict["postParameters"] = val

    @property
    def post_url(self):
        """Gets and sets the postUrl
        
        Returns: 
            str:
                The postUrl
        """
        if "postUrl" in self._prop_dict:
            return self._prop_dict["postUrl"]
        else:
            return None

    @post_url.setter
    def post_url(self, val):
        self._prop_dict["postUrl"] = val

