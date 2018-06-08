# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.edition_upgrade_license_type import EditionUpgradeLicenseType
from ..model.windows10_edition_type import Windows10EditionType
from ..one_drive_object_base import OneDriveObjectBase


class EditionUpgradeConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def license_type(self):
        """
        Gets and sets the licenseType
        
        Returns: 
            :class:`EditionUpgradeLicenseType<onedrivesdk.model.edition_upgrade_license_type.EditionUpgradeLicenseType>`:
                The licenseType
        """
        if "licenseType" in self._prop_dict:
            if isinstance(self._prop_dict["licenseType"], OneDriveObjectBase):
                return self._prop_dict["licenseType"]
            else :
                self._prop_dict["licenseType"] = EditionUpgradeLicenseType(self._prop_dict["licenseType"])
                return self._prop_dict["licenseType"]

        return None

    @license_type.setter
    def license_type(self, val):
        self._prop_dict["licenseType"] = val

    @property
    def target_edition(self):
        """
        Gets and sets the targetEdition
        
        Returns: 
            :class:`Windows10EditionType<onedrivesdk.model.windows10_edition_type.Windows10EditionType>`:
                The targetEdition
        """
        if "targetEdition" in self._prop_dict:
            if isinstance(self._prop_dict["targetEdition"], OneDriveObjectBase):
                return self._prop_dict["targetEdition"]
            else :
                self._prop_dict["targetEdition"] = Windows10EditionType(self._prop_dict["targetEdition"])
                return self._prop_dict["targetEdition"]

        return None

    @target_edition.setter
    def target_edition(self, val):
        self._prop_dict["targetEdition"] = val

    @property
    def license(self):
        """
        Gets and sets the license
        
        Returns:
            str:
                The license
        """
        if "license" in self._prop_dict:
            return self._prop_dict["license"]
        else:
            return None

    @license.setter
    def license(self, val):
        self._prop_dict["license"] = val

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

