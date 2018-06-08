# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookIcon(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def index(self):
        """Gets and sets the index
        
        Returns: 
            int:
                The index
        """
        if "index" in self._prop_dict:
            return self._prop_dict["index"]
        else:
            return None

    @index.setter
    def index(self, val):
        self._prop_dict["index"] = val

    @property
    def set(self):
        """Gets and sets the set
        
        Returns: 
            str:
                The set
        """
        if "set" in self._prop_dict:
            return self._prop_dict["set"]
        else:
            return None

    @set.setter
    def set(self, val):
        self._prop_dict["set"] = val

