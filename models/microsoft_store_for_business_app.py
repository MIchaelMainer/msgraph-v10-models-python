# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.microsoft_store_for_business_license_type import MicrosoftStoreForBusinessLicenseType
from ..one_drive_object_base import OneDriveObjectBase


class MicrosoftStoreForBusinessApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def product_key(self):
        """
        Gets and sets the productKey
        
        Returns:
            str:
                The productKey
        """
        if "productKey" in self._prop_dict:
            return self._prop_dict["productKey"]
        else:
            return None

    @product_key.setter
    def product_key(self, val):
        self._prop_dict["productKey"] = val

    @property
    def license_type(self):
        """
        Gets and sets the licenseType
        
        Returns: 
            :class:`MicrosoftStoreForBusinessLicenseType<onedrivesdk.model.microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType>`:
                The licenseType
        """
        if "licenseType" in self._prop_dict:
            if isinstance(self._prop_dict["licenseType"], OneDriveObjectBase):
                return self._prop_dict["licenseType"]
            else :
                self._prop_dict["licenseType"] = MicrosoftStoreForBusinessLicenseType(self._prop_dict["licenseType"])
                return self._prop_dict["licenseType"]

        return None

    @license_type.setter
    def license_type(self, val):
        self._prop_dict["licenseType"] = val

    @property
    def package_identity_name(self):
        """
        Gets and sets the packageIdentityName
        
        Returns:
            str:
                The packageIdentityName
        """
        if "packageIdentityName" in self._prop_dict:
            return self._prop_dict["packageIdentityName"]
        else:
            return None

    @package_identity_name.setter
    def package_identity_name(self, val):
        self._prop_dict["packageIdentityName"] = val

