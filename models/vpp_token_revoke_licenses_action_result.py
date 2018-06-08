# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.vpp_token_action_failure_reason import VppTokenActionFailureReason
from ..one_drive_object_base import OneDriveObjectBase


class VppTokenRevokeLicensesActionResult(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def total_licenses_count(self):
        """Gets and sets the totalLicensesCount
        
        Returns: 
            int:
                The totalLicensesCount
        """
        if "totalLicensesCount" in self._prop_dict:
            return self._prop_dict["totalLicensesCount"]
        else:
            return None

    @total_licenses_count.setter
    def total_licenses_count(self, val):
        self._prop_dict["totalLicensesCount"] = val

    @property
    def failed_licenses_count(self):
        """Gets and sets the failedLicensesCount
        
        Returns: 
            int:
                The failedLicensesCount
        """
        if "failedLicensesCount" in self._prop_dict:
            return self._prop_dict["failedLicensesCount"]
        else:
            return None

    @failed_licenses_count.setter
    def failed_licenses_count(self, val):
        self._prop_dict["failedLicensesCount"] = val

    @property
    def action_failure_reason(self):
        """
        Gets and sets the actionFailureReason
        
        Returns: 
            :class:`VppTokenActionFailureReason<onedrivesdk.model.vpp_token_action_failure_reason.VppTokenActionFailureReason>`:
                The actionFailureReason
        """
        if "actionFailureReason" in self._prop_dict:
            if isinstance(self._prop_dict["actionFailureReason"], OneDriveObjectBase):
                return self._prop_dict["actionFailureReason"]
            else :
                self._prop_dict["actionFailureReason"] = VppTokenActionFailureReason(self._prop_dict["actionFailureReason"])
                return self._prop_dict["actionFailureReason"]

        return None

    @action_failure_reason.setter
    def action_failure_reason(self, val):
        self._prop_dict["actionFailureReason"] = val
