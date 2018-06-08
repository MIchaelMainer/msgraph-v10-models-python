# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ListInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def content_types_enabled(self):
        """Gets and sets the contentTypesEnabled
        
        Returns: 
            bool:
                The contentTypesEnabled
        """
        if "contentTypesEnabled" in self._prop_dict:
            return self._prop_dict["contentTypesEnabled"]
        else:
            return None

    @content_types_enabled.setter
    def content_types_enabled(self, val):
        self._prop_dict["contentTypesEnabled"] = val

    @property
    def hidden(self):
        """Gets and sets the hidden
        
        Returns: 
            bool:
                The hidden
        """
        if "hidden" in self._prop_dict:
            return self._prop_dict["hidden"]
        else:
            return None

    @hidden.setter
    def hidden(self, val):
        self._prop_dict["hidden"] = val

    @property
    def template(self):
        """Gets and sets the template
        
        Returns: 
            str:
                The template
        """
        if "template" in self._prop_dict:
            return self._prop_dict["template"]
        else:
            return None

    @template.setter
    def template(self, val):
        self._prop_dict["template"] = val

