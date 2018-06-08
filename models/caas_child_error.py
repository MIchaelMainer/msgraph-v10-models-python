# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class CaasChildError(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def code(self):
        """Gets and sets the code
        
        Returns: 
            str:
                The code
        """
        if "code" in self._prop_dict:
            return self._prop_dict["code"]
        else:
            return None

    @code.setter
    def code(self, val):
        self._prop_dict["code"] = val

    @property
    def message(self):
        """Gets and sets the message
        
        Returns: 
            str:
                The message
        """
        if "message" in self._prop_dict:
            return self._prop_dict["message"]
        else:
            return None

    @message.setter
    def message(self, val):
        self._prop_dict["message"] = val

    @property
    def target(self):
        """Gets and sets the target
        
        Returns: 
            str:
                The target
        """
        if "target" in self._prop_dict:
            return self._prop_dict["target"]
        else:
            return None

    @target.setter
    def target(self, val):
        self._prop_dict["target"] = val

