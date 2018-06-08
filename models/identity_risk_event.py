# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.risk_level import RiskLevel
from ..model.risk_event_status import RiskEventStatus
from ..model.user import User
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class IdentityRiskEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_display_name(self):
        """
        Gets and sets the userDisplayName
        
        Returns:
            str:
                The userDisplayName
        """
        if "userDisplayName" in self._prop_dict:
            return self._prop_dict["userDisplayName"]
        else:
            return None

    @user_display_name.setter
    def user_display_name(self, val):
        self._prop_dict["userDisplayName"] = val

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

    @property
    def risk_event_date_time(self):
        """
        Gets and sets the riskEventDateTime
        
        Returns:
            datetime:
                The riskEventDateTime
        """
        if "riskEventDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["riskEventDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @risk_event_date_time.setter
    def risk_event_date_time(self, val):
        self._prop_dict["riskEventDateTime"] = val.isoformat()+"Z"

    @property
    def risk_event_type(self):
        """
        Gets and sets the riskEventType
        
        Returns:
            str:
                The riskEventType
        """
        if "riskEventType" in self._prop_dict:
            return self._prop_dict["riskEventType"]
        else:
            return None

    @risk_event_type.setter
    def risk_event_type(self, val):
        self._prop_dict["riskEventType"] = val

    @property
    def risk_level(self):
        """
        Gets and sets the riskLevel
        
        Returns: 
            :class:`RiskLevel<onedrivesdk.model.risk_level.RiskLevel>`:
                The riskLevel
        """
        if "riskLevel" in self._prop_dict:
            if isinstance(self._prop_dict["riskLevel"], OneDriveObjectBase):
                return self._prop_dict["riskLevel"]
            else :
                self._prop_dict["riskLevel"] = RiskLevel(self._prop_dict["riskLevel"])
                return self._prop_dict["riskLevel"]

        return None

    @risk_level.setter
    def risk_level(self, val):
        self._prop_dict["riskLevel"] = val

    @property
    def risk_event_status(self):
        """
        Gets and sets the riskEventStatus
        
        Returns: 
            :class:`RiskEventStatus<onedrivesdk.model.risk_event_status.RiskEventStatus>`:
                The riskEventStatus
        """
        if "riskEventStatus" in self._prop_dict:
            if isinstance(self._prop_dict["riskEventStatus"], OneDriveObjectBase):
                return self._prop_dict["riskEventStatus"]
            else :
                self._prop_dict["riskEventStatus"] = RiskEventStatus(self._prop_dict["riskEventStatus"])
                return self._prop_dict["riskEventStatus"]

        return None

    @risk_event_status.setter
    def risk_event_status(self, val):
        self._prop_dict["riskEventStatus"] = val

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
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def impacted_user(self):
        """
        Gets and sets the impactedUser
        
        Returns: 
            :class:`User<onedrivesdk.model.user.User>`:
                The impactedUser
        """
        if "impactedUser" in self._prop_dict:
            if isinstance(self._prop_dict["impactedUser"], OneDriveObjectBase):
                return self._prop_dict["impactedUser"]
            else :
                self._prop_dict["impactedUser"] = User(self._prop_dict["impactedUser"])
                return self._prop_dict["impactedUser"]

        return None

    @impacted_user.setter
    def impacted_user(self, val):
        self._prop_dict["impactedUser"] = val

