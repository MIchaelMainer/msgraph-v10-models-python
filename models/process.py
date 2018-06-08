# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.process_integrity_level import ProcessIntegrityLevel
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Process(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def authenticode_hash256(self):
        """Gets and sets the authenticodeHash256
        
        Returns: 
            str:
                The authenticodeHash256
        """
        if "authenticodeHash256" in self._prop_dict:
            return self._prop_dict["authenticodeHash256"]
        else:
            return None

    @authenticode_hash256.setter
    def authenticode_hash256(self, val):
        self._prop_dict["authenticodeHash256"] = val

    @property
    def command_line(self):
        """Gets and sets the commandLine
        
        Returns: 
            str:
                The commandLine
        """
        if "commandLine" in self._prop_dict:
            return self._prop_dict["commandLine"]
        else:
            return None

    @command_line.setter
    def command_line(self, val):
        self._prop_dict["commandLine"] = val

    @property
    def created_date_time(self):
        """Gets and sets the createdDateTime
        
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
    def integrity_level(self):
        """
        Gets and sets the integrityLevel
        
        Returns: 
            :class:`ProcessIntegrityLevel<onedrivesdk.model.process_integrity_level.ProcessIntegrityLevel>`:
                The integrityLevel
        """
        if "integrityLevel" in self._prop_dict:
            if isinstance(self._prop_dict["integrityLevel"], OneDriveObjectBase):
                return self._prop_dict["integrityLevel"]
            else :
                self._prop_dict["integrityLevel"] = ProcessIntegrityLevel(self._prop_dict["integrityLevel"])
                return self._prop_dict["integrityLevel"]

        return None

    @integrity_level.setter
    def integrity_level(self, val):
        self._prop_dict["integrityLevel"] = val
    @property
    def is_elevated(self):
        """Gets and sets the isElevated
        
        Returns: 
            bool:
                The isElevated
        """
        if "isElevated" in self._prop_dict:
            return self._prop_dict["isElevated"]
        else:
            return None

    @is_elevated.setter
    def is_elevated(self, val):
        self._prop_dict["isElevated"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def parent_process_created_date_time(self):
        """Gets and sets the parentProcessCreatedDateTime
        
        Returns: 
            datetime:
                The parentProcessCreatedDateTime
        """
        if "parentProcessCreatedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["parentProcessCreatedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @parent_process_created_date_time.setter
    def parent_process_created_date_time(self, val):
        self._prop_dict["parentProcessCreatedDateTime"] = val.isoformat()+"Z"

    @property
    def parent_process_id(self):
        """Gets and sets the parentProcessId
        
        Returns: 
            int:
                The parentProcessId
        """
        if "parentProcessId" in self._prop_dict:
            return self._prop_dict["parentProcessId"]
        else:
            return None

    @parent_process_id.setter
    def parent_process_id(self, val):
        self._prop_dict["parentProcessId"] = val

    @property
    def parent_process_name(self):
        """Gets and sets the parentProcessName
        
        Returns: 
            str:
                The parentProcessName
        """
        if "parentProcessName" in self._prop_dict:
            return self._prop_dict["parentProcessName"]
        else:
            return None

    @parent_process_name.setter
    def parent_process_name(self, val):
        self._prop_dict["parentProcessName"] = val

    @property
    def path(self):
        """Gets and sets the path
        
        Returns: 
            str:
                The path
        """
        if "path" in self._prop_dict:
            return self._prop_dict["path"]
        else:
            return None

    @path.setter
    def path(self, val):
        self._prop_dict["path"] = val

    @property
    def process_id(self):
        """Gets and sets the processId
        
        Returns: 
            int:
                The processId
        """
        if "processId" in self._prop_dict:
            return self._prop_dict["processId"]
        else:
            return None

    @process_id.setter
    def process_id(self, val):
        self._prop_dict["processId"] = val

    @property
    def sha256(self):
        """Gets and sets the sha256
        
        Returns: 
            str:
                The sha256
        """
        if "sha256" in self._prop_dict:
            return self._prop_dict["sha256"]
        else:
            return None

    @sha256.setter
    def sha256(self, val):
        self._prop_dict["sha256"] = val

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

