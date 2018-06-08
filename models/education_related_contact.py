# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_contact_relationship import EducationContactRelationship
from ..one_drive_object_base import OneDriveObjectBase


class EducationRelatedContact(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
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
    def display_name(self):
        """Gets and sets the displayName
        
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
    def email_address(self):
        """Gets and sets the emailAddress
        
        Returns: 
            str:
                The emailAddress
        """
        if "emailAddress" in self._prop_dict:
            return self._prop_dict["emailAddress"]
        else:
            return None

    @email_address.setter
    def email_address(self, val):
        self._prop_dict["emailAddress"] = val

    @property
    def mobile_phone(self):
        """Gets and sets the mobilePhone
        
        Returns: 
            str:
                The mobilePhone
        """
        if "mobilePhone" in self._prop_dict:
            return self._prop_dict["mobilePhone"]
        else:
            return None

    @mobile_phone.setter
    def mobile_phone(self, val):
        self._prop_dict["mobilePhone"] = val

    @property
    def relationship(self):
        """
        Gets and sets the relationship
        
        Returns: 
            :class:`EducationContactRelationship<onedrivesdk.model.education_contact_relationship.EducationContactRelationship>`:
                The relationship
        """
        if "relationship" in self._prop_dict:
            if isinstance(self._prop_dict["relationship"], OneDriveObjectBase):
                return self._prop_dict["relationship"]
            else :
                self._prop_dict["relationship"] = EducationContactRelationship(self._prop_dict["relationship"])
                return self._prop_dict["relationship"]

        return None

    @relationship.setter
    def relationship(self, val):
        self._prop_dict["relationship"] = val
    @property
    def access_consent(self):
        """Gets and sets the accessConsent
        
        Returns: 
            bool:
                The accessConsent
        """
        if "accessConsent" in self._prop_dict:
            return self._prop_dict["accessConsent"]
        else:
            return None

    @access_consent.setter
    def access_consent(self, val):
        self._prop_dict["accessConsent"] = val

