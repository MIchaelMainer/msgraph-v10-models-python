# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.certificate_destination_store import CertificateDestinationStore
from ..one_drive_object_base import OneDriveObjectBase


class Windows81TrustedRootCertificate(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def cert_file_name(self):
        """
        Gets and sets the certFileName
        
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
    def destination_store(self):
        """
        Gets and sets the destinationStore
        
        Returns: 
            :class:`CertificateDestinationStore<onedrivesdk.model.certificate_destination_store.CertificateDestinationStore>`:
                The destinationStore
        """
        if "destinationStore" in self._prop_dict:
            if isinstance(self._prop_dict["destinationStore"], OneDriveObjectBase):
                return self._prop_dict["destinationStore"]
            else :
                self._prop_dict["destinationStore"] = CertificateDestinationStore(self._prop_dict["destinationStore"])
                return self._prop_dict["destinationStore"]

        return None

    @destination_store.setter
    def destination_store(self, val):
        self._prop_dict["destinationStore"] = val

