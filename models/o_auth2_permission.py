# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class OAuth2Permission(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def admin_consent_description(self):
        """Gets and sets the adminConsentDescription
        
        Returns: 
            str:
                The adminConsentDescription
        """
        if "adminConsentDescription" in self._prop_dict:
            return self._prop_dict["adminConsentDescription"]
        else:
            return None

    @admin_consent_description.setter
    def admin_consent_description(self, val):
        self._prop_dict["adminConsentDescription"] = val

    @property
    def admin_consent_display_name(self):
        """Gets and sets the adminConsentDisplayName
        
        Returns: 
            str:
                The adminConsentDisplayName
        """
        if "adminConsentDisplayName" in self._prop_dict:
            return self._prop_dict["adminConsentDisplayName"]
        else:
            return None

    @admin_consent_display_name.setter
    def admin_consent_display_name(self, val):
        self._prop_dict["adminConsentDisplayName"] = val

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            UUID:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def is_enabled(self):
        """Gets and sets the isEnabled
        
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
    def origin(self):
        """Gets and sets the origin
        
        Returns: 
            str:
                The origin
        """
        if "origin" in self._prop_dict:
            return self._prop_dict["origin"]
        else:
            return None

    @origin.setter
    def origin(self, val):
        self._prop_dict["origin"] = val

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
    def user_consent_description(self):
        """Gets and sets the userConsentDescription
        
        Returns: 
            str:
                The userConsentDescription
        """
        if "userConsentDescription" in self._prop_dict:
            return self._prop_dict["userConsentDescription"]
        else:
            return None

    @user_consent_description.setter
    def user_consent_description(self, val):
        self._prop_dict["userConsentDescription"] = val

    @property
    def user_consent_display_name(self):
        """Gets and sets the userConsentDisplayName
        
        Returns: 
            str:
                The userConsentDisplayName
        """
        if "userConsentDisplayName" in self._prop_dict:
            return self._prop_dict["userConsentDisplayName"]
        else:
            return None

    @user_consent_display_name.setter
    def user_consent_display_name(self, val):
        self._prop_dict["userConsentDisplayName"] = val

    @property
    def value(self):
        """Gets and sets the value
        
        Returns: 
            str:
                The value
        """
        if "value" in self._prop_dict:
            return self._prop_dict["value"]
        else:
            return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val

