# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.byte import Byte
from ..one_drive_object_base import OneDriveObjectBase


class RgbColor(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def r(self):
        """
        Gets and sets the r
        
        Returns: 
            :class:`Byte<onedrivesdk.model.byte.Byte>`:
                The r
        """
        if "r" in self._prop_dict:
            if isinstance(self._prop_dict["r"], OneDriveObjectBase):
                return self._prop_dict["r"]
            else :
                self._prop_dict["r"] = Byte(self._prop_dict["r"])
                return self._prop_dict["r"]

        return None

    @r.setter
    def r(self, val):
        self._prop_dict["r"] = val
    @property
    def g(self):
        """
        Gets and sets the g
        
        Returns: 
            :class:`Byte<onedrivesdk.model.byte.Byte>`:
                The g
        """
        if "g" in self._prop_dict:
            if isinstance(self._prop_dict["g"], OneDriveObjectBase):
                return self._prop_dict["g"]
            else :
                self._prop_dict["g"] = Byte(self._prop_dict["g"])
                return self._prop_dict["g"]

        return None

    @g.setter
    def g(self, val):
        self._prop_dict["g"] = val
    @property
    def b(self):
        """
        Gets and sets the b
        
        Returns: 
            :class:`Byte<onedrivesdk.model.byte.Byte>`:
                The b
        """
        if "b" in self._prop_dict:
            if isinstance(self._prop_dict["b"], OneDriveObjectBase):
                return self._prop_dict["b"]
            else :
                self._prop_dict["b"] = Byte(self._prop_dict["b"])
                return self._prop_dict["b"]

        return None

    @b.setter
    def b(self, val):
        self._prop_dict["b"] = val
