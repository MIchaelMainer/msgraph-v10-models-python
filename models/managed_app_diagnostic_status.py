# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppDiagnosticStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def validation_name(self):
        """Gets and sets the validationName
        
        Returns: 
            str:
                The validationName
        """
        if "validationName" in self._prop_dict:
            return self._prop_dict["validationName"]
        else:
            return None

    @validation_name.setter
    def validation_name(self, val):
        self._prop_dict["validationName"] = val

    @property
    def state(self):
        """Gets and sets the state
        
        Returns: 
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def mitigation_instruction(self):
        """Gets and sets the mitigationInstruction
        
        Returns: 
            str:
                The mitigationInstruction
        """
        if "mitigationInstruction" in self._prop_dict:
            return self._prop_dict["mitigationInstruction"]
        else:
            return None

    @mitigation_instruction.setter
    def mitigation_instruction(self, val):
        self._prop_dict["mitigationInstruction"] = val

