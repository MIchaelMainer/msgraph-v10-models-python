# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_list_item import AppListItem
from ..model.app_list_type import AppListType
from ..model.media_content_rating_australia import MediaContentRatingAustralia
from ..model.media_content_rating_canada import MediaContentRatingCanada
from ..model.media_content_rating_france import MediaContentRatingFrance
from ..model.media_content_rating_germany import MediaContentRatingGermany
from ..model.media_content_rating_ireland import MediaContentRatingIreland
from ..model.media_content_rating_japan import MediaContentRatingJapan
from ..model.media_content_rating_new_zealand import MediaContentRatingNewZealand
from ..model.media_content_rating_united_kingdom import MediaContentRatingUnitedKingdom
from ..model.media_content_rating_united_states import MediaContentRatingUnitedStates
from ..model.ios_network_usage_rule import IosNetworkUsageRule
from ..model.rating_apps_type import RatingAppsType
from ..model.required_password_type import RequiredPasswordType
from ..model.web_browser_cookie_settings import WebBrowserCookieSettings
from ..one_drive_object_base import OneDriveObjectBase


class IosGeneralDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_block_modification(self):
        """
        Gets and sets the accountBlockModification
        
        Returns:
            bool:
                The accountBlockModification
        """
        if "accountBlockModification" in self._prop_dict:
            return self._prop_dict["accountBlockModification"]
        else:
            return None

    @account_block_modification.setter
    def account_block_modification(self, val):
        self._prop_dict["accountBlockModification"] = val

    @property
    def activation_lock_allow_when_supervised(self):
        """
        Gets and sets the activationLockAllowWhenSupervised
        
        Returns:
            bool:
                The activationLockAllowWhenSupervised
        """
        if "activationLockAllowWhenSupervised" in self._prop_dict:
            return self._prop_dict["activationLockAllowWhenSupervised"]
        else:
            return None

    @activation_lock_allow_when_supervised.setter
    def activation_lock_allow_when_supervised(self, val):
        self._prop_dict["activationLockAllowWhenSupervised"] = val

    @property
    def air_drop_blocked(self):
        """
        Gets and sets the airDropBlocked
        
        Returns:
            bool:
                The airDropBlocked
        """
        if "airDropBlocked" in self._prop_dict:
            return self._prop_dict["airDropBlocked"]
        else:
            return None

    @air_drop_blocked.setter
    def air_drop_blocked(self, val):
        self._prop_dict["airDropBlocked"] = val

    @property
    def air_drop_force_unmanaged_drop_target(self):
        """
        Gets and sets the airDropForceUnmanagedDropTarget
        
        Returns:
            bool:
                The airDropForceUnmanagedDropTarget
        """
        if "airDropForceUnmanagedDropTarget" in self._prop_dict:
            return self._prop_dict["airDropForceUnmanagedDropTarget"]
        else:
            return None

    @air_drop_force_unmanaged_drop_target.setter
    def air_drop_force_unmanaged_drop_target(self, val):
        self._prop_dict["airDropForceUnmanagedDropTarget"] = val

    @property
    def air_play_force_pairing_password_for_outgoing_requests(self):
        """
        Gets and sets the airPlayForcePairingPasswordForOutgoingRequests
        
        Returns:
            bool:
                The airPlayForcePairingPasswordForOutgoingRequests
        """
        if "airPlayForcePairingPasswordForOutgoingRequests" in self._prop_dict:
            return self._prop_dict["airPlayForcePairingPasswordForOutgoingRequests"]
        else:
            return None

    @air_play_force_pairing_password_for_outgoing_requests.setter
    def air_play_force_pairing_password_for_outgoing_requests(self, val):
        self._prop_dict["airPlayForcePairingPasswordForOutgoingRequests"] = val

    @property
    def apple_watch_block_pairing(self):
        """
        Gets and sets the appleWatchBlockPairing
        
        Returns:
            bool:
                The appleWatchBlockPairing
        """
        if "appleWatchBlockPairing" in self._prop_dict:
            return self._prop_dict["appleWatchBlockPairing"]
        else:
            return None

    @apple_watch_block_pairing.setter
    def apple_watch_block_pairing(self, val):
        self._prop_dict["appleWatchBlockPairing"] = val

    @property
    def apple_watch_force_wrist_detection(self):
        """
        Gets and sets the appleWatchForceWristDetection
        
        Returns:
            bool:
                The appleWatchForceWristDetection
        """
        if "appleWatchForceWristDetection" in self._prop_dict:
            return self._prop_dict["appleWatchForceWristDetection"]
        else:
            return None

    @apple_watch_force_wrist_detection.setter
    def apple_watch_force_wrist_detection(self, val):
        self._prop_dict["appleWatchForceWristDetection"] = val

    @property
    def apple_news_blocked(self):
        """
        Gets and sets the appleNewsBlocked
        
        Returns:
            bool:
                The appleNewsBlocked
        """
        if "appleNewsBlocked" in self._prop_dict:
            return self._prop_dict["appleNewsBlocked"]
        else:
            return None

    @apple_news_blocked.setter
    def apple_news_blocked(self, val):
        self._prop_dict["appleNewsBlocked"] = val

    @property
    def apps_single_app_mode_list(self):
        """Gets and sets the appsSingleAppModeList
        
        Returns: 
            :class:`AppsSingleAppModeListCollectionPage<onedrivesdk.request.apps_single_app_mode_list_collection.AppsSingleAppModeListCollectionPage>`:
                The appsSingleAppModeList
        """
        if "appsSingleAppModeList" in self._prop_dict:
            return AppsSingleAppModeListCollectionPage(self._prop_dict["appsSingleAppModeList"])
        else:
            return None

    @property
    def apps_visibility_list(self):
        """Gets and sets the appsVisibilityList
        
        Returns: 
            :class:`AppsVisibilityListCollectionPage<onedrivesdk.request.apps_visibility_list_collection.AppsVisibilityListCollectionPage>`:
                The appsVisibilityList
        """
        if "appsVisibilityList" in self._prop_dict:
            return AppsVisibilityListCollectionPage(self._prop_dict["appsVisibilityList"])
        else:
            return None

    @property
    def apps_visibility_list_type(self):
        """
        Gets and sets the appsVisibilityListType
        
        Returns: 
            :class:`AppListType<onedrivesdk.model.app_list_type.AppListType>`:
                The appsVisibilityListType
        """
        if "appsVisibilityListType" in self._prop_dict:
            if isinstance(self._prop_dict["appsVisibilityListType"], OneDriveObjectBase):
                return self._prop_dict["appsVisibilityListType"]
            else :
                self._prop_dict["appsVisibilityListType"] = AppListType(self._prop_dict["appsVisibilityListType"])
                return self._prop_dict["appsVisibilityListType"]

        return None

    @apps_visibility_list_type.setter
    def apps_visibility_list_type(self, val):
        self._prop_dict["appsVisibilityListType"] = val

    @property
    def app_store_block_automatic_downloads(self):
        """
        Gets and sets the appStoreBlockAutomaticDownloads
        
        Returns:
            bool:
                The appStoreBlockAutomaticDownloads
        """
        if "appStoreBlockAutomaticDownloads" in self._prop_dict:
            return self._prop_dict["appStoreBlockAutomaticDownloads"]
        else:
            return None

    @app_store_block_automatic_downloads.setter
    def app_store_block_automatic_downloads(self, val):
        self._prop_dict["appStoreBlockAutomaticDownloads"] = val

    @property
    def app_store_blocked(self):
        """
        Gets and sets the appStoreBlocked
        
        Returns:
            bool:
                The appStoreBlocked
        """
        if "appStoreBlocked" in self._prop_dict:
            return self._prop_dict["appStoreBlocked"]
        else:
            return None

    @app_store_blocked.setter
    def app_store_blocked(self, val):
        self._prop_dict["appStoreBlocked"] = val

    @property
    def app_store_block_in_app_purchases(self):
        """
        Gets and sets the appStoreBlockInAppPurchases
        
        Returns:
            bool:
                The appStoreBlockInAppPurchases
        """
        if "appStoreBlockInAppPurchases" in self._prop_dict:
            return self._prop_dict["appStoreBlockInAppPurchases"]
        else:
            return None

    @app_store_block_in_app_purchases.setter
    def app_store_block_in_app_purchases(self, val):
        self._prop_dict["appStoreBlockInAppPurchases"] = val

    @property
    def app_store_block_ui_app_installation(self):
        """
        Gets and sets the appStoreBlockUIAppInstallation
        
        Returns:
            bool:
                The appStoreBlockUIAppInstallation
        """
        if "appStoreBlockUIAppInstallation" in self._prop_dict:
            return self._prop_dict["appStoreBlockUIAppInstallation"]
        else:
            return None

    @app_store_block_ui_app_installation.setter
    def app_store_block_ui_app_installation(self, val):
        self._prop_dict["appStoreBlockUIAppInstallation"] = val

    @property
    def app_store_require_password(self):
        """
        Gets and sets the appStoreRequirePassword
        
        Returns:
            bool:
                The appStoreRequirePassword
        """
        if "appStoreRequirePassword" in self._prop_dict:
            return self._prop_dict["appStoreRequirePassword"]
        else:
            return None

    @app_store_require_password.setter
    def app_store_require_password(self, val):
        self._prop_dict["appStoreRequirePassword"] = val

    @property
    def bluetooth_block_modification(self):
        """
        Gets and sets the bluetoothBlockModification
        
        Returns:
            bool:
                The bluetoothBlockModification
        """
        if "bluetoothBlockModification" in self._prop_dict:
            return self._prop_dict["bluetoothBlockModification"]
        else:
            return None

    @bluetooth_block_modification.setter
    def bluetooth_block_modification(self, val):
        self._prop_dict["bluetoothBlockModification"] = val

    @property
    def camera_blocked(self):
        """
        Gets and sets the cameraBlocked
        
        Returns:
            bool:
                The cameraBlocked
        """
        if "cameraBlocked" in self._prop_dict:
            return self._prop_dict["cameraBlocked"]
        else:
            return None

    @camera_blocked.setter
    def camera_blocked(self, val):
        self._prop_dict["cameraBlocked"] = val

    @property
    def cellular_block_data_roaming(self):
        """
        Gets and sets the cellularBlockDataRoaming
        
        Returns:
            bool:
                The cellularBlockDataRoaming
        """
        if "cellularBlockDataRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockDataRoaming"]
        else:
            return None

    @cellular_block_data_roaming.setter
    def cellular_block_data_roaming(self, val):
        self._prop_dict["cellularBlockDataRoaming"] = val

    @property
    def cellular_block_global_background_fetch_while_roaming(self):
        """
        Gets and sets the cellularBlockGlobalBackgroundFetchWhileRoaming
        
        Returns:
            bool:
                The cellularBlockGlobalBackgroundFetchWhileRoaming
        """
        if "cellularBlockGlobalBackgroundFetchWhileRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockGlobalBackgroundFetchWhileRoaming"]
        else:
            return None

    @cellular_block_global_background_fetch_while_roaming.setter
    def cellular_block_global_background_fetch_while_roaming(self, val):
        self._prop_dict["cellularBlockGlobalBackgroundFetchWhileRoaming"] = val

    @property
    def cellular_block_per_app_data_modification(self):
        """
        Gets and sets the cellularBlockPerAppDataModification
        
        Returns:
            bool:
                The cellularBlockPerAppDataModification
        """
        if "cellularBlockPerAppDataModification" in self._prop_dict:
            return self._prop_dict["cellularBlockPerAppDataModification"]
        else:
            return None

    @cellular_block_per_app_data_modification.setter
    def cellular_block_per_app_data_modification(self, val):
        self._prop_dict["cellularBlockPerAppDataModification"] = val

    @property
    def cellular_block_personal_hotspot(self):
        """
        Gets and sets the cellularBlockPersonalHotspot
        
        Returns:
            bool:
                The cellularBlockPersonalHotspot
        """
        if "cellularBlockPersonalHotspot" in self._prop_dict:
            return self._prop_dict["cellularBlockPersonalHotspot"]
        else:
            return None

    @cellular_block_personal_hotspot.setter
    def cellular_block_personal_hotspot(self, val):
        self._prop_dict["cellularBlockPersonalHotspot"] = val

    @property
    def cellular_block_voice_roaming(self):
        """
        Gets and sets the cellularBlockVoiceRoaming
        
        Returns:
            bool:
                The cellularBlockVoiceRoaming
        """
        if "cellularBlockVoiceRoaming" in self._prop_dict:
            return self._prop_dict["cellularBlockVoiceRoaming"]
        else:
            return None

    @cellular_block_voice_roaming.setter
    def cellular_block_voice_roaming(self, val):
        self._prop_dict["cellularBlockVoiceRoaming"] = val

    @property
    def certificates_block_untrusted_tls_certificates(self):
        """
        Gets and sets the certificatesBlockUntrustedTlsCertificates
        
        Returns:
            bool:
                The certificatesBlockUntrustedTlsCertificates
        """
        if "certificatesBlockUntrustedTlsCertificates" in self._prop_dict:
            return self._prop_dict["certificatesBlockUntrustedTlsCertificates"]
        else:
            return None

    @certificates_block_untrusted_tls_certificates.setter
    def certificates_block_untrusted_tls_certificates(self, val):
        self._prop_dict["certificatesBlockUntrustedTlsCertificates"] = val

    @property
    def classroom_app_block_remote_screen_observation(self):
        """
        Gets and sets the classroomAppBlockRemoteScreenObservation
        
        Returns:
            bool:
                The classroomAppBlockRemoteScreenObservation
        """
        if "classroomAppBlockRemoteScreenObservation" in self._prop_dict:
            return self._prop_dict["classroomAppBlockRemoteScreenObservation"]
        else:
            return None

    @classroom_app_block_remote_screen_observation.setter
    def classroom_app_block_remote_screen_observation(self, val):
        self._prop_dict["classroomAppBlockRemoteScreenObservation"] = val

    @property
    def classroom_app_force_unprompted_screen_observation(self):
        """
        Gets and sets the classroomAppForceUnpromptedScreenObservation
        
        Returns:
            bool:
                The classroomAppForceUnpromptedScreenObservation
        """
        if "classroomAppForceUnpromptedScreenObservation" in self._prop_dict:
            return self._prop_dict["classroomAppForceUnpromptedScreenObservation"]
        else:
            return None

    @classroom_app_force_unprompted_screen_observation.setter
    def classroom_app_force_unprompted_screen_observation(self, val):
        self._prop_dict["classroomAppForceUnpromptedScreenObservation"] = val

    @property
    def compliant_apps_list(self):
        """Gets and sets the compliantAppsList
        
        Returns: 
            :class:`CompliantAppsListCollectionPage<onedrivesdk.request.compliant_apps_list_collection.CompliantAppsListCollectionPage>`:
                The compliantAppsList
        """
        if "compliantAppsList" in self._prop_dict:
            return CompliantAppsListCollectionPage(self._prop_dict["compliantAppsList"])
        else:
            return None

    @property
    def compliant_app_list_type(self):
        """
        Gets and sets the compliantAppListType
        
        Returns: 
            :class:`AppListType<onedrivesdk.model.app_list_type.AppListType>`:
                The compliantAppListType
        """
        if "compliantAppListType" in self._prop_dict:
            if isinstance(self._prop_dict["compliantAppListType"], OneDriveObjectBase):
                return self._prop_dict["compliantAppListType"]
            else :
                self._prop_dict["compliantAppListType"] = AppListType(self._prop_dict["compliantAppListType"])
                return self._prop_dict["compliantAppListType"]

        return None

    @compliant_app_list_type.setter
    def compliant_app_list_type(self, val):
        self._prop_dict["compliantAppListType"] = val

    @property
    def configuration_profile_block_changes(self):
        """
        Gets and sets the configurationProfileBlockChanges
        
        Returns:
            bool:
                The configurationProfileBlockChanges
        """
        if "configurationProfileBlockChanges" in self._prop_dict:
            return self._prop_dict["configurationProfileBlockChanges"]
        else:
            return None

    @configuration_profile_block_changes.setter
    def configuration_profile_block_changes(self, val):
        self._prop_dict["configurationProfileBlockChanges"] = val

    @property
    def definition_lookup_blocked(self):
        """
        Gets and sets the definitionLookupBlocked
        
        Returns:
            bool:
                The definitionLookupBlocked
        """
        if "definitionLookupBlocked" in self._prop_dict:
            return self._prop_dict["definitionLookupBlocked"]
        else:
            return None

    @definition_lookup_blocked.setter
    def definition_lookup_blocked(self, val):
        self._prop_dict["definitionLookupBlocked"] = val

    @property
    def device_block_enable_restrictions(self):
        """
        Gets and sets the deviceBlockEnableRestrictions
        
        Returns:
            bool:
                The deviceBlockEnableRestrictions
        """
        if "deviceBlockEnableRestrictions" in self._prop_dict:
            return self._prop_dict["deviceBlockEnableRestrictions"]
        else:
            return None

    @device_block_enable_restrictions.setter
    def device_block_enable_restrictions(self, val):
        self._prop_dict["deviceBlockEnableRestrictions"] = val

    @property
    def device_block_erase_content_and_settings(self):
        """
        Gets and sets the deviceBlockEraseContentAndSettings
        
        Returns:
            bool:
                The deviceBlockEraseContentAndSettings
        """
        if "deviceBlockEraseContentAndSettings" in self._prop_dict:
            return self._prop_dict["deviceBlockEraseContentAndSettings"]
        else:
            return None

    @device_block_erase_content_and_settings.setter
    def device_block_erase_content_and_settings(self, val):
        self._prop_dict["deviceBlockEraseContentAndSettings"] = val

    @property
    def device_block_name_modification(self):
        """
        Gets and sets the deviceBlockNameModification
        
        Returns:
            bool:
                The deviceBlockNameModification
        """
        if "deviceBlockNameModification" in self._prop_dict:
            return self._prop_dict["deviceBlockNameModification"]
        else:
            return None

    @device_block_name_modification.setter
    def device_block_name_modification(self, val):
        self._prop_dict["deviceBlockNameModification"] = val

    @property
    def diagnostic_data_block_submission(self):
        """
        Gets and sets the diagnosticDataBlockSubmission
        
        Returns:
            bool:
                The diagnosticDataBlockSubmission
        """
        if "diagnosticDataBlockSubmission" in self._prop_dict:
            return self._prop_dict["diagnosticDataBlockSubmission"]
        else:
            return None

    @diagnostic_data_block_submission.setter
    def diagnostic_data_block_submission(self, val):
        self._prop_dict["diagnosticDataBlockSubmission"] = val

    @property
    def diagnostic_data_block_submission_modification(self):
        """
        Gets and sets the diagnosticDataBlockSubmissionModification
        
        Returns:
            bool:
                The diagnosticDataBlockSubmissionModification
        """
        if "diagnosticDataBlockSubmissionModification" in self._prop_dict:
            return self._prop_dict["diagnosticDataBlockSubmissionModification"]
        else:
            return None

    @diagnostic_data_block_submission_modification.setter
    def diagnostic_data_block_submission_modification(self, val):
        self._prop_dict["diagnosticDataBlockSubmissionModification"] = val

    @property
    def documents_block_managed_documents_in_unmanaged_apps(self):
        """
        Gets and sets the documentsBlockManagedDocumentsInUnmanagedApps
        
        Returns:
            bool:
                The documentsBlockManagedDocumentsInUnmanagedApps
        """
        if "documentsBlockManagedDocumentsInUnmanagedApps" in self._prop_dict:
            return self._prop_dict["documentsBlockManagedDocumentsInUnmanagedApps"]
        else:
            return None

    @documents_block_managed_documents_in_unmanaged_apps.setter
    def documents_block_managed_documents_in_unmanaged_apps(self, val):
        self._prop_dict["documentsBlockManagedDocumentsInUnmanagedApps"] = val

    @property
    def documents_block_unmanaged_documents_in_managed_apps(self):
        """
        Gets and sets the documentsBlockUnmanagedDocumentsInManagedApps
        
        Returns:
            bool:
                The documentsBlockUnmanagedDocumentsInManagedApps
        """
        if "documentsBlockUnmanagedDocumentsInManagedApps" in self._prop_dict:
            return self._prop_dict["documentsBlockUnmanagedDocumentsInManagedApps"]
        else:
            return None

    @documents_block_unmanaged_documents_in_managed_apps.setter
    def documents_block_unmanaged_documents_in_managed_apps(self, val):
        self._prop_dict["documentsBlockUnmanagedDocumentsInManagedApps"] = val

    @property
    def email_in_domain_suffixes(self):
        """
        Gets and sets the emailInDomainSuffixes
        
        Returns:
            str:
                The emailInDomainSuffixes
        """
        if "emailInDomainSuffixes" in self._prop_dict:
            return self._prop_dict["emailInDomainSuffixes"]
        else:
            return None

    @email_in_domain_suffixes.setter
    def email_in_domain_suffixes(self, val):
        self._prop_dict["emailInDomainSuffixes"] = val

    @property
    def enterprise_app_block_trust(self):
        """
        Gets and sets the enterpriseAppBlockTrust
        
        Returns:
            bool:
                The enterpriseAppBlockTrust
        """
        if "enterpriseAppBlockTrust" in self._prop_dict:
            return self._prop_dict["enterpriseAppBlockTrust"]
        else:
            return None

    @enterprise_app_block_trust.setter
    def enterprise_app_block_trust(self, val):
        self._prop_dict["enterpriseAppBlockTrust"] = val

    @property
    def enterprise_app_block_trust_modification(self):
        """
        Gets and sets the enterpriseAppBlockTrustModification
        
        Returns:
            bool:
                The enterpriseAppBlockTrustModification
        """
        if "enterpriseAppBlockTrustModification" in self._prop_dict:
            return self._prop_dict["enterpriseAppBlockTrustModification"]
        else:
            return None

    @enterprise_app_block_trust_modification.setter
    def enterprise_app_block_trust_modification(self, val):
        self._prop_dict["enterpriseAppBlockTrustModification"] = val

    @property
    def face_time_blocked(self):
        """
        Gets and sets the faceTimeBlocked
        
        Returns:
            bool:
                The faceTimeBlocked
        """
        if "faceTimeBlocked" in self._prop_dict:
            return self._prop_dict["faceTimeBlocked"]
        else:
            return None

    @face_time_blocked.setter
    def face_time_blocked(self, val):
        self._prop_dict["faceTimeBlocked"] = val

    @property
    def find_my_friends_blocked(self):
        """
        Gets and sets the findMyFriendsBlocked
        
        Returns:
            bool:
                The findMyFriendsBlocked
        """
        if "findMyFriendsBlocked" in self._prop_dict:
            return self._prop_dict["findMyFriendsBlocked"]
        else:
            return None

    @find_my_friends_blocked.setter
    def find_my_friends_blocked(self, val):
        self._prop_dict["findMyFriendsBlocked"] = val

    @property
    def gaming_block_game_center_friends(self):
        """
        Gets and sets the gamingBlockGameCenterFriends
        
        Returns:
            bool:
                The gamingBlockGameCenterFriends
        """
        if "gamingBlockGameCenterFriends" in self._prop_dict:
            return self._prop_dict["gamingBlockGameCenterFriends"]
        else:
            return None

    @gaming_block_game_center_friends.setter
    def gaming_block_game_center_friends(self, val):
        self._prop_dict["gamingBlockGameCenterFriends"] = val

    @property
    def gaming_block_multiplayer(self):
        """
        Gets and sets the gamingBlockMultiplayer
        
        Returns:
            bool:
                The gamingBlockMultiplayer
        """
        if "gamingBlockMultiplayer" in self._prop_dict:
            return self._prop_dict["gamingBlockMultiplayer"]
        else:
            return None

    @gaming_block_multiplayer.setter
    def gaming_block_multiplayer(self, val):
        self._prop_dict["gamingBlockMultiplayer"] = val

    @property
    def game_center_blocked(self):
        """
        Gets and sets the gameCenterBlocked
        
        Returns:
            bool:
                The gameCenterBlocked
        """
        if "gameCenterBlocked" in self._prop_dict:
            return self._prop_dict["gameCenterBlocked"]
        else:
            return None

    @game_center_blocked.setter
    def game_center_blocked(self, val):
        self._prop_dict["gameCenterBlocked"] = val

    @property
    def host_pairing_blocked(self):
        """
        Gets and sets the hostPairingBlocked
        
        Returns:
            bool:
                The hostPairingBlocked
        """
        if "hostPairingBlocked" in self._prop_dict:
            return self._prop_dict["hostPairingBlocked"]
        else:
            return None

    @host_pairing_blocked.setter
    def host_pairing_blocked(self, val):
        self._prop_dict["hostPairingBlocked"] = val

    @property
    def i_books_store_blocked(self):
        """
        Gets and sets the iBooksStoreBlocked
        
        Returns:
            bool:
                The iBooksStoreBlocked
        """
        if "iBooksStoreBlocked" in self._prop_dict:
            return self._prop_dict["iBooksStoreBlocked"]
        else:
            return None

    @i_books_store_blocked.setter
    def i_books_store_blocked(self, val):
        self._prop_dict["iBooksStoreBlocked"] = val

    @property
    def i_books_store_block_erotica(self):
        """
        Gets and sets the iBooksStoreBlockErotica
        
        Returns:
            bool:
                The iBooksStoreBlockErotica
        """
        if "iBooksStoreBlockErotica" in self._prop_dict:
            return self._prop_dict["iBooksStoreBlockErotica"]
        else:
            return None

    @i_books_store_block_erotica.setter
    def i_books_store_block_erotica(self, val):
        self._prop_dict["iBooksStoreBlockErotica"] = val

    @property
    def i_cloud_block_activity_continuation(self):
        """
        Gets and sets the iCloudBlockActivityContinuation
        
        Returns:
            bool:
                The iCloudBlockActivityContinuation
        """
        if "iCloudBlockActivityContinuation" in self._prop_dict:
            return self._prop_dict["iCloudBlockActivityContinuation"]
        else:
            return None

    @i_cloud_block_activity_continuation.setter
    def i_cloud_block_activity_continuation(self, val):
        self._prop_dict["iCloudBlockActivityContinuation"] = val

    @property
    def i_cloud_block_backup(self):
        """
        Gets and sets the iCloudBlockBackup
        
        Returns:
            bool:
                The iCloudBlockBackup
        """
        if "iCloudBlockBackup" in self._prop_dict:
            return self._prop_dict["iCloudBlockBackup"]
        else:
            return None

    @i_cloud_block_backup.setter
    def i_cloud_block_backup(self, val):
        self._prop_dict["iCloudBlockBackup"] = val

    @property
    def i_cloud_block_document_sync(self):
        """
        Gets and sets the iCloudBlockDocumentSync
        
        Returns:
            bool:
                The iCloudBlockDocumentSync
        """
        if "iCloudBlockDocumentSync" in self._prop_dict:
            return self._prop_dict["iCloudBlockDocumentSync"]
        else:
            return None

    @i_cloud_block_document_sync.setter
    def i_cloud_block_document_sync(self, val):
        self._prop_dict["iCloudBlockDocumentSync"] = val

    @property
    def i_cloud_block_managed_apps_sync(self):
        """
        Gets and sets the iCloudBlockManagedAppsSync
        
        Returns:
            bool:
                The iCloudBlockManagedAppsSync
        """
        if "iCloudBlockManagedAppsSync" in self._prop_dict:
            return self._prop_dict["iCloudBlockManagedAppsSync"]
        else:
            return None

    @i_cloud_block_managed_apps_sync.setter
    def i_cloud_block_managed_apps_sync(self, val):
        self._prop_dict["iCloudBlockManagedAppsSync"] = val

    @property
    def i_cloud_block_photo_library(self):
        """
        Gets and sets the iCloudBlockPhotoLibrary
        
        Returns:
            bool:
                The iCloudBlockPhotoLibrary
        """
        if "iCloudBlockPhotoLibrary" in self._prop_dict:
            return self._prop_dict["iCloudBlockPhotoLibrary"]
        else:
            return None

    @i_cloud_block_photo_library.setter
    def i_cloud_block_photo_library(self, val):
        self._prop_dict["iCloudBlockPhotoLibrary"] = val

    @property
    def i_cloud_block_photo_stream_sync(self):
        """
        Gets and sets the iCloudBlockPhotoStreamSync
        
        Returns:
            bool:
                The iCloudBlockPhotoStreamSync
        """
        if "iCloudBlockPhotoStreamSync" in self._prop_dict:
            return self._prop_dict["iCloudBlockPhotoStreamSync"]
        else:
            return None

    @i_cloud_block_photo_stream_sync.setter
    def i_cloud_block_photo_stream_sync(self, val):
        self._prop_dict["iCloudBlockPhotoStreamSync"] = val

    @property
    def i_cloud_block_shared_photo_stream(self):
        """
        Gets and sets the iCloudBlockSharedPhotoStream
        
        Returns:
            bool:
                The iCloudBlockSharedPhotoStream
        """
        if "iCloudBlockSharedPhotoStream" in self._prop_dict:
            return self._prop_dict["iCloudBlockSharedPhotoStream"]
        else:
            return None

    @i_cloud_block_shared_photo_stream.setter
    def i_cloud_block_shared_photo_stream(self, val):
        self._prop_dict["iCloudBlockSharedPhotoStream"] = val

    @property
    def i_cloud_require_encrypted_backup(self):
        """
        Gets and sets the iCloudRequireEncryptedBackup
        
        Returns:
            bool:
                The iCloudRequireEncryptedBackup
        """
        if "iCloudRequireEncryptedBackup" in self._prop_dict:
            return self._prop_dict["iCloudRequireEncryptedBackup"]
        else:
            return None

    @i_cloud_require_encrypted_backup.setter
    def i_cloud_require_encrypted_backup(self, val):
        self._prop_dict["iCloudRequireEncryptedBackup"] = val

    @property
    def i_tunes_block_explicit_content(self):
        """
        Gets and sets the iTunesBlockExplicitContent
        
        Returns:
            bool:
                The iTunesBlockExplicitContent
        """
        if "iTunesBlockExplicitContent" in self._prop_dict:
            return self._prop_dict["iTunesBlockExplicitContent"]
        else:
            return None

    @i_tunes_block_explicit_content.setter
    def i_tunes_block_explicit_content(self, val):
        self._prop_dict["iTunesBlockExplicitContent"] = val

    @property
    def i_tunes_block_music_service(self):
        """
        Gets and sets the iTunesBlockMusicService
        
        Returns:
            bool:
                The iTunesBlockMusicService
        """
        if "iTunesBlockMusicService" in self._prop_dict:
            return self._prop_dict["iTunesBlockMusicService"]
        else:
            return None

    @i_tunes_block_music_service.setter
    def i_tunes_block_music_service(self, val):
        self._prop_dict["iTunesBlockMusicService"] = val

    @property
    def i_tunes_block_radio(self):
        """
        Gets and sets the iTunesBlockRadio
        
        Returns:
            bool:
                The iTunesBlockRadio
        """
        if "iTunesBlockRadio" in self._prop_dict:
            return self._prop_dict["iTunesBlockRadio"]
        else:
            return None

    @i_tunes_block_radio.setter
    def i_tunes_block_radio(self, val):
        self._prop_dict["iTunesBlockRadio"] = val

    @property
    def keyboard_block_auto_correct(self):
        """
        Gets and sets the keyboardBlockAutoCorrect
        
        Returns:
            bool:
                The keyboardBlockAutoCorrect
        """
        if "keyboardBlockAutoCorrect" in self._prop_dict:
            return self._prop_dict["keyboardBlockAutoCorrect"]
        else:
            return None

    @keyboard_block_auto_correct.setter
    def keyboard_block_auto_correct(self, val):
        self._prop_dict["keyboardBlockAutoCorrect"] = val

    @property
    def keyboard_block_dictation(self):
        """
        Gets and sets the keyboardBlockDictation
        
        Returns:
            bool:
                The keyboardBlockDictation
        """
        if "keyboardBlockDictation" in self._prop_dict:
            return self._prop_dict["keyboardBlockDictation"]
        else:
            return None

    @keyboard_block_dictation.setter
    def keyboard_block_dictation(self, val):
        self._prop_dict["keyboardBlockDictation"] = val

    @property
    def keyboard_block_predictive(self):
        """
        Gets and sets the keyboardBlockPredictive
        
        Returns:
            bool:
                The keyboardBlockPredictive
        """
        if "keyboardBlockPredictive" in self._prop_dict:
            return self._prop_dict["keyboardBlockPredictive"]
        else:
            return None

    @keyboard_block_predictive.setter
    def keyboard_block_predictive(self, val):
        self._prop_dict["keyboardBlockPredictive"] = val

    @property
    def keyboard_block_shortcuts(self):
        """
        Gets and sets the keyboardBlockShortcuts
        
        Returns:
            bool:
                The keyboardBlockShortcuts
        """
        if "keyboardBlockShortcuts" in self._prop_dict:
            return self._prop_dict["keyboardBlockShortcuts"]
        else:
            return None

    @keyboard_block_shortcuts.setter
    def keyboard_block_shortcuts(self, val):
        self._prop_dict["keyboardBlockShortcuts"] = val

    @property
    def keyboard_block_spell_check(self):
        """
        Gets and sets the keyboardBlockSpellCheck
        
        Returns:
            bool:
                The keyboardBlockSpellCheck
        """
        if "keyboardBlockSpellCheck" in self._prop_dict:
            return self._prop_dict["keyboardBlockSpellCheck"]
        else:
            return None

    @keyboard_block_spell_check.setter
    def keyboard_block_spell_check(self, val):
        self._prop_dict["keyboardBlockSpellCheck"] = val

    @property
    def kiosk_mode_allow_assistive_speak(self):
        """
        Gets and sets the kioskModeAllowAssistiveSpeak
        
        Returns:
            bool:
                The kioskModeAllowAssistiveSpeak
        """
        if "kioskModeAllowAssistiveSpeak" in self._prop_dict:
            return self._prop_dict["kioskModeAllowAssistiveSpeak"]
        else:
            return None

    @kiosk_mode_allow_assistive_speak.setter
    def kiosk_mode_allow_assistive_speak(self, val):
        self._prop_dict["kioskModeAllowAssistiveSpeak"] = val

    @property
    def kiosk_mode_allow_assistive_touch_settings(self):
        """
        Gets and sets the kioskModeAllowAssistiveTouchSettings
        
        Returns:
            bool:
                The kioskModeAllowAssistiveTouchSettings
        """
        if "kioskModeAllowAssistiveTouchSettings" in self._prop_dict:
            return self._prop_dict["kioskModeAllowAssistiveTouchSettings"]
        else:
            return None

    @kiosk_mode_allow_assistive_touch_settings.setter
    def kiosk_mode_allow_assistive_touch_settings(self, val):
        self._prop_dict["kioskModeAllowAssistiveTouchSettings"] = val

    @property
    def kiosk_mode_allow_auto_lock(self):
        """
        Gets and sets the kioskModeAllowAutoLock
        
        Returns:
            bool:
                The kioskModeAllowAutoLock
        """
        if "kioskModeAllowAutoLock" in self._prop_dict:
            return self._prop_dict["kioskModeAllowAutoLock"]
        else:
            return None

    @kiosk_mode_allow_auto_lock.setter
    def kiosk_mode_allow_auto_lock(self, val):
        self._prop_dict["kioskModeAllowAutoLock"] = val

    @property
    def kiosk_mode_allow_color_inversion_settings(self):
        """
        Gets and sets the kioskModeAllowColorInversionSettings
        
        Returns:
            bool:
                The kioskModeAllowColorInversionSettings
        """
        if "kioskModeAllowColorInversionSettings" in self._prop_dict:
            return self._prop_dict["kioskModeAllowColorInversionSettings"]
        else:
            return None

    @kiosk_mode_allow_color_inversion_settings.setter
    def kiosk_mode_allow_color_inversion_settings(self, val):
        self._prop_dict["kioskModeAllowColorInversionSettings"] = val

    @property
    def kiosk_mode_allow_ringer_switch(self):
        """
        Gets and sets the kioskModeAllowRingerSwitch
        
        Returns:
            bool:
                The kioskModeAllowRingerSwitch
        """
        if "kioskModeAllowRingerSwitch" in self._prop_dict:
            return self._prop_dict["kioskModeAllowRingerSwitch"]
        else:
            return None

    @kiosk_mode_allow_ringer_switch.setter
    def kiosk_mode_allow_ringer_switch(self, val):
        self._prop_dict["kioskModeAllowRingerSwitch"] = val

    @property
    def kiosk_mode_allow_screen_rotation(self):
        """
        Gets and sets the kioskModeAllowScreenRotation
        
        Returns:
            bool:
                The kioskModeAllowScreenRotation
        """
        if "kioskModeAllowScreenRotation" in self._prop_dict:
            return self._prop_dict["kioskModeAllowScreenRotation"]
        else:
            return None

    @kiosk_mode_allow_screen_rotation.setter
    def kiosk_mode_allow_screen_rotation(self, val):
        self._prop_dict["kioskModeAllowScreenRotation"] = val

    @property
    def kiosk_mode_allow_sleep_button(self):
        """
        Gets and sets the kioskModeAllowSleepButton
        
        Returns:
            bool:
                The kioskModeAllowSleepButton
        """
        if "kioskModeAllowSleepButton" in self._prop_dict:
            return self._prop_dict["kioskModeAllowSleepButton"]
        else:
            return None

    @kiosk_mode_allow_sleep_button.setter
    def kiosk_mode_allow_sleep_button(self, val):
        self._prop_dict["kioskModeAllowSleepButton"] = val

    @property
    def kiosk_mode_allow_touchscreen(self):
        """
        Gets and sets the kioskModeAllowTouchscreen
        
        Returns:
            bool:
                The kioskModeAllowTouchscreen
        """
        if "kioskModeAllowTouchscreen" in self._prop_dict:
            return self._prop_dict["kioskModeAllowTouchscreen"]
        else:
            return None

    @kiosk_mode_allow_touchscreen.setter
    def kiosk_mode_allow_touchscreen(self, val):
        self._prop_dict["kioskModeAllowTouchscreen"] = val

    @property
    def kiosk_mode_allow_voice_over_settings(self):
        """
        Gets and sets the kioskModeAllowVoiceOverSettings
        
        Returns:
            bool:
                The kioskModeAllowVoiceOverSettings
        """
        if "kioskModeAllowVoiceOverSettings" in self._prop_dict:
            return self._prop_dict["kioskModeAllowVoiceOverSettings"]
        else:
            return None

    @kiosk_mode_allow_voice_over_settings.setter
    def kiosk_mode_allow_voice_over_settings(self, val):
        self._prop_dict["kioskModeAllowVoiceOverSettings"] = val

    @property
    def kiosk_mode_allow_volume_buttons(self):
        """
        Gets and sets the kioskModeAllowVolumeButtons
        
        Returns:
            bool:
                The kioskModeAllowVolumeButtons
        """
        if "kioskModeAllowVolumeButtons" in self._prop_dict:
            return self._prop_dict["kioskModeAllowVolumeButtons"]
        else:
            return None

    @kiosk_mode_allow_volume_buttons.setter
    def kiosk_mode_allow_volume_buttons(self, val):
        self._prop_dict["kioskModeAllowVolumeButtons"] = val

    @property
    def kiosk_mode_allow_zoom_settings(self):
        """
        Gets and sets the kioskModeAllowZoomSettings
        
        Returns:
            bool:
                The kioskModeAllowZoomSettings
        """
        if "kioskModeAllowZoomSettings" in self._prop_dict:
            return self._prop_dict["kioskModeAllowZoomSettings"]
        else:
            return None

    @kiosk_mode_allow_zoom_settings.setter
    def kiosk_mode_allow_zoom_settings(self, val):
        self._prop_dict["kioskModeAllowZoomSettings"] = val

    @property
    def kiosk_mode_app_store_url(self):
        """
        Gets and sets the kioskModeAppStoreUrl
        
        Returns:
            str:
                The kioskModeAppStoreUrl
        """
        if "kioskModeAppStoreUrl" in self._prop_dict:
            return self._prop_dict["kioskModeAppStoreUrl"]
        else:
            return None

    @kiosk_mode_app_store_url.setter
    def kiosk_mode_app_store_url(self, val):
        self._prop_dict["kioskModeAppStoreUrl"] = val

    @property
    def kiosk_mode_require_assistive_touch(self):
        """
        Gets and sets the kioskModeRequireAssistiveTouch
        
        Returns:
            bool:
                The kioskModeRequireAssistiveTouch
        """
        if "kioskModeRequireAssistiveTouch" in self._prop_dict:
            return self._prop_dict["kioskModeRequireAssistiveTouch"]
        else:
            return None

    @kiosk_mode_require_assistive_touch.setter
    def kiosk_mode_require_assistive_touch(self, val):
        self._prop_dict["kioskModeRequireAssistiveTouch"] = val

    @property
    def kiosk_mode_require_color_inversion(self):
        """
        Gets and sets the kioskModeRequireColorInversion
        
        Returns:
            bool:
                The kioskModeRequireColorInversion
        """
        if "kioskModeRequireColorInversion" in self._prop_dict:
            return self._prop_dict["kioskModeRequireColorInversion"]
        else:
            return None

    @kiosk_mode_require_color_inversion.setter
    def kiosk_mode_require_color_inversion(self, val):
        self._prop_dict["kioskModeRequireColorInversion"] = val

    @property
    def kiosk_mode_require_mono_audio(self):
        """
        Gets and sets the kioskModeRequireMonoAudio
        
        Returns:
            bool:
                The kioskModeRequireMonoAudio
        """
        if "kioskModeRequireMonoAudio" in self._prop_dict:
            return self._prop_dict["kioskModeRequireMonoAudio"]
        else:
            return None

    @kiosk_mode_require_mono_audio.setter
    def kiosk_mode_require_mono_audio(self, val):
        self._prop_dict["kioskModeRequireMonoAudio"] = val

    @property
    def kiosk_mode_require_voice_over(self):
        """
        Gets and sets the kioskModeRequireVoiceOver
        
        Returns:
            bool:
                The kioskModeRequireVoiceOver
        """
        if "kioskModeRequireVoiceOver" in self._prop_dict:
            return self._prop_dict["kioskModeRequireVoiceOver"]
        else:
            return None

    @kiosk_mode_require_voice_over.setter
    def kiosk_mode_require_voice_over(self, val):
        self._prop_dict["kioskModeRequireVoiceOver"] = val

    @property
    def kiosk_mode_require_zoom(self):
        """
        Gets and sets the kioskModeRequireZoom
        
        Returns:
            bool:
                The kioskModeRequireZoom
        """
        if "kioskModeRequireZoom" in self._prop_dict:
            return self._prop_dict["kioskModeRequireZoom"]
        else:
            return None

    @kiosk_mode_require_zoom.setter
    def kiosk_mode_require_zoom(self, val):
        self._prop_dict["kioskModeRequireZoom"] = val

    @property
    def kiosk_mode_managed_app_id(self):
        """
        Gets and sets the kioskModeManagedAppId
        
        Returns:
            str:
                The kioskModeManagedAppId
        """
        if "kioskModeManagedAppId" in self._prop_dict:
            return self._prop_dict["kioskModeManagedAppId"]
        else:
            return None

    @kiosk_mode_managed_app_id.setter
    def kiosk_mode_managed_app_id(self, val):
        self._prop_dict["kioskModeManagedAppId"] = val

    @property
    def lock_screen_block_control_center(self):
        """
        Gets and sets the lockScreenBlockControlCenter
        
        Returns:
            bool:
                The lockScreenBlockControlCenter
        """
        if "lockScreenBlockControlCenter" in self._prop_dict:
            return self._prop_dict["lockScreenBlockControlCenter"]
        else:
            return None

    @lock_screen_block_control_center.setter
    def lock_screen_block_control_center(self, val):
        self._prop_dict["lockScreenBlockControlCenter"] = val

    @property
    def lock_screen_block_notification_view(self):
        """
        Gets and sets the lockScreenBlockNotificationView
        
        Returns:
            bool:
                The lockScreenBlockNotificationView
        """
        if "lockScreenBlockNotificationView" in self._prop_dict:
            return self._prop_dict["lockScreenBlockNotificationView"]
        else:
            return None

    @lock_screen_block_notification_view.setter
    def lock_screen_block_notification_view(self, val):
        self._prop_dict["lockScreenBlockNotificationView"] = val

    @property
    def lock_screen_block_passbook(self):
        """
        Gets and sets the lockScreenBlockPassbook
        
        Returns:
            bool:
                The lockScreenBlockPassbook
        """
        if "lockScreenBlockPassbook" in self._prop_dict:
            return self._prop_dict["lockScreenBlockPassbook"]
        else:
            return None

    @lock_screen_block_passbook.setter
    def lock_screen_block_passbook(self, val):
        self._prop_dict["lockScreenBlockPassbook"] = val

    @property
    def lock_screen_block_today_view(self):
        """
        Gets and sets the lockScreenBlockTodayView
        
        Returns:
            bool:
                The lockScreenBlockTodayView
        """
        if "lockScreenBlockTodayView" in self._prop_dict:
            return self._prop_dict["lockScreenBlockTodayView"]
        else:
            return None

    @lock_screen_block_today_view.setter
    def lock_screen_block_today_view(self, val):
        self._prop_dict["lockScreenBlockTodayView"] = val

    @property
    def media_content_rating_australia(self):
        """
        Gets and sets the mediaContentRatingAustralia
        
        Returns: 
            :class:`MediaContentRatingAustralia<onedrivesdk.model.media_content_rating_australia.MediaContentRatingAustralia>`:
                The mediaContentRatingAustralia
        """
        if "mediaContentRatingAustralia" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingAustralia"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingAustralia"]
            else :
                self._prop_dict["mediaContentRatingAustralia"] = MediaContentRatingAustralia(self._prop_dict["mediaContentRatingAustralia"])
                return self._prop_dict["mediaContentRatingAustralia"]

        return None

    @media_content_rating_australia.setter
    def media_content_rating_australia(self, val):
        self._prop_dict["mediaContentRatingAustralia"] = val

    @property
    def media_content_rating_canada(self):
        """
        Gets and sets the mediaContentRatingCanada
        
        Returns: 
            :class:`MediaContentRatingCanada<onedrivesdk.model.media_content_rating_canada.MediaContentRatingCanada>`:
                The mediaContentRatingCanada
        """
        if "mediaContentRatingCanada" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingCanada"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingCanada"]
            else :
                self._prop_dict["mediaContentRatingCanada"] = MediaContentRatingCanada(self._prop_dict["mediaContentRatingCanada"])
                return self._prop_dict["mediaContentRatingCanada"]

        return None

    @media_content_rating_canada.setter
    def media_content_rating_canada(self, val):
        self._prop_dict["mediaContentRatingCanada"] = val

    @property
    def media_content_rating_france(self):
        """
        Gets and sets the mediaContentRatingFrance
        
        Returns: 
            :class:`MediaContentRatingFrance<onedrivesdk.model.media_content_rating_france.MediaContentRatingFrance>`:
                The mediaContentRatingFrance
        """
        if "mediaContentRatingFrance" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingFrance"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingFrance"]
            else :
                self._prop_dict["mediaContentRatingFrance"] = MediaContentRatingFrance(self._prop_dict["mediaContentRatingFrance"])
                return self._prop_dict["mediaContentRatingFrance"]

        return None

    @media_content_rating_france.setter
    def media_content_rating_france(self, val):
        self._prop_dict["mediaContentRatingFrance"] = val

    @property
    def media_content_rating_germany(self):
        """
        Gets and sets the mediaContentRatingGermany
        
        Returns: 
            :class:`MediaContentRatingGermany<onedrivesdk.model.media_content_rating_germany.MediaContentRatingGermany>`:
                The mediaContentRatingGermany
        """
        if "mediaContentRatingGermany" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingGermany"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingGermany"]
            else :
                self._prop_dict["mediaContentRatingGermany"] = MediaContentRatingGermany(self._prop_dict["mediaContentRatingGermany"])
                return self._prop_dict["mediaContentRatingGermany"]

        return None

    @media_content_rating_germany.setter
    def media_content_rating_germany(self, val):
        self._prop_dict["mediaContentRatingGermany"] = val

    @property
    def media_content_rating_ireland(self):
        """
        Gets and sets the mediaContentRatingIreland
        
        Returns: 
            :class:`MediaContentRatingIreland<onedrivesdk.model.media_content_rating_ireland.MediaContentRatingIreland>`:
                The mediaContentRatingIreland
        """
        if "mediaContentRatingIreland" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingIreland"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingIreland"]
            else :
                self._prop_dict["mediaContentRatingIreland"] = MediaContentRatingIreland(self._prop_dict["mediaContentRatingIreland"])
                return self._prop_dict["mediaContentRatingIreland"]

        return None

    @media_content_rating_ireland.setter
    def media_content_rating_ireland(self, val):
        self._prop_dict["mediaContentRatingIreland"] = val

    @property
    def media_content_rating_japan(self):
        """
        Gets and sets the mediaContentRatingJapan
        
        Returns: 
            :class:`MediaContentRatingJapan<onedrivesdk.model.media_content_rating_japan.MediaContentRatingJapan>`:
                The mediaContentRatingJapan
        """
        if "mediaContentRatingJapan" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingJapan"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingJapan"]
            else :
                self._prop_dict["mediaContentRatingJapan"] = MediaContentRatingJapan(self._prop_dict["mediaContentRatingJapan"])
                return self._prop_dict["mediaContentRatingJapan"]

        return None

    @media_content_rating_japan.setter
    def media_content_rating_japan(self, val):
        self._prop_dict["mediaContentRatingJapan"] = val

    @property
    def media_content_rating_new_zealand(self):
        """
        Gets and sets the mediaContentRatingNewZealand
        
        Returns: 
            :class:`MediaContentRatingNewZealand<onedrivesdk.model.media_content_rating_new_zealand.MediaContentRatingNewZealand>`:
                The mediaContentRatingNewZealand
        """
        if "mediaContentRatingNewZealand" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingNewZealand"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingNewZealand"]
            else :
                self._prop_dict["mediaContentRatingNewZealand"] = MediaContentRatingNewZealand(self._prop_dict["mediaContentRatingNewZealand"])
                return self._prop_dict["mediaContentRatingNewZealand"]

        return None

    @media_content_rating_new_zealand.setter
    def media_content_rating_new_zealand(self, val):
        self._prop_dict["mediaContentRatingNewZealand"] = val

    @property
    def media_content_rating_united_kingdom(self):
        """
        Gets and sets the mediaContentRatingUnitedKingdom
        
        Returns: 
            :class:`MediaContentRatingUnitedKingdom<onedrivesdk.model.media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom>`:
                The mediaContentRatingUnitedKingdom
        """
        if "mediaContentRatingUnitedKingdom" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingUnitedKingdom"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingUnitedKingdom"]
            else :
                self._prop_dict["mediaContentRatingUnitedKingdom"] = MediaContentRatingUnitedKingdom(self._prop_dict["mediaContentRatingUnitedKingdom"])
                return self._prop_dict["mediaContentRatingUnitedKingdom"]

        return None

    @media_content_rating_united_kingdom.setter
    def media_content_rating_united_kingdom(self, val):
        self._prop_dict["mediaContentRatingUnitedKingdom"] = val

    @property
    def media_content_rating_united_states(self):
        """
        Gets and sets the mediaContentRatingUnitedStates
        
        Returns: 
            :class:`MediaContentRatingUnitedStates<onedrivesdk.model.media_content_rating_united_states.MediaContentRatingUnitedStates>`:
                The mediaContentRatingUnitedStates
        """
        if "mediaContentRatingUnitedStates" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingUnitedStates"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingUnitedStates"]
            else :
                self._prop_dict["mediaContentRatingUnitedStates"] = MediaContentRatingUnitedStates(self._prop_dict["mediaContentRatingUnitedStates"])
                return self._prop_dict["mediaContentRatingUnitedStates"]

        return None

    @media_content_rating_united_states.setter
    def media_content_rating_united_states(self, val):
        self._prop_dict["mediaContentRatingUnitedStates"] = val

    @property
    def network_usage_rules(self):
        """Gets and sets the networkUsageRules
        
        Returns: 
            :class:`NetworkUsageRulesCollectionPage<onedrivesdk.request.network_usage_rules_collection.NetworkUsageRulesCollectionPage>`:
                The networkUsageRules
        """
        if "networkUsageRules" in self._prop_dict:
            return NetworkUsageRulesCollectionPage(self._prop_dict["networkUsageRules"])
        else:
            return None

    @property
    def media_content_rating_apps(self):
        """
        Gets and sets the mediaContentRatingApps
        
        Returns: 
            :class:`RatingAppsType<onedrivesdk.model.rating_apps_type.RatingAppsType>`:
                The mediaContentRatingApps
        """
        if "mediaContentRatingApps" in self._prop_dict:
            if isinstance(self._prop_dict["mediaContentRatingApps"], OneDriveObjectBase):
                return self._prop_dict["mediaContentRatingApps"]
            else :
                self._prop_dict["mediaContentRatingApps"] = RatingAppsType(self._prop_dict["mediaContentRatingApps"])
                return self._prop_dict["mediaContentRatingApps"]

        return None

    @media_content_rating_apps.setter
    def media_content_rating_apps(self, val):
        self._prop_dict["mediaContentRatingApps"] = val

    @property
    def messages_blocked(self):
        """
        Gets and sets the messagesBlocked
        
        Returns:
            bool:
                The messagesBlocked
        """
        if "messagesBlocked" in self._prop_dict:
            return self._prop_dict["messagesBlocked"]
        else:
            return None

    @messages_blocked.setter
    def messages_blocked(self, val):
        self._prop_dict["messagesBlocked"] = val

    @property
    def notifications_block_settings_modification(self):
        """
        Gets and sets the notificationsBlockSettingsModification
        
        Returns:
            bool:
                The notificationsBlockSettingsModification
        """
        if "notificationsBlockSettingsModification" in self._prop_dict:
            return self._prop_dict["notificationsBlockSettingsModification"]
        else:
            return None

    @notifications_block_settings_modification.setter
    def notifications_block_settings_modification(self, val):
        self._prop_dict["notificationsBlockSettingsModification"] = val

    @property
    def passcode_block_fingerprint_unlock(self):
        """
        Gets and sets the passcodeBlockFingerprintUnlock
        
        Returns:
            bool:
                The passcodeBlockFingerprintUnlock
        """
        if "passcodeBlockFingerprintUnlock" in self._prop_dict:
            return self._prop_dict["passcodeBlockFingerprintUnlock"]
        else:
            return None

    @passcode_block_fingerprint_unlock.setter
    def passcode_block_fingerprint_unlock(self, val):
        self._prop_dict["passcodeBlockFingerprintUnlock"] = val

    @property
    def passcode_block_fingerprint_modification(self):
        """
        Gets and sets the passcodeBlockFingerprintModification
        
        Returns:
            bool:
                The passcodeBlockFingerprintModification
        """
        if "passcodeBlockFingerprintModification" in self._prop_dict:
            return self._prop_dict["passcodeBlockFingerprintModification"]
        else:
            return None

    @passcode_block_fingerprint_modification.setter
    def passcode_block_fingerprint_modification(self, val):
        self._prop_dict["passcodeBlockFingerprintModification"] = val

    @property
    def passcode_block_modification(self):
        """
        Gets and sets the passcodeBlockModification
        
        Returns:
            bool:
                The passcodeBlockModification
        """
        if "passcodeBlockModification" in self._prop_dict:
            return self._prop_dict["passcodeBlockModification"]
        else:
            return None

    @passcode_block_modification.setter
    def passcode_block_modification(self, val):
        self._prop_dict["passcodeBlockModification"] = val

    @property
    def passcode_block_simple(self):
        """
        Gets and sets the passcodeBlockSimple
        
        Returns:
            bool:
                The passcodeBlockSimple
        """
        if "passcodeBlockSimple" in self._prop_dict:
            return self._prop_dict["passcodeBlockSimple"]
        else:
            return None

    @passcode_block_simple.setter
    def passcode_block_simple(self, val):
        self._prop_dict["passcodeBlockSimple"] = val

    @property
    def passcode_expiration_days(self):
        """
        Gets and sets the passcodeExpirationDays
        
        Returns:
            int:
                The passcodeExpirationDays
        """
        if "passcodeExpirationDays" in self._prop_dict:
            return self._prop_dict["passcodeExpirationDays"]
        else:
            return None

    @passcode_expiration_days.setter
    def passcode_expiration_days(self, val):
        self._prop_dict["passcodeExpirationDays"] = val

    @property
    def passcode_minimum_length(self):
        """
        Gets and sets the passcodeMinimumLength
        
        Returns:
            int:
                The passcodeMinimumLength
        """
        if "passcodeMinimumLength" in self._prop_dict:
            return self._prop_dict["passcodeMinimumLength"]
        else:
            return None

    @passcode_minimum_length.setter
    def passcode_minimum_length(self, val):
        self._prop_dict["passcodeMinimumLength"] = val

    @property
    def passcode_minutes_of_inactivity_before_lock(self):
        """
        Gets and sets the passcodeMinutesOfInactivityBeforeLock
        
        Returns:
            int:
                The passcodeMinutesOfInactivityBeforeLock
        """
        if "passcodeMinutesOfInactivityBeforeLock" in self._prop_dict:
            return self._prop_dict["passcodeMinutesOfInactivityBeforeLock"]
        else:
            return None

    @passcode_minutes_of_inactivity_before_lock.setter
    def passcode_minutes_of_inactivity_before_lock(self, val):
        self._prop_dict["passcodeMinutesOfInactivityBeforeLock"] = val

    @property
    def passcode_minutes_of_inactivity_before_screen_timeout(self):
        """
        Gets and sets the passcodeMinutesOfInactivityBeforeScreenTimeout
        
        Returns:
            int:
                The passcodeMinutesOfInactivityBeforeScreenTimeout
        """
        if "passcodeMinutesOfInactivityBeforeScreenTimeout" in self._prop_dict:
            return self._prop_dict["passcodeMinutesOfInactivityBeforeScreenTimeout"]
        else:
            return None

    @passcode_minutes_of_inactivity_before_screen_timeout.setter
    def passcode_minutes_of_inactivity_before_screen_timeout(self, val):
        self._prop_dict["passcodeMinutesOfInactivityBeforeScreenTimeout"] = val

    @property
    def passcode_minimum_character_set_count(self):
        """
        Gets and sets the passcodeMinimumCharacterSetCount
        
        Returns:
            int:
                The passcodeMinimumCharacterSetCount
        """
        if "passcodeMinimumCharacterSetCount" in self._prop_dict:
            return self._prop_dict["passcodeMinimumCharacterSetCount"]
        else:
            return None

    @passcode_minimum_character_set_count.setter
    def passcode_minimum_character_set_count(self, val):
        self._prop_dict["passcodeMinimumCharacterSetCount"] = val

    @property
    def passcode_previous_passcode_block_count(self):
        """
        Gets and sets the passcodePreviousPasscodeBlockCount
        
        Returns:
            int:
                The passcodePreviousPasscodeBlockCount
        """
        if "passcodePreviousPasscodeBlockCount" in self._prop_dict:
            return self._prop_dict["passcodePreviousPasscodeBlockCount"]
        else:
            return None

    @passcode_previous_passcode_block_count.setter
    def passcode_previous_passcode_block_count(self, val):
        self._prop_dict["passcodePreviousPasscodeBlockCount"] = val

    @property
    def passcode_sign_in_failure_count_before_wipe(self):
        """
        Gets and sets the passcodeSignInFailureCountBeforeWipe
        
        Returns:
            int:
                The passcodeSignInFailureCountBeforeWipe
        """
        if "passcodeSignInFailureCountBeforeWipe" in self._prop_dict:
            return self._prop_dict["passcodeSignInFailureCountBeforeWipe"]
        else:
            return None

    @passcode_sign_in_failure_count_before_wipe.setter
    def passcode_sign_in_failure_count_before_wipe(self, val):
        self._prop_dict["passcodeSignInFailureCountBeforeWipe"] = val

    @property
    def passcode_required_type(self):
        """
        Gets and sets the passcodeRequiredType
        
        Returns: 
            :class:`RequiredPasswordType<onedrivesdk.model.required_password_type.RequiredPasswordType>`:
                The passcodeRequiredType
        """
        if "passcodeRequiredType" in self._prop_dict:
            if isinstance(self._prop_dict["passcodeRequiredType"], OneDriveObjectBase):
                return self._prop_dict["passcodeRequiredType"]
            else :
                self._prop_dict["passcodeRequiredType"] = RequiredPasswordType(self._prop_dict["passcodeRequiredType"])
                return self._prop_dict["passcodeRequiredType"]

        return None

    @passcode_required_type.setter
    def passcode_required_type(self, val):
        self._prop_dict["passcodeRequiredType"] = val

    @property
    def passcode_required(self):
        """
        Gets and sets the passcodeRequired
        
        Returns:
            bool:
                The passcodeRequired
        """
        if "passcodeRequired" in self._prop_dict:
            return self._prop_dict["passcodeRequired"]
        else:
            return None

    @passcode_required.setter
    def passcode_required(self, val):
        self._prop_dict["passcodeRequired"] = val

    @property
    def podcasts_blocked(self):
        """
        Gets and sets the podcastsBlocked
        
        Returns:
            bool:
                The podcastsBlocked
        """
        if "podcastsBlocked" in self._prop_dict:
            return self._prop_dict["podcastsBlocked"]
        else:
            return None

    @podcasts_blocked.setter
    def podcasts_blocked(self, val):
        self._prop_dict["podcastsBlocked"] = val

    @property
    def safari_block_autofill(self):
        """
        Gets and sets the safariBlockAutofill
        
        Returns:
            bool:
                The safariBlockAutofill
        """
        if "safariBlockAutofill" in self._prop_dict:
            return self._prop_dict["safariBlockAutofill"]
        else:
            return None

    @safari_block_autofill.setter
    def safari_block_autofill(self, val):
        self._prop_dict["safariBlockAutofill"] = val

    @property
    def safari_block_java_script(self):
        """
        Gets and sets the safariBlockJavaScript
        
        Returns:
            bool:
                The safariBlockJavaScript
        """
        if "safariBlockJavaScript" in self._prop_dict:
            return self._prop_dict["safariBlockJavaScript"]
        else:
            return None

    @safari_block_java_script.setter
    def safari_block_java_script(self, val):
        self._prop_dict["safariBlockJavaScript"] = val

    @property
    def safari_block_popups(self):
        """
        Gets and sets the safariBlockPopups
        
        Returns:
            bool:
                The safariBlockPopups
        """
        if "safariBlockPopups" in self._prop_dict:
            return self._prop_dict["safariBlockPopups"]
        else:
            return None

    @safari_block_popups.setter
    def safari_block_popups(self, val):
        self._prop_dict["safariBlockPopups"] = val

    @property
    def safari_blocked(self):
        """
        Gets and sets the safariBlocked
        
        Returns:
            bool:
                The safariBlocked
        """
        if "safariBlocked" in self._prop_dict:
            return self._prop_dict["safariBlocked"]
        else:
            return None

    @safari_blocked.setter
    def safari_blocked(self, val):
        self._prop_dict["safariBlocked"] = val

    @property
    def safari_cookie_settings(self):
        """
        Gets and sets the safariCookieSettings
        
        Returns: 
            :class:`WebBrowserCookieSettings<onedrivesdk.model.web_browser_cookie_settings.WebBrowserCookieSettings>`:
                The safariCookieSettings
        """
        if "safariCookieSettings" in self._prop_dict:
            if isinstance(self._prop_dict["safariCookieSettings"], OneDriveObjectBase):
                return self._prop_dict["safariCookieSettings"]
            else :
                self._prop_dict["safariCookieSettings"] = WebBrowserCookieSettings(self._prop_dict["safariCookieSettings"])
                return self._prop_dict["safariCookieSettings"]

        return None

    @safari_cookie_settings.setter
    def safari_cookie_settings(self, val):
        self._prop_dict["safariCookieSettings"] = val

    @property
    def safari_managed_domains(self):
        """
        Gets and sets the safariManagedDomains
        
        Returns:
            str:
                The safariManagedDomains
        """
        if "safariManagedDomains" in self._prop_dict:
            return self._prop_dict["safariManagedDomains"]
        else:
            return None

    @safari_managed_domains.setter
    def safari_managed_domains(self, val):
        self._prop_dict["safariManagedDomains"] = val

    @property
    def safari_password_auto_fill_domains(self):
        """
        Gets and sets the safariPasswordAutoFillDomains
        
        Returns:
            str:
                The safariPasswordAutoFillDomains
        """
        if "safariPasswordAutoFillDomains" in self._prop_dict:
            return self._prop_dict["safariPasswordAutoFillDomains"]
        else:
            return None

    @safari_password_auto_fill_domains.setter
    def safari_password_auto_fill_domains(self, val):
        self._prop_dict["safariPasswordAutoFillDomains"] = val

    @property
    def safari_require_fraud_warning(self):
        """
        Gets and sets the safariRequireFraudWarning
        
        Returns:
            bool:
                The safariRequireFraudWarning
        """
        if "safariRequireFraudWarning" in self._prop_dict:
            return self._prop_dict["safariRequireFraudWarning"]
        else:
            return None

    @safari_require_fraud_warning.setter
    def safari_require_fraud_warning(self, val):
        self._prop_dict["safariRequireFraudWarning"] = val

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
    def siri_blocked(self):
        """
        Gets and sets the siriBlocked
        
        Returns:
            bool:
                The siriBlocked
        """
        if "siriBlocked" in self._prop_dict:
            return self._prop_dict["siriBlocked"]
        else:
            return None

    @siri_blocked.setter
    def siri_blocked(self, val):
        self._prop_dict["siriBlocked"] = val

    @property
    def siri_blocked_when_locked(self):
        """
        Gets and sets the siriBlockedWhenLocked
        
        Returns:
            bool:
                The siriBlockedWhenLocked
        """
        if "siriBlockedWhenLocked" in self._prop_dict:
            return self._prop_dict["siriBlockedWhenLocked"]
        else:
            return None

    @siri_blocked_when_locked.setter
    def siri_blocked_when_locked(self, val):
        self._prop_dict["siriBlockedWhenLocked"] = val

    @property
    def siri_block_user_generated_content(self):
        """
        Gets and sets the siriBlockUserGeneratedContent
        
        Returns:
            bool:
                The siriBlockUserGeneratedContent
        """
        if "siriBlockUserGeneratedContent" in self._prop_dict:
            return self._prop_dict["siriBlockUserGeneratedContent"]
        else:
            return None

    @siri_block_user_generated_content.setter
    def siri_block_user_generated_content(self, val):
        self._prop_dict["siriBlockUserGeneratedContent"] = val

    @property
    def siri_require_profanity_filter(self):
        """
        Gets and sets the siriRequireProfanityFilter
        
        Returns:
            bool:
                The siriRequireProfanityFilter
        """
        if "siriRequireProfanityFilter" in self._prop_dict:
            return self._prop_dict["siriRequireProfanityFilter"]
        else:
            return None

    @siri_require_profanity_filter.setter
    def siri_require_profanity_filter(self, val):
        self._prop_dict["siriRequireProfanityFilter"] = val

    @property
    def spotlight_block_internet_results(self):
        """
        Gets and sets the spotlightBlockInternetResults
        
        Returns:
            bool:
                The spotlightBlockInternetResults
        """
        if "spotlightBlockInternetResults" in self._prop_dict:
            return self._prop_dict["spotlightBlockInternetResults"]
        else:
            return None

    @spotlight_block_internet_results.setter
    def spotlight_block_internet_results(self, val):
        self._prop_dict["spotlightBlockInternetResults"] = val

    @property
    def voice_dialing_blocked(self):
        """
        Gets and sets the voiceDialingBlocked
        
        Returns:
            bool:
                The voiceDialingBlocked
        """
        if "voiceDialingBlocked" in self._prop_dict:
            return self._prop_dict["voiceDialingBlocked"]
        else:
            return None

    @voice_dialing_blocked.setter
    def voice_dialing_blocked(self, val):
        self._prop_dict["voiceDialingBlocked"] = val

    @property
    def wallpaper_block_modification(self):
        """
        Gets and sets the wallpaperBlockModification
        
        Returns:
            bool:
                The wallpaperBlockModification
        """
        if "wallpaperBlockModification" in self._prop_dict:
            return self._prop_dict["wallpaperBlockModification"]
        else:
            return None

    @wallpaper_block_modification.setter
    def wallpaper_block_modification(self, val):
        self._prop_dict["wallpaperBlockModification"] = val

    @property
    def wi_fi_connect_only_to_configured_networks(self):
        """
        Gets and sets the wiFiConnectOnlyToConfiguredNetworks
        
        Returns:
            bool:
                The wiFiConnectOnlyToConfiguredNetworks
        """
        if "wiFiConnectOnlyToConfiguredNetworks" in self._prop_dict:
            return self._prop_dict["wiFiConnectOnlyToConfiguredNetworks"]
        else:
            return None

    @wi_fi_connect_only_to_configured_networks.setter
    def wi_fi_connect_only_to_configured_networks(self, val):
        self._prop_dict["wiFiConnectOnlyToConfiguredNetworks"] = val

