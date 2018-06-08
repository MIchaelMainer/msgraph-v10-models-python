# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.rating_new_zealand_movies_type import RatingNewZealandMoviesType
from ..model.rating_new_zealand_television_type import RatingNewZealandTelevisionType
from ..one_drive_object_base import OneDriveObjectBase


class MediaContentRatingNewZealand(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def movie_rating(self):
        """
        Gets and sets the movieRating
        
        Returns: 
            :class:`RatingNewZealandMoviesType<onedrivesdk.model.rating_new_zealand_movies_type.RatingNewZealandMoviesType>`:
                The movieRating
        """
        if "movieRating" in self._prop_dict:
            if isinstance(self._prop_dict["movieRating"], OneDriveObjectBase):
                return self._prop_dict["movieRating"]
            else :
                self._prop_dict["movieRating"] = RatingNewZealandMoviesType(self._prop_dict["movieRating"])
                return self._prop_dict["movieRating"]

        return None

    @movie_rating.setter
    def movie_rating(self, val):
        self._prop_dict["movieRating"] = val
    @property
    def tv_rating(self):
        """
        Gets and sets the tvRating
        
        Returns: 
            :class:`RatingNewZealandTelevisionType<onedrivesdk.model.rating_new_zealand_television_type.RatingNewZealandTelevisionType>`:
                The tvRating
        """
        if "tvRating" in self._prop_dict:
            if isinstance(self._prop_dict["tvRating"], OneDriveObjectBase):
                return self._prop_dict["tvRating"]
            else :
                self._prop_dict["tvRating"] = RatingNewZealandTelevisionType(self._prop_dict["tvRating"])
                return self._prop_dict["tvRating"]

        return None

    @tv_rating.setter
    def tv_rating(self, val):
        self._prop_dict["tvRating"] = val
