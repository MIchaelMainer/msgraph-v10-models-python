# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DaylightTimeZoneOffset(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def daylight_bias(self):
        """Gets and sets the daylightBias
        
        Returns: 
            int:
                The daylightBias
        """
        if "daylightBias" in self._prop_dict:
            return self._prop_dict["daylightBias"]
        else:
            return None

    @daylight_bias.setter
    def daylight_bias(self, val):
        self._prop_dict["daylightBias"] = val

