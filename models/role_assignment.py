# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.role_assignment_scope_type import RoleAssignmentScopeType
from ..model.role_definition import RoleDefinition
from ..one_drive_object_base import OneDriveObjectBase


class RoleAssignment(OneDriveObjectBase):

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

    @property
    def scope_members(self):
        """
        Gets and sets the scopeMembers
        
        Returns:
            str:
                The scopeMembers
        """
        if "scopeMembers" in self._prop_dict:
            return self._prop_dict["scopeMembers"]
        else:
            return None

    @scope_members.setter
    def scope_members(self, val):
        self._prop_dict["scopeMembers"] = val

    @property
    def scope_type(self):
        """
        Gets and sets the scopeType
        
        Returns: 
            :class:`RoleAssignmentScopeType<onedrivesdk.model.role_assignment_scope_type.RoleAssignmentScopeType>`:
                The scopeType
        """
        if "scopeType" in self._prop_dict:
            if isinstance(self._prop_dict["scopeType"], OneDriveObjectBase):
                return self._prop_dict["scopeType"]
            else :
                self._prop_dict["scopeType"] = RoleAssignmentScopeType(self._prop_dict["scopeType"])
                return self._prop_dict["scopeType"]

        return None

    @scope_type.setter
    def scope_type(self, val):
        self._prop_dict["scopeType"] = val

    @property
    def resource_scopes(self):
        """
        Gets and sets the resourceScopes
        
        Returns:
            str:
                The resourceScopes
        """
        if "resourceScopes" in self._prop_dict:
            return self._prop_dict["resourceScopes"]
        else:
            return None

    @resource_scopes.setter
    def resource_scopes(self, val):
        self._prop_dict["resourceScopes"] = val

    @property
    def role_definition(self):
        """
        Gets and sets the roleDefinition
        
        Returns: 
            :class:`RoleDefinition<onedrivesdk.model.role_definition.RoleDefinition>`:
                The roleDefinition
        """
        if "roleDefinition" in self._prop_dict:
            if isinstance(self._prop_dict["roleDefinition"], OneDriveObjectBase):
                return self._prop_dict["roleDefinition"]
            else :
                self._prop_dict["roleDefinition"] = RoleDefinition(self._prop_dict["roleDefinition"])
                return self._prop_dict["roleDefinition"]

        return None

    @role_definition.setter
    def role_definition(self, val):
        self._prop_dict["roleDefinition"] = val

