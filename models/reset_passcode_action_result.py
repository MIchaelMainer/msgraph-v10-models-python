# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ResetPasscodeActionResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def passcode(self):
        """Gets and sets the passcode
        
        Returns: 
            str:
                The passcode
        """
        if "passcode" in self._prop_dict:
            return self._prop_dict["passcode"]
        else:
            return None

    @passcode.setter
    def passcode(self, val):
        self._prop_dict["passcode"] = val

