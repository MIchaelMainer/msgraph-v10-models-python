# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDeviceModelsAndManufacturers(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_models(self):
        """Gets and sets the deviceModels
        
        Returns: 
            str:
                The deviceModels
        """
        if "deviceModels" in self._prop_dict:
            return self._prop_dict["deviceModels"]
        else:
            return None

    @device_models.setter
    def device_models(self, val):
        self._prop_dict["deviceModels"] = val

    @property
    def device_manufacturers(self):
        """Gets and sets the deviceManufacturers
        
        Returns: 
            str:
                The deviceManufacturers
        """
        if "deviceManufacturers" in self._prop_dict:
            return self._prop_dict["deviceManufacturers"]
        else:
            return None

    @device_manufacturers.setter
    def device_manufacturers(self, val):
        self._prop_dict["deviceManufacturers"] = val

