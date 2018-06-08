# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.field_value_set import FieldValueSet
from ..one_drive_object_base import OneDriveObjectBase


class ListItemVersion(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def fields(self):
        """
        Gets and sets the fields
        
        Returns: 
            :class:`FieldValueSet<onedrivesdk.model.field_value_set.FieldValueSet>`:
                The fields
        """
        if "fields" in self._prop_dict:
            if isinstance(self._prop_dict["fields"], OneDriveObjectBase):
                return self._prop_dict["fields"]
            else :
                self._prop_dict["fields"] = FieldValueSet(self._prop_dict["fields"])
                return self._prop_dict["fields"]

        return None

    @fields.setter
    def fields(self, val):
        self._prop_dict["fields"] = val

