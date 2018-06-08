# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.run_schedule import RunSchedule
from ..model.run_as_account_type import RunAsAccountType
from ..model.device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
from ..model.device_management_script_assignment import DeviceManagementScriptAssignment
from ..model.device_management_script_run_summary import DeviceManagementScriptRunSummary
from ..model.device_management_script_device_state import DeviceManagementScriptDeviceState
from ..model.device_management_script_user_state import DeviceManagementScriptUserState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementScript(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def run_schedule(self):
        """
        Gets and sets the runSchedule
        
        Returns: 
            :class:`RunSchedule<onedrivesdk.model.run_schedule.RunSchedule>`:
                The runSchedule
        """
        if "runSchedule" in self._prop_dict:
            if isinstance(self._prop_dict["runSchedule"], OneDriveObjectBase):
                return self._prop_dict["runSchedule"]
            else :
                self._prop_dict["runSchedule"] = RunSchedule(self._prop_dict["runSchedule"])
                return self._prop_dict["runSchedule"]

        return None

    @run_schedule.setter
    def run_schedule(self, val):
        self._prop_dict["runSchedule"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def run_as_account(self):
        """
        Gets and sets the runAsAccount
        
        Returns: 
            :class:`RunAsAccountType<onedrivesdk.model.run_as_account_type.RunAsAccountType>`:
                The runAsAccount
        """
        if "runAsAccount" in self._prop_dict:
            if isinstance(self._prop_dict["runAsAccount"], OneDriveObjectBase):
                return self._prop_dict["runAsAccount"]
            else :
                self._prop_dict["runAsAccount"] = RunAsAccountType(self._prop_dict["runAsAccount"])
                return self._prop_dict["runAsAccount"]

        return None

    @run_as_account.setter
    def run_as_account(self, val):
        self._prop_dict["runAsAccount"] = val

    @property
    def enforce_signature_check(self):
        """
        Gets and sets the enforceSignatureCheck
        
        Returns:
            bool:
                The enforceSignatureCheck
        """
        if "enforceSignatureCheck" in self._prop_dict:
            return self._prop_dict["enforceSignatureCheck"]
        else:
            return None

    @enforce_signature_check.setter
    def enforce_signature_check(self, val):
        self._prop_dict["enforceSignatureCheck"] = val

    @property
    def file_name(self):
        """
        Gets and sets the fileName
        
        Returns:
            str:
                The fileName
        """
        if "fileName" in self._prop_dict:
            return self._prop_dict["fileName"]
        else:
            return None

    @file_name.setter
    def file_name(self, val):
        self._prop_dict["fileName"] = val

    @property
    def group_assignments(self):
        """Gets and sets the groupAssignments
        
        Returns: 
            :class:`GroupAssignmentsCollectionPage<onedrivesdk.request.group_assignments_collection.GroupAssignmentsCollectionPage>`:
                The groupAssignments
        """
        if "groupAssignments" in self._prop_dict:
            return GroupAssignmentsCollectionPage(self._prop_dict["groupAssignments"])
        else:
            return None

    @property
    def assignments(self):
        """Gets and sets the assignments
        
        Returns: 
            :class:`AssignmentsCollectionPage<onedrivesdk.request.assignments_collection.AssignmentsCollectionPage>`:
                The assignments
        """
        if "assignments" in self._prop_dict:
            return AssignmentsCollectionPage(self._prop_dict["assignments"])
        else:
            return None

    @property
    def run_summary(self):
        """
        Gets and sets the runSummary
        
        Returns: 
            :class:`DeviceManagementScriptRunSummary<onedrivesdk.model.device_management_script_run_summary.DeviceManagementScriptRunSummary>`:
                The runSummary
        """
        if "runSummary" in self._prop_dict:
            if isinstance(self._prop_dict["runSummary"], OneDriveObjectBase):
                return self._prop_dict["runSummary"]
            else :
                self._prop_dict["runSummary"] = DeviceManagementScriptRunSummary(self._prop_dict["runSummary"])
                return self._prop_dict["runSummary"]

        return None

    @run_summary.setter
    def run_summary(self, val):
        self._prop_dict["runSummary"] = val

    @property
    def device_run_states(self):
        """Gets and sets the deviceRunStates
        
        Returns: 
            :class:`DeviceRunStatesCollectionPage<onedrivesdk.request.device_run_states_collection.DeviceRunStatesCollectionPage>`:
                The deviceRunStates
        """
        if "deviceRunStates" in self._prop_dict:
            return DeviceRunStatesCollectionPage(self._prop_dict["deviceRunStates"])
        else:
            return None

    @property
    def user_run_states(self):
        """Gets and sets the userRunStates
        
        Returns: 
            :class:`UserRunStatesCollectionPage<onedrivesdk.request.user_run_states_collection.UserRunStatesCollectionPage>`:
                The userRunStates
        """
        if "userRunStates" in self._prop_dict:
            return UserRunStatesCollectionPage(self._prop_dict["userRunStates"])
        else:
            return None

