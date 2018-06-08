# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DomainDnsSrvRecord(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name_target(self):
        """
        Gets and sets the nameTarget
        
        Returns:
            str:
                The nameTarget
        """
        if "nameTarget" in self._prop_dict:
            return self._prop_dict["nameTarget"]
        else:
            return None

    @name_target.setter
    def name_target(self, val):
        self._prop_dict["nameTarget"] = val

    @property
    def port(self):
        """
        Gets and sets the port
        
        Returns:
            int:
                The port
        """
        if "port" in self._prop_dict:
            return self._prop_dict["port"]
        else:
            return None

    @port.setter
    def port(self, val):
        self._prop_dict["port"] = val

    @property
    def priority(self):
        """
        Gets and sets the priority
        
        Returns:
            int:
                The priority
        """
        if "priority" in self._prop_dict:
            return self._prop_dict["priority"]
        else:
            return None

    @priority.setter
    def priority(self, val):
        self._prop_dict["priority"] = val

    @property
    def protocol(self):
        """
        Gets and sets the protocol
        
        Returns:
            str:
                The protocol
        """
        if "protocol" in self._prop_dict:
            return self._prop_dict["protocol"]
        else:
            return None

    @protocol.setter
    def protocol(self, val):
        self._prop_dict["protocol"] = val

    @property
    def service(self):
        """
        Gets and sets the service
        
        Returns:
            str:
                The service
        """
        if "service" in self._prop_dict:
            return self._prop_dict["service"]
        else:
            return None

    @service.setter
    def service(self, val):
        self._prop_dict["service"] = val

    @property
    def weight(self):
        """
        Gets and sets the weight
        
        Returns:
            int:
                The weight
        """
        if "weight" in self._prop_dict:
            return self._prop_dict["weight"]
        else:
            return None

    @weight.setter
    def weight(self, val):
        self._prop_dict["weight"] = val

