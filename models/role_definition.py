# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.role_permission import RolePermission
from ..model.role_assignment import RoleAssignment
from ..one_drive_object_base import OneDriveObjectBase


class RoleDefinition(OneDriveObjectBase):

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
    def permissions(self):
        """Gets and sets the permissions
        
        Returns: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The permissions
        """
        if "permissions" in self._prop_dict:
            return PermissionsCollectionPage(self._prop_dict["permissions"])
        else:
            return None

    @property
    def role_permissions(self):
        """Gets and sets the rolePermissions
        
        Returns: 
            :class:`RolePermissionsCollectionPage<onedrivesdk.request.role_permissions_collection.RolePermissionsCollectionPage>`:
                The rolePermissions
        """
        if "rolePermissions" in self._prop_dict:
            return RolePermissionsCollectionPage(self._prop_dict["rolePermissions"])
        else:
            return None

    @property
    def is_built_in_role_definition(self):
        """
        Gets and sets the isBuiltInRoleDefinition
        
        Returns:
            bool:
                The isBuiltInRoleDefinition
        """
        if "isBuiltInRoleDefinition" in self._prop_dict:
            return self._prop_dict["isBuiltInRoleDefinition"]
        else:
            return None

    @is_built_in_role_definition.setter
    def is_built_in_role_definition(self, val):
        self._prop_dict["isBuiltInRoleDefinition"] = val

    @property
    def is_built_in(self):
        """
        Gets and sets the isBuiltIn
        
        Returns:
            bool:
                The isBuiltIn
        """
        if "isBuiltIn" in self._prop_dict:
            return self._prop_dict["isBuiltIn"]
        else:
            return None

    @is_built_in.setter
    def is_built_in(self, val):
        self._prop_dict["isBuiltIn"] = val

    @property
    def role_assignments(self):
        """Gets and sets the roleAssignments
        
        Returns: 
            :class:`RoleAssignmentsCollectionPage<onedrivesdk.request.role_assignments_collection.RoleAssignmentsCollectionPage>`:
                The roleAssignments
        """
        if "roleAssignments" in self._prop_dict:
            return RoleAssignmentsCollectionPage(self._prop_dict["roleAssignments"])
        else:
            return None

