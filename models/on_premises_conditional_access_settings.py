# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class OnPremisesConditionalAccessSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def enabled(self):
        """
        Gets and sets the enabled
        
        Returns:
            bool:
                The enabled
        """
        if "enabled" in self._prop_dict:
            return self._prop_dict["enabled"]
        else:
            return None

    @enabled.setter
    def enabled(self, val):
        self._prop_dict["enabled"] = val

    @property
    def included_groups(self):
        """
        Gets and sets the includedGroups
        
        Returns:
            UUID:
                The includedGroups
        """
        if "includedGroups" in self._prop_dict:
            return self._prop_dict["includedGroups"]
        else:
            return None

    @included_groups.setter
    def included_groups(self, val):
        self._prop_dict["includedGroups"] = val

    @property
    def excluded_groups(self):
        """
        Gets and sets the excludedGroups
        
        Returns:
            UUID:
                The excludedGroups
        """
        if "excludedGroups" in self._prop_dict:
            return self._prop_dict["excludedGroups"]
        else:
            return None

    @excluded_groups.setter
    def excluded_groups(self, val):
        self._prop_dict["excludedGroups"] = val

    @property
    def override_default_rule(self):
        """
        Gets and sets the overrideDefaultRule
        
        Returns:
            bool:
                The overrideDefaultRule
        """
        if "overrideDefaultRule" in self._prop_dict:
            return self._prop_dict["overrideDefaultRule"]
        else:
            return None

    @override_default_rule.setter
    def override_default_rule(self, val):
        self._prop_dict["overrideDefaultRule"] = val

