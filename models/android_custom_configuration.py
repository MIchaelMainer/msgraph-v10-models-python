# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.oma_setting import OmaSetting
from ..one_drive_object_base import OneDriveObjectBase


class AndroidCustomConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def oma_settings(self):
        """Gets and sets the omaSettings
        
        Returns: 
            :class:`OmaSettingsCollectionPage<onedrivesdk.request.oma_settings_collection.OmaSettingsCollectionPage>`:
                The omaSettings
        """
        if "omaSettings" in self._prop_dict:
            return OmaSettingsCollectionPage(self._prop_dict["omaSettings"])
        else:
            return None

