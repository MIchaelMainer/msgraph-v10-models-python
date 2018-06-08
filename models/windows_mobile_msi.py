# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsMobileMSI(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def command_line(self):
        """
        Gets and sets the commandLine
        
        Returns:
            str:
                The commandLine
        """
        if "commandLine" in self._prop_dict:
            return self._prop_dict["commandLine"]
        else:
            return None

    @command_line.setter
    def command_line(self, val):
        self._prop_dict["commandLine"] = val

    @property
    def product_code(self):
        """
        Gets and sets the productCode
        
        Returns:
            str:
                The productCode
        """
        if "productCode" in self._prop_dict:
            return self._prop_dict["productCode"]
        else:
            return None

    @product_code.setter
    def product_code(self, val):
        self._prop_dict["productCode"] = val

    @property
    def product_version(self):
        """
        Gets and sets the productVersion
        
        Returns:
            str:
                The productVersion
        """
        if "productVersion" in self._prop_dict:
            return self._prop_dict["productVersion"]
        else:
            return None

    @product_version.setter
    def product_version(self, val):
        self._prop_dict["productVersion"] = val

    @property
    def ignore_version_detection(self):
        """
        Gets and sets the ignoreVersionDetection
        
        Returns:
            bool:
                The ignoreVersionDetection
        """
        if "ignoreVersionDetection" in self._prop_dict:
            return self._prop_dict["ignoreVersionDetection"]
        else:
            return None

    @ignore_version_detection.setter
    def ignore_version_detection(self, val):
        self._prop_dict["ignoreVersionDetection"] = val

