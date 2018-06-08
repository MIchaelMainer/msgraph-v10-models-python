# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.conditional_access_policy_result import ConditionalAccessPolicyResult
from ..one_drive_object_base import OneDriveObjectBase


class ConditionalAccessPolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def display_name(self):
        """Gets and sets the displayName
        
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
    def enforced_grant_controls(self):
        """Gets and sets the enforcedGrantControls
        
        Returns: 
            str:
                The enforcedGrantControls
        """
        if "enforcedGrantControls" in self._prop_dict:
            return self._prop_dict["enforcedGrantControls"]
        else:
            return None

    @enforced_grant_controls.setter
    def enforced_grant_controls(self, val):
        self._prop_dict["enforcedGrantControls"] = val

    @property
    def enforced_session_controls(self):
        """Gets and sets the enforcedSessionControls
        
        Returns: 
            str:
                The enforcedSessionControls
        """
        if "enforcedSessionControls" in self._prop_dict:
            return self._prop_dict["enforcedSessionControls"]
        else:
            return None

    @enforced_session_controls.setter
    def enforced_session_controls(self, val):
        self._prop_dict["enforcedSessionControls"] = val

    @property
    def result(self):
        """
        Gets and sets the result
        
        Returns: 
            :class:`ConditionalAccessPolicyResult<onedrivesdk.model.conditional_access_policy_result.ConditionalAccessPolicyResult>`:
                The result
        """
        if "result" in self._prop_dict:
            if isinstance(self._prop_dict["result"], OneDriveObjectBase):
                return self._prop_dict["result"]
            else :
                self._prop_dict["result"] = ConditionalAccessPolicyResult(self._prop_dict["result"])
                return self._prop_dict["result"]

        return None

    @result.setter
    def result(self, val):
        self._prop_dict["result"] = val
