# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_permission_action import AndroidPermissionAction
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkMobileAppConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def package_name(self):
        """
        Gets and sets the packageName
        
        Returns:
            str:
                The packageName
        """
        if "packageName" in self._prop_dict:
            return self._prop_dict["packageName"]
        else:
            return None

    @package_name.setter
    def package_name(self, val):
        self._prop_dict["packageName"] = val

    @property
    def payload_json(self):
        """
        Gets and sets the payloadJson
        
        Returns:
            str:
                The payloadJson
        """
        if "payloadJson" in self._prop_dict:
            return self._prop_dict["payloadJson"]
        else:
            return None

    @payload_json.setter
    def payload_json(self, val):
        self._prop_dict["payloadJson"] = val

    @property
    def permission_actions(self):
        """Gets and sets the permissionActions
        
        Returns: 
            :class:`PermissionActionsCollectionPage<onedrivesdk.request.permission_actions_collection.PermissionActionsCollectionPage>`:
                The permissionActions
        """
        if "permissionActions" in self._prop_dict:
            return PermissionActionsCollectionPage(self._prop_dict["permissionActions"])
        else:
            return None

