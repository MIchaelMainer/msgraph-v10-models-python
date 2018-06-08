# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookSessionInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def persist_changes(self):
        """Gets and sets the persistChanges
        
        Returns: 
            bool:
                The persistChanges
        """
        if "persistChanges" in self._prop_dict:
            return self._prop_dict["persistChanges"]
        else:
            return None

    @persist_changes.setter
    def persist_changes(self, val):
        self._prop_dict["persistChanges"] = val

