# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.message_rule_predicates import MessageRulePredicates
from ..model.message_rule_actions import MessageRuleActions
from ..one_drive_object_base import OneDriveObjectBase


class MessageRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def sequence(self):
        """
        Gets and sets the sequence
        
        Returns:
            int:
                The sequence
        """
        if "sequence" in self._prop_dict:
            return self._prop_dict["sequence"]
        else:
            return None

    @sequence.setter
    def sequence(self, val):
        self._prop_dict["sequence"] = val

    @property
    def conditions(self):
        """
        Gets and sets the conditions
        
        Returns: 
            :class:`MessageRulePredicates<onedrivesdk.model.message_rule_predicates.MessageRulePredicates>`:
                The conditions
        """
        if "conditions" in self._prop_dict:
            if isinstance(self._prop_dict["conditions"], OneDriveObjectBase):
                return self._prop_dict["conditions"]
            else :
                self._prop_dict["conditions"] = MessageRulePredicates(self._prop_dict["conditions"])
                return self._prop_dict["conditions"]

        return None

    @conditions.setter
    def conditions(self, val):
        self._prop_dict["conditions"] = val

    @property
    def actions(self):
        """
        Gets and sets the actions
        
        Returns: 
            :class:`MessageRuleActions<onedrivesdk.model.message_rule_actions.MessageRuleActions>`:
                The actions
        """
        if "actions" in self._prop_dict:
            if isinstance(self._prop_dict["actions"], OneDriveObjectBase):
                return self._prop_dict["actions"]
            else :
                self._prop_dict["actions"] = MessageRuleActions(self._prop_dict["actions"])
                return self._prop_dict["actions"]

        return None

    @actions.setter
    def actions(self, val):
        self._prop_dict["actions"] = val

    @property
    def exceptions(self):
        """
        Gets and sets the exceptions
        
        Returns: 
            :class:`MessageRulePredicates<onedrivesdk.model.message_rule_predicates.MessageRulePredicates>`:
                The exceptions
        """
        if "exceptions" in self._prop_dict:
            if isinstance(self._prop_dict["exceptions"], OneDriveObjectBase):
                return self._prop_dict["exceptions"]
            else :
                self._prop_dict["exceptions"] = MessageRulePredicates(self._prop_dict["exceptions"])
                return self._prop_dict["exceptions"]

        return None

    @exceptions.setter
    def exceptions(self, val):
        self._prop_dict["exceptions"] = val

    @property
    def is_enabled(self):
        """
        Gets and sets the isEnabled
        
        Returns:
            bool:
                The isEnabled
        """
        if "isEnabled" in self._prop_dict:
            return self._prop_dict["isEnabled"]
        else:
            return None

    @is_enabled.setter
    def is_enabled(self, val):
        self._prop_dict["isEnabled"] = val

    @property
    def has_error(self):
        """
        Gets and sets the hasError
        
        Returns:
            bool:
                The hasError
        """
        if "hasError" in self._prop_dict:
            return self._prop_dict["hasError"]
        else:
            return None

    @has_error.setter
    def has_error(self, val):
        self._prop_dict["hasError"] = val

    @property
    def is_read_only(self):
        """
        Gets and sets the isReadOnly
        
        Returns:
            bool:
                The isReadOnly
        """
        if "isReadOnly" in self._prop_dict:
            return self._prop_dict["isReadOnly"]
        else:
            return None

    @is_read_only.setter
    def is_read_only(self, val):
        self._prop_dict["isReadOnly"] = val

