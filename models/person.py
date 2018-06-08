# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.scored_email_address import ScoredEmailAddress
from ..model.phone import Phone
from ..model.location import Location
from ..model.website import Website
from ..model.person_type import PersonType
from ..one_drive_object_base import OneDriveObjectBase


class Person(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def given_name(self):
        """
        Gets and sets the givenName
        
        Returns:
            str:
                The givenName
        """
        if "givenName" in self._prop_dict:
            return self._prop_dict["givenName"]
        else:
            return None

    @given_name.setter
    def given_name(self, val):
        self._prop_dict["givenName"] = val

    @property
    def surname(self):
        """
        Gets and sets the surname
        
        Returns:
            str:
                The surname
        """
        if "surname" in self._prop_dict:
            return self._prop_dict["surname"]
        else:
            return None

    @surname.setter
    def surname(self, val):
        self._prop_dict["surname"] = val

    @property
    def birthday(self):
        """
        Gets and sets the birthday
        
        Returns:
            str:
                The birthday
        """
        if "birthday" in self._prop_dict:
            return self._prop_dict["birthday"]
        else:
            return None

    @birthday.setter
    def birthday(self, val):
        self._prop_dict["birthday"] = val

    @property
    def person_notes(self):
        """
        Gets and sets the personNotes
        
        Returns:
            str:
                The personNotes
        """
        if "personNotes" in self._prop_dict:
            return self._prop_dict["personNotes"]
        else:
            return None

    @person_notes.setter
    def person_notes(self, val):
        self._prop_dict["personNotes"] = val

    @property
    def is_favorite(self):
        """
        Gets and sets the isFavorite
        
        Returns:
            bool:
                The isFavorite
        """
        if "isFavorite" in self._prop_dict:
            return self._prop_dict["isFavorite"]
        else:
            return None

    @is_favorite.setter
    def is_favorite(self, val):
        self._prop_dict["isFavorite"] = val

    @property
    def scored_email_addresses(self):
        """Gets and sets the scoredEmailAddresses
        
        Returns: 
            :class:`ScoredEmailAddressesCollectionPage<onedrivesdk.request.scored_email_addresses_collection.ScoredEmailAddressesCollectionPage>`:
                The scoredEmailAddresses
        """
        if "scoredEmailAddresses" in self._prop_dict:
            return ScoredEmailAddressesCollectionPage(self._prop_dict["scoredEmailAddresses"])
        else:
            return None

    @property
    def phones(self):
        """Gets and sets the phones
        
        Returns: 
            :class:`PhonesCollectionPage<onedrivesdk.request.phones_collection.PhonesCollectionPage>`:
                The phones
        """
        if "phones" in self._prop_dict:
            return PhonesCollectionPage(self._prop_dict["phones"])
        else:
            return None

    @property
    def postal_addresses(self):
        """Gets and sets the postalAddresses
        
        Returns: 
            :class:`PostalAddressesCollectionPage<onedrivesdk.request.postal_addresses_collection.PostalAddressesCollectionPage>`:
                The postalAddresses
        """
        if "postalAddresses" in self._prop_dict:
            return PostalAddressesCollectionPage(self._prop_dict["postalAddresses"])
        else:
            return None

    @property
    def websites(self):
        """Gets and sets the websites
        
        Returns: 
            :class:`WebsitesCollectionPage<onedrivesdk.request.websites_collection.WebsitesCollectionPage>`:
                The websites
        """
        if "websites" in self._prop_dict:
            return WebsitesCollectionPage(self._prop_dict["websites"])
        else:
            return None

    @property
    def job_title(self):
        """
        Gets and sets the jobTitle
        
        Returns:
            str:
                The jobTitle
        """
        if "jobTitle" in self._prop_dict:
            return self._prop_dict["jobTitle"]
        else:
            return None

    @job_title.setter
    def job_title(self, val):
        self._prop_dict["jobTitle"] = val

    @property
    def company_name(self):
        """
        Gets and sets the companyName
        
        Returns:
            str:
                The companyName
        """
        if "companyName" in self._prop_dict:
            return self._prop_dict["companyName"]
        else:
            return None

    @company_name.setter
    def company_name(self, val):
        self._prop_dict["companyName"] = val

    @property
    def yomi_company(self):
        """
        Gets and sets the yomiCompany
        
        Returns:
            str:
                The yomiCompany
        """
        if "yomiCompany" in self._prop_dict:
            return self._prop_dict["yomiCompany"]
        else:
            return None

    @yomi_company.setter
    def yomi_company(self, val):
        self._prop_dict["yomiCompany"] = val

    @property
    def department(self):
        """
        Gets and sets the department
        
        Returns:
            str:
                The department
        """
        if "department" in self._prop_dict:
            return self._prop_dict["department"]
        else:
            return None

    @department.setter
    def department(self, val):
        self._prop_dict["department"] = val

    @property
    def office_location(self):
        """
        Gets and sets the officeLocation
        
        Returns:
            str:
                The officeLocation
        """
        if "officeLocation" in self._prop_dict:
            return self._prop_dict["officeLocation"]
        else:
            return None

    @office_location.setter
    def office_location(self, val):
        self._prop_dict["officeLocation"] = val

    @property
    def profession(self):
        """
        Gets and sets the profession
        
        Returns:
            str:
                The profession
        """
        if "profession" in self._prop_dict:
            return self._prop_dict["profession"]
        else:
            return None

    @profession.setter
    def profession(self, val):
        self._prop_dict["profession"] = val

    @property
    def person_type(self):
        """
        Gets and sets the personType
        
        Returns: 
            :class:`PersonType<onedrivesdk.model.person_type.PersonType>`:
                The personType
        """
        if "personType" in self._prop_dict:
            if isinstance(self._prop_dict["personType"], OneDriveObjectBase):
                return self._prop_dict["personType"]
            else :
                self._prop_dict["personType"] = PersonType(self._prop_dict["personType"])
                return self._prop_dict["personType"]

        return None

    @person_type.setter
    def person_type(self, val):
        self._prop_dict["personType"] = val

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
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
    def im_address(self):
        """
        Gets and sets the imAddress
        
        Returns:
            str:
                The imAddress
        """
        if "imAddress" in self._prop_dict:
            return self._prop_dict["imAddress"]
        else:
            return None

    @im_address.setter
    def im_address(self, val):
        self._prop_dict["imAddress"] = val

