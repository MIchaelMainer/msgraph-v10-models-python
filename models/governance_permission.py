# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class GovernancePermission(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def access_level(self):
        """Gets and sets the accessLevel
        
        Returns: 
            str:
                The accessLevel
        """
        if "accessLevel" in self._prop_dict:
            return self._prop_dict["accessLevel"]
        else:
            return None

    @access_level.setter
    def access_level(self, val):
        self._prop_dict["accessLevel"] = val

    @property
    def is_active(self):
        """Gets and sets the isActive
        
        Returns: 
            bool:
                The isActive
        """
        if "isActive" in self._prop_dict:
            return self._prop_dict["isActive"]
        else:
            return None

    @is_active.setter
    def is_active(self, val):
        self._prop_dict["isActive"] = val

    @property
    def is_eligible(self):
        """Gets and sets the isEligible
        
        Returns: 
            bool:
                The isEligible
        """
        if "isEligible" in self._prop_dict:
            return self._prop_dict["isEligible"]
        else:
            return None

    @is_eligible.setter
    def is_eligible(self, val):
        self._prop_dict["isEligible"] = val

