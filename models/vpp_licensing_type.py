# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class VppLicensingType(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def support_user_licensing(self):
        """Gets and sets the supportUserLicensing
        
        Returns: 
            bool:
                The supportUserLicensing
        """
        if "supportUserLicensing" in self._prop_dict:
            return self._prop_dict["supportUserLicensing"]
        else:
            return None

    @support_user_licensing.setter
    def support_user_licensing(self, val):
        self._prop_dict["supportUserLicensing"] = val

    @property
    def support_device_licensing(self):
        """Gets and sets the supportDeviceLicensing
        
        Returns: 
            bool:
                The supportDeviceLicensing
        """
        if "supportDeviceLicensing" in self._prop_dict:
            return self._prop_dict["supportDeviceLicensing"]
        else:
            return None

    @support_device_licensing.setter
    def support_device_licensing(self, val):
        self._prop_dict["supportDeviceLicensing"] = val

    @property
    def supports_user_licensing(self):
        """Gets and sets the supportsUserLicensing
        
        Returns: 
            bool:
                The supportsUserLicensing
        """
        if "supportsUserLicensing" in self._prop_dict:
            return self._prop_dict["supportsUserLicensing"]
        else:
            return None

    @supports_user_licensing.setter
    def supports_user_licensing(self, val):
        self._prop_dict["supportsUserLicensing"] = val

    @property
    def supports_device_licensing(self):
        """Gets and sets the supportsDeviceLicensing
        
        Returns: 
            bool:
                The supportsDeviceLicensing
        """
        if "supportsDeviceLicensing" in self._prop_dict:
            return self._prop_dict["supportsDeviceLicensing"]
        else:
            return None

    @supports_device_licensing.setter
    def supports_device_licensing(self, val):
        self._prop_dict["supportsDeviceLicensing"] = val

