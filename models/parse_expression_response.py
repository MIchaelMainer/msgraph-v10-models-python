# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.public_error import PublicError
from ..model.attribute_mapping_source import AttributeMappingSource
from ..one_drive_object_base import OneDriveObjectBase


class ParseExpressionResponse(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns: 
            :class:`PublicError<onedrivesdk.model.public_error.PublicError>`:
                The error
        """
        if "error" in self._prop_dict:
            if isinstance(self._prop_dict["error"], OneDriveObjectBase):
                return self._prop_dict["error"]
            else :
                self._prop_dict["error"] = PublicError(self._prop_dict["error"])
                return self._prop_dict["error"]

        return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val
    @property
    def evaluation_succeeded(self):
        """Gets and sets the evaluationSucceeded
        
        Returns: 
            bool:
                The evaluationSucceeded
        """
        if "evaluationSucceeded" in self._prop_dict:
            return self._prop_dict["evaluationSucceeded"]
        else:
            return None

    @evaluation_succeeded.setter
    def evaluation_succeeded(self, val):
        self._prop_dict["evaluationSucceeded"] = val

    @property
    def evaluation_result(self):
        """Gets and sets the evaluationResult
        
        Returns: 
            str:
                The evaluationResult
        """
        if "evaluationResult" in self._prop_dict:
            return self._prop_dict["evaluationResult"]
        else:
            return None

    @evaluation_result.setter
    def evaluation_result(self, val):
        self._prop_dict["evaluationResult"] = val

    @property
    def parsed_expression(self):
        """
        Gets and sets the parsedExpression
        
        Returns: 
            :class:`AttributeMappingSource<onedrivesdk.model.attribute_mapping_source.AttributeMappingSource>`:
                The parsedExpression
        """
        if "parsedExpression" in self._prop_dict:
            if isinstance(self._prop_dict["parsedExpression"], OneDriveObjectBase):
                return self._prop_dict["parsedExpression"]
            else :
                self._prop_dict["parsedExpression"] = AttributeMappingSource(self._prop_dict["parsedExpression"])
                return self._prop_dict["parsedExpression"]

        return None

    @parsed_expression.setter
    def parsed_expression(self, val):
        self._prop_dict["parsedExpression"] = val
    @property
    def parsing_succeeded(self):
        """Gets and sets the parsingSucceeded
        
        Returns: 
            bool:
                The parsingSucceeded
        """
        if "parsingSucceeded" in self._prop_dict:
            return self._prop_dict["parsingSucceeded"]
        else:
            return None

    @parsing_succeeded.setter
    def parsing_succeeded(self, val):
        self._prop_dict["parsingSucceeded"] = val

