# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidDeviceComplianceLocalActionLockDeviceWithPasscode(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def passcode(self):
        """
        Gets and sets the passcode
        
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

    @property
    def passcode_sign_in_failure_count_before_wipe(self):
        """
        Gets and sets the passcodeSignInFailureCountBeforeWipe
        
        Returns:
            int:
                The passcodeSignInFailureCountBeforeWipe
        """
        if "passcodeSignInFailureCountBeforeWipe" in self._prop_dict:
            return self._prop_dict["passcodeSignInFailureCountBeforeWipe"]
        else:
            return None

    @passcode_sign_in_failure_count_before_wipe.setter
    def passcode_sign_in_failure_count_before_wipe(self, val):
        self._prop_dict["passcodeSignInFailureCountBeforeWipe"] = val

