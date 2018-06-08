# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.privileged_role_settings import PrivilegedRoleSettings
from ..model.privileged_role_assignment import PrivilegedRoleAssignment
from ..model.privileged_role_summary import PrivilegedRoleSummary
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedRole(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def settings(self):
        """
        Gets and sets the settings
        
        Returns: 
            :class:`PrivilegedRoleSettings<onedrivesdk.model.privileged_role_settings.PrivilegedRoleSettings>`:
                The settings
        """
        if "settings" in self._prop_dict:
            if isinstance(self._prop_dict["settings"], OneDriveObjectBase):
                return self._prop_dict["settings"]
            else :
                self._prop_dict["settings"] = PrivilegedRoleSettings(self._prop_dict["settings"])
                return self._prop_dict["settings"]

        return None

    @settings.setter
    def settings(self, val):
        self._prop_dict["settings"] = val

    @property
    def assignments(self):
        """Gets and sets the assignments
        
        Returns: 
            :class:`AssignmentsCollectionPage<onedrivesdk.request.assignments_collection.AssignmentsCollectionPage>`:
                The assignments
        """
        if "assignments" in self._prop_dict:
            return AssignmentsCollectionPage(self._prop_dict["assignments"])
        else:
            return None

    @property
    def summary(self):
        """
        Gets and sets the summary
        
        Returns: 
            :class:`PrivilegedRoleSummary<onedrivesdk.model.privileged_role_summary.PrivilegedRoleSummary>`:
                The summary
        """
        if "summary" in self._prop_dict:
            if isinstance(self._prop_dict["summary"], OneDriveObjectBase):
                return self._prop_dict["summary"]
            else :
                self._prop_dict["summary"] = PrivilegedRoleSummary(self._prop_dict["summary"])
                return self._prop_dict["summary"]

        return None

    @summary.setter
    def summary(self, val):
        self._prop_dict["summary"] = val

