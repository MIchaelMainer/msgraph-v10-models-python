# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from ..model.managed_app_data_transfer_level import ManagedAppDataTransferLevel
from ..model.managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
from ..model.managed_app_pin_character_set import ManagedAppPinCharacterSet
from ..model.managed_app_data_storage_location import ManagedAppDataStorageLocation
from ..model.managed_app_remediation_action import ManagedAppRemediationAction
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def period_offline_before_access_check(self):
        """
        Gets and sets the periodOfflineBeforeAccessCheck
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The periodOfflineBeforeAccessCheck
        """
        if "periodOfflineBeforeAccessCheck" in self._prop_dict:
            if isinstance(self._prop_dict["periodOfflineBeforeAccessCheck"], OneDriveObjectBase):
                return self._prop_dict["periodOfflineBeforeAccessCheck"]
            else :
                self._prop_dict["periodOfflineBeforeAccessCheck"] = Duration(self._prop_dict["periodOfflineBeforeAccessCheck"])
                return self._prop_dict["periodOfflineBeforeAccessCheck"]

        return None

    @period_offline_before_access_check.setter
    def period_offline_before_access_check(self, val):
        self._prop_dict["periodOfflineBeforeAccessCheck"] = val

    @property
    def period_online_before_access_check(self):
        """
        Gets and sets the periodOnlineBeforeAccessCheck
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The periodOnlineBeforeAccessCheck
        """
        if "periodOnlineBeforeAccessCheck" in self._prop_dict:
            if isinstance(self._prop_dict["periodOnlineBeforeAccessCheck"], OneDriveObjectBase):
                return self._prop_dict["periodOnlineBeforeAccessCheck"]
            else :
                self._prop_dict["periodOnlineBeforeAccessCheck"] = Duration(self._prop_dict["periodOnlineBeforeAccessCheck"])
                return self._prop_dict["periodOnlineBeforeAccessCheck"]

        return None

    @period_online_before_access_check.setter
    def period_online_before_access_check(self, val):
        self._prop_dict["periodOnlineBeforeAccessCheck"] = val

    @property
    def allowed_inbound_data_transfer_sources(self):
        """
        Gets and sets the allowedInboundDataTransferSources
        
        Returns: 
            :class:`ManagedAppDataTransferLevel<onedrivesdk.model.managed_app_data_transfer_level.ManagedAppDataTransferLevel>`:
                The allowedInboundDataTransferSources
        """
        if "allowedInboundDataTransferSources" in self._prop_dict:
            if isinstance(self._prop_dict["allowedInboundDataTransferSources"], OneDriveObjectBase):
                return self._prop_dict["allowedInboundDataTransferSources"]
            else :
                self._prop_dict["allowedInboundDataTransferSources"] = ManagedAppDataTransferLevel(self._prop_dict["allowedInboundDataTransferSources"])
                return self._prop_dict["allowedInboundDataTransferSources"]

        return None

    @allowed_inbound_data_transfer_sources.setter
    def allowed_inbound_data_transfer_sources(self, val):
        self._prop_dict["allowedInboundDataTransferSources"] = val

    @property
    def allowed_outbound_data_transfer_destinations(self):
        """
        Gets and sets the allowedOutboundDataTransferDestinations
        
        Returns: 
            :class:`ManagedAppDataTransferLevel<onedrivesdk.model.managed_app_data_transfer_level.ManagedAppDataTransferLevel>`:
                The allowedOutboundDataTransferDestinations
        """
        if "allowedOutboundDataTransferDestinations" in self._prop_dict:
            if isinstance(self._prop_dict["allowedOutboundDataTransferDestinations"], OneDriveObjectBase):
                return self._prop_dict["allowedOutboundDataTransferDestinations"]
            else :
                self._prop_dict["allowedOutboundDataTransferDestinations"] = ManagedAppDataTransferLevel(self._prop_dict["allowedOutboundDataTransferDestinations"])
                return self._prop_dict["allowedOutboundDataTransferDestinations"]

        return None

    @allowed_outbound_data_transfer_destinations.setter
    def allowed_outbound_data_transfer_destinations(self, val):
        self._prop_dict["allowedOutboundDataTransferDestinations"] = val

    @property
    def organizational_credentials_required(self):
        """
        Gets and sets the organizationalCredentialsRequired
        
        Returns:
            bool:
                The organizationalCredentialsRequired
        """
        if "organizationalCredentialsRequired" in self._prop_dict:
            return self._prop_dict["organizationalCredentialsRequired"]
        else:
            return None

    @organizational_credentials_required.setter
    def organizational_credentials_required(self, val):
        self._prop_dict["organizationalCredentialsRequired"] = val

    @property
    def allowed_outbound_clipboard_sharing_level(self):
        """
        Gets and sets the allowedOutboundClipboardSharingLevel
        
        Returns: 
            :class:`ManagedAppClipboardSharingLevel<onedrivesdk.model.managed_app_clipboard_sharing_level.ManagedAppClipboardSharingLevel>`:
                The allowedOutboundClipboardSharingLevel
        """
        if "allowedOutboundClipboardSharingLevel" in self._prop_dict:
            if isinstance(self._prop_dict["allowedOutboundClipboardSharingLevel"], OneDriveObjectBase):
                return self._prop_dict["allowedOutboundClipboardSharingLevel"]
            else :
                self._prop_dict["allowedOutboundClipboardSharingLevel"] = ManagedAppClipboardSharingLevel(self._prop_dict["allowedOutboundClipboardSharingLevel"])
                return self._prop_dict["allowedOutboundClipboardSharingLevel"]

        return None

    @allowed_outbound_clipboard_sharing_level.setter
    def allowed_outbound_clipboard_sharing_level(self, val):
        self._prop_dict["allowedOutboundClipboardSharingLevel"] = val

    @property
    def data_backup_blocked(self):
        """
        Gets and sets the dataBackupBlocked
        
        Returns:
            bool:
                The dataBackupBlocked
        """
        if "dataBackupBlocked" in self._prop_dict:
            return self._prop_dict["dataBackupBlocked"]
        else:
            return None

    @data_backup_blocked.setter
    def data_backup_blocked(self, val):
        self._prop_dict["dataBackupBlocked"] = val

    @property
    def device_compliance_required(self):
        """
        Gets and sets the deviceComplianceRequired
        
        Returns:
            bool:
                The deviceComplianceRequired
        """
        if "deviceComplianceRequired" in self._prop_dict:
            return self._prop_dict["deviceComplianceRequired"]
        else:
            return None

    @device_compliance_required.setter
    def device_compliance_required(self, val):
        self._prop_dict["deviceComplianceRequired"] = val

    @property
    def managed_browser_to_open_links_required(self):
        """
        Gets and sets the managedBrowserToOpenLinksRequired
        
        Returns:
            bool:
                The managedBrowserToOpenLinksRequired
        """
        if "managedBrowserToOpenLinksRequired" in self._prop_dict:
            return self._prop_dict["managedBrowserToOpenLinksRequired"]
        else:
            return None

    @managed_browser_to_open_links_required.setter
    def managed_browser_to_open_links_required(self, val):
        self._prop_dict["managedBrowserToOpenLinksRequired"] = val

    @property
    def save_as_blocked(self):
        """
        Gets and sets the saveAsBlocked
        
        Returns:
            bool:
                The saveAsBlocked
        """
        if "saveAsBlocked" in self._prop_dict:
            return self._prop_dict["saveAsBlocked"]
        else:
            return None

    @save_as_blocked.setter
    def save_as_blocked(self, val):
        self._prop_dict["saveAsBlocked"] = val

    @property
    def period_offline_before_wipe_is_enforced(self):
        """
        Gets and sets the periodOfflineBeforeWipeIsEnforced
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The periodOfflineBeforeWipeIsEnforced
        """
        if "periodOfflineBeforeWipeIsEnforced" in self._prop_dict:
            if isinstance(self._prop_dict["periodOfflineBeforeWipeIsEnforced"], OneDriveObjectBase):
                return self._prop_dict["periodOfflineBeforeWipeIsEnforced"]
            else :
                self._prop_dict["periodOfflineBeforeWipeIsEnforced"] = Duration(self._prop_dict["periodOfflineBeforeWipeIsEnforced"])
                return self._prop_dict["periodOfflineBeforeWipeIsEnforced"]

        return None

    @period_offline_before_wipe_is_enforced.setter
    def period_offline_before_wipe_is_enforced(self, val):
        self._prop_dict["periodOfflineBeforeWipeIsEnforced"] = val

    @property
    def pin_required(self):
        """
        Gets and sets the pinRequired
        
        Returns:
            bool:
                The pinRequired
        """
        if "pinRequired" in self._prop_dict:
            return self._prop_dict["pinRequired"]
        else:
            return None

    @pin_required.setter
    def pin_required(self, val):
        self._prop_dict["pinRequired"] = val

    @property
    def maximum_pin_retries(self):
        """
        Gets and sets the maximumPinRetries
        
        Returns:
            int:
                The maximumPinRetries
        """
        if "maximumPinRetries" in self._prop_dict:
            return self._prop_dict["maximumPinRetries"]
        else:
            return None

    @maximum_pin_retries.setter
    def maximum_pin_retries(self, val):
        self._prop_dict["maximumPinRetries"] = val

    @property
    def simple_pin_blocked(self):
        """
        Gets and sets the simplePinBlocked
        
        Returns:
            bool:
                The simplePinBlocked
        """
        if "simplePinBlocked" in self._prop_dict:
            return self._prop_dict["simplePinBlocked"]
        else:
            return None

    @simple_pin_blocked.setter
    def simple_pin_blocked(self, val):
        self._prop_dict["simplePinBlocked"] = val

    @property
    def minimum_pin_length(self):
        """
        Gets and sets the minimumPinLength
        
        Returns:
            int:
                The minimumPinLength
        """
        if "minimumPinLength" in self._prop_dict:
            return self._prop_dict["minimumPinLength"]
        else:
            return None

    @minimum_pin_length.setter
    def minimum_pin_length(self, val):
        self._prop_dict["minimumPinLength"] = val

    @property
    def pin_character_set(self):
        """
        Gets and sets the pinCharacterSet
        
        Returns: 
            :class:`ManagedAppPinCharacterSet<onedrivesdk.model.managed_app_pin_character_set.ManagedAppPinCharacterSet>`:
                The pinCharacterSet
        """
        if "pinCharacterSet" in self._prop_dict:
            if isinstance(self._prop_dict["pinCharacterSet"], OneDriveObjectBase):
                return self._prop_dict["pinCharacterSet"]
            else :
                self._prop_dict["pinCharacterSet"] = ManagedAppPinCharacterSet(self._prop_dict["pinCharacterSet"])
                return self._prop_dict["pinCharacterSet"]

        return None

    @pin_character_set.setter
    def pin_character_set(self, val):
        self._prop_dict["pinCharacterSet"] = val

    @property
    def period_before_pin_reset(self):
        """
        Gets and sets the periodBeforePinReset
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The periodBeforePinReset
        """
        if "periodBeforePinReset" in self._prop_dict:
            if isinstance(self._prop_dict["periodBeforePinReset"], OneDriveObjectBase):
                return self._prop_dict["periodBeforePinReset"]
            else :
                self._prop_dict["periodBeforePinReset"] = Duration(self._prop_dict["periodBeforePinReset"])
                return self._prop_dict["periodBeforePinReset"]

        return None

    @period_before_pin_reset.setter
    def period_before_pin_reset(self, val):
        self._prop_dict["periodBeforePinReset"] = val

    @property
    def allowed_data_storage_locations(self):
        """Gets and sets the allowedDataStorageLocations
        
        Returns: 
            :class:`AllowedDataStorageLocationsCollectionPage<onedrivesdk.request.allowed_data_storage_locations_collection.AllowedDataStorageLocationsCollectionPage>`:
                The allowedDataStorageLocations
        """
        if "allowedDataStorageLocations" in self._prop_dict:
            return AllowedDataStorageLocationsCollectionPage(self._prop_dict["allowedDataStorageLocations"])
        else:
            return None

    @property
    def contact_sync_blocked(self):
        """
        Gets and sets the contactSyncBlocked
        
        Returns:
            bool:
                The contactSyncBlocked
        """
        if "contactSyncBlocked" in self._prop_dict:
            return self._prop_dict["contactSyncBlocked"]
        else:
            return None

    @contact_sync_blocked.setter
    def contact_sync_blocked(self, val):
        self._prop_dict["contactSyncBlocked"] = val

    @property
    def print_blocked(self):
        """
        Gets and sets the printBlocked
        
        Returns:
            bool:
                The printBlocked
        """
        if "printBlocked" in self._prop_dict:
            return self._prop_dict["printBlocked"]
        else:
            return None

    @print_blocked.setter
    def print_blocked(self, val):
        self._prop_dict["printBlocked"] = val

    @property
    def fingerprint_blocked(self):
        """
        Gets and sets the fingerprintBlocked
        
        Returns:
            bool:
                The fingerprintBlocked
        """
        if "fingerprintBlocked" in self._prop_dict:
            return self._prop_dict["fingerprintBlocked"]
        else:
            return None

    @fingerprint_blocked.setter
    def fingerprint_blocked(self, val):
        self._prop_dict["fingerprintBlocked"] = val

    @property
    def disable_app_pin_if_device_pin_is_set(self):
        """
        Gets and sets the disableAppPinIfDevicePinIsSet
        
        Returns:
            bool:
                The disableAppPinIfDevicePinIsSet
        """
        if "disableAppPinIfDevicePinIsSet" in self._prop_dict:
            return self._prop_dict["disableAppPinIfDevicePinIsSet"]
        else:
            return None

    @disable_app_pin_if_device_pin_is_set.setter
    def disable_app_pin_if_device_pin_is_set(self, val):
        self._prop_dict["disableAppPinIfDevicePinIsSet"] = val

    @property
    def minimum_required_os_version(self):
        """
        Gets and sets the minimumRequiredOsVersion
        
        Returns:
            str:
                The minimumRequiredOsVersion
        """
        if "minimumRequiredOsVersion" in self._prop_dict:
            return self._prop_dict["minimumRequiredOsVersion"]
        else:
            return None

    @minimum_required_os_version.setter
    def minimum_required_os_version(self, val):
        self._prop_dict["minimumRequiredOsVersion"] = val

    @property
    def minimum_warning_os_version(self):
        """
        Gets and sets the minimumWarningOsVersion
        
        Returns:
            str:
                The minimumWarningOsVersion
        """
        if "minimumWarningOsVersion" in self._prop_dict:
            return self._prop_dict["minimumWarningOsVersion"]
        else:
            return None

    @minimum_warning_os_version.setter
    def minimum_warning_os_version(self, val):
        self._prop_dict["minimumWarningOsVersion"] = val

    @property
    def minimum_required_app_version(self):
        """
        Gets and sets the minimumRequiredAppVersion
        
        Returns:
            str:
                The minimumRequiredAppVersion
        """
        if "minimumRequiredAppVersion" in self._prop_dict:
            return self._prop_dict["minimumRequiredAppVersion"]
        else:
            return None

    @minimum_required_app_version.setter
    def minimum_required_app_version(self, val):
        self._prop_dict["minimumRequiredAppVersion"] = val

    @property
    def minimum_warning_app_version(self):
        """
        Gets and sets the minimumWarningAppVersion
        
        Returns:
            str:
                The minimumWarningAppVersion
        """
        if "minimumWarningAppVersion" in self._prop_dict:
            return self._prop_dict["minimumWarningAppVersion"]
        else:
            return None

    @minimum_warning_app_version.setter
    def minimum_warning_app_version(self, val):
        self._prop_dict["minimumWarningAppVersion"] = val

    @property
    def minimum_wipe_os_version(self):
        """
        Gets and sets the minimumWipeOsVersion
        
        Returns:
            str:
                The minimumWipeOsVersion
        """
        if "minimumWipeOsVersion" in self._prop_dict:
            return self._prop_dict["minimumWipeOsVersion"]
        else:
            return None

    @minimum_wipe_os_version.setter
    def minimum_wipe_os_version(self, val):
        self._prop_dict["minimumWipeOsVersion"] = val

    @property
    def minimum_wipe_app_version(self):
        """
        Gets and sets the minimumWipeAppVersion
        
        Returns:
            str:
                The minimumWipeAppVersion
        """
        if "minimumWipeAppVersion" in self._prop_dict:
            return self._prop_dict["minimumWipeAppVersion"]
        else:
            return None

    @minimum_wipe_app_version.setter
    def minimum_wipe_app_version(self, val):
        self._prop_dict["minimumWipeAppVersion"] = val

    @property
    def app_action_if_device_compliance_required(self):
        """
        Gets and sets the appActionIfDeviceComplianceRequired
        
        Returns: 
            :class:`ManagedAppRemediationAction<onedrivesdk.model.managed_app_remediation_action.ManagedAppRemediationAction>`:
                The appActionIfDeviceComplianceRequired
        """
        if "appActionIfDeviceComplianceRequired" in self._prop_dict:
            if isinstance(self._prop_dict["appActionIfDeviceComplianceRequired"], OneDriveObjectBase):
                return self._prop_dict["appActionIfDeviceComplianceRequired"]
            else :
                self._prop_dict["appActionIfDeviceComplianceRequired"] = ManagedAppRemediationAction(self._prop_dict["appActionIfDeviceComplianceRequired"])
                return self._prop_dict["appActionIfDeviceComplianceRequired"]

        return None

    @app_action_if_device_compliance_required.setter
    def app_action_if_device_compliance_required(self, val):
        self._prop_dict["appActionIfDeviceComplianceRequired"] = val

    @property
    def app_action_if_maximum_pin_retries_exceeded(self):
        """
        Gets and sets the appActionIfMaximumPinRetriesExceeded
        
        Returns: 
            :class:`ManagedAppRemediationAction<onedrivesdk.model.managed_app_remediation_action.ManagedAppRemediationAction>`:
                The appActionIfMaximumPinRetriesExceeded
        """
        if "appActionIfMaximumPinRetriesExceeded" in self._prop_dict:
            if isinstance(self._prop_dict["appActionIfMaximumPinRetriesExceeded"], OneDriveObjectBase):
                return self._prop_dict["appActionIfMaximumPinRetriesExceeded"]
            else :
                self._prop_dict["appActionIfMaximumPinRetriesExceeded"] = ManagedAppRemediationAction(self._prop_dict["appActionIfMaximumPinRetriesExceeded"])
                return self._prop_dict["appActionIfMaximumPinRetriesExceeded"]

        return None

    @app_action_if_maximum_pin_retries_exceeded.setter
    def app_action_if_maximum_pin_retries_exceeded(self, val):
        self._prop_dict["appActionIfMaximumPinRetriesExceeded"] = val

    @property
    def pin_required_on_launch_instead_of_biometric(self):
        """
        Gets and sets the pinRequiredOnLaunchInsteadOfBiometric
        
        Returns:
            bool:
                The pinRequiredOnLaunchInsteadOfBiometric
        """
        if "pinRequiredOnLaunchInsteadOfBiometric" in self._prop_dict:
            return self._prop_dict["pinRequiredOnLaunchInsteadOfBiometric"]
        else:
            return None

    @pin_required_on_launch_instead_of_biometric.setter
    def pin_required_on_launch_instead_of_biometric(self, val):
        self._prop_dict["pinRequiredOnLaunchInsteadOfBiometric"] = val

    @property
    def pin_required_instead_of_biometric_timeout(self):
        """
        Gets and sets the pinRequiredInsteadOfBiometricTimeout
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The pinRequiredInsteadOfBiometricTimeout
        """
        if "pinRequiredInsteadOfBiometricTimeout" in self._prop_dict:
            if isinstance(self._prop_dict["pinRequiredInsteadOfBiometricTimeout"], OneDriveObjectBase):
                return self._prop_dict["pinRequiredInsteadOfBiometricTimeout"]
            else :
                self._prop_dict["pinRequiredInsteadOfBiometricTimeout"] = Duration(self._prop_dict["pinRequiredInsteadOfBiometricTimeout"])
                return self._prop_dict["pinRequiredInsteadOfBiometricTimeout"]

        return None

    @pin_required_instead_of_biometric_timeout.setter
    def pin_required_instead_of_biometric_timeout(self, val):
        self._prop_dict["pinRequiredInsteadOfBiometricTimeout"] = val

