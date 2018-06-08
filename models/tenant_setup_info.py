# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.setup_status import SetupStatus
from ..model.privileged_role_settings import PrivilegedRoleSettings
from ..one_drive_object_base import OneDriveObjectBase


class TenantSetupInfo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_roles_actions(self):
        """
        Gets and sets the userRolesActions
        
        Returns:
            str:
                The userRolesActions
        """
        if "userRolesActions" in self._prop_dict:
            return self._prop_dict["userRolesActions"]
        else:
            return None

    @user_roles_actions.setter
    def user_roles_actions(self, val):
        self._prop_dict["userRolesActions"] = val

    @property
    def first_time_setup(self):
        """
        Gets and sets the firstTimeSetup
        
        Returns:
            bool:
                The firstTimeSetup
        """
        if "firstTimeSetup" in self._prop_dict:
            return self._prop_dict["firstTimeSetup"]
        else:
            return None

    @first_time_setup.setter
    def first_time_setup(self, val):
        self._prop_dict["firstTimeSetup"] = val

    @property
    def relevant_roles_settings(self):
        """
        Gets and sets the relevantRolesSettings
        
        Returns:
            str:
                The relevantRolesSettings
        """
        if "relevantRolesSettings" in self._prop_dict:
            return self._prop_dict["relevantRolesSettings"]
        else:
            return None

    @relevant_roles_settings.setter
    def relevant_roles_settings(self, val):
        self._prop_dict["relevantRolesSettings"] = val

    @property
    def skip_setup(self):
        """
        Gets and sets the skipSetup
        
        Returns:
            bool:
                The skipSetup
        """
        if "skipSetup" in self._prop_dict:
            return self._prop_dict["skipSetup"]
        else:
            return None

    @skip_setup.setter
    def skip_setup(self, val):
        self._prop_dict["skipSetup"] = val

    @property
    def setup_status(self):
        """
        Gets and sets the setupStatus
        
        Returns: 
            :class:`SetupStatus<onedrivesdk.model.setup_status.SetupStatus>`:
                The setupStatus
        """
        if "setupStatus" in self._prop_dict:
            if isinstance(self._prop_dict["setupStatus"], OneDriveObjectBase):
                return self._prop_dict["setupStatus"]
            else :
                self._prop_dict["setupStatus"] = SetupStatus(self._prop_dict["setupStatus"])
                return self._prop_dict["setupStatus"]

        return None

    @setup_status.setter
    def setup_status(self, val):
        self._prop_dict["setupStatus"] = val

    @property
    def default_roles_settings(self):
        """
        Gets and sets the defaultRolesSettings
        
        Returns: 
            :class:`PrivilegedRoleSettings<onedrivesdk.model.privileged_role_settings.PrivilegedRoleSettings>`:
                The defaultRolesSettings
        """
        if "defaultRolesSettings" in self._prop_dict:
            if isinstance(self._prop_dict["defaultRolesSettings"], OneDriveObjectBase):
                return self._prop_dict["defaultRolesSettings"]
            else :
                self._prop_dict["defaultRolesSettings"] = PrivilegedRoleSettings(self._prop_dict["defaultRolesSettings"])
                return self._prop_dict["defaultRolesSettings"]

        return None

    @default_roles_settings.setter
    def default_roles_settings(self, val):
        self._prop_dict["defaultRolesSettings"] = val

