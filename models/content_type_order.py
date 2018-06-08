# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ContentTypeOrder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def default(self):
        """Gets and sets the default
        
        Returns: 
            bool:
                The default
        """
        if "default" in self._prop_dict:
            return self._prop_dict["default"]
        else:
            return None

    @default.setter
    def default(self, val):
        self._prop_dict["default"] = val

    @property
    def position(self):
        """Gets and sets the position
        
        Returns: 
            int:
                The position
        """
        if "position" in self._prop_dict:
            return self._prop_dict["position"]
        else:
            return None

    @position.setter
    def position(self, val):
        self._prop_dict["position"] = val

