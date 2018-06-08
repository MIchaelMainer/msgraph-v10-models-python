# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedDeviceMobileAppConfigurationUserSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def pending_count(self):
        """
        Gets and sets the pendingCount
        
        Returns:
            int:
                The pendingCount
        """
        if "pendingCount" in self._prop_dict:
            return self._prop_dict["pendingCount"]
        else:
            return None

    @pending_count.setter
    def pending_count(self, val):
        self._prop_dict["pendingCount"] = val

    @property
    def not_applicable_count(self):
        """
        Gets and sets the notApplicableCount
        
        Returns:
            int:
                The notApplicableCount
        """
        if "notApplicableCount" in self._prop_dict:
            return self._prop_dict["notApplicableCount"]
        else:
            return None

    @not_applicable_count.setter
    def not_applicable_count(self, val):
        self._prop_dict["notApplicableCount"] = val

    @property
    def success_count(self):
        """
        Gets and sets the successCount
        
        Returns:
            int:
                The successCount
        """
        if "successCount" in self._prop_dict:
            return self._prop_dict["successCount"]
        else:
            return None

    @success_count.setter
    def success_count(self, val):
        self._prop_dict["successCount"] = val

    @property
    def error_count(self):
        """
        Gets and sets the errorCount
        
        Returns:
            int:
                The errorCount
        """
        if "errorCount" in self._prop_dict:
            return self._prop_dict["errorCount"]
        else:
            return None

    @error_count.setter
    def error_count(self, val):
        self._prop_dict["errorCount"] = val

    @property
    def failed_count(self):
        """
        Gets and sets the failedCount
        
        Returns:
            int:
                The failedCount
        """
        if "failedCount" in self._prop_dict:
            return self._prop_dict["failedCount"]
        else:
            return None

    @failed_count.setter
    def failed_count(self, val):
        self._prop_dict["failedCount"] = val

    @property
    def conflict_count(self):
        """
        Gets and sets the conflictCount
        
        Returns:
            int:
                The conflictCount
        """
        if "conflictCount" in self._prop_dict:
            return self._prop_dict["conflictCount"]
        else:
            return None

    @conflict_count.setter
    def conflict_count(self, val):
        self._prop_dict["conflictCount"] = val

    @property
    def last_update_date_time(self):
        """
        Gets and sets the lastUpdateDateTime
        
        Returns:
            datetime:
                The lastUpdateDateTime
        """
        if "lastUpdateDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastUpdateDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_update_date_time.setter
    def last_update_date_time(self, val):
        self._prop_dict["lastUpdateDateTime"] = val.isoformat()+"Z"

    @property
    def configuration_version(self):
        """
        Gets and sets the configurationVersion
        
        Returns:
            int:
                The configurationVersion
        """
        if "configurationVersion" in self._prop_dict:
            return self._prop_dict["configurationVersion"]
        else:
            return None

    @configuration_version.setter
    def configuration_version(self, val):
        self._prop_dict["configurationVersion"] = val

