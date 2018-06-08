# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PublicationFacet(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def level(self):
        """Gets and sets the level
        
        Returns: 
            str:
                The level
        """
        if "level" in self._prop_dict:
            return self._prop_dict["level"]
        else:
            return None

    @level.setter
    def level(self, val):
        self._prop_dict["level"] = val

    @property
    def version_id(self):
        """Gets and sets the versionId
        
        Returns: 
            str:
                The versionId
        """
        if "versionId" in self._prop_dict:
            return self._prop_dict["versionId"]
        else:
            return None

    @version_id.setter
    def version_id(self, val):
        self._prop_dict["versionId"] = val

