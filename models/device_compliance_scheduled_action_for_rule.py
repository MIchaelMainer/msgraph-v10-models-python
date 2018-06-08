# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_compliance_action_item import DeviceComplianceActionItem
from ..one_drive_object_base import OneDriveObjectBase


class DeviceComplianceScheduledActionForRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def rule_name(self):
        """
        Gets and sets the ruleName
        
        Returns:
            str:
                The ruleName
        """
        if "ruleName" in self._prop_dict:
            return self._prop_dict["ruleName"]
        else:
            return None

    @rule_name.setter
    def rule_name(self, val):
        self._prop_dict["ruleName"] = val

    @property
    def scheduled_action_configurations(self):
        """Gets and sets the scheduledActionConfigurations
        
        Returns: 
            :class:`ScheduledActionConfigurationsCollectionPage<onedrivesdk.request.scheduled_action_configurations_collection.ScheduledActionConfigurationsCollectionPage>`:
                The scheduledActionConfigurations
        """
        if "scheduledActionConfigurations" in self._prop_dict:
            return ScheduledActionConfigurationsCollectionPage(self._prop_dict["scheduledActionConfigurations"])
        else:
            return None

