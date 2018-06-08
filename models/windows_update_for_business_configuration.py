# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode
from ..model.prerelease_features import PrereleaseFeatures
from ..model.automatic_update_mode import AutomaticUpdateMode
from ..model.windows_update_install_schedule_type import WindowsUpdateInstallScheduleType
from ..model.windows_update_type import WindowsUpdateType
from ..model.windows_update_insider_build_control import WindowsUpdateInsiderBuildControl
from ..model.windows_update_for_business_update_weeks import WindowsUpdateForBusinessUpdateWeeks
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class WindowsUpdateForBusinessConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def delivery_optimization_mode(self):
        """
        Gets and sets the deliveryOptimizationMode
        
        Returns: 
            :class:`WindowsDeliveryOptimizationMode<onedrivesdk.model.windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode>`:
                The deliveryOptimizationMode
        """
        if "deliveryOptimizationMode" in self._prop_dict:
            if isinstance(self._prop_dict["deliveryOptimizationMode"], OneDriveObjectBase):
                return self._prop_dict["deliveryOptimizationMode"]
            else :
                self._prop_dict["deliveryOptimizationMode"] = WindowsDeliveryOptimizationMode(self._prop_dict["deliveryOptimizationMode"])
                return self._prop_dict["deliveryOptimizationMode"]

        return None

    @delivery_optimization_mode.setter
    def delivery_optimization_mode(self, val):
        self._prop_dict["deliveryOptimizationMode"] = val

    @property
    def prerelease_features(self):
        """
        Gets and sets the prereleaseFeatures
        
        Returns: 
            :class:`PrereleaseFeatures<onedrivesdk.model.prerelease_features.PrereleaseFeatures>`:
                The prereleaseFeatures
        """
        if "prereleaseFeatures" in self._prop_dict:
            if isinstance(self._prop_dict["prereleaseFeatures"], OneDriveObjectBase):
                return self._prop_dict["prereleaseFeatures"]
            else :
                self._prop_dict["prereleaseFeatures"] = PrereleaseFeatures(self._prop_dict["prereleaseFeatures"])
                return self._prop_dict["prereleaseFeatures"]

        return None

    @prerelease_features.setter
    def prerelease_features(self, val):
        self._prop_dict["prereleaseFeatures"] = val

    @property
    def automatic_update_mode(self):
        """
        Gets and sets the automaticUpdateMode
        
        Returns: 
            :class:`AutomaticUpdateMode<onedrivesdk.model.automatic_update_mode.AutomaticUpdateMode>`:
                The automaticUpdateMode
        """
        if "automaticUpdateMode" in self._prop_dict:
            if isinstance(self._prop_dict["automaticUpdateMode"], OneDriveObjectBase):
                return self._prop_dict["automaticUpdateMode"]
            else :
                self._prop_dict["automaticUpdateMode"] = AutomaticUpdateMode(self._prop_dict["automaticUpdateMode"])
                return self._prop_dict["automaticUpdateMode"]

        return None

    @automatic_update_mode.setter
    def automatic_update_mode(self, val):
        self._prop_dict["automaticUpdateMode"] = val

    @property
    def microsoft_update_service_allowed(self):
        """
        Gets and sets the microsoftUpdateServiceAllowed
        
        Returns:
            bool:
                The microsoftUpdateServiceAllowed
        """
        if "microsoftUpdateServiceAllowed" in self._prop_dict:
            return self._prop_dict["microsoftUpdateServiceAllowed"]
        else:
            return None

    @microsoft_update_service_allowed.setter
    def microsoft_update_service_allowed(self, val):
        self._prop_dict["microsoftUpdateServiceAllowed"] = val

    @property
    def drivers_excluded(self):
        """
        Gets and sets the driversExcluded
        
        Returns:
            bool:
                The driversExcluded
        """
        if "driversExcluded" in self._prop_dict:
            return self._prop_dict["driversExcluded"]
        else:
            return None

    @drivers_excluded.setter
    def drivers_excluded(self, val):
        self._prop_dict["driversExcluded"] = val

    @property
    def installation_schedule(self):
        """
        Gets and sets the installationSchedule
        
        Returns: 
            :class:`WindowsUpdateInstallScheduleType<onedrivesdk.model.windows_update_install_schedule_type.WindowsUpdateInstallScheduleType>`:
                The installationSchedule
        """
        if "installationSchedule" in self._prop_dict:
            if isinstance(self._prop_dict["installationSchedule"], OneDriveObjectBase):
                return self._prop_dict["installationSchedule"]
            else :
                self._prop_dict["installationSchedule"] = WindowsUpdateInstallScheduleType(self._prop_dict["installationSchedule"])
                return self._prop_dict["installationSchedule"]

        return None

    @installation_schedule.setter
    def installation_schedule(self, val):
        self._prop_dict["installationSchedule"] = val

    @property
    def quality_updates_deferral_period_in_days(self):
        """
        Gets and sets the qualityUpdatesDeferralPeriodInDays
        
        Returns:
            int:
                The qualityUpdatesDeferralPeriodInDays
        """
        if "qualityUpdatesDeferralPeriodInDays" in self._prop_dict:
            return self._prop_dict["qualityUpdatesDeferralPeriodInDays"]
        else:
            return None

    @quality_updates_deferral_period_in_days.setter
    def quality_updates_deferral_period_in_days(self, val):
        self._prop_dict["qualityUpdatesDeferralPeriodInDays"] = val

    @property
    def feature_updates_deferral_period_in_days(self):
        """
        Gets and sets the featureUpdatesDeferralPeriodInDays
        
        Returns:
            int:
                The featureUpdatesDeferralPeriodInDays
        """
        if "featureUpdatesDeferralPeriodInDays" in self._prop_dict:
            return self._prop_dict["featureUpdatesDeferralPeriodInDays"]
        else:
            return None

    @feature_updates_deferral_period_in_days.setter
    def feature_updates_deferral_period_in_days(self, val):
        self._prop_dict["featureUpdatesDeferralPeriodInDays"] = val

    @property
    def quality_updates_paused(self):
        """
        Gets and sets the qualityUpdatesPaused
        
        Returns:
            bool:
                The qualityUpdatesPaused
        """
        if "qualityUpdatesPaused" in self._prop_dict:
            return self._prop_dict["qualityUpdatesPaused"]
        else:
            return None

    @quality_updates_paused.setter
    def quality_updates_paused(self, val):
        self._prop_dict["qualityUpdatesPaused"] = val

    @property
    def feature_updates_paused(self):
        """
        Gets and sets the featureUpdatesPaused
        
        Returns:
            bool:
                The featureUpdatesPaused
        """
        if "featureUpdatesPaused" in self._prop_dict:
            return self._prop_dict["featureUpdatesPaused"]
        else:
            return None

    @feature_updates_paused.setter
    def feature_updates_paused(self, val):
        self._prop_dict["featureUpdatesPaused"] = val

    @property
    def quality_updates_pause_expiry_date_time(self):
        """
        Gets and sets the qualityUpdatesPauseExpiryDateTime
        
        Returns:
            datetime:
                The qualityUpdatesPauseExpiryDateTime
        """
        if "qualityUpdatesPauseExpiryDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["qualityUpdatesPauseExpiryDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @quality_updates_pause_expiry_date_time.setter
    def quality_updates_pause_expiry_date_time(self, val):
        self._prop_dict["qualityUpdatesPauseExpiryDateTime"] = val.isoformat()+"Z"

    @property
    def feature_updates_pause_expiry_date_time(self):
        """
        Gets and sets the featureUpdatesPauseExpiryDateTime
        
        Returns:
            datetime:
                The featureUpdatesPauseExpiryDateTime
        """
        if "featureUpdatesPauseExpiryDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["featureUpdatesPauseExpiryDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @feature_updates_pause_expiry_date_time.setter
    def feature_updates_pause_expiry_date_time(self, val):
        self._prop_dict["featureUpdatesPauseExpiryDateTime"] = val.isoformat()+"Z"

    @property
    def business_ready_updates_only(self):
        """
        Gets and sets the businessReadyUpdatesOnly
        
        Returns: 
            :class:`WindowsUpdateType<onedrivesdk.model.windows_update_type.WindowsUpdateType>`:
                The businessReadyUpdatesOnly
        """
        if "businessReadyUpdatesOnly" in self._prop_dict:
            if isinstance(self._prop_dict["businessReadyUpdatesOnly"], OneDriveObjectBase):
                return self._prop_dict["businessReadyUpdatesOnly"]
            else :
                self._prop_dict["businessReadyUpdatesOnly"] = WindowsUpdateType(self._prop_dict["businessReadyUpdatesOnly"])
                return self._prop_dict["businessReadyUpdatesOnly"]

        return None

    @business_ready_updates_only.setter
    def business_ready_updates_only(self, val):
        self._prop_dict["businessReadyUpdatesOnly"] = val

    @property
    def preview_build_setting(self):
        """
        Gets and sets the previewBuildSetting
        
        Returns: 
            :class:`WindowsUpdateInsiderBuildControl<onedrivesdk.model.windows_update_insider_build_control.WindowsUpdateInsiderBuildControl>`:
                The previewBuildSetting
        """
        if "previewBuildSetting" in self._prop_dict:
            if isinstance(self._prop_dict["previewBuildSetting"], OneDriveObjectBase):
                return self._prop_dict["previewBuildSetting"]
            else :
                self._prop_dict["previewBuildSetting"] = WindowsUpdateInsiderBuildControl(self._prop_dict["previewBuildSetting"])
                return self._prop_dict["previewBuildSetting"]

        return None

    @preview_build_setting.setter
    def preview_build_setting(self, val):
        self._prop_dict["previewBuildSetting"] = val

    @property
    def skip_checks_before_restart(self):
        """
        Gets and sets the skipChecksBeforeRestart
        
        Returns:
            bool:
                The skipChecksBeforeRestart
        """
        if "skipChecksBeforeRestart" in self._prop_dict:
            return self._prop_dict["skipChecksBeforeRestart"]
        else:
            return None

    @skip_checks_before_restart.setter
    def skip_checks_before_restart(self, val):
        self._prop_dict["skipChecksBeforeRestart"] = val

    @property
    def update_weeks(self):
        """
        Gets and sets the updateWeeks
        
        Returns: 
            :class:`WindowsUpdateForBusinessUpdateWeeks<onedrivesdk.model.windows_update_for_business_update_weeks.WindowsUpdateForBusinessUpdateWeeks>`:
                The updateWeeks
        """
        if "updateWeeks" in self._prop_dict:
            if isinstance(self._prop_dict["updateWeeks"], OneDriveObjectBase):
                return self._prop_dict["updateWeeks"]
            else :
                self._prop_dict["updateWeeks"] = WindowsUpdateForBusinessUpdateWeeks(self._prop_dict["updateWeeks"])
                return self._prop_dict["updateWeeks"]

        return None

    @update_weeks.setter
    def update_weeks(self, val):
        self._prop_dict["updateWeeks"] = val

