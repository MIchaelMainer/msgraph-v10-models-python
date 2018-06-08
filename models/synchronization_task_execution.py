# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.synchronization_task_execution_result import SynchronizationTaskExecutionResult
from ..model.synchronization_error import SynchronizationError
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationTaskExecution(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def activity_identifier(self):
        """Gets and sets the activityIdentifier
        
        Returns: 
            str:
                The activityIdentifier
        """
        if "activityIdentifier" in self._prop_dict:
            return self._prop_dict["activityIdentifier"]
        else:
            return None

    @activity_identifier.setter
    def activity_identifier(self, val):
        self._prop_dict["activityIdentifier"] = val

    @property
    def count_entitled(self):
        """Gets and sets the countEntitled
        
        Returns: 
            int:
                The countEntitled
        """
        if "countEntitled" in self._prop_dict:
            return self._prop_dict["countEntitled"]
        else:
            return None

    @count_entitled.setter
    def count_entitled(self, val):
        self._prop_dict["countEntitled"] = val

    @property
    def count_entitled_for_provisioning(self):
        """Gets and sets the countEntitledForProvisioning
        
        Returns: 
            int:
                The countEntitledForProvisioning
        """
        if "countEntitledForProvisioning" in self._prop_dict:
            return self._prop_dict["countEntitledForProvisioning"]
        else:
            return None

    @count_entitled_for_provisioning.setter
    def count_entitled_for_provisioning(self, val):
        self._prop_dict["countEntitledForProvisioning"] = val

    @property
    def count_escrowed(self):
        """Gets and sets the countEscrowed
        
        Returns: 
            int:
                The countEscrowed
        """
        if "countEscrowed" in self._prop_dict:
            return self._prop_dict["countEscrowed"]
        else:
            return None

    @count_escrowed.setter
    def count_escrowed(self, val):
        self._prop_dict["countEscrowed"] = val

    @property
    def count_escrowed_raw(self):
        """Gets and sets the countEscrowedRaw
        
        Returns: 
            int:
                The countEscrowedRaw
        """
        if "countEscrowedRaw" in self._prop_dict:
            return self._prop_dict["countEscrowedRaw"]
        else:
            return None

    @count_escrowed_raw.setter
    def count_escrowed_raw(self, val):
        self._prop_dict["countEscrowedRaw"] = val

    @property
    def count_exported(self):
        """Gets and sets the countExported
        
        Returns: 
            int:
                The countExported
        """
        if "countExported" in self._prop_dict:
            return self._prop_dict["countExported"]
        else:
            return None

    @count_exported.setter
    def count_exported(self, val):
        self._prop_dict["countExported"] = val

    @property
    def count_exports(self):
        """Gets and sets the countExports
        
        Returns: 
            int:
                The countExports
        """
        if "countExports" in self._prop_dict:
            return self._prop_dict["countExports"]
        else:
            return None

    @count_exports.setter
    def count_exports(self, val):
        self._prop_dict["countExports"] = val

    @property
    def count_imported(self):
        """Gets and sets the countImported
        
        Returns: 
            int:
                The countImported
        """
        if "countImported" in self._prop_dict:
            return self._prop_dict["countImported"]
        else:
            return None

    @count_imported.setter
    def count_imported(self, val):
        self._prop_dict["countImported"] = val

    @property
    def count_imported_deltas(self):
        """Gets and sets the countImportedDeltas
        
        Returns: 
            int:
                The countImportedDeltas
        """
        if "countImportedDeltas" in self._prop_dict:
            return self._prop_dict["countImportedDeltas"]
        else:
            return None

    @count_imported_deltas.setter
    def count_imported_deltas(self, val):
        self._prop_dict["countImportedDeltas"] = val

    @property
    def count_imported_reference_deltas(self):
        """Gets and sets the countImportedReferenceDeltas
        
        Returns: 
            int:
                The countImportedReferenceDeltas
        """
        if "countImportedReferenceDeltas" in self._prop_dict:
            return self._prop_dict["countImportedReferenceDeltas"]
        else:
            return None

    @count_imported_reference_deltas.setter
    def count_imported_reference_deltas(self, val):
        self._prop_dict["countImportedReferenceDeltas"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`SynchronizationTaskExecutionResult<onedrivesdk.model.synchronization_task_execution_result.SynchronizationTaskExecutionResult>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = SynchronizationTaskExecutionResult(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val
    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns: 
            :class:`SynchronizationError<onedrivesdk.model.synchronization_error.SynchronizationError>`:
                The error
        """
        if "error" in self._prop_dict:
            if isinstance(self._prop_dict["error"], OneDriveObjectBase):
                return self._prop_dict["error"]
            else :
                self._prop_dict["error"] = SynchronizationError(self._prop_dict["error"])
                return self._prop_dict["error"]

        return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val
    @property
    def time_began(self):
        """Gets and sets the timeBegan
        
        Returns: 
            datetime:
                The timeBegan
        """
        if "timeBegan" in self._prop_dict:
            return datetime.strptime(self._prop_dict["timeBegan"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @time_began.setter
    def time_began(self, val):
        self._prop_dict["timeBegan"] = val.isoformat()+"Z"

    @property
    def time_ended(self):
        """Gets and sets the timeEnded
        
        Returns: 
            datetime:
                The timeEnded
        """
        if "timeEnded" in self._prop_dict:
            return datetime.strptime(self._prop_dict["timeEnded"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @time_ended.setter
    def time_ended(self, val):
        self._prop_dict["timeEnded"] = val.isoformat()+"Z"

