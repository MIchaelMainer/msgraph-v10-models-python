# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsAppXAppAssignmentSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def use_device_context(self):
        """Gets and sets the useDeviceContext
        
        Returns: 
            bool:
                The useDeviceContext
        """
        if "useDeviceContext" in self._prop_dict:
            return self._prop_dict["useDeviceContext"]
        else:
            return None

    @use_device_context.setter
    def use_device_context(self, val):
        self._prop_dict["useDeviceContext"] = val

