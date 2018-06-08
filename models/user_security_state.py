# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.logon_type import LogonType
from ..model.user_account_security_type import UserAccountSecurityType
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class UserSecurityState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_name(self):
        """Gets and sets the accountName
        
        Returns: 
            str:
                The accountName
        """
        if "accountName" in self._prop_dict:
            return self._prop_dict["accountName"]
        else:
            return None

    @account_name.setter
    def account_name(self, val):
        self._prop_dict["accountName"] = val

    @property
    def domain_name(self):
        """Gets and sets the domainName
        
        Returns: 
            str:
                The domainName
        """
        if "domainName" in self._prop_dict:
            return self._prop_dict["domainName"]
        else:
            return None

    @domain_name.setter
    def domain_name(self, val):
        self._prop_dict["domainName"] = val

    @property
    def logon_date_time(self):
        """Gets and sets the logonDateTime
        
        Returns: 
            datetime:
                The logonDateTime
        """
        if "logonDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["logonDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @logon_date_time.setter
    def logon_date_time(self, val):
        self._prop_dict["logonDateTime"] = val.isoformat()+"Z"

    @property
    def logon_id(self):
        """Gets and sets the logonId
        
        Returns: 
            str:
                The logonId
        """
        if "logonId" in self._prop_dict:
            return self._prop_dict["logonId"]
        else:
            return None

    @logon_id.setter
    def logon_id(self, val):
        self._prop_dict["logonId"] = val

    @property
    def logon_ip_address(self):
        """Gets and sets the logonIpAddress
        
        Returns: 
            str:
                The logonIpAddress
        """
        if "logonIpAddress" in self._prop_dict:
            return self._prop_dict["logonIpAddress"]
        else:
            return None

    @logon_ip_address.setter
    def logon_ip_address(self, val):
        self._prop_dict["logonIpAddress"] = val

    @property
    def logon_location(self):
        """Gets and sets the logonLocation
        
        Returns: 
            str:
                The logonLocation
        """
        if "logonLocation" in self._prop_dict:
            return self._prop_dict["logonLocation"]
        else:
            return None

    @logon_location.setter
    def logon_location(self, val):
        self._prop_dict["logonLocation"] = val

    @property
    def logon_type(self):
        """
        Gets and sets the logonType
        
        Returns: 
            :class:`LogonType<onedrivesdk.model.logon_type.LogonType>`:
                The logonType
        """
        if "logonType" in self._prop_dict:
            if isinstance(self._prop_dict["logonType"], OneDriveObjectBase):
                return self._prop_dict["logonType"]
            else :
                self._prop_dict["logonType"] = LogonType(self._prop_dict["logonType"])
                return self._prop_dict["logonType"]

        return None

    @logon_type.setter
    def logon_type(self, val):
        self._prop_dict["logonType"] = val
    @property
    def on_premises_security_identifier(self):
        """Gets and sets the onPremisesSecurityIdentifier
        
        Returns: 
            str:
                The onPremisesSecurityIdentifier
        """
        if "onPremisesSecurityIdentifier" in self._prop_dict:
            return self._prop_dict["onPremisesSecurityIdentifier"]
        else:
            return None

    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self, val):
        self._prop_dict["onPremisesSecurityIdentifier"] = val

    @property
    def risk_score(self):
        """Gets and sets the riskScore
        
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
    def user_account_type(self):
        """
        Gets and sets the userAccountType
        
        Returns: 
            :class:`UserAccountSecurityType<onedrivesdk.model.user_account_security_type.UserAccountSecurityType>`:
                The userAccountType
        """
        if "userAccountType" in self._prop_dict:
            if isinstance(self._prop_dict["userAccountType"], OneDriveObjectBase):
                return self._prop_dict["userAccountType"]
            else :
                self._prop_dict["userAccountType"] = UserAccountSecurityType(self._prop_dict["userAccountType"])
                return self._prop_dict["userAccountType"]

        return None

    @user_account_type.setter
    def user_account_type(self, val):
        self._prop_dict["userAccountType"] = val
    @property
    def user_principal_name(self):
        """Gets and sets the userPrincipalName
        
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

