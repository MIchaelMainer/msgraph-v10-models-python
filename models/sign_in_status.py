# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SignInStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def error_code(self):
        """Gets and sets the errorCode
        
        Returns: 
            int:
                The errorCode
        """
        if "errorCode" in self._prop_dict:
            return self._prop_dict["errorCode"]
        else:
            return None

    @error_code.setter
    def error_code(self, val):
        self._prop_dict["errorCode"] = val

    @property
    def failure_reason(self):
        """Gets and sets the failureReason
        
        Returns: 
            str:
                The failureReason
        """
        if "failureReason" in self._prop_dict:
            return self._prop_dict["failureReason"]
        else:
            return None

    @failure_reason.setter
    def failure_reason(self, val):
        self._prop_dict["failureReason"] = val

    @property
    def additional_details(self):
        """Gets and sets the additionalDetails
        
        Returns: 
            str:
                The additionalDetails
        """
        if "additionalDetails" in self._prop_dict:
            return self._prop_dict["additionalDetails"]
        else:
            return None

    @additional_details.setter
    def additional_details(self, val):
        self._prop_dict["additionalDetails"] = val

