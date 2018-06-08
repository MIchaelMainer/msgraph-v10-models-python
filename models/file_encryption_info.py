# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class FileEncryptionInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def profile_identifier(self):
        """Gets and sets the profileIdentifier
        
        Returns: 
            str:
                The profileIdentifier
        """
        if "profileIdentifier" in self._prop_dict:
            return self._prop_dict["profileIdentifier"]
        else:
            return None

    @profile_identifier.setter
    def profile_identifier(self, val):
        self._prop_dict["profileIdentifier"] = val

    @property
    def file_digest_algorithm(self):
        """Gets and sets the fileDigestAlgorithm
        
        Returns: 
            str:
                The fileDigestAlgorithm
        """
        if "fileDigestAlgorithm" in self._prop_dict:
            return self._prop_dict["fileDigestAlgorithm"]
        else:
            return None

    @file_digest_algorithm.setter
    def file_digest_algorithm(self, val):
        self._prop_dict["fileDigestAlgorithm"] = val

