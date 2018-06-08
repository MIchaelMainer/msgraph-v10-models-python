# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DomainDnsCnameRecord(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def canonical_name(self):
        """
        Gets and sets the canonicalName
        
        Returns:
            str:
                The canonicalName
        """
        if "canonicalName" in self._prop_dict:
            return self._prop_dict["canonicalName"]
        else:
            return None

    @canonical_name.setter
    def canonical_name(self, val):
        self._prop_dict["canonicalName"] = val

