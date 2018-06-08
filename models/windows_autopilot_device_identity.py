# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_autopilot_profile_assignment_status import WindowsAutopilotProfileAssignmentStatus
from ..model.enrollment_state import EnrollmentState
from ..model.windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class WindowsAutopilotDeviceIdentity(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def deployment_profile_assignment_status(self):
        """
        Gets and sets the deploymentProfileAssignmentStatus
        
        Returns: 
            :class:`WindowsAutopilotProfileAssignmentStatus<onedrivesdk.model.windows_autopilot_profile_assignment_status.WindowsAutopilotProfileAssignmentStatus>`:
                The deploymentProfileAssignmentStatus
        """
        if "deploymentProfileAssignmentStatus" in self._prop_dict:
            if isinstance(self._prop_dict["deploymentProfileAssignmentStatus"], OneDriveObjectBase):
                return self._prop_dict["deploymentProfileAssignmentStatus"]
            else :
                self._prop_dict["deploymentProfileAssignmentStatus"] = WindowsAutopilotProfileAssignmentStatus(self._prop_dict["deploymentProfileAssignmentStatus"])
                return self._prop_dict["deploymentProfileAssignmentStatus"]

        return None

    @deployment_profile_assignment_status.setter
    def deployment_profile_assignment_status(self, val):
        self._prop_dict["deploymentProfileAssignmentStatus"] = val

    @property
    def deployment_profile_assigned_date_time(self):
        """
        Gets and sets the deploymentProfileAssignedDateTime
        
        Returns:
            datetime:
                The deploymentProfileAssignedDateTime
        """
        if "deploymentProfileAssignedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["deploymentProfileAssignedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @deployment_profile_assigned_date_time.setter
    def deployment_profile_assigned_date_time(self, val):
        self._prop_dict["deploymentProfileAssignedDateTime"] = val.isoformat()+"Z"

    @property
    def order_identifier(self):
        """
        Gets and sets the orderIdentifier
        
        Returns:
            str:
                The orderIdentifier
        """
        if "orderIdentifier" in self._prop_dict:
            return self._prop_dict["orderIdentifier"]
        else:
            return None

    @order_identifier.setter
    def order_identifier(self, val):
        self._prop_dict["orderIdentifier"] = val

    @property
    def purchase_order_identifier(self):
        """
        Gets and sets the purchaseOrderIdentifier
        
        Returns:
            str:
                The purchaseOrderIdentifier
        """
        if "purchaseOrderIdentifier" in self._prop_dict:
            return self._prop_dict["purchaseOrderIdentifier"]
        else:
            return None

    @purchase_order_identifier.setter
    def purchase_order_identifier(self, val):
        self._prop_dict["purchaseOrderIdentifier"] = val

    @property
    def serial_number(self):
        """
        Gets and sets the serialNumber
        
        Returns:
            str:
                The serialNumber
        """
        if "serialNumber" in self._prop_dict:
            return self._prop_dict["serialNumber"]
        else:
            return None

    @serial_number.setter
    def serial_number(self, val):
        self._prop_dict["serialNumber"] = val

    @property
    def product_key(self):
        """
        Gets and sets the productKey
        
        Returns:
            str:
                The productKey
        """
        if "productKey" in self._prop_dict:
            return self._prop_dict["productKey"]
        else:
            return None

    @product_key.setter
    def product_key(self, val):
        self._prop_dict["productKey"] = val

    @property
    def manufacturer(self):
        """
        Gets and sets the manufacturer
        
        Returns:
            str:
                The manufacturer
        """
        if "manufacturer" in self._prop_dict:
            return self._prop_dict["manufacturer"]
        else:
            return None

    @manufacturer.setter
    def manufacturer(self, val):
        self._prop_dict["manufacturer"] = val

    @property
    def model(self):
        """
        Gets and sets the model
        
        Returns:
            str:
                The model
        """
        if "model" in self._prop_dict:
            return self._prop_dict["model"]
        else:
            return None

    @model.setter
    def model(self, val):
        self._prop_dict["model"] = val

    @property
    def enrollment_state(self):
        """
        Gets and sets the enrollmentState
        
        Returns: 
            :class:`EnrollmentState<onedrivesdk.model.enrollment_state.EnrollmentState>`:
                The enrollmentState
        """
        if "enrollmentState" in self._prop_dict:
            if isinstance(self._prop_dict["enrollmentState"], OneDriveObjectBase):
                return self._prop_dict["enrollmentState"]
            else :
                self._prop_dict["enrollmentState"] = EnrollmentState(self._prop_dict["enrollmentState"])
                return self._prop_dict["enrollmentState"]

        return None

    @enrollment_state.setter
    def enrollment_state(self, val):
        self._prop_dict["enrollmentState"] = val

    @property
    def last_contacted_date_time(self):
        """
        Gets and sets the lastContactedDateTime
        
        Returns:
            datetime:
                The lastContactedDateTime
        """
        if "lastContactedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastContactedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_contacted_date_time.setter
    def last_contacted_date_time(self, val):
        self._prop_dict["lastContactedDateTime"] = val.isoformat()+"Z"

    @property
    def deployment_profile(self):
        """
        Gets and sets the deploymentProfile
        
        Returns: 
            :class:`WindowsAutopilotDeploymentProfile<onedrivesdk.model.windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile>`:
                The deploymentProfile
        """
        if "deploymentProfile" in self._prop_dict:
            if isinstance(self._prop_dict["deploymentProfile"], OneDriveObjectBase):
                return self._prop_dict["deploymentProfile"]
            else :
                self._prop_dict["deploymentProfile"] = WindowsAutopilotDeploymentProfile(self._prop_dict["deploymentProfile"])
                return self._prop_dict["deploymentProfile"]

        return None

    @deployment_profile.setter
    def deployment_profile(self, val):
        self._prop_dict["deploymentProfile"] = val

