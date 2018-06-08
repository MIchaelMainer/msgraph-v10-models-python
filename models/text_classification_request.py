# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class TextClassificationRequest(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def text(self):
        """
        Gets and sets the text
        
        Returns:
            str:
                The text
        """
        if "text" in self._prop_dict:
            return self._prop_dict["text"]
        else:
            return None

    @text.setter
    def text(self, val):
        self._prop_dict["text"] = val

    @property
    def sensitive_type_ids(self):
        """
        Gets and sets the sensitiveTypeIds
        
        Returns:
            str:
                The sensitiveTypeIds
        """
        if "sensitiveTypeIds" in self._prop_dict:
            return self._prop_dict["sensitiveTypeIds"]
        else:
            return None

    @sensitive_type_ids.setter
    def sensitive_type_ids(self, val):
        self._prop_dict["sensitiveTypeIds"] = val

