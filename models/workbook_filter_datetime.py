# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookFilterDatetime(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def date(self):
        """Gets and sets the date
        
        Returns: 
            str:
                The date
        """
        if "date" in self._prop_dict:
            return self._prop_dict["date"]
        else:
            return None

    @date.setter
    def date(self, val):
        self._prop_dict["date"] = val

    @property
    def specificity(self):
        """Gets and sets the specificity
        
        Returns: 
            str:
                The specificity
        """
        if "specificity" in self._prop_dict:
            return self._prop_dict["specificity"]
        else:
            return None

    @specificity.setter
    def specificity(self, val):
        self._prop_dict["specificity"] = val

