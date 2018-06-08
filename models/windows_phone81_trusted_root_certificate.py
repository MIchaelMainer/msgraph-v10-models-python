# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhone81TrustedRootCertificate(OneDriveObjectBase):

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

