# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def package_id(self):
        """
        Gets and sets the packageId
        
        Returns:
            str:
                The packageId
        """
        if "packageId" in self._prop_dict:
            return self._prop_dict["packageId"]
        else:
            return None

    @package_id.setter
    def package_id(self, val):
        self._prop_dict["packageId"] = val

    @property
    def app_identifier(self):
        """
        Gets and sets the appIdentifier
        
        Returns:
            str:
                The appIdentifier
        """
        if "appIdentifier" in self._prop_dict:
            return self._prop_dict["appIdentifier"]
        else:
            return None

    @app_identifier.setter
    def app_identifier(self, val):
        self._prop_dict["appIdentifier"] = val

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
    def app_store_url(self):
        """
        Gets and sets the appStoreUrl
        
        Returns:
            str:
                The appStoreUrl
        """
        if "appStoreUrl" in self._prop_dict:
            return self._prop_dict["appStoreUrl"]
        else:
            return None

    @app_store_url.setter
    def app_store_url(self, val):
        self._prop_dict["appStoreUrl"] = val

