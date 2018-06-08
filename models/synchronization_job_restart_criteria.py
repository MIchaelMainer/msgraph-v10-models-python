# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.synchronization_job_restart_scope import SynchronizationJobRestartScope
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationJobRestartCriteria(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def reset_scope(self):
        """
        Gets and sets the resetScope
        
        Returns: 
            :class:`SynchronizationJobRestartScope<onedrivesdk.model.synchronization_job_restart_scope.SynchronizationJobRestartScope>`:
                The resetScope
        """
        if "resetScope" in self._prop_dict:
            if isinstance(self._prop_dict["resetScope"], OneDriveObjectBase):
                return self._prop_dict["resetScope"]
            else :
                self._prop_dict["resetScope"] = SynchronizationJobRestartScope(self._prop_dict["resetScope"])
                return self._prop_dict["resetScope"]

        return None

    @reset_scope.setter
    def reset_scope(self, val):
        self._prop_dict["resetScope"] = val
