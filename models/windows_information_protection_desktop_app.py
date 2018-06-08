# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionDesktopApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def binary_name(self):
        """Gets and sets the binaryName
        
        Returns: 
            str:
                The binaryName
        """
        if "binaryName" in self._prop_dict:
            return self._prop_dict["binaryName"]
        else:
            return None

    @binary_name.setter
    def binary_name(self, val):
        self._prop_dict["binaryName"] = val

    @property
    def binary_version_low(self):
        """Gets and sets the binaryVersionLow
        
        Returns: 
            str:
                The binaryVersionLow
        """
        if "binaryVersionLow" in self._prop_dict:
            return self._prop_dict["binaryVersionLow"]
        else:
            return None

    @binary_version_low.setter
    def binary_version_low(self, val):
        self._prop_dict["binaryVersionLow"] = val

    @property
    def binary_version_high(self):
        """Gets and sets the binaryVersionHigh
        
        Returns: 
            str:
                The binaryVersionHigh
        """
        if "binaryVersionHigh" in self._prop_dict:
            return self._prop_dict["binaryVersionHigh"]
        else:
            return None

    @binary_version_high.setter
    def binary_version_high(self, val):
        self._prop_dict["binaryVersionHigh"] = val

