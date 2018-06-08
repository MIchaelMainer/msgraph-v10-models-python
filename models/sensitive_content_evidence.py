# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SensitiveContentEvidence(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def match(self):
        """Gets and sets the match
        
        Returns: 
            str:
                The match
        """
        if "match" in self._prop_dict:
            return self._prop_dict["match"]
        else:
            return None

    @match.setter
    def match(self, val):
        self._prop_dict["match"] = val

    @property
    def offset(self):
        """Gets and sets the offset
        
        Returns: 
            int:
                The offset
        """
        if "offset" in self._prop_dict:
            return self._prop_dict["offset"]
        else:
            return None

    @offset.setter
    def offset(self, val):
        self._prop_dict["offset"] = val

    @property
    def length(self):
        """Gets and sets the length
        
        Returns: 
            int:
                The length
        """
        if "length" in self._prop_dict:
            return self._prop_dict["length"]
        else:
            return None

    @length.setter
    def length(self, val):
        self._prop_dict["length"] = val

