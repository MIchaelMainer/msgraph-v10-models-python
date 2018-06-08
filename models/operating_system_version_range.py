# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class OperatingSystemVersionRange(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def description(self):
        """Gets and sets the description
        
        Returns: 
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def lowest_version(self):
        """Gets and sets the lowestVersion
        
        Returns: 
            str:
                The lowestVersion
        """
        if "lowestVersion" in self._prop_dict:
            return self._prop_dict["lowestVersion"]
        else:
            return None

    @lowest_version.setter
    def lowest_version(self, val):
        self._prop_dict["lowestVersion"] = val

    @property
    def highest_version(self):
        """Gets and sets the highestVersion
        
        Returns: 
            str:
                The highestVersion
        """
        if "highestVersion" in self._prop_dict:
            return self._prop_dict["highestVersion"]
        else:
            return None

    @highest_version.setter
    def highest_version(self, val):
        self._prop_dict["highestVersion"] = val

