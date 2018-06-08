# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MacOSLobChildApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bundle_id(self):
        """Gets and sets the bundleId
        
        Returns: 
            str:
                The bundleId
        """
        if "bundleId" in self._prop_dict:
            return self._prop_dict["bundleId"]
        else:
            return None

    @bundle_id.setter
    def bundle_id(self, val):
        self._prop_dict["bundleId"] = val

    @property
    def build_number(self):
        """Gets and sets the buildNumber
        
        Returns: 
            str:
                The buildNumber
        """
        if "buildNumber" in self._prop_dict:
            return self._prop_dict["buildNumber"]
        else:
            return None

    @build_number.setter
    def build_number(self, val):
        self._prop_dict["buildNumber"] = val

    @property
    def version_number(self):
        """Gets and sets the versionNumber
        
        Returns: 
            str:
                The versionNumber
        """
        if "versionNumber" in self._prop_dict:
            return self._prop_dict["versionNumber"]
        else:
            return None

    @version_number.setter
    def version_number(self, val):
        self._prop_dict["versionNumber"] = val

