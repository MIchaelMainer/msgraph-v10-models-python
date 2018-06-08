# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.secure_assessment_account_type import SecureAssessmentAccountType
from ..one_drive_object_base import OneDriveObjectBase


class Windows10SecureAssessmentConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def launch_uri(self):
        """
        Gets and sets the launchUri
        
        Returns:
            str:
                The launchUri
        """
        if "launchUri" in self._prop_dict:
            return self._prop_dict["launchUri"]
        else:
            return None

    @launch_uri.setter
    def launch_uri(self, val):
        self._prop_dict["launchUri"] = val

    @property
    def configuration_account(self):
        """
        Gets and sets the configurationAccount
        
        Returns:
            str:
                The configurationAccount
        """
        if "configurationAccount" in self._prop_dict:
            return self._prop_dict["configurationAccount"]
        else:
            return None

    @configuration_account.setter
    def configuration_account(self, val):
        self._prop_dict["configurationAccount"] = val

    @property
    def configuration_account_type(self):
        """
        Gets and sets the configurationAccountType
        
        Returns: 
            :class:`SecureAssessmentAccountType<onedrivesdk.model.secure_assessment_account_type.SecureAssessmentAccountType>`:
                The configurationAccountType
        """
        if "configurationAccountType" in self._prop_dict:
            if isinstance(self._prop_dict["configurationAccountType"], OneDriveObjectBase):
                return self._prop_dict["configurationAccountType"]
            else :
                self._prop_dict["configurationAccountType"] = SecureAssessmentAccountType(self._prop_dict["configurationAccountType"])
                return self._prop_dict["configurationAccountType"]

        return None

    @configuration_account_type.setter
    def configuration_account_type(self, val):
        self._prop_dict["configurationAccountType"] = val

    @property
    def allow_printing(self):
        """
        Gets and sets the allowPrinting
        
        Returns:
            bool:
                The allowPrinting
        """
        if "allowPrinting" in self._prop_dict:
            return self._prop_dict["allowPrinting"]
        else:
            return None

    @allow_printing.setter
    def allow_printing(self, val):
        self._prop_dict["allowPrinting"] = val

    @property
    def allow_screen_capture(self):
        """
        Gets and sets the allowScreenCapture
        
        Returns:
            bool:
                The allowScreenCapture
        """
        if "allowScreenCapture" in self._prop_dict:
            return self._prop_dict["allowScreenCapture"]
        else:
            return None

    @allow_screen_capture.setter
    def allow_screen_capture(self, val):
        self._prop_dict["allowScreenCapture"] = val

    @property
    def allow_text_suggestion(self):
        """
        Gets and sets the allowTextSuggestion
        
        Returns:
            bool:
                The allowTextSuggestion
        """
        if "allowTextSuggestion" in self._prop_dict:
            return self._prop_dict["allowTextSuggestion"]
        else:
            return None

    @allow_text_suggestion.setter
    def allow_text_suggestion(self, val):
        self._prop_dict["allowTextSuggestion"] = val

