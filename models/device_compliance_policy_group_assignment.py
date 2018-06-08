# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_compliance_policy import DeviceCompliancePolicy
from ..one_drive_object_base import OneDriveObjectBase


class DeviceCompliancePolicyGroupAssignment(OneDriveObjectBase):

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

    @property
    def exclude_group(self):
        """
        Gets and sets the excludeGroup
        
        Returns:
            bool:
                The excludeGroup
        """
        if "excludeGroup" in self._prop_dict:
            return self._prop_dict["excludeGroup"]
        else:
            return None

    @exclude_group.setter
    def exclude_group(self, val):
        self._prop_dict["excludeGroup"] = val

    @property
    def device_compliance_policy(self):
        """
        Gets and sets the deviceCompliancePolicy
        
        Returns: 
            :class:`DeviceCompliancePolicy<onedrivesdk.model.device_compliance_policy.DeviceCompliancePolicy>`:
                The deviceCompliancePolicy
        """
        if "deviceCompliancePolicy" in self._prop_dict:
            if isinstance(self._prop_dict["deviceCompliancePolicy"], OneDriveObjectBase):
                return self._prop_dict["deviceCompliancePolicy"]
            else :
                self._prop_dict["deviceCompliancePolicy"] = DeviceCompliancePolicy(self._prop_dict["deviceCompliancePolicy"])
                return self._prop_dict["deviceCompliancePolicy"]

        return None

    @device_compliance_policy.setter
    def device_compliance_policy(self, val):
        self._prop_dict["deviceCompliancePolicy"] = val

