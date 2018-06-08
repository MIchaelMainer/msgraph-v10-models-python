# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.agreement_acceptance_state import AgreementAcceptanceState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class AgreementAcceptance(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def agreement_id(self):
        """
        Gets and sets the agreementId
        
        Returns:
            str:
                The agreementId
        """
        if "agreementId" in self._prop_dict:
            return self._prop_dict["agreementId"]
        else:
            return None

    @agreement_id.setter
    def agreement_id(self, val):
        self._prop_dict["agreementId"] = val

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
    def agreement_file_id(self):
        """
        Gets and sets the agreementFileId
        
        Returns:
            str:
                The agreementFileId
        """
        if "agreementFileId" in self._prop_dict:
            return self._prop_dict["agreementFileId"]
        else:
            return None

    @agreement_file_id.setter
    def agreement_file_id(self, val):
        self._prop_dict["agreementFileId"] = val

    @property
    def recorded_date_time(self):
        """
        Gets and sets the recordedDateTime
        
        Returns:
            datetime:
                The recordedDateTime
        """
        if "recordedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["recordedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @recorded_date_time.setter
    def recorded_date_time(self, val):
        self._prop_dict["recordedDateTime"] = val.isoformat()+"Z"

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
    def user_email(self):
        """
        Gets and sets the userEmail
        
        Returns:
            str:
                The userEmail
        """
        if "userEmail" in self._prop_dict:
            return self._prop_dict["userEmail"]
        else:
            return None

    @user_email.setter
    def user_email(self, val):
        self._prop_dict["userEmail"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`AgreementAcceptanceState<onedrivesdk.model.agreement_acceptance_state.AgreementAcceptanceState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = AgreementAcceptanceState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

