# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidMinimumOperatingSystem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def v4_0(self):
        """Gets and sets the v4_0
        
        Returns: 
            bool:
                The v4_0
        """
        if "v4_0" in self._prop_dict:
            return self._prop_dict["v4_0"]
        else:
            return None

    @v4_0.setter
    def v4_0(self, val):
        self._prop_dict["v4_0"] = val

    @property
    def v4_0_3(self):
        """Gets and sets the v4_0_3
        
        Returns: 
            bool:
                The v4_0_3
        """
        if "v4_0_3" in self._prop_dict:
            return self._prop_dict["v4_0_3"]
        else:
            return None

    @v4_0_3.setter
    def v4_0_3(self, val):
        self._prop_dict["v4_0_3"] = val

    @property
    def v4_1(self):
        """Gets and sets the v4_1
        
        Returns: 
            bool:
                The v4_1
        """
        if "v4_1" in self._prop_dict:
            return self._prop_dict["v4_1"]
        else:
            return None

    @v4_1.setter
    def v4_1(self, val):
        self._prop_dict["v4_1"] = val

    @property
    def v4_2(self):
        """Gets and sets the v4_2
        
        Returns: 
            bool:
                The v4_2
        """
        if "v4_2" in self._prop_dict:
            return self._prop_dict["v4_2"]
        else:
            return None

    @v4_2.setter
    def v4_2(self, val):
        self._prop_dict["v4_2"] = val

    @property
    def v4_3(self):
        """Gets and sets the v4_3
        
        Returns: 
            bool:
                The v4_3
        """
        if "v4_3" in self._prop_dict:
            return self._prop_dict["v4_3"]
        else:
            return None

    @v4_3.setter
    def v4_3(self, val):
        self._prop_dict["v4_3"] = val

    @property
    def v4_4(self):
        """Gets and sets the v4_4
        
        Returns: 
            bool:
                The v4_4
        """
        if "v4_4" in self._prop_dict:
            return self._prop_dict["v4_4"]
        else:
            return None

    @v4_4.setter
    def v4_4(self, val):
        self._prop_dict["v4_4"] = val

    @property
    def v5_0(self):
        """Gets and sets the v5_0
        
        Returns: 
            bool:
                The v5_0
        """
        if "v5_0" in self._prop_dict:
            return self._prop_dict["v5_0"]
        else:
            return None

    @v5_0.setter
    def v5_0(self, val):
        self._prop_dict["v5_0"] = val

    @property
    def v5_1(self):
        """Gets and sets the v5_1
        
        Returns: 
            bool:
                The v5_1
        """
        if "v5_1" in self._prop_dict:
            return self._prop_dict["v5_1"]
        else:
            return None

    @v5_1.setter
    def v5_1(self, val):
        self._prop_dict["v5_1"] = val

