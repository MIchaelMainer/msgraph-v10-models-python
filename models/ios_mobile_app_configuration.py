# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_configuration_setting_item import AppConfigurationSettingItem
from ..one_drive_object_base import OneDriveObjectBase


class IosMobileAppConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def setting_xml(self):
        """
        Gets and sets the settingXml
        
        Returns:
            str:
                The settingXml
        """
        if "settingXml" in self._prop_dict:
            return self._prop_dict["settingXml"]
        else:
            return None

    @setting_xml.setter
    def setting_xml(self, val):
        self._prop_dict["settingXml"] = val

    @property
    def settings(self):
        """Gets and sets the settings
        
        Returns: 
            :class:`SettingsCollectionPage<onedrivesdk.request.settings_collection.SettingsCollectionPage>`:
                The settings
        """
        if "settings" in self._prop_dict:
            return SettingsCollectionPage(self._prop_dict["settings"])
        else:
            return None

