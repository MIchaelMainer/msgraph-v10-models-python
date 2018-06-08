# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class WindowsAssignedAccessProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def profile_name(self):
        """
        Gets and sets the profileName
        
        Returns:
            str:
                The profileName
        """
        if "profileName" in self._prop_dict:
            return self._prop_dict["profileName"]
        else:
            return None

    @profile_name.setter
    def profile_name(self, val):
        self._prop_dict["profileName"] = val

    @property
    def show_task_bar(self):
        """
        Gets and sets the showTaskBar
        
        Returns:
            bool:
                The showTaskBar
        """
        if "showTaskBar" in self._prop_dict:
            return self._prop_dict["showTaskBar"]
        else:
            return None

    @show_task_bar.setter
    def show_task_bar(self, val):
        self._prop_dict["showTaskBar"] = val

    @property
    def app_user_model_ids(self):
        """
        Gets and sets the appUserModelIds
        
        Returns:
            str:
                The appUserModelIds
        """
        if "appUserModelIds" in self._prop_dict:
            return self._prop_dict["appUserModelIds"]
        else:
            return None

    @app_user_model_ids.setter
    def app_user_model_ids(self, val):
        self._prop_dict["appUserModelIds"] = val

    @property
    def desktop_app_paths(self):
        """
        Gets and sets the desktopAppPaths
        
        Returns:
            str:
                The desktopAppPaths
        """
        if "desktopAppPaths" in self._prop_dict:
            return self._prop_dict["desktopAppPaths"]
        else:
            return None

    @desktop_app_paths.setter
    def desktop_app_paths(self, val):
        self._prop_dict["desktopAppPaths"] = val

    @property
    def user_accounts(self):
        """
        Gets and sets the userAccounts
        
        Returns:
            str:
                The userAccounts
        """
        if "userAccounts" in self._prop_dict:
            return self._prop_dict["userAccounts"]
        else:
            return None

    @user_accounts.setter
    def user_accounts(self, val):
        self._prop_dict["userAccounts"] = val

