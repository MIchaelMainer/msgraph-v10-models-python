# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.filter_operand import FilterOperand
from ..one_drive_object_base import OneDriveObjectBase


class FilterClause(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def operator_name(self):
        """Gets and sets the operatorName
        
        Returns: 
            str:
                The operatorName
        """
        if "operatorName" in self._prop_dict:
            return self._prop_dict["operatorName"]
        else:
            return None

    @operator_name.setter
    def operator_name(self, val):
        self._prop_dict["operatorName"] = val

    @property
    def source_operand_name(self):
        """Gets and sets the sourceOperandName
        
        Returns: 
            str:
                The sourceOperandName
        """
        if "sourceOperandName" in self._prop_dict:
            return self._prop_dict["sourceOperandName"]
        else:
            return None

    @source_operand_name.setter
    def source_operand_name(self, val):
        self._prop_dict["sourceOperandName"] = val

    @property
    def target_operand(self):
        """
        Gets and sets the targetOperand
        
        Returns: 
            :class:`FilterOperand<onedrivesdk.model.filter_operand.FilterOperand>`:
                The targetOperand
        """
        if "targetOperand" in self._prop_dict:
            if isinstance(self._prop_dict["targetOperand"], OneDriveObjectBase):
                return self._prop_dict["targetOperand"]
            else :
                self._prop_dict["targetOperand"] = FilterOperand(self._prop_dict["targetOperand"])
                return self._prop_dict["targetOperand"]

        return None

    @target_operand.setter
    def target_operand(self, val):
        self._prop_dict["targetOperand"] = val
