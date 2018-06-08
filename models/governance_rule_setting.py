# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceRuleSetting(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def rule_identifier(self):
        """Gets and sets the ruleIdentifier
        
        Returns: 
            str:
                The ruleIdentifier
        """
        if "ruleIdentifier" in self._prop_dict:
            return self._prop_dict["ruleIdentifier"]
        else:
            return None

    @rule_identifier.setter
    def rule_identifier(self, val):
        self._prop_dict["ruleIdentifier"] = val

    @property
    def setting(self):
        """Gets and sets the setting
        
        Returns: 
            str:
                The setting
        """
        if "setting" in self._prop_dict:
            return self._prop_dict["setting"]
        else:
            return None

    @setting.setter
    def setting(self, val):
        self._prop_dict["setting"] = val

