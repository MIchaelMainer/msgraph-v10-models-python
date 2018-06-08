# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mac_os_minimum_operating_system import MacOSMinimumOperatingSystem
from ..model.mac_os_lob_child_app import MacOSLobChildApp
from ..one_drive_object_base import OneDriveObjectBase


class MacOSLobApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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

    @property
    def minimum_supported_operating_system(self):
        """
        Gets and sets the minimumSupportedOperatingSystem
        
        Returns: 
            :class:`MacOSMinimumOperatingSystem<onedrivesdk.model.mac_os_minimum_operating_system.MacOSMinimumOperatingSystem>`:
                The minimumSupportedOperatingSystem
        """
        if "minimumSupportedOperatingSystem" in self._prop_dict:
            if isinstance(self._prop_dict["minimumSupportedOperatingSystem"], OneDriveObjectBase):
                return self._prop_dict["minimumSupportedOperatingSystem"]
            else :
                self._prop_dict["minimumSupportedOperatingSystem"] = MacOSMinimumOperatingSystem(self._prop_dict["minimumSupportedOperatingSystem"])
                return self._prop_dict["minimumSupportedOperatingSystem"]

        return None

    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self, val):
        self._prop_dict["minimumSupportedOperatingSystem"] = val

    @property
    def build_number(self):
        """
        Gets and sets the buildNumber
        
        Returns:
            str:
                The buildNumber
        """
        if "buildNumber" in self._prop_dict:
            return self._prop_dict["buildNumber"]
        else:
            return None

    @build_number.setter
    def build_number(self, val):
        self._prop_dict["buildNumber"] = val

    @property
    def version_number(self):
        """
        Gets and sets the versionNumber
        
        Returns:
            str:
                The versionNumber
        """
        if "versionNumber" in self._prop_dict:
            return self._prop_dict["versionNumber"]
        else:
            return None

    @version_number.setter
    def version_number(self, val):
        self._prop_dict["versionNumber"] = val

    @property
    def child_apps(self):
        """Gets and sets the childApps
        
        Returns: 
            :class:`ChildAppsCollectionPage<onedrivesdk.request.child_apps_collection.ChildAppsCollectionPage>`:
                The childApps
        """
        if "childApps" in self._prop_dict:
            return ChildAppsCollectionPage(self._prop_dict["childApps"])
        else:
            return None

    @property
    def identity_version(self):
        """
        Gets and sets the identityVersion
        
        Returns:
            str:
                The identityVersion
        """
        if "identityVersion" in self._prop_dict:
            return self._prop_dict["identityVersion"]
        else:
            return None

    @identity_version.setter
    def identity_version(self, val):
        self._prop_dict["identityVersion"] = val

    @property
    def md5_hash_chunk_size(self):
        """
        Gets and sets the md5HashChunkSize
        
        Returns:
            int:
                The md5HashChunkSize
        """
        if "md5HashChunkSize" in self._prop_dict:
            return self._prop_dict["md5HashChunkSize"]
        else:
            return None

    @md5_hash_chunk_size.setter
    def md5_hash_chunk_size(self, val):
        self._prop_dict["md5HashChunkSize"] = val

    @property
    def md5_hash(self):
        """
        Gets and sets the md5Hash
        
        Returns:
            str:
                The md5Hash
        """
        if "md5Hash" in self._prop_dict:
            return self._prop_dict["md5Hash"]
        else:
            return None

    @md5_hash.setter
    def md5_hash(self, val):
        self._prop_dict["md5Hash"] = val

    @property
    def ignore_version_detection(self):
        """
        Gets and sets the ignoreVersionDetection
        
        Returns:
            bool:
                The ignoreVersionDetection
        """
        if "ignoreVersionDetection" in self._prop_dict:
            return self._prop_dict["ignoreVersionDetection"]
        else:
            return None

    @ignore_version_detection.setter
    def ignore_version_detection(self, val):
        self._prop_dict["ignoreVersionDetection"] = val

