# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppProvisioningConfigGroupAssignment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def target_group_id(self):
        """
        Gets and sets the targetGroupId
        
        Returns:
            str:
                The targetGroupId
        """
        if "targetGroupId" in self._prop_dict:
            return self._prop_dict["targetGroupId"]
        else:
            return None

    @target_group_id.setter
    def target_group_id(self, val):
        self._prop_dict["targetGroupId"] = val

