# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ip_range import IpRange
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionIPRangeCollection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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
    def ranges(self):
        """
        Gets and sets the ranges
        
        Returns: 
            :class:`IpRange<onedrivesdk.model.ip_range.IpRange>`:
                The ranges
        """
        if "ranges" in self._prop_dict:
            if isinstance(self._prop_dict["ranges"], OneDriveObjectBase):
                return self._prop_dict["ranges"]
            else :
                self._prop_dict["ranges"] = IpRange(self._prop_dict["ranges"])
                return self._prop_dict["ranges"]

        return None

    @ranges.setter
    def ranges(self, val):
        self._prop_dict["ranges"] = val
