# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.api import Api
from ..model.app_role import AppRole
from ..model.installed_client import InstalledClient
from ..model.informational_url import InformationalUrl
from ..model.key_credential import KeyCredential
from ..model.password_credential import PasswordCredential
from ..model.pre_authorized_application import PreAuthorizedApplication
from ..model.required_resource_access import RequiredResourceAccess
from ..model.web import Web
from ..model.extension_property import ExtensionProperty
from ..model.directory_object import DirectoryObject
from ..model.synchronization import Synchronization
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Application(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def api(self):
        """
        Gets and sets the api
        
        Returns: 
            :class:`Api<onedrivesdk.model.api.Api>`:
                The api
        """
        if "api" in self._prop_dict:
            if isinstance(self._prop_dict["api"], OneDriveObjectBase):
                return self._prop_dict["api"]
            else :
                self._prop_dict["api"] = Api(self._prop_dict["api"])
                return self._prop_dict["api"]

        return None

    @api.setter
    def api(self, val):
        self._prop_dict["api"] = val

    @property
    def allow_public_client(self):
        """
        Gets and sets the allowPublicClient
        
        Returns:
            bool:
                The allowPublicClient
        """
        if "allowPublicClient" in self._prop_dict:
            return self._prop_dict["allowPublicClient"]
        else:
            return None

    @allow_public_client.setter
    def allow_public_client(self, val):
        self._prop_dict["allowPublicClient"] = val

    @property
    def application_aliases(self):
        """
        Gets and sets the applicationAliases
        
        Returns:
            str:
                The applicationAliases
        """
        if "applicationAliases" in self._prop_dict:
            return self._prop_dict["applicationAliases"]
        else:
            return None

    @application_aliases.setter
    def application_aliases(self, val):
        self._prop_dict["applicationAliases"] = val

    @property
    def app_roles(self):
        """Gets and sets the appRoles
        
        Returns: 
            :class:`AppRolesCollectionPage<onedrivesdk.request.app_roles_collection.AppRolesCollectionPage>`:
                The appRoles
        """
        if "appRoles" in self._prop_dict:
            return AppRolesCollectionPage(self._prop_dict["appRoles"])
        else:
            return None

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def installed_clients(self):
        """
        Gets and sets the installedClients
        
        Returns: 
            :class:`InstalledClient<onedrivesdk.model.installed_client.InstalledClient>`:
                The installedClients
        """
        if "installedClients" in self._prop_dict:
            if isinstance(self._prop_dict["installedClients"], OneDriveObjectBase):
                return self._prop_dict["installedClients"]
            else :
                self._prop_dict["installedClients"] = InstalledClient(self._prop_dict["installedClients"])
                return self._prop_dict["installedClients"]

        return None

    @installed_clients.setter
    def installed_clients(self, val):
        self._prop_dict["installedClients"] = val

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
    def info(self):
        """
        Gets and sets the info
        
        Returns: 
            :class:`InformationalUrl<onedrivesdk.model.informational_url.InformationalUrl>`:
                The info
        """
        if "info" in self._prop_dict:
            if isinstance(self._prop_dict["info"], OneDriveObjectBase):
                return self._prop_dict["info"]
            else :
                self._prop_dict["info"] = InformationalUrl(self._prop_dict["info"])
                return self._prop_dict["info"]

        return None

    @info.setter
    def info(self, val):
        self._prop_dict["info"] = val

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
    def org_restrictions(self):
        """
        Gets and sets the orgRestrictions
        
        Returns:
            UUID:
                The orgRestrictions
        """
        if "orgRestrictions" in self._prop_dict:
            return self._prop_dict["orgRestrictions"]
        else:
            return None

    @org_restrictions.setter
    def org_restrictions(self, val):
        self._prop_dict["orgRestrictions"] = val

    @property
    def password_credentials(self):
        """Gets and sets the passwordCredentials
        
        Returns: 
            :class:`PasswordCredentialsCollectionPage<onedrivesdk.request.password_credentials_collection.PasswordCredentialsCollectionPage>`:
                The passwordCredentials
        """
        if "passwordCredentials" in self._prop_dict:
            return PasswordCredentialsCollectionPage(self._prop_dict["passwordCredentials"])
        else:
            return None

    @property
    def pre_authorized_applications(self):
        """Gets and sets the preAuthorizedApplications
        
        Returns: 
            :class:`PreAuthorizedApplicationsCollectionPage<onedrivesdk.request.pre_authorized_applications_collection.PreAuthorizedApplicationsCollectionPage>`:
                The preAuthorizedApplications
        """
        if "preAuthorizedApplications" in self._prop_dict:
            return PreAuthorizedApplicationsCollectionPage(self._prop_dict["preAuthorizedApplications"])
        else:
            return None

    @property
    def required_resource_access(self):
        """Gets and sets the requiredResourceAccess
        
        Returns: 
            :class:`RequiredResourceAccessCollectionPage<onedrivesdk.request.required_resource_access_collection.RequiredResourceAccessCollectionPage>`:
                The requiredResourceAccess
        """
        if "requiredResourceAccess" in self._prop_dict:
            return RequiredResourceAccessCollectionPage(self._prop_dict["requiredResourceAccess"])
        else:
            return None

    @property
    def tags(self):
        """
        Gets and sets the tags
        
        Returns:
            str:
                The tags
        """
        if "tags" in self._prop_dict:
            return self._prop_dict["tags"]
        else:
            return None

    @tags.setter
    def tags(self, val):
        self._prop_dict["tags"] = val

    @property
    def web(self):
        """
        Gets and sets the web
        
        Returns: 
            :class:`Web<onedrivesdk.model.web.Web>`:
                The web
        """
        if "web" in self._prop_dict:
            if isinstance(self._prop_dict["web"], OneDriveObjectBase):
                return self._prop_dict["web"]
            else :
                self._prop_dict["web"] = Web(self._prop_dict["web"])
                return self._prop_dict["web"]

        return None

    @web.setter
    def web(self, val):
        self._prop_dict["web"] = val

    @property
    def extension_properties(self):
        """Gets and sets the extensionProperties
        
        Returns: 
            :class:`ExtensionPropertiesCollectionPage<onedrivesdk.request.extension_properties_collection.ExtensionPropertiesCollectionPage>`:
                The extensionProperties
        """
        if "extensionProperties" in self._prop_dict:
            return ExtensionPropertiesCollectionPage(self._prop_dict["extensionProperties"])
        else:
            return None

    @property
    def created_on_behalf_of(self):
        """
        Gets and sets the createdOnBehalfOf
        
        Returns: 
            :class:`DirectoryObject<onedrivesdk.model.directory_object.DirectoryObject>`:
                The createdOnBehalfOf
        """
        if "createdOnBehalfOf" in self._prop_dict:
            if isinstance(self._prop_dict["createdOnBehalfOf"], OneDriveObjectBase):
                return self._prop_dict["createdOnBehalfOf"]
            else :
                self._prop_dict["createdOnBehalfOf"] = DirectoryObject(self._prop_dict["createdOnBehalfOf"])
                return self._prop_dict["createdOnBehalfOf"]

        return None

    @created_on_behalf_of.setter
    def created_on_behalf_of(self, val):
        self._prop_dict["createdOnBehalfOf"] = val

    @property
    def owners(self):
        """Gets and sets the owners
        
        Returns: 
            :class:`OwnersCollectionPage<onedrivesdk.request.owners_collection.OwnersCollectionPage>`:
                The owners
        """
        if "owners" in self._prop_dict:
            return OwnersCollectionPage(self._prop_dict["owners"])
        else:
            return None

    @property
    def policies(self):
        """Gets and sets the policies
        
        Returns: 
            :class:`PoliciesCollectionPage<onedrivesdk.request.policies_collection.PoliciesCollectionPage>`:
                The policies
        """
        if "policies" in self._prop_dict:
            return PoliciesCollectionPage(self._prop_dict["policies"])
        else:
            return None

    @property
    def synchronization(self):
        """
        Gets and sets the synchronization
        
        Returns: 
            :class:`Synchronization<onedrivesdk.model.synchronization.Synchronization>`:
                The synchronization
        """
        if "synchronization" in self._prop_dict:
            if isinstance(self._prop_dict["synchronization"], OneDriveObjectBase):
                return self._prop_dict["synchronization"]
            else :
                self._prop_dict["synchronization"] = Synchronization(self._prop_dict["synchronization"])
                return self._prop_dict["synchronization"]

        return None

    @synchronization.setter
    def synchronization(self, val):
        self._prop_dict["synchronization"] = val

