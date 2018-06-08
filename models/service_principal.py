# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.add_in import AddIn
from ..model.app_role import AppRole
from ..model.key_credential import KeyCredential
from ..model.o_auth2_permission import OAuth2Permission
from ..model.password_credential import PasswordCredential
from ..model.app_role_assignment import AppRoleAssignment
from ..model.o_auth2_permission_grant import OAuth2PermissionGrant
from ..model.directory_object import DirectoryObject
from ..model.license_details import LicenseDetails
from ..model.synchronization import Synchronization
from ..one_drive_object_base import OneDriveObjectBase


class ServicePrincipal(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_enabled(self):
        """
        Gets and sets the accountEnabled
        
        Returns:
            bool:
                The accountEnabled
        """
        if "accountEnabled" in self._prop_dict:
            return self._prop_dict["accountEnabled"]
        else:
            return None

    @account_enabled.setter
    def account_enabled(self, val):
        self._prop_dict["accountEnabled"] = val

    @property
    def add_ins(self):
        """Gets and sets the addIns
        
        Returns: 
            :class:`AddInsCollectionPage<onedrivesdk.request.add_ins_collection.AddInsCollectionPage>`:
                The addIns
        """
        if "addIns" in self._prop_dict:
            return AddInsCollectionPage(self._prop_dict["addIns"])
        else:
            return None

    @property
    def app_display_name(self):
        """
        Gets and sets the appDisplayName
        
        Returns:
            str:
                The appDisplayName
        """
        if "appDisplayName" in self._prop_dict:
            return self._prop_dict["appDisplayName"]
        else:
            return None

    @app_display_name.setter
    def app_display_name(self, val):
        self._prop_dict["appDisplayName"] = val

    @property
    def app_id(self):
        """
        Gets and sets the appId
        
        Returns:
            str:
                The appId
        """
        if "appId" in self._prop_dict:
            return self._prop_dict["appId"]
        else:
            return None

    @app_id.setter
    def app_id(self, val):
        self._prop_dict["appId"] = val

    @property
    def app_owner_organization_id(self):
        """
        Gets and sets the appOwnerOrganizationId
        
        Returns:
            UUID:
                The appOwnerOrganizationId
        """
        if "appOwnerOrganizationId" in self._prop_dict:
            return self._prop_dict["appOwnerOrganizationId"]
        else:
            return None

    @app_owner_organization_id.setter
    def app_owner_organization_id(self, val):
        self._prop_dict["appOwnerOrganizationId"] = val

    @property
    def app_role_assignment_required(self):
        """
        Gets and sets the appRoleAssignmentRequired
        
        Returns:
            bool:
                The appRoleAssignmentRequired
        """
        if "appRoleAssignmentRequired" in self._prop_dict:
            return self._prop_dict["appRoleAssignmentRequired"]
        else:
            return None

    @app_role_assignment_required.setter
    def app_role_assignment_required(self, val):
        self._prop_dict["appRoleAssignmentRequired"] = val

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
    def error_url(self):
        """
        Gets and sets the errorUrl
        
        Returns:
            str:
                The errorUrl
        """
        if "errorUrl" in self._prop_dict:
            return self._prop_dict["errorUrl"]
        else:
            return None

    @error_url.setter
    def error_url(self, val):
        self._prop_dict["errorUrl"] = val

    @property
    def homepage(self):
        """
        Gets and sets the homepage
        
        Returns:
            str:
                The homepage
        """
        if "homepage" in self._prop_dict:
            return self._prop_dict["homepage"]
        else:
            return None

    @homepage.setter
    def homepage(self, val):
        self._prop_dict["homepage"] = val

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
    def logout_url(self):
        """
        Gets and sets the logoutUrl
        
        Returns:
            str:
                The logoutUrl
        """
        if "logoutUrl" in self._prop_dict:
            return self._prop_dict["logoutUrl"]
        else:
            return None

    @logout_url.setter
    def logout_url(self, val):
        self._prop_dict["logoutUrl"] = val

    @property
    def oauth2_permissions(self):
        """Gets and sets the oauth2Permissions
        
        Returns: 
            :class:`Oauth2PermissionsCollectionPage<onedrivesdk.request.oauth2_permissions_collection.Oauth2PermissionsCollectionPage>`:
                The oauth2Permissions
        """
        if "oauth2Permissions" in self._prop_dict:
            return Oauth2PermissionsCollectionPage(self._prop_dict["oauth2Permissions"])
        else:
            return None

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
    def preferred_token_signing_key_thumbprint(self):
        """
        Gets and sets the preferredTokenSigningKeyThumbprint
        
        Returns:
            str:
                The preferredTokenSigningKeyThumbprint
        """
        if "preferredTokenSigningKeyThumbprint" in self._prop_dict:
            return self._prop_dict["preferredTokenSigningKeyThumbprint"]
        else:
            return None

    @preferred_token_signing_key_thumbprint.setter
    def preferred_token_signing_key_thumbprint(self, val):
        self._prop_dict["preferredTokenSigningKeyThumbprint"] = val

    @property
    def publisher_name(self):
        """
        Gets and sets the publisherName
        
        Returns:
            str:
                The publisherName
        """
        if "publisherName" in self._prop_dict:
            return self._prop_dict["publisherName"]
        else:
            return None

    @publisher_name.setter
    def publisher_name(self, val):
        self._prop_dict["publisherName"] = val

    @property
    def reply_urls(self):
        """
        Gets and sets the replyUrls
        
        Returns:
            str:
                The replyUrls
        """
        if "replyUrls" in self._prop_dict:
            return self._prop_dict["replyUrls"]
        else:
            return None

    @reply_urls.setter
    def reply_urls(self, val):
        self._prop_dict["replyUrls"] = val

    @property
    def saml_metadata_url(self):
        """
        Gets and sets the samlMetadataUrl
        
        Returns:
            str:
                The samlMetadataUrl
        """
        if "samlMetadataUrl" in self._prop_dict:
            return self._prop_dict["samlMetadataUrl"]
        else:
            return None

    @saml_metadata_url.setter
    def saml_metadata_url(self, val):
        self._prop_dict["samlMetadataUrl"] = val

    @property
    def service_principal_names(self):
        """
        Gets and sets the servicePrincipalNames
        
        Returns:
            str:
                The servicePrincipalNames
        """
        if "servicePrincipalNames" in self._prop_dict:
            return self._prop_dict["servicePrincipalNames"]
        else:
            return None

    @service_principal_names.setter
    def service_principal_names(self, val):
        self._prop_dict["servicePrincipalNames"] = val

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
    def app_role_assigned_to(self):
        """Gets and sets the appRoleAssignedTo
        
        Returns: 
            :class:`AppRoleAssignedToCollectionPage<onedrivesdk.request.app_role_assigned_to_collection.AppRoleAssignedToCollectionPage>`:
                The appRoleAssignedTo
        """
        if "appRoleAssignedTo" in self._prop_dict:
            return AppRoleAssignedToCollectionPage(self._prop_dict["appRoleAssignedTo"])
        else:
            return None

    @property
    def app_role_assignments(self):
        """Gets and sets the appRoleAssignments
        
        Returns: 
            :class:`AppRoleAssignmentsCollectionPage<onedrivesdk.request.app_role_assignments_collection.AppRoleAssignmentsCollectionPage>`:
                The appRoleAssignments
        """
        if "appRoleAssignments" in self._prop_dict:
            return AppRoleAssignmentsCollectionPage(self._prop_dict["appRoleAssignments"])
        else:
            return None

    @property
    def oauth2_permission_grants(self):
        """Gets and sets the oauth2PermissionGrants
        
        Returns: 
            :class:`Oauth2PermissionGrantsCollectionPage<onedrivesdk.request.oauth2_permission_grants_collection.Oauth2PermissionGrantsCollectionPage>`:
                The oauth2PermissionGrants
        """
        if "oauth2PermissionGrants" in self._prop_dict:
            return Oauth2PermissionGrantsCollectionPage(self._prop_dict["oauth2PermissionGrants"])
        else:
            return None

    @property
    def member_of(self):
        """Gets and sets the memberOf
        
        Returns: 
            :class:`MemberOfCollectionPage<onedrivesdk.request.member_of_collection.MemberOfCollectionPage>`:
                The memberOf
        """
        if "memberOf" in self._prop_dict:
            return MemberOfCollectionPage(self._prop_dict["memberOf"])
        else:
            return None

    @property
    def created_objects(self):
        """Gets and sets the createdObjects
        
        Returns: 
            :class:`CreatedObjectsCollectionPage<onedrivesdk.request.created_objects_collection.CreatedObjectsCollectionPage>`:
                The createdObjects
        """
        if "createdObjects" in self._prop_dict:
            return CreatedObjectsCollectionPage(self._prop_dict["createdObjects"])
        else:
            return None

    @property
    def license_details(self):
        """Gets and sets the licenseDetails
        
        Returns: 
            :class:`LicenseDetailsCollectionPage<onedrivesdk.request.license_details_collection.LicenseDetailsCollectionPage>`:
                The licenseDetails
        """
        if "licenseDetails" in self._prop_dict:
            return LicenseDetailsCollectionPage(self._prop_dict["licenseDetails"])
        else:
            return None

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
    def owned_objects(self):
        """Gets and sets the ownedObjects
        
        Returns: 
            :class:`OwnedObjectsCollectionPage<onedrivesdk.request.owned_objects_collection.OwnedObjectsCollectionPage>`:
                The ownedObjects
        """
        if "ownedObjects" in self._prop_dict:
            return OwnedObjectsCollectionPage(self._prop_dict["ownedObjects"])
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

