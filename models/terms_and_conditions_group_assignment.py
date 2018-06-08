# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.terms_and_conditions import TermsAndConditions
from ..one_drive_object_base import OneDriveObjectBase


class TermsAndConditionsGroupAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def target_group_id(self):
        """
        Gets and sets the targetGroupId
        
        Returns:
            str:
                The targetGroupId
        """
        if "targetGroupId" in self._prop_dict:
            return self._prop_dict["targetGroupId"]
        else:
            return None

    @target_group_id.setter
    def target_group_id(self, val):
        self._prop_dict["targetGroupId"] = val

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

