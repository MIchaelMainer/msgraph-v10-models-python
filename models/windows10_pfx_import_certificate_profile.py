# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_storage_provider_option import KeyStorageProviderOption
from ..one_drive_object_base import OneDriveObjectBase


class Windows10PFXImportCertificateProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

