# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_certificate_profile_base import IosCertificateProfileBase
from ..one_drive_object_base import OneDriveObjectBase


class IosVpnConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def identity_certificate(self):
        """
        Gets and sets the identityCertificate
        
        Returns: 
            :class:`IosCertificateProfileBase<onedrivesdk.model.ios_certificate_profile_base.IosCertificateProfileBase>`:
                The identityCertificate
        """
        if "identityCertificate" in self._prop_dict:
            if isinstance(self._prop_dict["identityCertificate"], OneDriveObjectBase):
                return self._prop_dict["identityCertificate"]
            else :
                self._prop_dict["identityCertificate"] = IosCertificateProfileBase(self._prop_dict["identityCertificate"])
                return self._prop_dict["identityCertificate"]

        return None

    @identity_certificate.setter
    def identity_certificate(self, val):
        self._prop_dict["identityCertificate"] = val

