# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_usages import KeyUsages
from ..model.key_size import KeySize
from ..model.hash_algorithms import HashAlgorithms
from ..model.certificate_store import CertificateStore
from ..model.windows81_trusted_root_certificate import Windows81TrustedRootCertificate
from ..model.managed_device_certificate_state import ManagedDeviceCertificateState
from ..one_drive_object_base import OneDriveObjectBase


class Windows81SCEPCertificateProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def scep_server_urls(self):
        """
        Gets and sets the scepServerUrls
        
        Returns:
            str:
                The scepServerUrls
        """
        if "scepServerUrls" in self._prop_dict:
            return self._prop_dict["scepServerUrls"]
        else:
            return None

    @scep_server_urls.setter
    def scep_server_urls(self, val):
        self._prop_dict["scepServerUrls"] = val

    @property
    def subject_name_format_string(self):
        """
        Gets and sets the subjectNameFormatString
        
        Returns:
            str:
                The subjectNameFormatString
        """
        if "subjectNameFormatString" in self._prop_dict:
            return self._prop_dict["subjectNameFormatString"]
        else:
            return None

    @subject_name_format_string.setter
    def subject_name_format_string(self, val):
        self._prop_dict["subjectNameFormatString"] = val

    @property
    def key_usage(self):
        """
        Gets and sets the keyUsage
        
        Returns: 
            :class:`KeyUsages<onedrivesdk.model.key_usages.KeyUsages>`:
                The keyUsage
        """
        if "keyUsage" in self._prop_dict:
            if isinstance(self._prop_dict["keyUsage"], OneDriveObjectBase):
                return self._prop_dict["keyUsage"]
            else :
                self._prop_dict["keyUsage"] = KeyUsages(self._prop_dict["keyUsage"])
                return self._prop_dict["keyUsage"]

        return None

    @key_usage.setter
    def key_usage(self, val):
        self._prop_dict["keyUsage"] = val

    @property
    def key_size(self):
        """
        Gets and sets the keySize
        
        Returns: 
            :class:`KeySize<onedrivesdk.model.key_size.KeySize>`:
                The keySize
        """
        if "keySize" in self._prop_dict:
            if isinstance(self._prop_dict["keySize"], OneDriveObjectBase):
                return self._prop_dict["keySize"]
            else :
                self._prop_dict["keySize"] = KeySize(self._prop_dict["keySize"])
                return self._prop_dict["keySize"]

        return None

    @key_size.setter
    def key_size(self, val):
        self._prop_dict["keySize"] = val

    @property
    def hash_algorithm(self):
        """
        Gets and sets the hashAlgorithm
        
        Returns: 
            :class:`HashAlgorithms<onedrivesdk.model.hash_algorithms.HashAlgorithms>`:
                The hashAlgorithm
        """
        if "hashAlgorithm" in self._prop_dict:
            if isinstance(self._prop_dict["hashAlgorithm"], OneDriveObjectBase):
                return self._prop_dict["hashAlgorithm"]
            else :
                self._prop_dict["hashAlgorithm"] = HashAlgorithms(self._prop_dict["hashAlgorithm"])
                return self._prop_dict["hashAlgorithm"]

        return None

    @hash_algorithm.setter
    def hash_algorithm(self, val):
        self._prop_dict["hashAlgorithm"] = val

    @property
    def subject_alternative_name_format_string(self):
        """
        Gets and sets the subjectAlternativeNameFormatString
        
        Returns:
            str:
                The subjectAlternativeNameFormatString
        """
        if "subjectAlternativeNameFormatString" in self._prop_dict:
            return self._prop_dict["subjectAlternativeNameFormatString"]
        else:
            return None

    @subject_alternative_name_format_string.setter
    def subject_alternative_name_format_string(self, val):
        self._prop_dict["subjectAlternativeNameFormatString"] = val

    @property
    def certificate_store(self):
        """
        Gets and sets the certificateStore
        
        Returns: 
            :class:`CertificateStore<onedrivesdk.model.certificate_store.CertificateStore>`:
                The certificateStore
        """
        if "certificateStore" in self._prop_dict:
            if isinstance(self._prop_dict["certificateStore"], OneDriveObjectBase):
                return self._prop_dict["certificateStore"]
            else :
                self._prop_dict["certificateStore"] = CertificateStore(self._prop_dict["certificateStore"])
                return self._prop_dict["certificateStore"]

        return None

    @certificate_store.setter
    def certificate_store(self, val):
        self._prop_dict["certificateStore"] = val

    @property
    def root_certificate(self):
        """
        Gets and sets the rootCertificate
        
        Returns: 
            :class:`Windows81TrustedRootCertificate<onedrivesdk.model.windows81_trusted_root_certificate.Windows81TrustedRootCertificate>`:
                The rootCertificate
        """
        if "rootCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["rootCertificate"], OneDriveObjectBase):
                return self._prop_dict["rootCertificate"]
            else :
                self._prop_dict["rootCertificate"] = Windows81TrustedRootCertificate(self._prop_dict["rootCertificate"])
                return self._prop_dict["rootCertificate"]

        return None

    @root_certificate.setter
    def root_certificate(self, val):
        self._prop_dict["rootCertificate"] = val

    @property
    def managed_device_certificate_states(self):
        """Gets and sets the managedDeviceCertificateStates
        
        Returns: 
            :class:`ManagedDeviceCertificateStatesCollectionPage<onedrivesdk.request.managed_device_certificate_states_collection.ManagedDeviceCertificateStatesCollectionPage>`:
                The managedDeviceCertificateStates
        """
        if "managedDeviceCertificateStates" in self._prop_dict:
            return ManagedDeviceCertificateStatesCollectionPage(self._prop_dict["managedDeviceCertificateStates"])
        else:
            return None

