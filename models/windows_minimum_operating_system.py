# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsMinimumOperatingSystem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def v8_0(self):
        """Gets and sets the v8_0
        
        Returns: 
            bool:
                The v8_0
        """
        if "v8_0" in self._prop_dict:
            return self._prop_dict["v8_0"]
        else:
            return None

    @v8_0.setter
    def v8_0(self, val):
        self._prop_dict["v8_0"] = val

    @property
    def v8_1(self):
        """Gets and sets the v8_1
        
        Returns: 
            bool:
                The v8_1
        """
        if "v8_1" in self._prop_dict:
            return self._prop_dict["v8_1"]
        else:
            return None

    @v8_1.setter
    def v8_1(self, val):
        self._prop_dict["v8_1"] = val

    @property
    def v10_0(self):
        """Gets and sets the v10_0
        
        Returns: 
            bool:
                The v10_0
        """
        if "v10_0" in self._prop_dict:
            return self._prop_dict["v10_0"]
        else:
            return None

    @v10_0.setter
    def v10_0(self, val):
        self._prop_dict["v10_0"] = val

