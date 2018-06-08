# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class OmaSettingDateTime(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def value(self):
        """Gets and sets the value
        
        Returns: 
            datetime:
                The value
        """
        if "value" in self._prop_dict:
            return datetime.strptime(self._prop_dict["value"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val.isoformat()+"Z"

