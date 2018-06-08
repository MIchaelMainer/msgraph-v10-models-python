# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_platform_type import DevicePlatformType
from ..model.key_usages import KeyUsages
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDeviceCertificateState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_platform(self):
        """
        Gets and sets the devicePlatform
        
        Returns: 
            :class:`DevicePlatformType<onedrivesdk.model.device_platform_type.DevicePlatformType>`:
                The devicePlatform
        """
        if "devicePlatform" in self._prop_dict:
            if isinstance(self._prop_dict["devicePlatform"], OneDriveObjectBase):
                return self._prop_dict["devicePlatform"]
            else :
                self._prop_dict["devicePlatform"] = DevicePlatformType(self._prop_dict["devicePlatform"])
                return self._prop_dict["devicePlatform"]

        return None

    @device_platform.setter
    def device_platform(self, val):
        self._prop_dict["devicePlatform"] = val

    @property
    def certificate_key_usage(self):
        """
        Gets and sets the certificateKeyUsage
        
        Returns: 
            :class:`KeyUsages<onedrivesdk.model.key_usages.KeyUsages>`:
                The certificateKeyUsage
        """
        if "certificateKeyUsage" in self._prop_dict:
            if isinstance(self._prop_dict["certificateKeyUsage"], OneDriveObjectBase):
                return self._prop_dict["certificateKeyUsage"]
            else :
                self._prop_dict["certificateKeyUsage"] = KeyUsages(self._prop_dict["certificateKeyUsage"])
                return self._prop_dict["certificateKeyUsage"]

        return None

    @certificate_key_usage.setter
    def certificate_key_usage(self, val):
        self._prop_dict["certificateKeyUsage"] = val

    @property
    def certificate_profile_display_name(self):
        """
        Gets and sets the certificateProfileDisplayName
        
        Returns:
            str:
                The certificateProfileDisplayName
        """
        if "certificateProfileDisplayName" in self._prop_dict:
            return self._prop_dict["certificateProfileDisplayName"]
        else:
            return None

    @certificate_profile_display_name.setter
    def certificate_profile_display_name(self, val):
        self._prop_dict["certificateProfileDisplayName"] = val

    @property
    def device_display_name(self):
        """
        Gets and sets the deviceDisplayName
        
        Returns:
            str:
                The deviceDisplayName
        """
        if "deviceDisplayName" in self._prop_dict:
            return self._prop_dict["deviceDisplayName"]
        else:
            return None

    @device_display_name.setter
    def device_display_name(self, val):
        self._prop_dict["deviceDisplayName"] = val

    @property
    def user_display_name(self):
        """
        Gets and sets the userDisplayName
        
        Returns:
            str:
                The userDisplayName
        """
        if "userDisplayName" in self._prop_dict:
            return self._prop_dict["userDisplayName"]
        else:
            return None

    @user_display_name.setter
    def user_display_name(self, val):
        self._prop_dict["userDisplayName"] = val

    @property
    def server_url(self):
        """
        Gets and sets the serverUrl
        
        Returns:
            str:
                The serverUrl
        """
        if "serverUrl" in self._prop_dict:
            return self._prop_dict["serverUrl"]
        else:
            return None

    @server_url.setter
    def server_url(self, val):
        self._prop_dict["serverUrl"] = val

    @property
    def certificate_expiration_date_time(self):
        """
        Gets and sets the certificateExpirationDateTime
        
        Returns:
            datetime:
                The certificateExpirationDateTime
        """
        if "certificateExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["certificateExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @certificate_expiration_date_time.setter
    def certificate_expiration_date_time(self, val):
        self._prop_dict["certificateExpirationDateTime"] = val.isoformat()+"Z"

    @property
    def last_certificate_state_change_date_time(self):
        """
        Gets and sets the lastCertificateStateChangeDateTime
        
        Returns:
            datetime:
                The lastCertificateStateChangeDateTime
        """
        if "lastCertificateStateChangeDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastCertificateStateChangeDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_certificate_state_change_date_time.setter
    def last_certificate_state_change_date_time(self, val):
        self._prop_dict["lastCertificateStateChangeDateTime"] = val.isoformat()+"Z"

    @property
    def certificate_issuer(self):
        """
        Gets and sets the certificateIssuer
        
        Returns:
            str:
                The certificateIssuer
        """
        if "certificateIssuer" in self._prop_dict:
            return self._prop_dict["certificateIssuer"]
        else:
            return None

    @certificate_issuer.setter
    def certificate_issuer(self, val):
        self._prop_dict["certificateIssuer"] = val

    @property
    def certificate_thumbprint(self):
        """
        Gets and sets the certificateThumbprint
        
        Returns:
            str:
                The certificateThumbprint
        """
        if "certificateThumbprint" in self._prop_dict:
            return self._prop_dict["certificateThumbprint"]
        else:
            return None

    @certificate_thumbprint.setter
    def certificate_thumbprint(self, val):
        self._prop_dict["certificateThumbprint"] = val

    @property
    def certificate_serial_number(self):
        """
        Gets and sets the certificateSerialNumber
        
        Returns:
            str:
                The certificateSerialNumber
        """
        if "certificateSerialNumber" in self._prop_dict:
            return self._prop_dict["certificateSerialNumber"]
        else:
            return None

    @certificate_serial_number.setter
    def certificate_serial_number(self, val):
        self._prop_dict["certificateSerialNumber"] = val

    @property
    def certificate_key_length(self):
        """
        Gets and sets the certificateKeyLength
        
        Returns:
            int:
                The certificateKeyLength
        """
        if "certificateKeyLength" in self._prop_dict:
            return self._prop_dict["certificateKeyLength"]
        else:
            return None

    @certificate_key_length.setter
    def certificate_key_length(self, val):
        self._prop_dict["certificateKeyLength"] = val

    @property
    def enhanced_key_usage(self):
        """
        Gets and sets the enhancedKeyUsage
        
        Returns:
            str:
                The enhancedKeyUsage
        """
        if "enhancedKeyUsage" in self._prop_dict:
            return self._prop_dict["enhancedKeyUsage"]
        else:
            return None

    @enhanced_key_usage.setter
    def enhanced_key_usage(self, val):
        self._prop_dict["enhancedKeyUsage"] = val

