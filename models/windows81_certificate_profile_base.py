# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.extended_key_usage import ExtendedKeyUsage
from ..one_drive_object_base import OneDriveObjectBase


class Windows81CertificateProfileBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

