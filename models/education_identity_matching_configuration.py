# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_identity_matching_options import EducationIdentityMatchingOptions
from ..one_drive_object_base import OneDriveObjectBase


class EducationIdentityMatchingConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def matching_options(self):
        """
        Gets and sets the matchingOptions
        
        Returns: 
            :class:`EducationIdentityMatchingOptions<onedrivesdk.model.education_identity_matching_options.EducationIdentityMatchingOptions>`:
                The matchingOptions
        """
        if "matchingOptions" in self._prop_dict:
            if isinstance(self._prop_dict["matchingOptions"], OneDriveObjectBase):
                return self._prop_dict["matchingOptions"]
            else :
                self._prop_dict["matchingOptions"] = EducationIdentityMatchingOptions(self._prop_dict["matchingOptions"])
                return self._prop_dict["matchingOptions"]

        return None

    @matching_options.setter
    def matching_options(self, val):
        self._prop_dict["matchingOptions"] = val
