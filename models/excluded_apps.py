# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ExcludedApps(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def access(self):
        """Gets and sets the access
        
        Returns: 
            bool:
                The access
        """
        if "access" in self._prop_dict:
            return self._prop_dict["access"]
        else:
            return None

    @access.setter
    def access(self, val):
        self._prop_dict["access"] = val

    @property
    def excel(self):
        """Gets and sets the excel
        
        Returns: 
            bool:
                The excel
        """
        if "excel" in self._prop_dict:
            return self._prop_dict["excel"]
        else:
            return None

    @excel.setter
    def excel(self, val):
        self._prop_dict["excel"] = val

    @property
    def groove(self):
        """Gets and sets the groove
        
        Returns: 
            bool:
                The groove
        """
        if "groove" in self._prop_dict:
            return self._prop_dict["groove"]
        else:
            return None

    @groove.setter
    def groove(self, val):
        self._prop_dict["groove"] = val

    @property
    def info_path(self):
        """Gets and sets the infoPath
        
        Returns: 
            bool:
                The infoPath
        """
        if "infoPath" in self._prop_dict:
            return self._prop_dict["infoPath"]
        else:
            return None

    @info_path.setter
    def info_path(self, val):
        self._prop_dict["infoPath"] = val

    @property
    def lync(self):
        """Gets and sets the lync
        
        Returns: 
            bool:
                The lync
        """
        if "lync" in self._prop_dict:
            return self._prop_dict["lync"]
        else:
            return None

    @lync.setter
    def lync(self, val):
        self._prop_dict["lync"] = val

    @property
    def one_drive(self):
        """Gets and sets the oneDrive
        
        Returns: 
            bool:
                The oneDrive
        """
        if "oneDrive" in self._prop_dict:
            return self._prop_dict["oneDrive"]
        else:
            return None

    @one_drive.setter
    def one_drive(self, val):
        self._prop_dict["oneDrive"] = val

    @property
    def one_note(self):
        """Gets and sets the oneNote
        
        Returns: 
            bool:
                The oneNote
        """
        if "oneNote" in self._prop_dict:
            return self._prop_dict["oneNote"]
        else:
            return None

    @one_note.setter
    def one_note(self, val):
        self._prop_dict["oneNote"] = val

    @property
    def outlook(self):
        """Gets and sets the outlook
        
        Returns: 
            bool:
                The outlook
        """
        if "outlook" in self._prop_dict:
            return self._prop_dict["outlook"]
        else:
            return None

    @outlook.setter
    def outlook(self, val):
        self._prop_dict["outlook"] = val

    @property
    def power_point(self):
        """Gets and sets the powerPoint
        
        Returns: 
            bool:
                The powerPoint
        """
        if "powerPoint" in self._prop_dict:
            return self._prop_dict["powerPoint"]
        else:
            return None

    @power_point.setter
    def power_point(self, val):
        self._prop_dict["powerPoint"] = val

    @property
    def publisher(self):
        """Gets and sets the publisher
        
        Returns: 
            bool:
                The publisher
        """
        if "publisher" in self._prop_dict:
            return self._prop_dict["publisher"]
        else:
            return None

    @publisher.setter
    def publisher(self, val):
        self._prop_dict["publisher"] = val

    @property
    def share_point_designer(self):
        """Gets and sets the sharePointDesigner
        
        Returns: 
            bool:
                The sharePointDesigner
        """
        if "sharePointDesigner" in self._prop_dict:
            return self._prop_dict["sharePointDesigner"]
        else:
            return None

    @share_point_designer.setter
    def share_point_designer(self, val):
        self._prop_dict["sharePointDesigner"] = val

    @property
    def visio(self):
        """Gets and sets the visio
        
        Returns: 
            bool:
                The visio
        """
        if "visio" in self._prop_dict:
            return self._prop_dict["visio"]
        else:
            return None

    @visio.setter
    def visio(self, val):
        self._prop_dict["visio"] = val

    @property
    def word(self):
        """Gets and sets the word
        
        Returns: 
            bool:
                The word
        """
        if "word" in self._prop_dict:
            return self._prop_dict["word"]
        else:
            return None

    @word.setter
    def word(self, val):
        self._prop_dict["word"] = val

