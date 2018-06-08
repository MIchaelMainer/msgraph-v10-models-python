# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.vpp_licensing_type import VppLicensingType
from ..model.ios_device_type import IosDeviceType
from ..model.vpp_token_account_type import VppTokenAccountType
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class IosVppApp(OneDriveObjectBase):

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
    def release_date_time(self):
        """
        Gets and sets the releaseDateTime
        
        Returns:
            datetime:
                The releaseDateTime
        """
        if "releaseDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["releaseDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @release_date_time.setter
    def release_date_time(self, val):
        self._prop_dict["releaseDateTime"] = val.isoformat()+"Z"

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

    @property
    def licensing_type(self):
        """
        Gets and sets the licensingType
        
        Returns: 
            :class:`VppLicensingType<onedrivesdk.model.vpp_licensing_type.VppLicensingType>`:
                The licensingType
        """
        if "licensingType" in self._prop_dict:
            if isinstance(self._prop_dict["licensingType"], OneDriveObjectBase):
                return self._prop_dict["licensingType"]
            else :
                self._prop_dict["licensingType"] = VppLicensingType(self._prop_dict["licensingType"])
                return self._prop_dict["licensingType"]

        return None

    @licensing_type.setter
    def licensing_type(self, val):
        self._prop_dict["licensingType"] = val

    @property
    def applicable_device_type(self):
        """
        Gets and sets the applicableDeviceType
        
        Returns: 
            :class:`IosDeviceType<onedrivesdk.model.ios_device_type.IosDeviceType>`:
                The applicableDeviceType
        """
        if "applicableDeviceType" in self._prop_dict:
            if isinstance(self._prop_dict["applicableDeviceType"], OneDriveObjectBase):
                return self._prop_dict["applicableDeviceType"]
            else :
                self._prop_dict["applicableDeviceType"] = IosDeviceType(self._prop_dict["applicableDeviceType"])
                return self._prop_dict["applicableDeviceType"]

        return None

    @applicable_device_type.setter
    def applicable_device_type(self, val):
        self._prop_dict["applicableDeviceType"] = val

    @property
    def vpp_token_organization_name(self):
        """
        Gets and sets the vppTokenOrganizationName
        
        Returns:
            str:
                The vppTokenOrganizationName
        """
        if "vppTokenOrganizationName" in self._prop_dict:
            return self._prop_dict["vppTokenOrganizationName"]
        else:
            return None

    @vpp_token_organization_name.setter
    def vpp_token_organization_name(self, val):
        self._prop_dict["vppTokenOrganizationName"] = val

    @property
    def vpp_token_account_type(self):
        """
        Gets and sets the vppTokenAccountType
        
        Returns: 
            :class:`VppTokenAccountType<onedrivesdk.model.vpp_token_account_type.VppTokenAccountType>`:
                The vppTokenAccountType
        """
        if "vppTokenAccountType" in self._prop_dict:
            if isinstance(self._prop_dict["vppTokenAccountType"], OneDriveObjectBase):
                return self._prop_dict["vppTokenAccountType"]
            else :
                self._prop_dict["vppTokenAccountType"] = VppTokenAccountType(self._prop_dict["vppTokenAccountType"])
                return self._prop_dict["vppTokenAccountType"]

        return None

    @vpp_token_account_type.setter
    def vpp_token_account_type(self, val):
        self._prop_dict["vppTokenAccountType"] = val

    @property
    def vpp_token_apple_id(self):
        """
        Gets and sets the vppTokenAppleId
        
        Returns:
            str:
                The vppTokenAppleId
        """
        if "vppTokenAppleId" in self._prop_dict:
            return self._prop_dict["vppTokenAppleId"]
        else:
            return None

    @vpp_token_apple_id.setter
    def vpp_token_apple_id(self, val):
        self._prop_dict["vppTokenAppleId"] = val

    @property
    def bundle_id(self):
        """
        Gets and sets the bundleId
        
        Returns:
            str:
                The bundleId
        """
        if "bundleId" in self._prop_dict:
            return self._prop_dict["bundleId"]
        else:
            return None

    @bundle_id.setter
    def bundle_id(self, val):
        self._prop_dict["bundleId"] = val

