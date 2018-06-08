# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class RenameAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def new_name(self):
        """Gets and sets the newName
        
        Returns: 
            str:
                The newName
        """
        if "newName" in self._prop_dict:
            return self._prop_dict["newName"]
        else:
            return None

    @new_name.setter
    def new_name(self, val):
        self._prop_dict["newName"] = val

    @property
    def old_name(self):
        """Gets and sets the oldName
        
        Returns: 
            str:
                The oldName
        """
        if "oldName" in self._prop_dict:
            return self._prop_dict["oldName"]
        else:
            return None

    @old_name.setter
    def old_name(self, val):
        self._prop_dict["oldName"] = val

