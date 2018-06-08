# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionNetworkLearningSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def url(self):
        """
        Gets and sets the url
        
        Returns:
            str:
                The url
        """
        if "url" in self._prop_dict:
            return self._prop_dict["url"]
        else:
            return None

    @url.setter
    def url(self, val):
        self._prop_dict["url"] = val

    @property
    def device_count(self):
        """
        Gets and sets the deviceCount
        
        Returns:
            int:
                The deviceCount
        """
        if "deviceCount" in self._prop_dict:
            return self._prop_dict["deviceCount"]
        else:
            return None

    @device_count.setter
    def device_count(self, val):
        self._prop_dict["deviceCount"] = val

