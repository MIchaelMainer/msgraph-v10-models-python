# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_app_data_encryption_type import ManagedAppDataEncryptionType
from ..model.key_value_pair import KeyValuePair
from ..model.managed_app_remediation_action import ManagedAppRemediationAction
from ..model.managed_mobile_app import ManagedMobileApp
from ..model.managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
from ..one_drive_object_base import OneDriveObjectBase


class IosManagedAppProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_data_encryption_type(self):
        """
        Gets and sets the appDataEncryptionType
        
        Returns: 
            :class:`ManagedAppDataEncryptionType<onedrivesdk.model.managed_app_data_encryption_type.ManagedAppDataEncryptionType>`:
                The appDataEncryptionType
        """
        if "appDataEncryptionType" in self._prop_dict:
            if isinstance(self._prop_dict["appDataEncryptionType"], OneDriveObjectBase):
                return self._prop_dict["appDataEncryptionType"]
            else :
                self._prop_dict["appDataEncryptionType"] = ManagedAppDataEncryptionType(self._prop_dict["appDataEncryptionType"])
                return self._prop_dict["appDataEncryptionType"]

        return None

    @app_data_encryption_type.setter
    def app_data_encryption_type(self, val):
        self._prop_dict["appDataEncryptionType"] = val

    @property
    def minimum_required_sdk_version(self):
        """
        Gets and sets the minimumRequiredSdkVersion
        
        Returns:
            str:
                The minimumRequiredSdkVersion
        """
        if "minimumRequiredSdkVersion" in self._prop_dict:
            return self._prop_dict["minimumRequiredSdkVersion"]
        else:
            return None

    @minimum_required_sdk_version.setter
    def minimum_required_sdk_version(self, val):
        self._prop_dict["minimumRequiredSdkVersion"] = val

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
    def face_id_blocked(self):
        """
        Gets and sets the faceIdBlocked
        
        Returns:
            bool:
                The faceIdBlocked
        """
        if "faceIdBlocked" in self._prop_dict:
            return self._prop_dict["faceIdBlocked"]
        else:
            return None

    @face_id_blocked.setter
    def face_id_blocked(self, val):
        self._prop_dict["faceIdBlocked"] = val

    @property
    def exempted_app_protocols(self):
        """Gets and sets the exemptedAppProtocols
        
        Returns: 
            :class:`ExemptedAppProtocolsCollectionPage<onedrivesdk.request.exempted_app_protocols_collection.ExemptedAppProtocolsCollectionPage>`:
                The exemptedAppProtocols
        """
        if "exemptedAppProtocols" in self._prop_dict:
            return ExemptedAppProtocolsCollectionPage(self._prop_dict["exemptedAppProtocols"])
        else:
            return None

    @property
    def minimum_wipe_sdk_version(self):
        """
        Gets and sets the minimumWipeSdkVersion
        
        Returns:
            str:
                The minimumWipeSdkVersion
        """
        if "minimumWipeSdkVersion" in self._prop_dict:
            return self._prop_dict["minimumWipeSdkVersion"]
        else:
            return None

    @minimum_wipe_sdk_version.setter
    def minimum_wipe_sdk_version(self, val):
        self._prop_dict["minimumWipeSdkVersion"] = val

    @property
    def allowed_ios_device_models(self):
        """
        Gets and sets the allowedIosDeviceModels
        
        Returns:
            str:
                The allowedIosDeviceModels
        """
        if "allowedIosDeviceModels" in self._prop_dict:
            return self._prop_dict["allowedIosDeviceModels"]
        else:
            return None

    @allowed_ios_device_models.setter
    def allowed_ios_device_models(self, val):
        self._prop_dict["allowedIosDeviceModels"] = val

    @property
    def app_action_if_ios_device_model_not_allowed(self):
        """
        Gets and sets the appActionIfIosDeviceModelNotAllowed
        
        Returns: 
            :class:`ManagedAppRemediationAction<onedrivesdk.model.managed_app_remediation_action.ManagedAppRemediationAction>`:
                The appActionIfIosDeviceModelNotAllowed
        """
        if "appActionIfIosDeviceModelNotAllowed" in self._prop_dict:
            if isinstance(self._prop_dict["appActionIfIosDeviceModelNotAllowed"], OneDriveObjectBase):
                return self._prop_dict["appActionIfIosDeviceModelNotAllowed"]
            else :
                self._prop_dict["appActionIfIosDeviceModelNotAllowed"] = ManagedAppRemediationAction(self._prop_dict["appActionIfIosDeviceModelNotAllowed"])
                return self._prop_dict["appActionIfIosDeviceModelNotAllowed"]

        return None

    @app_action_if_ios_device_model_not_allowed.setter
    def app_action_if_ios_device_model_not_allowed(self, val):
        self._prop_dict["appActionIfIosDeviceModelNotAllowed"] = val

    @property
    def third_party_keyboards_blocked(self):
        """
        Gets and sets the thirdPartyKeyboardsBlocked
        
        Returns:
            bool:
                The thirdPartyKeyboardsBlocked
        """
        if "thirdPartyKeyboardsBlocked" in self._prop_dict:
            return self._prop_dict["thirdPartyKeyboardsBlocked"]
        else:
            return None

    @third_party_keyboards_blocked.setter
    def third_party_keyboards_blocked(self, val):
        self._prop_dict["thirdPartyKeyboardsBlocked"] = val

    @property
    def filter_open_in_to_only_managed_apps(self):
        """
        Gets and sets the filterOpenInToOnlyManagedApps
        
        Returns:
            bool:
                The filterOpenInToOnlyManagedApps
        """
        if "filterOpenInToOnlyManagedApps" in self._prop_dict:
            return self._prop_dict["filterOpenInToOnlyManagedApps"]
        else:
            return None

    @filter_open_in_to_only_managed_apps.setter
    def filter_open_in_to_only_managed_apps(self, val):
        self._prop_dict["filterOpenInToOnlyManagedApps"] = val

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

