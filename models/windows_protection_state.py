# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_device_health_state import WindowsDeviceHealthState
from ..model.windows_device_malware_state import WindowsDeviceMalwareState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class WindowsProtectionState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def malware_protection_enabled(self):
        """
        Gets and sets the malwareProtectionEnabled
        
        Returns:
            bool:
                The malwareProtectionEnabled
        """
        if "malwareProtectionEnabled" in self._prop_dict:
            return self._prop_dict["malwareProtectionEnabled"]
        else:
            return None

    @malware_protection_enabled.setter
    def malware_protection_enabled(self, val):
        self._prop_dict["malwareProtectionEnabled"] = val

    @property
    def device_state(self):
        """
        Gets and sets the deviceState
        
        Returns: 
            :class:`WindowsDeviceHealthState<onedrivesdk.model.windows_device_health_state.WindowsDeviceHealthState>`:
                The deviceState
        """
        if "deviceState" in self._prop_dict:
            if isinstance(self._prop_dict["deviceState"], OneDriveObjectBase):
                return self._prop_dict["deviceState"]
            else :
                self._prop_dict["deviceState"] = WindowsDeviceHealthState(self._prop_dict["deviceState"])
                return self._prop_dict["deviceState"]

        return None

    @device_state.setter
    def device_state(self, val):
        self._prop_dict["deviceState"] = val

    @property
    def real_time_protection_enabled(self):
        """
        Gets and sets the realTimeProtectionEnabled
        
        Returns:
            bool:
                The realTimeProtectionEnabled
        """
        if "realTimeProtectionEnabled" in self._prop_dict:
            return self._prop_dict["realTimeProtectionEnabled"]
        else:
            return None

    @real_time_protection_enabled.setter
    def real_time_protection_enabled(self, val):
        self._prop_dict["realTimeProtectionEnabled"] = val

    @property
    def network_inspection_system_enabled(self):
        """
        Gets and sets the networkInspectionSystemEnabled
        
        Returns:
            bool:
                The networkInspectionSystemEnabled
        """
        if "networkInspectionSystemEnabled" in self._prop_dict:
            return self._prop_dict["networkInspectionSystemEnabled"]
        else:
            return None

    @network_inspection_system_enabled.setter
    def network_inspection_system_enabled(self, val):
        self._prop_dict["networkInspectionSystemEnabled"] = val

    @property
    def quick_scan_overdue(self):
        """
        Gets and sets the quickScanOverdue
        
        Returns:
            bool:
                The quickScanOverdue
        """
        if "quickScanOverdue" in self._prop_dict:
            return self._prop_dict["quickScanOverdue"]
        else:
            return None

    @quick_scan_overdue.setter
    def quick_scan_overdue(self, val):
        self._prop_dict["quickScanOverdue"] = val

    @property
    def full_scan_overdue(self):
        """
        Gets and sets the fullScanOverdue
        
        Returns:
            bool:
                The fullScanOverdue
        """
        if "fullScanOverdue" in self._prop_dict:
            return self._prop_dict["fullScanOverdue"]
        else:
            return None

    @full_scan_overdue.setter
    def full_scan_overdue(self, val):
        self._prop_dict["fullScanOverdue"] = val

    @property
    def signature_update_overdue(self):
        """
        Gets and sets the signatureUpdateOverdue
        
        Returns:
            bool:
                The signatureUpdateOverdue
        """
        if "signatureUpdateOverdue" in self._prop_dict:
            return self._prop_dict["signatureUpdateOverdue"]
        else:
            return None

    @signature_update_overdue.setter
    def signature_update_overdue(self, val):
        self._prop_dict["signatureUpdateOverdue"] = val

    @property
    def reboot_required(self):
        """
        Gets and sets the rebootRequired
        
        Returns:
            bool:
                The rebootRequired
        """
        if "rebootRequired" in self._prop_dict:
            return self._prop_dict["rebootRequired"]
        else:
            return None

    @reboot_required.setter
    def reboot_required(self, val):
        self._prop_dict["rebootRequired"] = val

    @property
    def full_scan_required(self):
        """
        Gets and sets the fullScanRequired
        
        Returns:
            bool:
                The fullScanRequired
        """
        if "fullScanRequired" in self._prop_dict:
            return self._prop_dict["fullScanRequired"]
        else:
            return None

    @full_scan_required.setter
    def full_scan_required(self, val):
        self._prop_dict["fullScanRequired"] = val

    @property
    def engine_version(self):
        """
        Gets and sets the engineVersion
        
        Returns:
            str:
                The engineVersion
        """
        if "engineVersion" in self._prop_dict:
            return self._prop_dict["engineVersion"]
        else:
            return None

    @engine_version.setter
    def engine_version(self, val):
        self._prop_dict["engineVersion"] = val

    @property
    def signature_version(self):
        """
        Gets and sets the signatureVersion
        
        Returns:
            str:
                The signatureVersion
        """
        if "signatureVersion" in self._prop_dict:
            return self._prop_dict["signatureVersion"]
        else:
            return None

    @signature_version.setter
    def signature_version(self, val):
        self._prop_dict["signatureVersion"] = val

    @property
    def anti_malware_version(self):
        """
        Gets and sets the antiMalwareVersion
        
        Returns:
            str:
                The antiMalwareVersion
        """
        if "antiMalwareVersion" in self._prop_dict:
            return self._prop_dict["antiMalwareVersion"]
        else:
            return None

    @anti_malware_version.setter
    def anti_malware_version(self, val):
        self._prop_dict["antiMalwareVersion"] = val

    @property
    def last_quick_scan_date_time(self):
        """
        Gets and sets the lastQuickScanDateTime
        
        Returns:
            datetime:
                The lastQuickScanDateTime
        """
        if "lastQuickScanDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastQuickScanDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_quick_scan_date_time.setter
    def last_quick_scan_date_time(self, val):
        self._prop_dict["lastQuickScanDateTime"] = val.isoformat()+"Z"

    @property
    def last_full_scan_date_time(self):
        """
        Gets and sets the lastFullScanDateTime
        
        Returns:
            datetime:
                The lastFullScanDateTime
        """
        if "lastFullScanDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastFullScanDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_full_scan_date_time.setter
    def last_full_scan_date_time(self, val):
        self._prop_dict["lastFullScanDateTime"] = val.isoformat()+"Z"

    @property
    def last_quick_scan_signature_version(self):
        """
        Gets and sets the lastQuickScanSignatureVersion
        
        Returns:
            str:
                The lastQuickScanSignatureVersion
        """
        if "lastQuickScanSignatureVersion" in self._prop_dict:
            return self._prop_dict["lastQuickScanSignatureVersion"]
        else:
            return None

    @last_quick_scan_signature_version.setter
    def last_quick_scan_signature_version(self, val):
        self._prop_dict["lastQuickScanSignatureVersion"] = val

    @property
    def last_full_scan_signature_version(self):
        """
        Gets and sets the lastFullScanSignatureVersion
        
        Returns:
            str:
                The lastFullScanSignatureVersion
        """
        if "lastFullScanSignatureVersion" in self._prop_dict:
            return self._prop_dict["lastFullScanSignatureVersion"]
        else:
            return None

    @last_full_scan_signature_version.setter
    def last_full_scan_signature_version(self, val):
        self._prop_dict["lastFullScanSignatureVersion"] = val

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
    def detected_malware_state(self):
        """Gets and sets the detectedMalwareState
        
        Returns: 
            :class:`DetectedMalwareStateCollectionPage<onedrivesdk.request.detected_malware_state_collection.DetectedMalwareStateCollectionPage>`:
                The detectedMalwareState
        """
        if "detectedMalwareState" in self._prop_dict:
            return DetectedMalwareStateCollectionPage(self._prop_dict["detectedMalwareState"])
        else:
            return None

