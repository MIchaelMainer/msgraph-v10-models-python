# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.extension import Extension
from ..model.directory_object import DirectoryObject
from ..model.scoped_role_membership import ScopedRoleMembership
from ..one_drive_object_base import OneDriveObjectBase


class AdministrativeUnit(OneDriveObjectBase):

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
    def visibility(self):
        """
        Gets and sets the visibility
        
        Returns:
            str:
                The visibility
        """
        if "visibility" in self._prop_dict:
            return self._prop_dict["visibility"]
        else:
            return None

    @visibility.setter
    def visibility(self, val):
        self._prop_dict["visibility"] = val

    @property
    def extensions(self):
        """Gets and sets the extensions
        
        Returns: 
            :class:`ExtensionsCollectionPage<onedrivesdk.request.extensions_collection.ExtensionsCollectionPage>`:
                The extensions
        """
        if "extensions" in self._prop_dict:
            return ExtensionsCollectionPage(self._prop_dict["extensions"])
        else:
            return None

    @property
    def members(self):
        """Gets and sets the members
        
        Returns: 
            :class:`MembersCollectionPage<onedrivesdk.request.members_collection.MembersCollectionPage>`:
                The members
        """
        if "members" in self._prop_dict:
            return MembersCollectionPage(self._prop_dict["members"])
        else:
            return None

    @property
    def scoped_role_members(self):
        """Gets and sets the scopedRoleMembers
        
        Returns: 
            :class:`ScopedRoleMembersCollectionPage<onedrivesdk.request.scoped_role_members_collection.ScopedRoleMembersCollectionPage>`:
                The scopedRoleMembers
        """
        if "scopedRoleMembers" in self._prop_dict:
            return ScopedRoleMembersCollectionPage(self._prop_dict["scopedRoleMembers"])
        else:
            return None

