# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MicrosoftStoreForBusinessContainedApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_user_model_id(self):
        """
        Gets and sets the appUserModelId
        
        Returns:
            str:
                The appUserModelId
        """
        if "appUserModelId" in self._prop_dict:
            return self._prop_dict["appUserModelId"]
        else:
            return None

    @app_user_model_id.setter
    def app_user_model_id(self, val):
        self._prop_dict["appUserModelId"] = val

