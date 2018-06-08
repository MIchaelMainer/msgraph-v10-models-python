# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ExtensionProperty(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_display_name(self):
        """
        Gets and sets the appDisplayName
        
        Returns:
            str:
                The appDisplayName
        """
        if "appDisplayName" in self._prop_dict:
            return self._prop_dict["appDisplayName"]
        else:
            return None

    @app_display_name.setter
    def app_display_name(self, val):
        self._prop_dict["appDisplayName"] = val

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def data_type(self):
        """
        Gets and sets the dataType
        
        Returns:
            str:
                The dataType
        """
        if "dataType" in self._prop_dict:
            return self._prop_dict["dataType"]
        else:
            return None

    @data_type.setter
    def data_type(self, val):
        self._prop_dict["dataType"] = val

    @property
    def is_synced_from_on_premises(self):
        """
        Gets and sets the isSyncedFromOnPremises
        
        Returns:
            bool:
                The isSyncedFromOnPremises
        """
        if "isSyncedFromOnPremises" in self._prop_dict:
            return self._prop_dict["isSyncedFromOnPremises"]
        else:
            return None

    @is_synced_from_on_premises.setter
    def is_synced_from_on_premises(self, val):
        self._prop_dict["isSyncedFromOnPremises"] = val

    @property
    def target_objects(self):
        """
        Gets and sets the targetObjects
        
        Returns:
            str:
                The targetObjects
        """
        if "targetObjects" in self._prop_dict:
            return self._prop_dict["targetObjects"]
        else:
            return None

    @target_objects.setter
    def target_objects(self, val):
        self._prop_dict["targetObjects"] = val

