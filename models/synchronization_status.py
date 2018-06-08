# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.string_key_long_value_pair import StringKeyLongValuePair
from ..model.synchronization_status_code import SynchronizationStatusCode
from ..model.synchronization_task_execution import SynchronizationTaskExecution
from ..model.synchronization_quarantine import SynchronizationQuarantine
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationStatus(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def count_successive_complete_failures(self):
        """Gets and sets the countSuccessiveCompleteFailures
        
        Returns: 
            int:
                The countSuccessiveCompleteFailures
        """
        if "countSuccessiveCompleteFailures" in self._prop_dict:
            return self._prop_dict["countSuccessiveCompleteFailures"]
        else:
            return None

    @count_successive_complete_failures.setter
    def count_successive_complete_failures(self, val):
        self._prop_dict["countSuccessiveCompleteFailures"] = val

    @property
    def escrows_pruned(self):
        """Gets and sets the escrowsPruned
        
        Returns: 
            bool:
                The escrowsPruned
        """
        if "escrowsPruned" in self._prop_dict:
            return self._prop_dict["escrowsPruned"]
        else:
            return None

    @escrows_pruned.setter
    def escrows_pruned(self, val):
        self._prop_dict["escrowsPruned"] = val

    @property
    def synchronized_entry_count_by_type(self):
        """
        Gets and sets the synchronizedEntryCountByType
        
        Returns: 
            :class:`StringKeyLongValuePair<onedrivesdk.model.string_key_long_value_pair.StringKeyLongValuePair>`:
                The synchronizedEntryCountByType
        """
        if "synchronizedEntryCountByType" in self._prop_dict:
            if isinstance(self._prop_dict["synchronizedEntryCountByType"], OneDriveObjectBase):
                return self._prop_dict["synchronizedEntryCountByType"]
            else :
                self._prop_dict["synchronizedEntryCountByType"] = StringKeyLongValuePair(self._prop_dict["synchronizedEntryCountByType"])
                return self._prop_dict["synchronizedEntryCountByType"]

        return None

    @synchronized_entry_count_by_type.setter
    def synchronized_entry_count_by_type(self, val):
        self._prop_dict["synchronizedEntryCountByType"] = val
    @property
    def code(self):
        """
        Gets and sets the code
        
        Returns: 
            :class:`SynchronizationStatusCode<onedrivesdk.model.synchronization_status_code.SynchronizationStatusCode>`:
                The code
        """
        if "code" in self._prop_dict:
            if isinstance(self._prop_dict["code"], OneDriveObjectBase):
                return self._prop_dict["code"]
            else :
                self._prop_dict["code"] = SynchronizationStatusCode(self._prop_dict["code"])
                return self._prop_dict["code"]

        return None

    @code.setter
    def code(self, val):
        self._prop_dict["code"] = val
    @property
    def last_execution(self):
        """
        Gets and sets the lastExecution
        
        Returns: 
            :class:`SynchronizationTaskExecution<onedrivesdk.model.synchronization_task_execution.SynchronizationTaskExecution>`:
                The lastExecution
        """
        if "lastExecution" in self._prop_dict:
            if isinstance(self._prop_dict["lastExecution"], OneDriveObjectBase):
                return self._prop_dict["lastExecution"]
            else :
                self._prop_dict["lastExecution"] = SynchronizationTaskExecution(self._prop_dict["lastExecution"])
                return self._prop_dict["lastExecution"]

        return None

    @last_execution.setter
    def last_execution(self, val):
        self._prop_dict["lastExecution"] = val
    @property
    def last_successful_execution(self):
        """
        Gets and sets the lastSuccessfulExecution
        
        Returns: 
            :class:`SynchronizationTaskExecution<onedrivesdk.model.synchronization_task_execution.SynchronizationTaskExecution>`:
                The lastSuccessfulExecution
        """
        if "lastSuccessfulExecution" in self._prop_dict:
            if isinstance(self._prop_dict["lastSuccessfulExecution"], OneDriveObjectBase):
                return self._prop_dict["lastSuccessfulExecution"]
            else :
                self._prop_dict["lastSuccessfulExecution"] = SynchronizationTaskExecution(self._prop_dict["lastSuccessfulExecution"])
                return self._prop_dict["lastSuccessfulExecution"]

        return None

    @last_successful_execution.setter
    def last_successful_execution(self, val):
        self._prop_dict["lastSuccessfulExecution"] = val
    @property
    def last_successful_execution_with_exports(self):
        """
        Gets and sets the lastSuccessfulExecutionWithExports
        
        Returns: 
            :class:`SynchronizationTaskExecution<onedrivesdk.model.synchronization_task_execution.SynchronizationTaskExecution>`:
                The lastSuccessfulExecutionWithExports
        """
        if "lastSuccessfulExecutionWithExports" in self._prop_dict:
            if isinstance(self._prop_dict["lastSuccessfulExecutionWithExports"], OneDriveObjectBase):
                return self._prop_dict["lastSuccessfulExecutionWithExports"]
            else :
                self._prop_dict["lastSuccessfulExecutionWithExports"] = SynchronizationTaskExecution(self._prop_dict["lastSuccessfulExecutionWithExports"])
                return self._prop_dict["lastSuccessfulExecutionWithExports"]

        return None

    @last_successful_execution_with_exports.setter
    def last_successful_execution_with_exports(self, val):
        self._prop_dict["lastSuccessfulExecutionWithExports"] = val
    @property
    def steady_state_first_achieved_time(self):
        """Gets and sets the steadyStateFirstAchievedTime
        
        Returns: 
            datetime:
                The steadyStateFirstAchievedTime
        """
        if "steadyStateFirstAchievedTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["steadyStateFirstAchievedTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @steady_state_first_achieved_time.setter
    def steady_state_first_achieved_time(self, val):
        self._prop_dict["steadyStateFirstAchievedTime"] = val.isoformat()+"Z"

    @property
    def steady_state_last_achieved_time(self):
        """Gets and sets the steadyStateLastAchievedTime
        
        Returns: 
            datetime:
                The steadyStateLastAchievedTime
        """
        if "steadyStateLastAchievedTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["steadyStateLastAchievedTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @steady_state_last_achieved_time.setter
    def steady_state_last_achieved_time(self, val):
        self._prop_dict["steadyStateLastAchievedTime"] = val.isoformat()+"Z"

    @property
    def quarantine(self):
        """
        Gets and sets the quarantine
        
        Returns: 
            :class:`SynchronizationQuarantine<onedrivesdk.model.synchronization_quarantine.SynchronizationQuarantine>`:
                The quarantine
        """
        if "quarantine" in self._prop_dict:
            if isinstance(self._prop_dict["quarantine"], OneDriveObjectBase):
                return self._prop_dict["quarantine"]
            else :
                self._prop_dict["quarantine"] = SynchronizationQuarantine(self._prop_dict["quarantine"])
                return self._prop_dict["quarantine"]

        return None

    @quarantine.setter
    def quarantine(self, val):
        self._prop_dict["quarantine"] = val
    @property
    def troubleshooting_url(self):
        """Gets and sets the troubleshootingUrl
        
        Returns: 
            str:
                The troubleshootingUrl
        """
        if "troubleshootingUrl" in self._prop_dict:
            return self._prop_dict["troubleshootingUrl"]
        else:
            return None

    @troubleshooting_url.setter
    def troubleshooting_url(self, val):
        self._prop_dict["troubleshootingUrl"] = val

