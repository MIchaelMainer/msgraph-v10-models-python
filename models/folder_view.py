# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class FolderView(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def sort_by(self):
        """Gets and sets the sortBy
        
        Returns: 
            str:
                The sortBy
        """
        if "sortBy" in self._prop_dict:
            return self._prop_dict["sortBy"]
        else:
            return None

    @sort_by.setter
    def sort_by(self, val):
        self._prop_dict["sortBy"] = val

    @property
    def sort_order(self):
        """Gets and sets the sortOrder
        
        Returns: 
            str:
                The sortOrder
        """
        if "sortOrder" in self._prop_dict:
            return self._prop_dict["sortOrder"]
        else:
            return None

    @sort_order.setter
    def sort_order(self, val):
        self._prop_dict["sortOrder"] = val

    @property
    def view_type(self):
        """Gets and sets the viewType
        
        Returns: 
            str:
                The viewType
        """
        if "viewType" in self._prop_dict:
            return self._prop_dict["viewType"]
        else:
            return None

    @view_type.setter
    def view_type(self, val):
        self._prop_dict["viewType"] = val

