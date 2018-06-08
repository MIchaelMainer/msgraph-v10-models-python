# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.activity_group_state import ActivityGroupState
from ..model.application_security_state import ApplicationSecurityState
from ..model.alert_feedback import AlertFeedback
from ..model.file_security_state import FileSecurityState
from ..model.host_security_state import HostSecurityState
from ..model.malware_state import MalwareState
from ..model.network_connection import NetworkConnection
from ..model.process import Process
from ..model.alert_status import AlertStatus
from ..model.alert_trigger import AlertTrigger
from ..model.alert_type import AlertType
from ..model.user_security_state import UserSecurityState
from ..model.security_vendor_information import SecurityVendorInformation
from ..model.vulnerability_state import VulnerabilityState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Alert(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def activity_group_states(self):
        """Gets and sets the activityGroupStates
        
        Returns: 
            :class:`ActivityGroupStatesCollectionPage<onedrivesdk.request.activity_group_states_collection.ActivityGroupStatesCollectionPage>`:
                The activityGroupStates
        """
        if "activityGroupStates" in self._prop_dict:
            return ActivityGroupStatesCollectionPage(self._prop_dict["activityGroupStates"])
        else:
            return None

    @property
    def application_states(self):
        """Gets and sets the applicationStates
        
        Returns: 
            :class:`ApplicationStatesCollectionPage<onedrivesdk.request.application_states_collection.ApplicationStatesCollectionPage>`:
                The applicationStates
        """
        if "applicationStates" in self._prop_dict:
            return ApplicationStatesCollectionPage(self._prop_dict["applicationStates"])
        else:
            return None

    @property
    def assigned_to(self):
        """
        Gets and sets the assignedTo
        
        Returns:
            str:
                The assignedTo
        """
        if "assignedTo" in self._prop_dict:
            return self._prop_dict["assignedTo"]
        else:
            return None

    @assigned_to.setter
    def assigned_to(self, val):
        self._prop_dict["assignedTo"] = val

    @property
    def azure_subscription_id(self):
        """
        Gets and sets the azureSubscriptionId
        
        Returns:
            str:
                The azureSubscriptionId
        """
        if "azureSubscriptionId" in self._prop_dict:
            return self._prop_dict["azureSubscriptionId"]
        else:
            return None

    @azure_subscription_id.setter
    def azure_subscription_id(self, val):
        self._prop_dict["azureSubscriptionId"] = val

    @property
    def category(self):
        """
        Gets and sets the category
        
        Returns:
            str:
                The category
        """
        if "category" in self._prop_dict:
            return self._prop_dict["category"]
        else:
            return None

    @category.setter
    def category(self, val):
        self._prop_dict["category"] = val

    @property
    def closed_date_time(self):
        """
        Gets and sets the closedDateTime
        
        Returns:
            datetime:
                The closedDateTime
        """
        if "closedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["closedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @closed_date_time.setter
    def closed_date_time(self, val):
        self._prop_dict["closedDateTime"] = val.isoformat()+"Z"

    @property
    def comments(self):
        """
        Gets and sets the comments
        
        Returns:
            str:
                The comments
        """
        if "comments" in self._prop_dict:
            return self._prop_dict["comments"]
        else:
            return None

    @comments.setter
    def comments(self, val):
        self._prop_dict["comments"] = val

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
    def detection_ids(self):
        """
        Gets and sets the detectionIds
        
        Returns:
            str:
                The detectionIds
        """
        if "detectionIds" in self._prop_dict:
            return self._prop_dict["detectionIds"]
        else:
            return None

    @detection_ids.setter
    def detection_ids(self, val):
        self._prop_dict["detectionIds"] = val

    @property
    def event_date_time(self):
        """
        Gets and sets the eventDateTime
        
        Returns:
            datetime:
                The eventDateTime
        """
        if "eventDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["eventDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @event_date_time.setter
    def event_date_time(self, val):
        self._prop_dict["eventDateTime"] = val.isoformat()+"Z"

    @property
    def feedback(self):
        """
        Gets and sets the feedback
        
        Returns: 
            :class:`AlertFeedback<onedrivesdk.model.alert_feedback.AlertFeedback>`:
                The feedback
        """
        if "feedback" in self._prop_dict:
            if isinstance(self._prop_dict["feedback"], OneDriveObjectBase):
                return self._prop_dict["feedback"]
            else :
                self._prop_dict["feedback"] = AlertFeedback(self._prop_dict["feedback"])
                return self._prop_dict["feedback"]

        return None

    @feedback.setter
    def feedback(self, val):
        self._prop_dict["feedback"] = val

    @property
    def file_states(self):
        """Gets and sets the fileStates
        
        Returns: 
            :class:`FileStatesCollectionPage<onedrivesdk.request.file_states_collection.FileStatesCollectionPage>`:
                The fileStates
        """
        if "fileStates" in self._prop_dict:
            return FileStatesCollectionPage(self._prop_dict["fileStates"])
        else:
            return None

    @property
    def host_states(self):
        """Gets and sets the hostStates
        
        Returns: 
            :class:`HostStatesCollectionPage<onedrivesdk.request.host_states_collection.HostStatesCollectionPage>`:
                The hostStates
        """
        if "hostStates" in self._prop_dict:
            return HostStatesCollectionPage(self._prop_dict["hostStates"])
        else:
            return None

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
    def malware_states(self):
        """Gets and sets the malwareStates
        
        Returns: 
            :class:`MalwareStatesCollectionPage<onedrivesdk.request.malware_states_collection.MalwareStatesCollectionPage>`:
                The malwareStates
        """
        if "malwareStates" in self._prop_dict:
            return MalwareStatesCollectionPage(self._prop_dict["malwareStates"])
        else:
            return None

    @property
    def malware_was_running(self):
        """
        Gets and sets the malwareWasRunning
        
        Returns:
            bool:
                The malwareWasRunning
        """
        if "malwareWasRunning" in self._prop_dict:
            return self._prop_dict["malwareWasRunning"]
        else:
            return None

    @malware_was_running.setter
    def malware_was_running(self, val):
        self._prop_dict["malwareWasRunning"] = val

    @property
    def network_connections(self):
        """Gets and sets the networkConnections
        
        Returns: 
            :class:`NetworkConnectionsCollectionPage<onedrivesdk.request.network_connections_collection.NetworkConnectionsCollectionPage>`:
                The networkConnections
        """
        if "networkConnections" in self._prop_dict:
            return NetworkConnectionsCollectionPage(self._prop_dict["networkConnections"])
        else:
            return None

    @property
    def processes(self):
        """Gets and sets the processes
        
        Returns: 
            :class:`ProcessesCollectionPage<onedrivesdk.request.processes_collection.ProcessesCollectionPage>`:
                The processes
        """
        if "processes" in self._prop_dict:
            return ProcessesCollectionPage(self._prop_dict["processes"])
        else:
            return None

    @property
    def recommended_actions(self):
        """
        Gets and sets the recommendedActions
        
        Returns:
            str:
                The recommendedActions
        """
        if "recommendedActions" in self._prop_dict:
            return self._prop_dict["recommendedActions"]
        else:
            return None

    @recommended_actions.setter
    def recommended_actions(self, val):
        self._prop_dict["recommendedActions"] = val

    @property
    def risk_score(self):
        """
        Gets and sets the riskScore
        
        Returns:
            str:
                The riskScore
        """
        if "riskScore" in self._prop_dict:
            return self._prop_dict["riskScore"]
        else:
            return None

    @risk_score.setter
    def risk_score(self, val):
        self._prop_dict["riskScore"] = val

    @property
    def tags(self):
        """
        Gets and sets the tags
        
        Returns:
            str:
                The tags
        """
        if "tags" in self._prop_dict:
            return self._prop_dict["tags"]
        else:
            return None

    @tags.setter
    def tags(self, val):
        self._prop_dict["tags"] = val

    @property
    def severity(self):
        """
        Gets and sets the severity
        
        Returns:
            str:
                The severity
        """
        if "severity" in self._prop_dict:
            return self._prop_dict["severity"]
        else:
            return None

    @severity.setter
    def severity(self, val):
        self._prop_dict["severity"] = val

    @property
    def source_materials(self):
        """
        Gets and sets the sourceMaterials
        
        Returns:
            str:
                The sourceMaterials
        """
        if "sourceMaterials" in self._prop_dict:
            return self._prop_dict["sourceMaterials"]
        else:
            return None

    @source_materials.setter
    def source_materials(self, val):
        self._prop_dict["sourceMaterials"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`AlertStatus<onedrivesdk.model.alert_status.AlertStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = AlertStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def azure_tenant_id(self):
        """
        Gets and sets the azureTenantId
        
        Returns:
            str:
                The azureTenantId
        """
        if "azureTenantId" in self._prop_dict:
            return self._prop_dict["azureTenantId"]
        else:
            return None

    @azure_tenant_id.setter
    def azure_tenant_id(self, val):
        self._prop_dict["azureTenantId"] = val

    @property
    def title(self):
        """
        Gets and sets the title
        
        Returns:
            str:
                The title
        """
        if "title" in self._prop_dict:
            return self._prop_dict["title"]
        else:
            return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

    @property
    def triggers(self):
        """Gets and sets the triggers
        
        Returns: 
            :class:`TriggersCollectionPage<onedrivesdk.request.triggers_collection.TriggersCollectionPage>`:
                The triggers
        """
        if "triggers" in self._prop_dict:
            return TriggersCollectionPage(self._prop_dict["triggers"])
        else:
            return None

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns: 
            :class:`AlertType<onedrivesdk.model.alert_type.AlertType>`:
                The type
        """
        if "type" in self._prop_dict:
            if isinstance(self._prop_dict["type"], OneDriveObjectBase):
                return self._prop_dict["type"]
            else :
                self._prop_dict["type"] = AlertType(self._prop_dict["type"])
                return self._prop_dict["type"]

        return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def user_states(self):
        """Gets and sets the userStates
        
        Returns: 
            :class:`UserStatesCollectionPage<onedrivesdk.request.user_states_collection.UserStatesCollectionPage>`:
                The userStates
        """
        if "userStates" in self._prop_dict:
            return UserStatesCollectionPage(self._prop_dict["userStates"])
        else:
            return None

    @property
    def vendor_information(self):
        """
        Gets and sets the vendorInformation
        
        Returns: 
            :class:`SecurityVendorInformation<onedrivesdk.model.security_vendor_information.SecurityVendorInformation>`:
                The vendorInformation
        """
        if "vendorInformation" in self._prop_dict:
            if isinstance(self._prop_dict["vendorInformation"], OneDriveObjectBase):
                return self._prop_dict["vendorInformation"]
            else :
                self._prop_dict["vendorInformation"] = SecurityVendorInformation(self._prop_dict["vendorInformation"])
                return self._prop_dict["vendorInformation"]

        return None

    @vendor_information.setter
    def vendor_information(self, val):
        self._prop_dict["vendorInformation"] = val

    @property
    def vulnerability_states(self):
        """Gets and sets the vulnerabilityStates
        
        Returns: 
            :class:`VulnerabilityStatesCollectionPage<onedrivesdk.request.vulnerability_states_collection.VulnerabilityStatesCollectionPage>`:
                The vulnerabilityStates
        """
        if "vulnerabilityStates" in self._prop_dict:
            return VulnerabilityStatesCollectionPage(self._prop_dict["vulnerabilityStates"])
        else:
            return None

