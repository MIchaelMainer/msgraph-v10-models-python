# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.user_account_security_type import UserAccountSecurityType
from ..model.logon_type import LogonType
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class LogonUser(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_type(self):
        """
        Gets and sets the accountType
        
        Returns: 
            :class:`UserAccountSecurityType<onedrivesdk.model.user_account_security_type.UserAccountSecurityType>`:
                The accountType
        """
        if "accountType" in self._prop_dict:
            if isinstance(self._prop_dict["accountType"], OneDriveObjectBase):
                return self._prop_dict["accountType"]
            else :
                self._prop_dict["accountType"] = UserAccountSecurityType(self._prop_dict["accountType"])
                return self._prop_dict["accountType"]

        return None

    @account_type.setter
    def account_type(self, val):
        self._prop_dict["accountType"] = val
    @property
    def first_seen_date_time(self):
        """Gets and sets the firstSeenDateTime
        
        Returns: 
            datetime:
                The firstSeenDateTime
        """
        if "firstSeenDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["firstSeenDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @first_seen_date_time.setter
    def first_seen_date_time(self, val):
        self._prop_dict["firstSeenDateTime"] = val.isoformat()+"Z"

    @property
    def last_seen_date_time(self):
        """Gets and sets the lastSeenDateTime
        
        Returns: 
            datetime:
                The lastSeenDateTime
        """
        if "lastSeenDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSeenDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_seen_date_time.setter
    def last_seen_date_time(self, val):
        self._prop_dict["lastSeenDateTime"] = val.isoformat()+"Z"

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
    def account_domain(self):
        """Gets and sets the accountDomain
        
        Returns: 
            str:
                The accountDomain
        """
        if "accountDomain" in self._prop_dict:
            return self._prop_dict["accountDomain"]
        else:
            return None

    @account_domain.setter
    def account_domain(self, val):
        self._prop_dict["accountDomain"] = val

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
    def logon_types(self):
        """
        Gets and sets the logonTypes
        
        Returns: 
            :class:`LogonType<onedrivesdk.model.logon_type.LogonType>`:
                The logonTypes
        """
        if "logonTypes" in self._prop_dict:
            if isinstance(self._prop_dict["logonTypes"], OneDriveObjectBase):
                return self._prop_dict["logonTypes"]
            else :
                self._prop_dict["logonTypes"] = LogonType(self._prop_dict["logonTypes"])
                return self._prop_dict["logonTypes"]

        return None

    @logon_types.setter
    def logon_types(self, val):
        self._prop_dict["logonTypes"] = val
