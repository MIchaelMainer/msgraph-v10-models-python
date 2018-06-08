# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidMobileAppIdentifier(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def package_id(self):
        """Gets and sets the packageId
        
        Returns: 
            str:
                The packageId
        """
        if "packageId" in self._prop_dict:
            return self._prop_dict["packageId"]
        else:
            return None

    @package_id.setter
    def package_id(self, val):
        self._prop_dict["packageId"] = val

