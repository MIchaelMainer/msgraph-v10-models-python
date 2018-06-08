# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedRoleSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def approver_ids(self):
        """
        Gets and sets the approverIds
        
        Returns:
            str:
                The approverIds
        """
        if "approverIds" in self._prop_dict:
            return self._prop_dict["approverIds"]
        else:
            return None

    @approver_ids.setter
    def approver_ids(self, val):
        self._prop_dict["approverIds"] = val

    @property
    def min_elevation_duration(self):
        """
        Gets and sets the minElevationDuration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The minElevationDuration
        """
        if "minElevationDuration" in self._prop_dict:
            if isinstance(self._prop_dict["minElevationDuration"], OneDriveObjectBase):
                return self._prop_dict["minElevationDuration"]
            else :
                self._prop_dict["minElevationDuration"] = Duration(self._prop_dict["minElevationDuration"])
                return self._prop_dict["minElevationDuration"]

        return None

    @min_elevation_duration.setter
    def min_elevation_duration(self, val):
        self._prop_dict["minElevationDuration"] = val

    @property
    def max_elavation_duration(self):
        """
        Gets and sets the maxElavationDuration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The maxElavationDuration
        """
        if "maxElavationDuration" in self._prop_dict:
            if isinstance(self._prop_dict["maxElavationDuration"], OneDriveObjectBase):
                return self._prop_dict["maxElavationDuration"]
            else :
                self._prop_dict["maxElavationDuration"] = Duration(self._prop_dict["maxElavationDuration"])
                return self._prop_dict["maxElavationDuration"]

        return None

    @max_elavation_duration.setter
    def max_elavation_duration(self, val):
        self._prop_dict["maxElavationDuration"] = val

    @property
    def elevation_duration(self):
        """
        Gets and sets the elevationDuration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The elevationDuration
        """
        if "elevationDuration" in self._prop_dict:
            if isinstance(self._prop_dict["elevationDuration"], OneDriveObjectBase):
                return self._prop_dict["elevationDuration"]
            else :
                self._prop_dict["elevationDuration"] = Duration(self._prop_dict["elevationDuration"])
                return self._prop_dict["elevationDuration"]

        return None

    @elevation_duration.setter
    def elevation_duration(self, val):
        self._prop_dict["elevationDuration"] = val

    @property
    def notification_to_user_on_elevation(self):
        """
        Gets and sets the notificationToUserOnElevation
        
        Returns:
            bool:
                The notificationToUserOnElevation
        """
        if "notificationToUserOnElevation" in self._prop_dict:
            return self._prop_dict["notificationToUserOnElevation"]
        else:
            return None

    @notification_to_user_on_elevation.setter
    def notification_to_user_on_elevation(self, val):
        self._prop_dict["notificationToUserOnElevation"] = val

    @property
    def ticketing_info_on_elevation(self):
        """
        Gets and sets the ticketingInfoOnElevation
        
        Returns:
            bool:
                The ticketingInfoOnElevation
        """
        if "ticketingInfoOnElevation" in self._prop_dict:
            return self._prop_dict["ticketingInfoOnElevation"]
        else:
            return None

    @ticketing_info_on_elevation.setter
    def ticketing_info_on_elevation(self, val):
        self._prop_dict["ticketingInfoOnElevation"] = val

    @property
    def mfa_on_elevation(self):
        """
        Gets and sets the mfaOnElevation
        
        Returns:
            bool:
                The mfaOnElevation
        """
        if "mfaOnElevation" in self._prop_dict:
            return self._prop_dict["mfaOnElevation"]
        else:
            return None

    @mfa_on_elevation.setter
    def mfa_on_elevation(self, val):
        self._prop_dict["mfaOnElevation"] = val

    @property
    def last_global_admin(self):
        """
        Gets and sets the lastGlobalAdmin
        
        Returns:
            bool:
                The lastGlobalAdmin
        """
        if "lastGlobalAdmin" in self._prop_dict:
            return self._prop_dict["lastGlobalAdmin"]
        else:
            return None

    @last_global_admin.setter
    def last_global_admin(self, val):
        self._prop_dict["lastGlobalAdmin"] = val

    @property
    def is_mfa_on_elevation_configurable(self):
        """
        Gets and sets the isMfaOnElevationConfigurable
        
        Returns:
            bool:
                The isMfaOnElevationConfigurable
        """
        if "isMfaOnElevationConfigurable" in self._prop_dict:
            return self._prop_dict["isMfaOnElevationConfigurable"]
        else:
            return None

    @is_mfa_on_elevation_configurable.setter
    def is_mfa_on_elevation_configurable(self, val):
        self._prop_dict["isMfaOnElevationConfigurable"] = val

    @property
    def approval_on_elevation(self):
        """
        Gets and sets the approvalOnElevation
        
        Returns:
            bool:
                The approvalOnElevation
        """
        if "approvalOnElevation" in self._prop_dict:
            return self._prop_dict["approvalOnElevation"]
        else:
            return None

    @approval_on_elevation.setter
    def approval_on_elevation(self, val):
        self._prop_dict["approvalOnElevation"] = val

