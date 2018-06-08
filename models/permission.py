# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.item_reference import ItemReference
from ..model.sharing_invitation import SharingInvitation
from ..model.sharing_link import SharingLink
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Permission(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

    @property
    def granted_to(self):
        """
        Gets and sets the grantedTo
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The grantedTo
        """
        if "grantedTo" in self._prop_dict:
            if isinstance(self._prop_dict["grantedTo"], OneDriveObjectBase):
                return self._prop_dict["grantedTo"]
            else :
                self._prop_dict["grantedTo"] = IdentitySet(self._prop_dict["grantedTo"])
                return self._prop_dict["grantedTo"]

        return None

    @granted_to.setter
    def granted_to(self, val):
        self._prop_dict["grantedTo"] = val

    @property
    def granted_to_identities(self):
        """Gets and sets the grantedToIdentities
        
        Returns: 
            :class:`GrantedToIdentitiesCollectionPage<onedrivesdk.request.granted_to_identities_collection.GrantedToIdentitiesCollectionPage>`:
                The grantedToIdentities
        """
        if "grantedToIdentities" in self._prop_dict:
            return GrantedToIdentitiesCollectionPage(self._prop_dict["grantedToIdentities"])
        else:
            return None

    @property
    def inherited_from(self):
        """
        Gets and sets the inheritedFrom
        
        Returns: 
            :class:`ItemReference<onedrivesdk.model.item_reference.ItemReference>`:
                The inheritedFrom
        """
        if "inheritedFrom" in self._prop_dict:
            if isinstance(self._prop_dict["inheritedFrom"], OneDriveObjectBase):
                return self._prop_dict["inheritedFrom"]
            else :
                self._prop_dict["inheritedFrom"] = ItemReference(self._prop_dict["inheritedFrom"])
                return self._prop_dict["inheritedFrom"]

        return None

    @inherited_from.setter
    def inherited_from(self, val):
        self._prop_dict["inheritedFrom"] = val

    @property
    def invitation(self):
        """
        Gets and sets the invitation
        
        Returns: 
            :class:`SharingInvitation<onedrivesdk.model.sharing_invitation.SharingInvitation>`:
                The invitation
        """
        if "invitation" in self._prop_dict:
            if isinstance(self._prop_dict["invitation"], OneDriveObjectBase):
                return self._prop_dict["invitation"]
            else :
                self._prop_dict["invitation"] = SharingInvitation(self._prop_dict["invitation"])
                return self._prop_dict["invitation"]

        return None

    @invitation.setter
    def invitation(self, val):
        self._prop_dict["invitation"] = val

    @property
    def link(self):
        """
        Gets and sets the link
        
        Returns: 
            :class:`SharingLink<onedrivesdk.model.sharing_link.SharingLink>`:
                The link
        """
        if "link" in self._prop_dict:
            if isinstance(self._prop_dict["link"], OneDriveObjectBase):
                return self._prop_dict["link"]
            else :
                self._prop_dict["link"] = SharingLink(self._prop_dict["link"])
                return self._prop_dict["link"]

        return None

    @link.setter
    def link(self, val):
        self._prop_dict["link"] = val

    @property
    def roles(self):
        """
        Gets and sets the roles
        
        Returns:
            str:
                The roles
        """
        if "roles" in self._prop_dict:
            return self._prop_dict["roles"]
        else:
            return None

    @roles.setter
    def roles(self, val):
        self._prop_dict["roles"] = val

    @property
    def share_id(self):
        """
        Gets and sets the shareId
        
        Returns:
            str:
                The shareId
        """
        if "shareId" in self._prop_dict:
            return self._prop_dict["shareId"]
        else:
            return None

    @share_id.setter
    def share_id(self, val):
        self._prop_dict["shareId"] = val

