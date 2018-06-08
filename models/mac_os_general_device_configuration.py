# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_list_item import AppListItem
from ..model.app_list_type import AppListType
from ..model.required_password_type import RequiredPasswordType
from ..one_drive_object_base import OneDriveObjectBase


class MacOSGeneralDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def compliant_apps_list(self):
        """Gets and sets the compliantAppsList
        
        Returns: 
            :class:`CompliantAppsListCollectionPage<onedrivesdk.request.compliant_apps_list_collection.CompliantAppsListCollectionPage>`:
                The compliantAppsList
        """
        if "compliantAppsList" in self._prop_dict:
            return CompliantAppsListCollectionPage(self._prop_dict["compliantAppsList"])
        else:
            return None

    @property
    def compliant_app_list_type(self):
        """
        Gets and sets the compliantAppListType
        
        Returns: 
            :class:`AppListType<onedrivesdk.model.app_list_type.AppListType>`:
                The compliantAppListType
        """
        if "compliantAppListType" in self._prop_dict:
            if isinstance(self._prop_dict["compliantAppListType"], OneDriveObjectBase):
                return self._prop_dict["compliantAppListType"]
            else :
                self._prop_dict["compliantAppListType"] = AppListType(self._prop_dict["compliantAppListType"])
                return self._prop_dict["compliantAppListType"]

        return None

    @compliant_app_list_type.setter
    def compliant_app_list_type(self, val):
        self._prop_dict["compliantAppListType"] = val

    @property
    def email_in_domain_suffixes(self):
        """
        Gets and sets the emailInDomainSuffixes
        
        Returns:
            str:
                The emailInDomainSuffixes
        """
        if "emailInDomainSuffixes" in self._prop_dict:
            return self._prop_dict["emailInDomainSuffixes"]
        else:
            return None

    @email_in_domain_suffixes.setter
    def email_in_domain_suffixes(self, val):
        self._prop_dict["emailInDomainSuffixes"] = val

    @property
    def password_block_simple(self):
        """
        Gets and sets the passwordBlockSimple
        
        Returns:
            bool:
                The passwordBlockSimple
        """
        if "passwordBlockSimple" in self._prop_dict:
            return self._prop_dict["passwordBlockSimple"]
        else:
            return None

    @password_block_simple.setter
    def password_block_simple(self, val):
        self._prop_dict["passwordBlockSimple"] = val

    @property
    def password_expiration_days(self):
        """
        Gets and sets the passwordExpirationDays
        
        Returns:
            int:
                The passwordExpirationDays
        """
        if "passwordExpirationDays" in self._prop_dict:
            return self._prop_dict["passwordExpirationDays"]
        else:
            return None

    @password_expiration_days.setter
    def password_expiration_days(self, val):
        self._prop_dict["passwordExpirationDays"] = val

    @property
    def password_minimum_character_set_count(self):
        """
        Gets and sets the passwordMinimumCharacterSetCount
        
        Returns:
            int:
                The passwordMinimumCharacterSetCount
        """
        if "passwordMinimumCharacterSetCount" in self._prop_dict:
            return self._prop_dict["passwordMinimumCharacterSetCount"]
        else:
            return None

    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self, val):
        self._prop_dict["passwordMinimumCharacterSetCount"] = val

    @property
    def password_minimum_length(self):
        """
        Gets and sets the passwordMinimumLength
        
        Returns:
            int:
                The passwordMinimumLength
        """
        if "passwordMinimumLength" in self._prop_dict:
            return self._prop_dict["passwordMinimumLength"]
        else:
            return None

    @password_minimum_length.setter
    def password_minimum_length(self, val):
        self._prop_dict["passwordMinimumLength"] = val

    @property
    def password_minutes_of_inactivity_before_lock(self):
        """
        Gets and sets the passwordMinutesOfInactivityBeforeLock
        
        Returns:
            int:
                The passwordMinutesOfInactivityBeforeLock
        """
        if "passwordMinutesOfInactivityBeforeLock" in self._prop_dict:
            return self._prop_dict["passwordMinutesOfInactivityBeforeLock"]
        else:
            return None

    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self, val):
        self._prop_dict["passwordMinutesOfInactivityBeforeLock"] = val

    @property
    def password_minutes_of_inactivity_before_screen_timeout(self):
        """
        Gets and sets the passwordMinutesOfInactivityBeforeScreenTimeout
        
        Returns:
            int:
                The passwordMinutesOfInactivityBeforeScreenTimeout
        """
        if "passwordMinutesOfInactivityBeforeScreenTimeout" in self._prop_dict:
            return self._prop_dict["passwordMinutesOfInactivityBeforeScreenTimeout"]
        else:
            return None

    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self, val):
        self._prop_dict["passwordMinutesOfInactivityBeforeScreenTimeout"] = val

    @property
    def password_previous_password_block_count(self):
        """
        Gets and sets the passwordPreviousPasswordBlockCount
        
        Returns:
            int:
                The passwordPreviousPasswordBlockCount
        """
        if "passwordPreviousPasswordBlockCount" in self._prop_dict:
            return self._prop_dict["passwordPreviousPasswordBlockCount"]
        else:
            return None

    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self, val):
        self._prop_dict["passwordPreviousPasswordBlockCount"] = val

    @property
    def password_required_type(self):
        """
        Gets and sets the passwordRequiredType
        
        Returns: 
            :class:`RequiredPasswordType<onedrivesdk.model.required_password_type.RequiredPasswordType>`:
                The passwordRequiredType
        """
        if "passwordRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passwordRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passwordRequiredType"]
            else :
                self._prop_dict["passwordRequiredType"] = RequiredPasswordType(self._prop_dict["passwordRequiredType"])
                return self._prop_dict["passwordRequiredType"]

        return None

    @password_required_type.setter
    def password_required_type(self, val):
        self._prop_dict["passwordRequiredType"] = val

    @property
    def password_required(self):
        """
        Gets and sets the passwordRequired
        
        Returns:
            bool:
                The passwordRequired
        """
        if "passwordRequired" in self._prop_dict:
            return self._prop_dict["passwordRequired"]
        else:
            return None

    @password_required.setter
    def password_required(self, val):
        self._prop_dict["passwordRequired"] = val

