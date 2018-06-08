# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationError(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def entry_type(self):
        """
        Gets and sets the entryType
        
        Returns:
            str:
                The entryType
        """
        if "entryType" in self._prop_dict:
            return self._prop_dict["entryType"]
        else:
            return None

    @entry_type.setter
    def entry_type(self, val):
        self._prop_dict["entryType"] = val

    @property
    def error_code(self):
        """
        Gets and sets the errorCode
        
        Returns:
            str:
                The errorCode
        """
        if "errorCode" in self._prop_dict:
            return self._prop_dict["errorCode"]
        else:
            return None

    @error_code.setter
    def error_code(self, val):
        self._prop_dict["errorCode"] = val

    @property
    def error_message(self):
        """
        Gets and sets the errorMessage
        
        Returns:
            str:
                The errorMessage
        """
        if "errorMessage" in self._prop_dict:
            return self._prop_dict["errorMessage"]
        else:
            return None

    @error_message.setter
    def error_message(self, val):
        self._prop_dict["errorMessage"] = val

    @property
    def joining_value(self):
        """
        Gets and sets the joiningValue
        
        Returns:
            str:
                The joiningValue
        """
        if "joiningValue" in self._prop_dict:
            return self._prop_dict["joiningValue"]
        else:
            return None

    @joining_value.setter
    def joining_value(self, val):
        self._prop_dict["joiningValue"] = val

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
    def reportable_identifier(self):
        """
        Gets and sets the reportableIdentifier
        
        Returns:
            str:
                The reportableIdentifier
        """
        if "reportableIdentifier" in self._prop_dict:
            return self._prop_dict["reportableIdentifier"]
        else:
            return None

    @reportable_identifier.setter
    def reportable_identifier(self, val):
        self._prop_dict["reportableIdentifier"] = val

