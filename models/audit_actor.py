# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AuditActor(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def user_permissions(self):
        """Gets and sets the userPermissions
        
        Returns: 
            str:
                The userPermissions
        """
        if "userPermissions" in self._prop_dict:
            return self._prop_dict["userPermissions"]
        else:
            return None

    @user_permissions.setter
    def user_permissions(self, val):
        self._prop_dict["userPermissions"] = val

    @property
    def application_id(self):
        """Gets and sets the applicationId
        
        Returns: 
            str:
                The applicationId
        """
        if "applicationId" in self._prop_dict:
            return self._prop_dict["applicationId"]
        else:
            return None

    @application_id.setter
    def application_id(self, val):
        self._prop_dict["applicationId"] = val

    @property
    def application_display_name(self):
        """Gets and sets the applicationDisplayName
        
        Returns: 
            str:
                The applicationDisplayName
        """
        if "applicationDisplayName" in self._prop_dict:
            return self._prop_dict["applicationDisplayName"]
        else:
            return None

    @application_display_name.setter
    def application_display_name(self, val):
        self._prop_dict["applicationDisplayName"] = val

    @property
    def user_principal_name(self):
        """Gets and sets the userPrincipalName
        
        Returns: 
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def service_principal_name(self):
        """Gets and sets the servicePrincipalName
        
        Returns: 
            str:
                The servicePrincipalName
        """
        if "servicePrincipalName" in self._prop_dict:
            return self._prop_dict["servicePrincipalName"]
        else:
            return None

    @service_principal_name.setter
    def service_principal_name(self, val):
        self._prop_dict["servicePrincipalName"] = val

    @property
    def ip_address(self):
        """Gets and sets the ipAddress
        
        Returns: 
            str:
                The ipAddress
        """
        if "ipAddress" in self._prop_dict:
            return self._prop_dict["ipAddress"]
        else:
            return None

    @ip_address.setter
    def ip_address(self, val):
        self._prop_dict["ipAddress"] = val

    @property
    def user_id(self):
        """Gets and sets the userId
        
        Returns: 
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

