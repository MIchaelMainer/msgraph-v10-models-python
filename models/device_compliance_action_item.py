# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_compliance_action_type import DeviceComplianceActionType
from ..one_drive_object_base import OneDriveObjectBase


class DeviceComplianceActionItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def grace_period_hours(self):
        """
        Gets and sets the gracePeriodHours
        
        Returns:
            int:
                The gracePeriodHours
        """
        if "gracePeriodHours" in self._prop_dict:
            return self._prop_dict["gracePeriodHours"]
        else:
            return None

    @grace_period_hours.setter
    def grace_period_hours(self, val):
        self._prop_dict["gracePeriodHours"] = val

    @property
    def action_type(self):
        """
        Gets and sets the actionType
        
        Returns: 
            :class:`DeviceComplianceActionType<onedrivesdk.model.device_compliance_action_type.DeviceComplianceActionType>`:
                The actionType
        """
        if "actionType" in self._prop_dict:
            if isinstance(self._prop_dict["actionType"], OneDriveObjectBase):
                return self._prop_dict["actionType"]
            else :
                self._prop_dict["actionType"] = DeviceComplianceActionType(self._prop_dict["actionType"])
                return self._prop_dict["actionType"]

        return None

    @action_type.setter
    def action_type(self, val):
        self._prop_dict["actionType"] = val

    @property
    def notification_template_id(self):
        """
        Gets and sets the notificationTemplateId
        
        Returns:
            str:
                The notificationTemplateId
        """
        if "notificationTemplateId" in self._prop_dict:
            return self._prop_dict["notificationTemplateId"]
        else:
            return None

    @notification_template_id.setter
    def notification_template_id(self, val):
        self._prop_dict["notificationTemplateId"] = val

    @property
    def notification_message_cc_list(self):
        """
        Gets and sets the notificationMessageCCList
        
        Returns:
            str:
                The notificationMessageCCList
        """
        if "notificationMessageCCList" in self._prop_dict:
            return self._prop_dict["notificationMessageCCList"]
        else:
            return None

    @notification_message_cc_list.setter
    def notification_message_cc_list(self, val):
        self._prop_dict["notificationMessageCCList"] = val

