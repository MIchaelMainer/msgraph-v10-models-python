# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionAppLockerFile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def file_hash(self):
        """
        Gets and sets the fileHash
        
        Returns:
            str:
                The fileHash
        """
        if "fileHash" in self._prop_dict:
            return self._prop_dict["fileHash"]
        else:
            return None

    @file_hash.setter
    def file_hash(self, val):
        self._prop_dict["fileHash"] = val

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            str:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

