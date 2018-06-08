# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.intended_purpose import IntendedPurpose
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhone81ImportedPFXCertificateProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def intended_purpose(self):
        """
        Gets and sets the intendedPurpose
        
        Returns: 
            :class:`IntendedPurpose<onedrivesdk.model.intended_purpose.IntendedPurpose>`:
                The intendedPurpose
        """
        if "intendedPurpose" in self._prop_dict:
            if isinstance(self._prop_dict["intendedPurpose"], OneDriveObjectBase):
                return self._prop_dict["intendedPurpose"]
            else :
                self._prop_dict["intendedPurpose"] = IntendedPurpose(self._prop_dict["intendedPurpose"])
                return self._prop_dict["intendedPurpose"]

        return None

    @intended_purpose.setter
    def intended_purpose(self, val):
        self._prop_dict["intendedPurpose"] = val

