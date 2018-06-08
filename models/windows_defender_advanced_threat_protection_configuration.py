# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsDefenderAdvancedThreatProtectionConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def advanced_threat_protection_onboarding_blob(self):
        """
        Gets and sets the advancedThreatProtectionOnboardingBlob
        
        Returns:
            str:
                The advancedThreatProtectionOnboardingBlob
        """
        if "advancedThreatProtectionOnboardingBlob" in self._prop_dict:
            return self._prop_dict["advancedThreatProtectionOnboardingBlob"]
        else:
            return None

    @advanced_threat_protection_onboarding_blob.setter
    def advanced_threat_protection_onboarding_blob(self, val):
        self._prop_dict["advancedThreatProtectionOnboardingBlob"] = val

    @property
    def advanced_threat_protection_onboarding_filename(self):
        """
        Gets and sets the advancedThreatProtectionOnboardingFilename
        
        Returns:
            str:
                The advancedThreatProtectionOnboardingFilename
        """
        if "advancedThreatProtectionOnboardingFilename" in self._prop_dict:
            return self._prop_dict["advancedThreatProtectionOnboardingFilename"]
        else:
            return None

    @advanced_threat_protection_onboarding_filename.setter
    def advanced_threat_protection_onboarding_filename(self, val):
        self._prop_dict["advancedThreatProtectionOnboardingFilename"] = val

    @property
    def allow_sample_sharing(self):
        """
        Gets and sets the allowSampleSharing
        
        Returns:
            bool:
                The allowSampleSharing
        """
        if "allowSampleSharing" in self._prop_dict:
            return self._prop_dict["allowSampleSharing"]
        else:
            return None

    @allow_sample_sharing.setter
    def allow_sample_sharing(self, val):
        self._prop_dict["allowSampleSharing"] = val

    @property
    def enable_expedited_telemetry_reporting(self):
        """
        Gets and sets the enableExpeditedTelemetryReporting
        
        Returns:
            bool:
                The enableExpeditedTelemetryReporting
        """
        if "enableExpeditedTelemetryReporting" in self._prop_dict:
            return self._prop_dict["enableExpeditedTelemetryReporting"]
        else:
            return None

    @enable_expedited_telemetry_reporting.setter
    def enable_expedited_telemetry_reporting(self, val):
        self._prop_dict["enableExpeditedTelemetryReporting"] = val

    @property
    def advanced_threat_protection_offboarding_blob(self):
        """
        Gets and sets the advancedThreatProtectionOffboardingBlob
        
        Returns:
            str:
                The advancedThreatProtectionOffboardingBlob
        """
        if "advancedThreatProtectionOffboardingBlob" in self._prop_dict:
            return self._prop_dict["advancedThreatProtectionOffboardingBlob"]
        else:
            return None

    @advanced_threat_protection_offboarding_blob.setter
    def advanced_threat_protection_offboarding_blob(self, val):
        self._prop_dict["advancedThreatProtectionOffboardingBlob"] = val

    @property
    def advanced_threat_protection_offboarding_filename(self):
        """
        Gets and sets the advancedThreatProtectionOffboardingFilename
        
        Returns:
            str:
                The advancedThreatProtectionOffboardingFilename
        """
        if "advancedThreatProtectionOffboardingFilename" in self._prop_dict:
            return self._prop_dict["advancedThreatProtectionOffboardingFilename"]
        else:
            return None

    @advanced_threat_protection_offboarding_filename.setter
    def advanced_threat_protection_offboarding_filename(self, val):
        self._prop_dict["advancedThreatProtectionOffboardingFilename"] = val

