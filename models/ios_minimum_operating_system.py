# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class IosMinimumOperatingSystem(OneDriveObjectBase):

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
    def v9_0(self):
        """Gets and sets the v9_0
        
        Returns: 
            bool:
                The v9_0
        """
        if "v9_0" in self._prop_dict:
            return self._prop_dict["v9_0"]
        else:
            return None

    @v9_0.setter
    def v9_0(self, val):
        self._prop_dict["v9_0"] = val

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

    @property
    def v11_0(self):
        """Gets and sets the v11_0
        
        Returns: 
            bool:
                The v11_0
        """
        if "v11_0" in self._prop_dict:
            return self._prop_dict["v11_0"]
        else:
            return None

    @v11_0.setter
    def v11_0(self, val):
        self._prop_dict["v11_0"] = val

