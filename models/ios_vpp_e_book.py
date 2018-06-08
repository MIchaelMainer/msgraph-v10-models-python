# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class IosVppEBook(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def vpp_token_id(self):
        """
        Gets and sets the vppTokenId
        
        Returns:
            UUID:
                The vppTokenId
        """
        if "vppTokenId" in self._prop_dict:
            return self._prop_dict["vppTokenId"]
        else:
            return None

    @vpp_token_id.setter
    def vpp_token_id(self, val):
        self._prop_dict["vppTokenId"] = val

    @property
    def apple_id(self):
        """
        Gets and sets the appleId
        
        Returns:
            str:
                The appleId
        """
        if "appleId" in self._prop_dict:
            return self._prop_dict["appleId"]
        else:
            return None

    @apple_id.setter
    def apple_id(self, val):
        self._prop_dict["appleId"] = val

    @property
    def vpp_organization_name(self):
        """
        Gets and sets the vppOrganizationName
        
        Returns:
            str:
                The vppOrganizationName
        """
        if "vppOrganizationName" in self._prop_dict:
            return self._prop_dict["vppOrganizationName"]
        else:
            return None

    @vpp_organization_name.setter
    def vpp_organization_name(self, val):
        self._prop_dict["vppOrganizationName"] = val

    @property
    def genres(self):
        """
        Gets and sets the genres
        
        Returns:
            str:
                The genres
        """
        if "genres" in self._prop_dict:
            return self._prop_dict["genres"]
        else:
            return None

    @genres.setter
    def genres(self, val):
        self._prop_dict["genres"] = val

    @property
    def language(self):
        """
        Gets and sets the language
        
        Returns:
            str:
                The language
        """
        if "language" in self._prop_dict:
            return self._prop_dict["language"]
        else:
            return None

    @language.setter
    def language(self, val):
        self._prop_dict["language"] = val

    @property
    def seller(self):
        """
        Gets and sets the seller
        
        Returns:
            str:
                The seller
        """
        if "seller" in self._prop_dict:
            return self._prop_dict["seller"]
        else:
            return None

    @seller.setter
    def seller(self, val):
        self._prop_dict["seller"] = val

    @property
    def total_license_count(self):
        """
        Gets and sets the totalLicenseCount
        
        Returns:
            int:
                The totalLicenseCount
        """
        if "totalLicenseCount" in self._prop_dict:
            return self._prop_dict["totalLicenseCount"]
        else:
            return None

    @total_license_count.setter
    def total_license_count(self, val):
        self._prop_dict["totalLicenseCount"] = val

    @property
    def used_license_count(self):
        """
        Gets and sets the usedLicenseCount
        
        Returns:
            int:
                The usedLicenseCount
        """
        if "usedLicenseCount" in self._prop_dict:
            return self._prop_dict["usedLicenseCount"]
        else:
            return None

    @used_license_count.setter
    def used_license_count(self, val):
        self._prop_dict["usedLicenseCount"] = val

