# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class RoleSuccessStatistics(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def role_id(self):
        """Gets and sets the roleId
        
        Returns: 
            str:
                The roleId
        """
        if "roleId" in self._prop_dict:
            return self._prop_dict["roleId"]
        else:
            return None

    @role_id.setter
    def role_id(self, val):
        self._prop_dict["roleId"] = val

    @property
    def role_name(self):
        """Gets and sets the roleName
        
        Returns: 
            str:
                The roleName
        """
        if "roleName" in self._prop_dict:
            return self._prop_dict["roleName"]
        else:
            return None

    @role_name.setter
    def role_name(self, val):
        self._prop_dict["roleName"] = val

    @property
    def temporary_success(self):
        """Gets and sets the temporarySuccess
        
        Returns: 
            int:
                The temporarySuccess
        """
        if "temporarySuccess" in self._prop_dict:
            return self._prop_dict["temporarySuccess"]
        else:
            return None

    @temporary_success.setter
    def temporary_success(self, val):
        self._prop_dict["temporarySuccess"] = val

    @property
    def temporary_fail(self):
        """Gets and sets the temporaryFail
        
        Returns: 
            int:
                The temporaryFail
        """
        if "temporaryFail" in self._prop_dict:
            return self._prop_dict["temporaryFail"]
        else:
            return None

    @temporary_fail.setter
    def temporary_fail(self, val):
        self._prop_dict["temporaryFail"] = val

    @property
    def permanent_success(self):
        """Gets and sets the permanentSuccess
        
        Returns: 
            int:
                The permanentSuccess
        """
        if "permanentSuccess" in self._prop_dict:
            return self._prop_dict["permanentSuccess"]
        else:
            return None

    @permanent_success.setter
    def permanent_success(self, val):
        self._prop_dict["permanentSuccess"] = val

    @property
    def permanent_fail(self):
        """Gets and sets the permanentFail
        
        Returns: 
            int:
                The permanentFail
        """
        if "permanentFail" in self._prop_dict:
            return self._prop_dict["permanentFail"]
        else:
            return None

    @permanent_fail.setter
    def permanent_fail(self, val):
        self._prop_dict["permanentFail"] = val

    @property
    def remove_success(self):
        """Gets and sets the removeSuccess
        
        Returns: 
            int:
                The removeSuccess
        """
        if "removeSuccess" in self._prop_dict:
            return self._prop_dict["removeSuccess"]
        else:
            return None

    @remove_success.setter
    def remove_success(self, val):
        self._prop_dict["removeSuccess"] = val

    @property
    def remove_fail(self):
        """Gets and sets the removeFail
        
        Returns: 
            int:
                The removeFail
        """
        if "removeFail" in self._prop_dict:
            return self._prop_dict["removeFail"]
        else:
            return None

    @remove_fail.setter
    def remove_fail(self, val):
        self._prop_dict["removeFail"] = val

    @property
    def unknown_fail(self):
        """Gets and sets the unknownFail
        
        Returns: 
            int:
                The unknownFail
        """
        if "unknownFail" in self._prop_dict:
            return self._prop_dict["unknownFail"]
        else:
            return None

    @unknown_fail.setter
    def unknown_fail(self, val):
        self._prop_dict["unknownFail"] = val

