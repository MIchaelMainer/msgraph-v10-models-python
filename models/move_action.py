# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MoveAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def from(self):
        """Gets and sets the from
        
        Returns: 
            str:
                The from
        """
        if "from" in self._prop_dict:
            return self._prop_dict["from"]
        else:
            return None

    @from.setter
    def from(self, val):
        self._prop_dict["from"] = val

    @property
    def to(self):
        """Gets and sets the to
        
        Returns: 
            str:
                The to
        """
        if "to" in self._prop_dict:
            return self._prop_dict["to"]
        else:
            return None

    @to.setter
    def to(self, val):
        self._prop_dict["to"] = val

