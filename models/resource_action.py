# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ResourceAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allowed_resource_actions(self):
        """Gets and sets the allowedResourceActions
        
        Returns: 
            str:
                The allowedResourceActions
        """
        if "allowedResourceActions" in self._prop_dict:
            return self._prop_dict["allowedResourceActions"]
        else:
            return None

    @allowed_resource_actions.setter
    def allowed_resource_actions(self, val):
        self._prop_dict["allowedResourceActions"] = val

    @property
    def not_allowed_resource_actions(self):
        """Gets and sets the notAllowedResourceActions
        
        Returns: 
            str:
                The notAllowedResourceActions
        """
        if "notAllowedResourceActions" in self._prop_dict:
            return self._prop_dict["notAllowedResourceActions"]
        else:
            return None

    @not_allowed_resource_actions.setter
    def not_allowed_resource_actions(self, val):
        self._prop_dict["notAllowedResourceActions"] = val

