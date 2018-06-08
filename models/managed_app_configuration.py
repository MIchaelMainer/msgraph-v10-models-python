# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.key_value_pair import KeyValuePair
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def custom_settings(self):
        """Gets and sets the customSettings
        
        Returns: 
            :class:`CustomSettingsCollectionPage<onedrivesdk.request.custom_settings_collection.CustomSettingsCollectionPage>`:
                The customSettings
        """
        if "customSettings" in self._prop_dict:
            return CustomSettingsCollectionPage(self._prop_dict["customSettings"])
        else:
            return None

