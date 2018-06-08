# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.terms_and_conditions import TermsAndConditions
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class TermsAndConditionsAcceptanceStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_display_name(self):
        """
        Gets and sets the userDisplayName
        
        Returns:
            str:
                The userDisplayName
        """
        if "userDisplayName" in self._prop_dict:
            return self._prop_dict["userDisplayName"]
        else:
            return None

    @user_display_name.setter
    def user_display_name(self, val):
        self._prop_dict["userDisplayName"] = val

    @property
    def accepted_version(self):
        """
        Gets and sets the acceptedVersion
        
        Returns:
            int:
                The acceptedVersion
        """
        if "acceptedVersion" in self._prop_dict:
            return self._prop_dict["acceptedVersion"]
        else:
            return None

    @accepted_version.setter
    def accepted_version(self, val):
        self._prop_dict["acceptedVersion"] = val

    @property
    def accepted_date_time(self):
        """
        Gets and sets the acceptedDateTime
        
        Returns:
            datetime:
                The acceptedDateTime
        """
        if "acceptedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["acceptedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @accepted_date_time.setter
    def accepted_date_time(self, val):
        self._prop_dict["acceptedDateTime"] = val.isoformat()+"Z"

    @property
    def terms_and_conditions(self):
        """
        Gets and sets the termsAndConditions
        
        Returns: 
            :class:`TermsAndConditions<onedrivesdk.model.terms_and_conditions.TermsAndConditions>`:
                The termsAndConditions
        """
        if "termsAndConditions" in self._prop_dict:
            if isinstance(self._prop_dict["termsAndConditions"], OneDriveObjectBase):
                return self._prop_dict["termsAndConditions"]
            else :
                self._prop_dict["termsAndConditions"] = TermsAndConditions(self._prop_dict["termsAndConditions"])
                return self._prop_dict["termsAndConditions"]

        return None

    @terms_and_conditions.setter
    def terms_and_conditions(self, val):
        self._prop_dict["termsAndConditions"] = val

