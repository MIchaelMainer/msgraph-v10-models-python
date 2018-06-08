# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class CalculatedColumn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def format(self):
        """Gets and sets the format
        
        Returns: 
            str:
                The format
        """
        if "format" in self._prop_dict:
            return self._prop_dict["format"]
        else:
            return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

    @property
    def formula(self):
        """Gets and sets the formula
        
        Returns: 
            str:
                The formula
        """
        if "formula" in self._prop_dict:
            return self._prop_dict["formula"]
        else:
            return None

    @formula.setter
    def formula(self, val):
        self._prop_dict["formula"] = val

    @property
    def output_type(self):
        """Gets and sets the outputType
        
        Returns: 
            str:
                The outputType
        """
        if "outputType" in self._prop_dict:
            return self._prop_dict["outputType"]
        else:
            return None

    @output_type.setter
    def output_type(self, val):
        self._prop_dict["outputType"] = val

