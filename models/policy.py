# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_credential import KeyCredential
from ..model.directory_object import DirectoryObject
from ..one_drive_object_base import OneDriveObjectBase


class Policy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def alternative_identifier(self):
        """
        Gets and sets the alternativeIdentifier
        
        Returns:
            str:
                The alternativeIdentifier
        """
        if "alternativeIdentifier" in self._prop_dict:
            return self._prop_dict["alternativeIdentifier"]
        else:
            return None

    @alternative_identifier.setter
    def alternative_identifier(self, val):
        self._prop_dict["alternativeIdentifier"] = val

    @property
    def definition(self):
        """
        Gets and sets the definition
        
        Returns:
            str:
                The definition
        """
        if "definition" in self._prop_dict:
            return self._prop_dict["definition"]
        else:
            return None

    @definition.setter
    def definition(self, val):
        self._prop_dict["definition"] = val

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
    def is_organization_default(self):
        """
        Gets and sets the isOrganizationDefault
        
        Returns:
            bool:
                The isOrganizationDefault
        """
        if "isOrganizationDefault" in self._prop_dict:
            return self._prop_dict["isOrganizationDefault"]
        else:
            return None

    @is_organization_default.setter
    def is_organization_default(self, val):
        self._prop_dict["isOrganizationDefault"] = val

    @property
    def key_credentials(self):
        """Gets and sets the keyCredentials
        
        Returns: 
            :class:`KeyCredentialsCollectionPage<onedrivesdk.request.key_credentials_collection.KeyCredentialsCollectionPage>`:
                The keyCredentials
        """
        if "keyCredentials" in self._prop_dict:
            return KeyCredentialsCollectionPage(self._prop_dict["keyCredentials"])
        else:
            return None

    @property
    def type(self):
        """
        Gets and sets the type
        
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
    def applies_to(self):
        """Gets and sets the appliesTo
        
        Returns: 
            :class:`AppliesToCollectionPage<onedrivesdk.request.applies_to_collection.AppliesToCollectionPage>`:
                The appliesTo
        """
        if "appliesTo" in self._prop_dict:
            return AppliesToCollectionPage(self._prop_dict["appliesTo"])
        else:
            return None

