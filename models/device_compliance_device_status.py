# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.compliance_status import ComplianceStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceComplianceDeviceStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_display_name(self):
        """
        Gets and sets the deviceDisplayName
        
        Returns:
            str:
                The deviceDisplayName
        """
        if "deviceDisplayName" in self._prop_dict:
            return self._prop_dict["deviceDisplayName"]
        else:
            return None

    @device_display_name.setter
    def device_display_name(self, val):
        self._prop_dict["deviceDisplayName"] = val

    @property
    def user_name(self):
        """
        Gets and sets the userName
        
        Returns:
            str:
                The userName
        """
        if "userName" in self._prop_dict:
            return self._prop_dict["userName"]
        else:
            return None

    @user_name.setter
    def user_name(self, val):
        self._prop_dict["userName"] = val

    @property
    def device_model(self):
        """
        Gets and sets the deviceModel
        
        Returns:
            str:
                The deviceModel
        """
        if "deviceModel" in self._prop_dict:
            return self._prop_dict["deviceModel"]
        else:
            return None

    @device_model.setter
    def device_model(self, val):
        self._prop_dict["deviceModel"] = val

    @property
    def compliance_grace_period_expiration_date_time(self):
        """
        Gets and sets the complianceGracePeriodExpirationDateTime
        
        Returns:
            datetime:
                The complianceGracePeriodExpirationDateTime
        """
        if "complianceGracePeriodExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["complianceGracePeriodExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self, val):
        self._prop_dict["complianceGracePeriodExpirationDateTime"] = val.isoformat()+"Z"

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`ComplianceStatus<onedrivesdk.model.compliance_status.ComplianceStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = ComplianceStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def last_reported_date_time(self):
        """
        Gets and sets the lastReportedDateTime
        
        Returns:
            datetime:
                The lastReportedDateTime
        """
        if "lastReportedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastReportedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_reported_date_time.setter
    def last_reported_date_time(self, val):
        self._prop_dict["lastReportedDateTime"] = val.isoformat()+"Z"

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

