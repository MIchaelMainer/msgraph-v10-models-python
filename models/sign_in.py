# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sign_in_status import SignInStatus
from ..model.device_detail import DeviceDetail
from ..model.sign_in_location import SignInLocation
from ..model.mfa_detail import MfaDetail
from ..model.conditional_access_status import ConditionalAccessStatus
from ..model.conditional_access_policy import ConditionalAccessPolicy
from ..model.risk_level import RiskLevel
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class SignIn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def app_id(self):
        """
        Gets and sets the appId
        
        Returns:
            str:
                The appId
        """
        if "appId" in self._prop_dict:
            return self._prop_dict["appId"]
        else:
            return None

    @app_id.setter
    def app_id(self, val):
        self._prop_dict["appId"] = val

    @property
    def app_display_name(self):
        """
        Gets and sets the appDisplayName
        
        Returns:
            str:
                The appDisplayName
        """
        if "appDisplayName" in self._prop_dict:
            return self._prop_dict["appDisplayName"]
        else:
            return None

    @app_display_name.setter
    def app_display_name(self, val):
        self._prop_dict["appDisplayName"] = val

    @property
    def ip_address(self):
        """
        Gets and sets the ipAddress
        
        Returns:
            str:
                The ipAddress
        """
        if "ipAddress" in self._prop_dict:
            return self._prop_dict["ipAddress"]
        else:
            return None

    @ip_address.setter
    def ip_address(self, val):
        self._prop_dict["ipAddress"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`SignInStatus<onedrivesdk.model.sign_in_status.SignInStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = SignInStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def client_app_used(self):
        """
        Gets and sets the clientAppUsed
        
        Returns:
            str:
                The clientAppUsed
        """
        if "clientAppUsed" in self._prop_dict:
            return self._prop_dict["clientAppUsed"]
        else:
            return None

    @client_app_used.setter
    def client_app_used(self, val):
        self._prop_dict["clientAppUsed"] = val

    @property
    def device_detail(self):
        """
        Gets and sets the deviceDetail
        
        Returns: 
            :class:`DeviceDetail<onedrivesdk.model.device_detail.DeviceDetail>`:
                The deviceDetail
        """
        if "deviceDetail" in self._prop_dict:
            if isinstance(self._prop_dict["deviceDetail"], OneDriveObjectBase):
                return self._prop_dict["deviceDetail"]
            else :
                self._prop_dict["deviceDetail"] = DeviceDetail(self._prop_dict["deviceDetail"])
                return self._prop_dict["deviceDetail"]

        return None

    @device_detail.setter
    def device_detail(self, val):
        self._prop_dict["deviceDetail"] = val

    @property
    def location(self):
        """
        Gets and sets the location
        
        Returns: 
            :class:`SignInLocation<onedrivesdk.model.sign_in_location.SignInLocation>`:
                The location
        """
        if "location" in self._prop_dict:
            if isinstance(self._prop_dict["location"], OneDriveObjectBase):
                return self._prop_dict["location"]
            else :
                self._prop_dict["location"] = SignInLocation(self._prop_dict["location"])
                return self._prop_dict["location"]

        return None

    @location.setter
    def location(self, val):
        self._prop_dict["location"] = val

    @property
    def mfa_detail(self):
        """
        Gets and sets the mfaDetail
        
        Returns: 
            :class:`MfaDetail<onedrivesdk.model.mfa_detail.MfaDetail>`:
                The mfaDetail
        """
        if "mfaDetail" in self._prop_dict:
            if isinstance(self._prop_dict["mfaDetail"], OneDriveObjectBase):
                return self._prop_dict["mfaDetail"]
            else :
                self._prop_dict["mfaDetail"] = MfaDetail(self._prop_dict["mfaDetail"])
                return self._prop_dict["mfaDetail"]

        return None

    @mfa_detail.setter
    def mfa_detail(self, val):
        self._prop_dict["mfaDetail"] = val

    @property
    def correlation_id(self):
        """
        Gets and sets the correlationId
        
        Returns:
            str:
                The correlationId
        """
        if "correlationId" in self._prop_dict:
            return self._prop_dict["correlationId"]
        else:
            return None

    @correlation_id.setter
    def correlation_id(self, val):
        self._prop_dict["correlationId"] = val

    @property
    def conditional_access_status(self):
        """
        Gets and sets the conditionalAccessStatus
        
        Returns: 
            :class:`ConditionalAccessStatus<onedrivesdk.model.conditional_access_status.ConditionalAccessStatus>`:
                The conditionalAccessStatus
        """
        if "conditionalAccessStatus" in self._prop_dict:
            if isinstance(self._prop_dict["conditionalAccessStatus"], OneDriveObjectBase):
                return self._prop_dict["conditionalAccessStatus"]
            else :
                self._prop_dict["conditionalAccessStatus"] = ConditionalAccessStatus(self._prop_dict["conditionalAccessStatus"])
                return self._prop_dict["conditionalAccessStatus"]

        return None

    @conditional_access_status.setter
    def conditional_access_status(self, val):
        self._prop_dict["conditionalAccessStatus"] = val

    @property
    def conditional_access_policies(self):
        """Gets and sets the conditionalAccessPolicies
        
        Returns: 
            :class:`ConditionalAccessPoliciesCollectionPage<onedrivesdk.request.conditional_access_policies_collection.ConditionalAccessPoliciesCollectionPage>`:
                The conditionalAccessPolicies
        """
        if "conditionalAccessPolicies" in self._prop_dict:
            return ConditionalAccessPoliciesCollectionPage(self._prop_dict["conditionalAccessPolicies"])
        else:
            return None

    @property
    def is_risky(self):
        """
        Gets and sets the isRisky
        
        Returns:
            bool:
                The isRisky
        """
        if "isRisky" in self._prop_dict:
            return self._prop_dict["isRisky"]
        else:
            return None

    @is_risky.setter
    def is_risky(self, val):
        self._prop_dict["isRisky"] = val

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

