# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PersonType(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def class(self):
        """Gets and sets the class
        
        Returns: 
            str:
                The class
        """
        if "class" in self._prop_dict:
            return self._prop_dict["class"]
        else:
            return None

    @class.setter
    def class(self, val):
        self._prop_dict["class"] = val

    @property
    def subclass(self):
        """Gets and sets the subclass
        
        Returns: 
            str:
                The subclass
        """
        if "subclass" in self._prop_dict:
            return self._prop_dict["subclass"]
        else:
            return None

    @subclass.setter
    def subclass(self, val):
        self._prop_dict["subclass"] = val

