# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.setting_value import SettingValue
from ..one_drive_object_base import OneDriveObjectBase


class GroupSetting(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def template_id(self):
        """
        Gets and sets the templateId
        
        Returns:
            str:
                The templateId
        """
        if "templateId" in self._prop_dict:
            return self._prop_dict["templateId"]
        else:
            return None

    @template_id.setter
    def template_id(self, val):
        self._prop_dict["templateId"] = val

    @property
    def values(self):
        """Gets and sets the values
        
        Returns: 
            :class:`ValuesCollectionPage<onedrivesdk.request.values_collection.ValuesCollectionPage>`:
                The values
        """
        if "values" in self._prop_dict:
            return ValuesCollectionPage(self._prop_dict["values"])
        else:
            return None

