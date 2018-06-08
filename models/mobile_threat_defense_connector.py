# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class MobileThreatDefenseConnector(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_heartbeat_date_time(self):
        """
        Gets and sets the lastHeartbeatDateTime
        
        Returns:
            datetime:
                The lastHeartbeatDateTime
        """
        if "lastHeartbeatDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastHeartbeatDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_heartbeat_date_time.setter
    def last_heartbeat_date_time(self, val):
        self._prop_dict["lastHeartbeatDateTime"] = val.isoformat()+"Z"

    @property
    def partner_state(self):
        """
        Gets and sets the partnerState
        
        Returns: 
            :class:`MobileThreatPartnerTenantState<onedrivesdk.model.mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState>`:
                The partnerState
        """
        if "partnerState" in self._prop_dict:
            if isinstance(self._prop_dict["partnerState"], OneDriveObjectBase):
                return self._prop_dict["partnerState"]
            else :
                self._prop_dict["partnerState"] = MobileThreatPartnerTenantState(self._prop_dict["partnerState"])
                return self._prop_dict["partnerState"]

        return None

    @partner_state.setter
    def partner_state(self, val):
        self._prop_dict["partnerState"] = val

    @property
    def android_enabled(self):
        """
        Gets and sets the androidEnabled
        
        Returns:
            bool:
                The androidEnabled
        """
        if "androidEnabled" in self._prop_dict:
            return self._prop_dict["androidEnabled"]
        else:
            return None

    @android_enabled.setter
    def android_enabled(self, val):
        self._prop_dict["androidEnabled"] = val

    @property
    def ios_enabled(self):
        """
        Gets and sets the iosEnabled
        
        Returns:
            bool:
                The iosEnabled
        """
        if "iosEnabled" in self._prop_dict:
            return self._prop_dict["iosEnabled"]
        else:
            return None

    @ios_enabled.setter
    def ios_enabled(self, val):
        self._prop_dict["iosEnabled"] = val

    @property
    def android_device_blocked_on_missing_partner_data(self):
        """
        Gets and sets the androidDeviceBlockedOnMissingPartnerData
        
        Returns:
            bool:
                The androidDeviceBlockedOnMissingPartnerData
        """
        if "androidDeviceBlockedOnMissingPartnerData" in self._prop_dict:
            return self._prop_dict["androidDeviceBlockedOnMissingPartnerData"]
        else:
            return None

    @android_device_blocked_on_missing_partner_data.setter
    def android_device_blocked_on_missing_partner_data(self, val):
        self._prop_dict["androidDeviceBlockedOnMissingPartnerData"] = val

    @property
    def ios_device_blocked_on_missing_partner_data(self):
        """
        Gets and sets the iosDeviceBlockedOnMissingPartnerData
        
        Returns:
            bool:
                The iosDeviceBlockedOnMissingPartnerData
        """
        if "iosDeviceBlockedOnMissingPartnerData" in self._prop_dict:
            return self._prop_dict["iosDeviceBlockedOnMissingPartnerData"]
        else:
            return None

    @ios_device_blocked_on_missing_partner_data.setter
    def ios_device_blocked_on_missing_partner_data(self, val):
        self._prop_dict["iosDeviceBlockedOnMissingPartnerData"] = val

    @property
    def partner_unsupported_os_version_blocked(self):
        """
        Gets and sets the partnerUnsupportedOsVersionBlocked
        
        Returns:
            bool:
                The partnerUnsupportedOsVersionBlocked
        """
        if "partnerUnsupportedOsVersionBlocked" in self._prop_dict:
            return self._prop_dict["partnerUnsupportedOsVersionBlocked"]
        else:
            return None

    @partner_unsupported_os_version_blocked.setter
    def partner_unsupported_os_version_blocked(self, val):
        self._prop_dict["partnerUnsupportedOsVersionBlocked"] = val

    @property
    def partner_unresponsiveness_threshold_in_days(self):
        """
        Gets and sets the partnerUnresponsivenessThresholdInDays
        
        Returns:
            int:
                The partnerUnresponsivenessThresholdInDays
        """
        if "partnerUnresponsivenessThresholdInDays" in self._prop_dict:
            return self._prop_dict["partnerUnresponsivenessThresholdInDays"]
        else:
            return None

    @partner_unresponsiveness_threshold_in_days.setter
    def partner_unresponsiveness_threshold_in_days(self, val):
        self._prop_dict["partnerUnresponsivenessThresholdInDays"] = val

