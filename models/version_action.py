# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class VersionAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def new_version(self):
        """Gets and sets the newVersion
        
        Returns: 
            str:
                The newVersion
        """
        if "newVersion" in self._prop_dict:
            return self._prop_dict["newVersion"]
        else:
            return None

    @new_version.setter
    def new_version(self, val):
        self._prop_dict["newVersion"] = val
