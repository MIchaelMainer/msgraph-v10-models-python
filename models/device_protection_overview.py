# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceProtectionOverview(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def total_reported_device_count(self):
        """Gets and sets the totalReportedDeviceCount
        
        Returns: 
            int:
                The totalReportedDeviceCount
        """
        if "totalReportedDeviceCount" in self._prop_dict:
            return self._prop_dict["totalReportedDeviceCount"]
        else:
            return None

    @total_reported_device_count.setter
    def total_reported_device_count(self, val):
        self._prop_dict["totalReportedDeviceCount"] = val

    @property
    def inactive_threat_agent_device_count(self):
        """Gets and sets the inactiveThreatAgentDeviceCount
        
        Returns: 
            int:
                The inactiveThreatAgentDeviceCount
        """
        if "inactiveThreatAgentDeviceCount" in self._prop_dict:
            return self._prop_dict["inactiveThreatAgentDeviceCount"]
        else:
            return None

    @inactive_threat_agent_device_count.setter
    def inactive_threat_agent_device_count(self, val):
        self._prop_dict["inactiveThreatAgentDeviceCount"] = val

    @property
    def unknown_state_threat_agent_device_count(self):
        """Gets and sets the unknownStateThreatAgentDeviceCount
        
        Returns: 
            int:
                The unknownStateThreatAgentDeviceCount
        """
        if "unknownStateThreatAgentDeviceCount" in self._prop_dict:
            return self._prop_dict["unknownStateThreatAgentDeviceCount"]
        else:
            return None

    @unknown_state_threat_agent_device_count.setter
    def unknown_state_threat_agent_device_count(self, val):
        self._prop_dict["unknownStateThreatAgentDeviceCount"] = val

    @property
    def pending_signature_update_device_count(self):
        """Gets and sets the pendingSignatureUpdateDeviceCount
        
        Returns: 
            int:
                The pendingSignatureUpdateDeviceCount
        """
        if "pendingSignatureUpdateDeviceCount" in self._prop_dict:
            return self._prop_dict["pendingSignatureUpdateDeviceCount"]
        else:
            return None

    @pending_signature_update_device_count.setter
    def pending_signature_update_device_count(self, val):
        self._prop_dict["pendingSignatureUpdateDeviceCount"] = val

    @property
    def clean_device_count(self):
        """Gets and sets the cleanDeviceCount
        
        Returns: 
            int:
                The cleanDeviceCount
        """
        if "cleanDeviceCount" in self._prop_dict:
            return self._prop_dict["cleanDeviceCount"]
        else:
            return None

    @clean_device_count.setter
    def clean_device_count(self, val):
        self._prop_dict["cleanDeviceCount"] = val

    @property
    def pending_full_scan_device_count(self):
        """Gets and sets the pendingFullScanDeviceCount
        
        Returns: 
            int:
                The pendingFullScanDeviceCount
        """
        if "pendingFullScanDeviceCount" in self._prop_dict:
            return self._prop_dict["pendingFullScanDeviceCount"]
        else:
            return None

    @pending_full_scan_device_count.setter
    def pending_full_scan_device_count(self, val):
        self._prop_dict["pendingFullScanDeviceCount"] = val

    @property
    def pending_restart_device_count(self):
        """Gets and sets the pendingRestartDeviceCount
        
        Returns: 
            int:
                The pendingRestartDeviceCount
        """
        if "pendingRestartDeviceCount" in self._prop_dict:
            return self._prop_dict["pendingRestartDeviceCount"]
        else:
            return None

    @pending_restart_device_count.setter
    def pending_restart_device_count(self, val):
        self._prop_dict["pendingRestartDeviceCount"] = val

    @property
    def pending_manual_steps_device_count(self):
        """Gets and sets the pendingManualStepsDeviceCount
        
        Returns: 
            int:
                The pendingManualStepsDeviceCount
        """
        if "pendingManualStepsDeviceCount" in self._prop_dict:
            return self._prop_dict["pendingManualStepsDeviceCount"]
        else:
            return None

    @pending_manual_steps_device_count.setter
    def pending_manual_steps_device_count(self, val):
        self._prop_dict["pendingManualStepsDeviceCount"] = val

    @property
    def pending_offline_scan_device_count(self):
        """Gets and sets the pendingOfflineScanDeviceCount
        
        Returns: 
            int:
                The pendingOfflineScanDeviceCount
        """
        if "pendingOfflineScanDeviceCount" in self._prop_dict:
            return self._prop_dict["pendingOfflineScanDeviceCount"]
        else:
            return None

    @pending_offline_scan_device_count.setter
    def pending_offline_scan_device_count(self, val):
        self._prop_dict["pendingOfflineScanDeviceCount"] = val

    @property
    def critical_failures_device_count(self):
        """Gets and sets the criticalFailuresDeviceCount
        
        Returns: 
            int:
                The criticalFailuresDeviceCount
        """
        if "criticalFailuresDeviceCount" in self._prop_dict:
            return self._prop_dict["criticalFailuresDeviceCount"]
        else:
            return None

    @critical_failures_device_count.setter
    def critical_failures_device_count(self, val):
        self._prop_dict["criticalFailuresDeviceCount"] = val

