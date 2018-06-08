# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ResourceOperation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource_name(self):
        """
        Gets and sets the resourceName
        
        Returns:
            str:
                The resourceName
        """
        if "resourceName" in self._prop_dict:
            return self._prop_dict["resourceName"]
        else:
            return None

    @resource_name.setter
    def resource_name(self, val):
        self._prop_dict["resourceName"] = val

    @property
    def action_name(self):
        """
        Gets and sets the actionName
        
        Returns:
            str:
                The actionName
        """
        if "actionName" in self._prop_dict:
            return self._prop_dict["actionName"]
        else:
            return None

    @action_name.setter
    def action_name(self, val):
        self._prop_dict["actionName"] = val

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

