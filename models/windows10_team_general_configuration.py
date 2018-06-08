# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.time_of_day import TimeOfDay
from ..model.miracast_channel import MiracastChannel
from ..model.welcome_screen_meeting_information import WelcomeScreenMeetingInformation
from ..one_drive_object_base import OneDriveObjectBase


class Windows10TeamGeneralConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def azure_operational_insights_block_telemetry(self):
        """
        Gets and sets the azureOperationalInsightsBlockTelemetry
        
        Returns:
            bool:
                The azureOperationalInsightsBlockTelemetry
        """
        if "azureOperationalInsightsBlockTelemetry" in self._prop_dict:
            return self._prop_dict["azureOperationalInsightsBlockTelemetry"]
        else:
            return None

    @azure_operational_insights_block_telemetry.setter
    def azure_operational_insights_block_telemetry(self, val):
        self._prop_dict["azureOperationalInsightsBlockTelemetry"] = val

    @property
    def azure_operational_insights_workspace_id(self):
        """
        Gets and sets the azureOperationalInsightsWorkspaceId
        
        Returns:
            str:
                The azureOperationalInsightsWorkspaceId
        """
        if "azureOperationalInsightsWorkspaceId" in self._prop_dict:
            return self._prop_dict["azureOperationalInsightsWorkspaceId"]
        else:
            return None

    @azure_operational_insights_workspace_id.setter
    def azure_operational_insights_workspace_id(self, val):
        self._prop_dict["azureOperationalInsightsWorkspaceId"] = val

    @property
    def azure_operational_insights_workspace_key(self):
        """
        Gets and sets the azureOperationalInsightsWorkspaceKey
        
        Returns:
            str:
                The azureOperationalInsightsWorkspaceKey
        """
        if "azureOperationalInsightsWorkspaceKey" in self._prop_dict:
            return self._prop_dict["azureOperationalInsightsWorkspaceKey"]
        else:
            return None

    @azure_operational_insights_workspace_key.setter
    def azure_operational_insights_workspace_key(self, val):
        self._prop_dict["azureOperationalInsightsWorkspaceKey"] = val

    @property
    def connect_app_block_auto_launch(self):
        """
        Gets and sets the connectAppBlockAutoLaunch
        
        Returns:
            bool:
                The connectAppBlockAutoLaunch
        """
        if "connectAppBlockAutoLaunch" in self._prop_dict:
            return self._prop_dict["connectAppBlockAutoLaunch"]
        else:
            return None

    @connect_app_block_auto_launch.setter
    def connect_app_block_auto_launch(self, val):
        self._prop_dict["connectAppBlockAutoLaunch"] = val

    @property
    def maintenance_window_blocked(self):
        """
        Gets and sets the maintenanceWindowBlocked
        
        Returns:
            bool:
                The maintenanceWindowBlocked
        """
        if "maintenanceWindowBlocked" in self._prop_dict:
            return self._prop_dict["maintenanceWindowBlocked"]
        else:
            return None

    @maintenance_window_blocked.setter
    def maintenance_window_blocked(self, val):
        self._prop_dict["maintenanceWindowBlocked"] = val

    @property
    def maintenance_window_duration_in_hours(self):
        """
        Gets and sets the maintenanceWindowDurationInHours
        
        Returns:
            int:
                The maintenanceWindowDurationInHours
        """
        if "maintenanceWindowDurationInHours" in self._prop_dict:
            return self._prop_dict["maintenanceWindowDurationInHours"]
        else:
            return None

    @maintenance_window_duration_in_hours.setter
    def maintenance_window_duration_in_hours(self, val):
        self._prop_dict["maintenanceWindowDurationInHours"] = val

    @property
    def maintenance_window_start_time(self):
        """
        Gets and sets the maintenanceWindowStartTime
        
        Returns: 
            :class:`TimeOfDay<onedrivesdk.model.time_of_day.TimeOfDay>`:
                The maintenanceWindowStartTime
        """
        if "maintenanceWindowStartTime" in self._prop_dict:
            if isinstance(self._prop_dict["maintenanceWindowStartTime"], OneDriveObjectBase):
                return self._prop_dict["maintenanceWindowStartTime"]
            else :
                self._prop_dict["maintenanceWindowStartTime"] = TimeOfDay(self._prop_dict["maintenanceWindowStartTime"])
                return self._prop_dict["maintenanceWindowStartTime"]

        return None

    @maintenance_window_start_time.setter
    def maintenance_window_start_time(self, val):
        self._prop_dict["maintenanceWindowStartTime"] = val

    @property
    def miracast_channel(self):
        """
        Gets and sets the miracastChannel
        
        Returns: 
            :class:`MiracastChannel<onedrivesdk.model.miracast_channel.MiracastChannel>`:
                The miracastChannel
        """
        if "miracastChannel" in self._prop_dict:
            if isinstance(self._prop_dict["miracastChannel"], OneDriveObjectBase):
                return self._prop_dict["miracastChannel"]
            else :
                self._prop_dict["miracastChannel"] = MiracastChannel(self._prop_dict["miracastChannel"])
                return self._prop_dict["miracastChannel"]

        return None

    @miracast_channel.setter
    def miracast_channel(self, val):
        self._prop_dict["miracastChannel"] = val

    @property
    def miracast_blocked(self):
        """
        Gets and sets the miracastBlocked
        
        Returns:
            bool:
                The miracastBlocked
        """
        if "miracastBlocked" in self._prop_dict:
            return self._prop_dict["miracastBlocked"]
        else:
            return None

    @miracast_blocked.setter
    def miracast_blocked(self, val):
        self._prop_dict["miracastBlocked"] = val

    @property
    def miracast_require_pin(self):
        """
        Gets and sets the miracastRequirePin
        
        Returns:
            bool:
                The miracastRequirePin
        """
        if "miracastRequirePin" in self._prop_dict:
            return self._prop_dict["miracastRequirePin"]
        else:
            return None

    @miracast_require_pin.setter
    def miracast_require_pin(self, val):
        self._prop_dict["miracastRequirePin"] = val

    @property
    def settings_block_my_meetings_and_files(self):
        """
        Gets and sets the settingsBlockMyMeetingsAndFiles
        
        Returns:
            bool:
                The settingsBlockMyMeetingsAndFiles
        """
        if "settingsBlockMyMeetingsAndFiles" in self._prop_dict:
            return self._prop_dict["settingsBlockMyMeetingsAndFiles"]
        else:
            return None

    @settings_block_my_meetings_and_files.setter
    def settings_block_my_meetings_and_files(self, val):
        self._prop_dict["settingsBlockMyMeetingsAndFiles"] = val

    @property
    def settings_block_session_resume(self):
        """
        Gets and sets the settingsBlockSessionResume
        
        Returns:
            bool:
                The settingsBlockSessionResume
        """
        if "settingsBlockSessionResume" in self._prop_dict:
            return self._prop_dict["settingsBlockSessionResume"]
        else:
            return None

    @settings_block_session_resume.setter
    def settings_block_session_resume(self, val):
        self._prop_dict["settingsBlockSessionResume"] = val

    @property
    def settings_block_signin_suggestions(self):
        """
        Gets and sets the settingsBlockSigninSuggestions
        
        Returns:
            bool:
                The settingsBlockSigninSuggestions
        """
        if "settingsBlockSigninSuggestions" in self._prop_dict:
            return self._prop_dict["settingsBlockSigninSuggestions"]
        else:
            return None

    @settings_block_signin_suggestions.setter
    def settings_block_signin_suggestions(self, val):
        self._prop_dict["settingsBlockSigninSuggestions"] = val

    @property
    def settings_default_volume(self):
        """
        Gets and sets the settingsDefaultVolume
        
        Returns:
            int:
                The settingsDefaultVolume
        """
        if "settingsDefaultVolume" in self._prop_dict:
            return self._prop_dict["settingsDefaultVolume"]
        else:
            return None

    @settings_default_volume.setter
    def settings_default_volume(self, val):
        self._prop_dict["settingsDefaultVolume"] = val

    @property
    def settings_screen_timeout_in_minutes(self):
        """
        Gets and sets the settingsScreenTimeoutInMinutes
        
        Returns:
            int:
                The settingsScreenTimeoutInMinutes
        """
        if "settingsScreenTimeoutInMinutes" in self._prop_dict:
            return self._prop_dict["settingsScreenTimeoutInMinutes"]
        else:
            return None

    @settings_screen_timeout_in_minutes.setter
    def settings_screen_timeout_in_minutes(self, val):
        self._prop_dict["settingsScreenTimeoutInMinutes"] = val

    @property
    def settings_session_timeout_in_minutes(self):
        """
        Gets and sets the settingsSessionTimeoutInMinutes
        
        Returns:
            int:
                The settingsSessionTimeoutInMinutes
        """
        if "settingsSessionTimeoutInMinutes" in self._prop_dict:
            return self._prop_dict["settingsSessionTimeoutInMinutes"]
        else:
            return None

    @settings_session_timeout_in_minutes.setter
    def settings_session_timeout_in_minutes(self, val):
        self._prop_dict["settingsSessionTimeoutInMinutes"] = val

    @property
    def settings_sleep_timeout_in_minutes(self):
        """
        Gets and sets the settingsSleepTimeoutInMinutes
        
        Returns:
            int:
                The settingsSleepTimeoutInMinutes
        """
        if "settingsSleepTimeoutInMinutes" in self._prop_dict:
            return self._prop_dict["settingsSleepTimeoutInMinutes"]
        else:
            return None

    @settings_sleep_timeout_in_minutes.setter
    def settings_sleep_timeout_in_minutes(self, val):
        self._prop_dict["settingsSleepTimeoutInMinutes"] = val

    @property
    def welcome_screen_block_automatic_wake_up(self):
        """
        Gets and sets the welcomeScreenBlockAutomaticWakeUp
        
        Returns:
            bool:
                The welcomeScreenBlockAutomaticWakeUp
        """
        if "welcomeScreenBlockAutomaticWakeUp" in self._prop_dict:
            return self._prop_dict["welcomeScreenBlockAutomaticWakeUp"]
        else:
            return None

    @welcome_screen_block_automatic_wake_up.setter
    def welcome_screen_block_automatic_wake_up(self, val):
        self._prop_dict["welcomeScreenBlockAutomaticWakeUp"] = val

    @property
    def welcome_screen_background_image_url(self):
        """
        Gets and sets the welcomeScreenBackgroundImageUrl
        
        Returns:
            str:
                The welcomeScreenBackgroundImageUrl
        """
        if "welcomeScreenBackgroundImageUrl" in self._prop_dict:
            return self._prop_dict["welcomeScreenBackgroundImageUrl"]
        else:
            return None

    @welcome_screen_background_image_url.setter
    def welcome_screen_background_image_url(self, val):
        self._prop_dict["welcomeScreenBackgroundImageUrl"] = val

    @property
    def welcome_screen_meeting_information(self):
        """
        Gets and sets the welcomeScreenMeetingInformation
        
        Returns: 
            :class:`WelcomeScreenMeetingInformation<onedrivesdk.model.welcome_screen_meeting_information.WelcomeScreenMeetingInformation>`:
                The welcomeScreenMeetingInformation
        """
        if "welcomeScreenMeetingInformation" in self._prop_dict:
            if isinstance(self._prop_dict["welcomeScreenMeetingInformation"], OneDriveObjectBase):
                return self._prop_dict["welcomeScreenMeetingInformation"]
            else :
                self._prop_dict["welcomeScreenMeetingInformation"] = WelcomeScreenMeetingInformation(self._prop_dict["welcomeScreenMeetingInformation"])
                return self._prop_dict["welcomeScreenMeetingInformation"]

        return None

    @welcome_screen_meeting_information.setter
    def welcome_screen_meeting_information(self, val):
        self._prop_dict["welcomeScreenMeetingInformation"] = val

