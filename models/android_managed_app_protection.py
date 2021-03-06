# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_mobile_app import ManagedMobileApp
from ..model.managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
from ..one_drive_object_base import OneDriveObjectBase


class AndroidManagedAppProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def screen_capture_blocked(self):
        """
        Gets and sets the screenCaptureBlocked
        
        Returns:
            bool:
                The screenCaptureBlocked
        """
        if "screenCaptureBlocked" in self._prop_dict:
            return self._prop_dict["screenCaptureBlocked"]
        else:
            return None

    @screen_capture_blocked.setter
    def screen_capture_blocked(self, val):
        self._prop_dict["screenCaptureBlocked"] = val

    @property
    def disable_app_encryption_if_device_encryption_is_enabled(self):
        """
        Gets and sets the disableAppEncryptionIfDeviceEncryptionIsEnabled
        
        Returns:
            bool:
                The disableAppEncryptionIfDeviceEncryptionIsEnabled
        """
        if "disableAppEncryptionIfDeviceEncryptionIsEnabled" in self._prop_dict:
            return self._prop_dict["disableAppEncryptionIfDeviceEncryptionIsEnabled"]
        else:
            return None

    @disable_app_encryption_if_device_encryption_is_enabled.setter
    def disable_app_encryption_if_device_encryption_is_enabled(self, val):
        self._prop_dict["disableAppEncryptionIfDeviceEncryptionIsEnabled"] = val

    @property
    def encrypt_app_data(self):
        """
        Gets and sets the encryptAppData
        
        Returns:
            bool:
                The encryptAppData
        """
        if "encryptAppData" in self._prop_dict:
            return self._prop_dict["encryptAppData"]
        else:
            return None

    @encrypt_app_data.setter
    def encrypt_app_data(self, val):
        self._prop_dict["encryptAppData"] = val

    @property
    def deployed_app_count(self):
        """
        Gets and sets the deployedAppCount
        
        Returns:
            int:
                The deployedAppCount
        """
        if "deployedAppCount" in self._prop_dict:
            return self._prop_dict["deployedAppCount"]
        else:
            return None

    @deployed_app_count.setter
    def deployed_app_count(self, val):
        self._prop_dict["deployedAppCount"] = val

    @property
    def minimum_required_patch_version(self):
        """
        Gets and sets the minimumRequiredPatchVersion
        
        Returns:
            str:
                The minimumRequiredPatchVersion
        """
        if "minimumRequiredPatchVersion" in self._prop_dict:
            return self._prop_dict["minimumRequiredPatchVersion"]
        else:
            return None

    @minimum_required_patch_version.setter
    def minimum_required_patch_version(self, val):
        self._prop_dict["minimumRequiredPatchVersion"] = val

    @property
    def minimum_warning_patch_version(self):
        """
        Gets and sets the minimumWarningPatchVersion
        
        Returns:
            str:
                The minimumWarningPatchVersion
        """
        if "minimumWarningPatchVersion" in self._prop_dict:
            return self._prop_dict["minimumWarningPatchVersion"]
        else:
            return None

    @minimum_warning_patch_version.setter
    def minimum_warning_patch_version(self, val):
        self._prop_dict["minimumWarningPatchVersion"] = val

    @property
    def apps(self):
        """Gets and sets the apps
        
        Returns: 
            :class:`AppsCollectionPage<onedrivesdk.request.apps_collection.AppsCollectionPage>`:
                The apps
        """
        if "apps" in self._prop_dict:
            return AppsCollectionPage(self._prop_dict["apps"])
        else:
            return None

    @property
    def deployment_summary(self):
        """
        Gets and sets the deploymentSummary
        
        Returns: 
            :class:`ManagedAppPolicyDeploymentSummary<onedrivesdk.model.managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary>`:
                The deploymentSummary
        """
        if "deploymentSummary" in self._prop_dict:
            if isinstance(self._prop_dict["deploymentSummary"], OneDriveObjectBase):
                return self._prop_dict["deploymentSummary"]
            else :
                self._prop_dict["deploymentSummary"] = ManagedAppPolicyDeploymentSummary(self._prop_dict["deploymentSummary"])
                return self._prop_dict["deploymentSummary"]

        return None

    @deployment_summary.setter
    def deployment_summary(self, val):
        self._prop_dict["deploymentSummary"] = val

