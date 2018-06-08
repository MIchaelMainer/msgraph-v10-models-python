# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_storage_provider_option import KeyStorageProviderOption
from ..model.subject_name_format import SubjectNameFormat
from ..model.subject_alternative_name_type import SubjectAlternativeNameType
from ..model.certificate_validity_period_scale import CertificateValidityPeriodScale
from ..model.extended_key_usage import ExtendedKeyUsage
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhone81CertificateProfileBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def renewal_threshold_percentage(self):
        """
        Gets and sets the renewalThresholdPercentage
        
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
    def key_storage_provider(self):
        """
        Gets and sets the keyStorageProvider
        
        Returns: 
            :class:`KeyStorageProviderOption<onedrivesdk.model.key_storage_provider_option.KeyStorageProviderOption>`:
                The keyStorageProvider
        """
        if "keyStorageProvider" in self._prop_dict:
            if isinstance(self._prop_dict["keyStorageProvider"], OneDriveObjectBase):
                return self._prop_dict["keyStorageProvider"]
            else :
                self._prop_dict["keyStorageProvider"] = KeyStorageProviderOption(self._prop_dict["keyStorageProvider"])
                return self._prop_dict["keyStorageProvider"]

        return None

    @key_storage_provider.setter
    def key_storage_provider(self, val):
        self._prop_dict["keyStorageProvider"] = val

    @property
    def subject_name_format(self):
        """
        Gets and sets the subjectNameFormat
        
        Returns: 
            :class:`SubjectNameFormat<onedrivesdk.model.subject_name_format.SubjectNameFormat>`:
                The subjectNameFormat
        """
        if "subjectNameFormat" in self._prop_dict:
            if isinstance(self._prop_dict["subjectNameFormat"], OneDriveObjectBase):
                return self._prop_dict["subjectNameFormat"]
            else :
                self._prop_dict["subjectNameFormat"] = SubjectNameFormat(self._prop_dict["subjectNameFormat"])
                return self._prop_dict["subjectNameFormat"]

        return None

    @subject_name_format.setter
    def subject_name_format(self, val):
        self._prop_dict["subjectNameFormat"] = val

    @property
    def subject_alternative_name_type(self):
        """
        Gets and sets the subjectAlternativeNameType
        
        Returns: 
            :class:`SubjectAlternativeNameType<onedrivesdk.model.subject_alternative_name_type.SubjectAlternativeNameType>`:
                The subjectAlternativeNameType
        """
        if "subjectAlternativeNameType" in self._prop_dict:
            if isinstance(self._prop_dict["subjectAlternativeNameType"], OneDriveObjectBase):
                return self._prop_dict["subjectAlternativeNameType"]
            else :
                self._prop_dict["subjectAlternativeNameType"] = SubjectAlternativeNameType(self._prop_dict["subjectAlternativeNameType"])
                return self._prop_dict["subjectAlternativeNameType"]

        return None

    @subject_alternative_name_type.setter
    def subject_alternative_name_type(self, val):
        self._prop_dict["subjectAlternativeNameType"] = val

    @property
    def certificate_validity_period_value(self):
        """
        Gets and sets the certificateValidityPeriodValue
        
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

    @property
    def extended_key_usages(self):
        """Gets and sets the extendedKeyUsages
        
        Returns: 
            :class:`ExtendedKeyUsagesCollectionPage<onedrivesdk.request.extended_key_usages_collection.ExtendedKeyUsagesCollectionPage>`:
                The extendedKeyUsages
        """
        if "extendedKeyUsages" in self._prop_dict:
            return ExtendedKeyUsagesCollectionPage(self._prop_dict["extendedKeyUsages"])
        else:
            return None

