# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookFormatProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def formula_hidden(self):
        """
        Gets and sets the formulaHidden
        
        Returns:
            bool:
                The formulaHidden
        """
        if "formulaHidden" in self._prop_dict:
            return self._prop_dict["formulaHidden"]
        else:
            return None

    @formula_hidden.setter
    def formula_hidden(self, val):
        self._prop_dict["formulaHidden"] = val

    @property
    def locked(self):
        """
        Gets and sets the locked
        
        Returns:
            bool:
                The locked
        """
        if "locked" in self._prop_dict:
            return self._prop_dict["locked"]
        else:
            return None

    @locked.setter
    def locked(self, val):
        self._prop_dict["locked"] = val

