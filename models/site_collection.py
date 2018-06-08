# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.root import Root
from ..one_drive_object_base import OneDriveObjectBase


class SiteCollection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def data_location_code(self):
        """Gets and sets the dataLocationCode
        
        Returns: 
            str:
                The dataLocationCode
        """
        if "dataLocationCode" in self._prop_dict:
            return self._prop_dict["dataLocationCode"]
        else:
            return None

    @data_location_code.setter
    def data_location_code(self, val):
        self._prop_dict["dataLocationCode"] = val

    @property
    def hostname(self):
        """Gets and sets the hostname
        
        Returns: 
            str:
                The hostname
        """
        if "hostname" in self._prop_dict:
            return self._prop_dict["hostname"]
        else:
            return None

    @hostname.setter
    def hostname(self, val):
        self._prop_dict["hostname"] = val

    @property
    def root(self):
        """
        Gets and sets the root
        
        Returns: 
            :class:`Root<onedrivesdk.model.root.Root>`:
                The root
        """
        if "root" in self._prop_dict:
            if isinstance(self._prop_dict["root"], OneDriveObjectBase):
                return self._prop_dict["root"]
            else :
                self._prop_dict["root"] = Root(self._prop_dict["root"])
                return self._prop_dict["root"]

        return None

    @root.setter
    def root(self, val):
        self._prop_dict["root"] = val
