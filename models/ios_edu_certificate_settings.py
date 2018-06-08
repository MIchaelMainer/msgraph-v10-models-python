# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.certificate_validity_period_scale import CertificateValidityPeriodScale
from ..one_drive_object_base import OneDriveObjectBase


class IosEduCertificateSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def cert_file_name(self):
        """Gets and sets the certFileName
        
        Returns: 
            str:
                The certFileName
        """
        if "certFileName" in self._prop_dict:
            return self._prop_dict["certFileName"]
        else:
            return None

    @cert_file_name.setter
    def cert_file_name(self, val):
        self._prop_dict["certFileName"] = val

    @property
    def certification_authority(self):
        """Gets and sets the certificationAuthority
        
        Returns: 
            str:
                The certificationAuthority
        """
        if "certificationAuthority" in self._prop_dict:
            return self._prop_dict["certificationAuthority"]
        else:
            return None

    @certification_authority.setter
    def certification_authority(self, val):
        self._prop_dict["certificationAuthority"] = val

    @property
    def certification_authority_name(self):
        """Gets and sets the certificationAuthorityName
        
        Returns: 
            str:
                The certificationAuthorityName
        """
        if "certificationAuthorityName" in self._prop_dict:
            return self._prop_dict["certificationAuthorityName"]
        else:
            return None

    @certification_authority_name.setter
    def certification_authority_name(self, val):
        self._prop_dict["certificationAuthorityName"] = val

    @property
    def certificate_template_name(self):
        """Gets and sets the certificateTemplateName
        
        Returns: 
            str:
                The certificateTemplateName
        """
        if "certificateTemplateName" in self._prop_dict:
            return self._prop_dict["certificateTemplateName"]
        else:
            return None

    @certificate_template_name.setter
    def certificate_template_name(self, val):
        self._prop_dict["certificateTemplateName"] = val

    @property
    def renewal_threshold_percentage(self):
        """Gets and sets the renewalThresholdPercentage
        
        Returns: 
            int:
                The renewalThresholdPercentage
        """
        if "renewalThresholdPercentage" in self._prop_dict:
            return self._prop_dict["renewalThresholdPercentage"]
        else:
            return None

    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self, val):
        self._prop_dict["renewalThresholdPercentage"] = val

    @property
    def certificate_validity_period_value(self):
        """Gets and sets the certificateValidityPeriodValue
        
        Returns: 
            int:
                The certificateValidityPeriodValue
        """
        if "certificateValidityPeriodValue" in self._prop_dict:
            return self._prop_dict["certificateValidityPeriodValue"]
        else:
            return None

    @certificate_validity_period_value.setter
    def certificate_validity_period_value(self, val):
        self._prop_dict["certificateValidityPeriodValue"] = val

    @property
    def certificate_validity_period_scale(self):
        """
        Gets and sets the certificateValidityPeriodScale
        
        Returns: 
            :class:`CertificateValidityPeriodScale<onedrivesdk.model.certificate_validity_period_scale.CertificateValidityPeriodScale>`:
                The certificateValidityPeriodScale
        """
        if "certificateValidityPeriodScale" in self._prop_dict:
            if isinstance(self._prop_dict["certificateValidityPeriodScale"], OneDriveObjectBase):
                return self._prop_dict["certificateValidityPeriodScale"]
            else :
                self._prop_dict["certificateValidityPeriodScale"] = CertificateValidityPeriodScale(self._prop_dict["certificateValidityPeriodScale"])
                return self._prop_dict["certificateValidityPeriodScale"]

        return None

    @certificate_validity_period_scale.setter
    def certificate_validity_period_scale(self, val):
        self._prop_dict["certificateValidityPeriodScale"] = val
