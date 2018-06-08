# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidDeviceComplianceLocalActionBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def grace_period_in_minutes(self):
        """
        Gets and sets the gracePeriodInMinutes
        
        Returns:
            int:
                The gracePeriodInMinutes
        """
        if "gracePeriodInMinutes" in self._prop_dict:
            return self._prop_dict["gracePeriodInMinutes"]
        else:
            return None

    @grace_period_in_minutes.setter
    def grace_period_in_minutes(self, val):
        self._prop_dict["gracePeriodInMinutes"] = val

