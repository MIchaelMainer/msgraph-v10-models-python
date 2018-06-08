# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class SkypeForBusinessActivityUserDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def total_peer_to_peer_session_count(self):
        """
        Gets and sets the totalPeerToPeerSessionCount
        
        Returns:
            int:
                The totalPeerToPeerSessionCount
        """
        if "totalPeerToPeerSessionCount" in self._prop_dict:
            return self._prop_dict["totalPeerToPeerSessionCount"]
        else:
            return None

    @total_peer_to_peer_session_count.setter
    def total_peer_to_peer_session_count(self, val):
        self._prop_dict["totalPeerToPeerSessionCount"] = val

    @property
    def total_organized_conference_count(self):
        """
        Gets and sets the totalOrganizedConferenceCount
        
        Returns:
            int:
                The totalOrganizedConferenceCount
        """
        if "totalOrganizedConferenceCount" in self._prop_dict:
            return self._prop_dict["totalOrganizedConferenceCount"]
        else:
            return None

    @total_organized_conference_count.setter
    def total_organized_conference_count(self, val):
        self._prop_dict["totalOrganizedConferenceCount"] = val

    @property
    def total_participated_conference_count(self):
        """
        Gets and sets the totalParticipatedConferenceCount
        
        Returns:
            int:
                The totalParticipatedConferenceCount
        """
        if "totalParticipatedConferenceCount" in self._prop_dict:
            return self._prop_dict["totalParticipatedConferenceCount"]
        else:
            return None

    @total_participated_conference_count.setter
    def total_participated_conference_count(self, val):
        self._prop_dict["totalParticipatedConferenceCount"] = val

    @property
    def peer_to_peer_last_activity_date(self):
        """
        Gets and sets the peerToPeerLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The peerToPeerLastActivityDate
        """
        if "peerToPeerLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["peerToPeerLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["peerToPeerLastActivityDate"]
            else :
                self._prop_dict["peerToPeerLastActivityDate"] = Date(self._prop_dict["peerToPeerLastActivityDate"])
                return self._prop_dict["peerToPeerLastActivityDate"]

        return None

    @peer_to_peer_last_activity_date.setter
    def peer_to_peer_last_activity_date(self, val):
        self._prop_dict["peerToPeerLastActivityDate"] = val

    @property
    def organized_conference_last_activity_date(self):
        """
        Gets and sets the organizedConferenceLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The organizedConferenceLastActivityDate
        """
        if "organizedConferenceLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["organizedConferenceLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["organizedConferenceLastActivityDate"]
            else :
                self._prop_dict["organizedConferenceLastActivityDate"] = Date(self._prop_dict["organizedConferenceLastActivityDate"])
                return self._prop_dict["organizedConferenceLastActivityDate"]

        return None

    @organized_conference_last_activity_date.setter
    def organized_conference_last_activity_date(self, val):
        self._prop_dict["organizedConferenceLastActivityDate"] = val

    @property
    def participated_conference_last_activity_date(self):
        """
        Gets and sets the participatedConferenceLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The participatedConferenceLastActivityDate
        """
        if "participatedConferenceLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["participatedConferenceLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["participatedConferenceLastActivityDate"]
            else :
                self._prop_dict["participatedConferenceLastActivityDate"] = Date(self._prop_dict["participatedConferenceLastActivityDate"])
                return self._prop_dict["participatedConferenceLastActivityDate"]

        return None

    @participated_conference_last_activity_date.setter
    def participated_conference_last_activity_date(self, val):
        self._prop_dict["participatedConferenceLastActivityDate"] = val

    @property
    def peer_to_peer_im_count(self):
        """
        Gets and sets the peerToPeerIMCount
        
        Returns:
            int:
                The peerToPeerIMCount
        """
        if "peerToPeerIMCount" in self._prop_dict:
            return self._prop_dict["peerToPeerIMCount"]
        else:
            return None

    @peer_to_peer_im_count.setter
    def peer_to_peer_im_count(self, val):
        self._prop_dict["peerToPeerIMCount"] = val

    @property
    def peer_to_peer_audio_count(self):
        """
        Gets and sets the peerToPeerAudioCount
        
        Returns:
            int:
                The peerToPeerAudioCount
        """
        if "peerToPeerAudioCount" in self._prop_dict:
            return self._prop_dict["peerToPeerAudioCount"]
        else:
            return None

    @peer_to_peer_audio_count.setter
    def peer_to_peer_audio_count(self, val):
        self._prop_dict["peerToPeerAudioCount"] = val

    @property
    def peer_to_peer_audio_minutes(self):
        """
        Gets and sets the peerToPeerAudioMinutes
        
        Returns:
            int:
                The peerToPeerAudioMinutes
        """
        if "peerToPeerAudioMinutes" in self._prop_dict:
            return self._prop_dict["peerToPeerAudioMinutes"]
        else:
            return None

    @peer_to_peer_audio_minutes.setter
    def peer_to_peer_audio_minutes(self, val):
        self._prop_dict["peerToPeerAudioMinutes"] = val

    @property
    def peer_to_peer_video_count(self):
        """
        Gets and sets the peerToPeerVideoCount
        
        Returns:
            int:
                The peerToPeerVideoCount
        """
        if "peerToPeerVideoCount" in self._prop_dict:
            return self._prop_dict["peerToPeerVideoCount"]
        else:
            return None

    @peer_to_peer_video_count.setter
    def peer_to_peer_video_count(self, val):
        self._prop_dict["peerToPeerVideoCount"] = val

    @property
    def peer_to_peer_video_minutes(self):
        """
        Gets and sets the peerToPeerVideoMinutes
        
        Returns:
            int:
                The peerToPeerVideoMinutes
        """
        if "peerToPeerVideoMinutes" in self._prop_dict:
            return self._prop_dict["peerToPeerVideoMinutes"]
        else:
            return None

    @peer_to_peer_video_minutes.setter
    def peer_to_peer_video_minutes(self, val):
        self._prop_dict["peerToPeerVideoMinutes"] = val

    @property
    def peer_to_peer_app_sharing_count(self):
        """
        Gets and sets the peerToPeerAppSharingCount
        
        Returns:
            int:
                The peerToPeerAppSharingCount
        """
        if "peerToPeerAppSharingCount" in self._prop_dict:
            return self._prop_dict["peerToPeerAppSharingCount"]
        else:
            return None

    @peer_to_peer_app_sharing_count.setter
    def peer_to_peer_app_sharing_count(self, val):
        self._prop_dict["peerToPeerAppSharingCount"] = val

    @property
    def peer_to_peer_file_transfer_count(self):
        """
        Gets and sets the peerToPeerFileTransferCount
        
        Returns:
            int:
                The peerToPeerFileTransferCount
        """
        if "peerToPeerFileTransferCount" in self._prop_dict:
            return self._prop_dict["peerToPeerFileTransferCount"]
        else:
            return None

    @peer_to_peer_file_transfer_count.setter
    def peer_to_peer_file_transfer_count(self, val):
        self._prop_dict["peerToPeerFileTransferCount"] = val

    @property
    def organized_conference_im_count(self):
        """
        Gets and sets the organizedConferenceIMCount
        
        Returns:
            int:
                The organizedConferenceIMCount
        """
        if "organizedConferenceIMCount" in self._prop_dict:
            return self._prop_dict["organizedConferenceIMCount"]
        else:
            return None

    @organized_conference_im_count.setter
    def organized_conference_im_count(self, val):
        self._prop_dict["organizedConferenceIMCount"] = val

    @property
    def organized_conference_audio_video_count(self):
        """
        Gets and sets the organizedConferenceAudioVideoCount
        
        Returns:
            int:
                The organizedConferenceAudioVideoCount
        """
        if "organizedConferenceAudioVideoCount" in self._prop_dict:
            return self._prop_dict["organizedConferenceAudioVideoCount"]
        else:
            return None

    @organized_conference_audio_video_count.setter
    def organized_conference_audio_video_count(self, val):
        self._prop_dict["organizedConferenceAudioVideoCount"] = val

    @property
    def organized_conference_audio_video_minutes(self):
        """
        Gets and sets the organizedConferenceAudioVideoMinutes
        
        Returns:
            int:
                The organizedConferenceAudioVideoMinutes
        """
        if "organizedConferenceAudioVideoMinutes" in self._prop_dict:
            return self._prop_dict["organizedConferenceAudioVideoMinutes"]
        else:
            return None

    @organized_conference_audio_video_minutes.setter
    def organized_conference_audio_video_minutes(self, val):
        self._prop_dict["organizedConferenceAudioVideoMinutes"] = val

    @property
    def organized_conference_app_sharing_count(self):
        """
        Gets and sets the organizedConferenceAppSharingCount
        
        Returns:
            int:
                The organizedConferenceAppSharingCount
        """
        if "organizedConferenceAppSharingCount" in self._prop_dict:
            return self._prop_dict["organizedConferenceAppSharingCount"]
        else:
            return None

    @organized_conference_app_sharing_count.setter
    def organized_conference_app_sharing_count(self, val):
        self._prop_dict["organizedConferenceAppSharingCount"] = val

    @property
    def organized_conference_web_count(self):
        """
        Gets and sets the organizedConferenceWebCount
        
        Returns:
            int:
                The organizedConferenceWebCount
        """
        if "organizedConferenceWebCount" in self._prop_dict:
            return self._prop_dict["organizedConferenceWebCount"]
        else:
            return None

    @organized_conference_web_count.setter
    def organized_conference_web_count(self, val):
        self._prop_dict["organizedConferenceWebCount"] = val

    @property
    def organized_conference_dial_in_out3rd_party_count(self):
        """
        Gets and sets the organizedConferenceDialInOut3rdPartyCount
        
        Returns:
            int:
                The organizedConferenceDialInOut3rdPartyCount
        """
        if "organizedConferenceDialInOut3rdPartyCount" in self._prop_dict:
            return self._prop_dict["organizedConferenceDialInOut3rdPartyCount"]
        else:
            return None

    @organized_conference_dial_in_out3rd_party_count.setter
    def organized_conference_dial_in_out3rd_party_count(self, val):
        self._prop_dict["organizedConferenceDialInOut3rdPartyCount"] = val

    @property
    def organized_conference_cloud_dial_in_out_microsoft_count(self):
        """
        Gets and sets the organizedConferenceCloudDialInOutMicrosoftCount
        
        Returns:
            int:
                The organizedConferenceCloudDialInOutMicrosoftCount
        """
        if "organizedConferenceCloudDialInOutMicrosoftCount" in self._prop_dict:
            return self._prop_dict["organizedConferenceCloudDialInOutMicrosoftCount"]
        else:
            return None

    @organized_conference_cloud_dial_in_out_microsoft_count.setter
    def organized_conference_cloud_dial_in_out_microsoft_count(self, val):
        self._prop_dict["organizedConferenceCloudDialInOutMicrosoftCount"] = val

    @property
    def organized_conference_cloud_dial_in_microsoft_minutes(self):
        """
        Gets and sets the organizedConferenceCloudDialInMicrosoftMinutes
        
        Returns:
            int:
                The organizedConferenceCloudDialInMicrosoftMinutes
        """
        if "organizedConferenceCloudDialInMicrosoftMinutes" in self._prop_dict:
            return self._prop_dict["organizedConferenceCloudDialInMicrosoftMinutes"]
        else:
            return None

    @organized_conference_cloud_dial_in_microsoft_minutes.setter
    def organized_conference_cloud_dial_in_microsoft_minutes(self, val):
        self._prop_dict["organizedConferenceCloudDialInMicrosoftMinutes"] = val

    @property
    def organized_conference_cloud_dial_out_microsoft_minutes(self):
        """
        Gets and sets the organizedConferenceCloudDialOutMicrosoftMinutes
        
        Returns:
            int:
                The organizedConferenceCloudDialOutMicrosoftMinutes
        """
        if "organizedConferenceCloudDialOutMicrosoftMinutes" in self._prop_dict:
            return self._prop_dict["organizedConferenceCloudDialOutMicrosoftMinutes"]
        else:
            return None

    @organized_conference_cloud_dial_out_microsoft_minutes.setter
    def organized_conference_cloud_dial_out_microsoft_minutes(self, val):
        self._prop_dict["organizedConferenceCloudDialOutMicrosoftMinutes"] = val

    @property
    def participated_conference_im_count(self):
        """
        Gets and sets the participatedConferenceIMCount
        
        Returns:
            int:
                The participatedConferenceIMCount
        """
        if "participatedConferenceIMCount" in self._prop_dict:
            return self._prop_dict["participatedConferenceIMCount"]
        else:
            return None

    @participated_conference_im_count.setter
    def participated_conference_im_count(self, val):
        self._prop_dict["participatedConferenceIMCount"] = val

    @property
    def participated_conference_audio_video_count(self):
        """
        Gets and sets the participatedConferenceAudioVideoCount
        
        Returns:
            int:
                The participatedConferenceAudioVideoCount
        """
        if "participatedConferenceAudioVideoCount" in self._prop_dict:
            return self._prop_dict["participatedConferenceAudioVideoCount"]
        else:
            return None

    @participated_conference_audio_video_count.setter
    def participated_conference_audio_video_count(self, val):
        self._prop_dict["participatedConferenceAudioVideoCount"] = val

    @property
    def participated_conference_audio_video_minutes(self):
        """
        Gets and sets the participatedConferenceAudioVideoMinutes
        
        Returns:
            int:
                The participatedConferenceAudioVideoMinutes
        """
        if "participatedConferenceAudioVideoMinutes" in self._prop_dict:
            return self._prop_dict["participatedConferenceAudioVideoMinutes"]
        else:
            return None

    @participated_conference_audio_video_minutes.setter
    def participated_conference_audio_video_minutes(self, val):
        self._prop_dict["participatedConferenceAudioVideoMinutes"] = val

    @property
    def participated_conference_app_sharing_count(self):
        """
        Gets and sets the participatedConferenceAppSharingCount
        
        Returns:
            int:
                The participatedConferenceAppSharingCount
        """
        if "participatedConferenceAppSharingCount" in self._prop_dict:
            return self._prop_dict["participatedConferenceAppSharingCount"]
        else:
            return None

    @participated_conference_app_sharing_count.setter
    def participated_conference_app_sharing_count(self, val):
        self._prop_dict["participatedConferenceAppSharingCount"] = val

    @property
    def participated_conference_web_count(self):
        """
        Gets and sets the participatedConferenceWebCount
        
        Returns:
            int:
                The participatedConferenceWebCount
        """
        if "participatedConferenceWebCount" in self._prop_dict:
            return self._prop_dict["participatedConferenceWebCount"]
        else:
            return None

    @participated_conference_web_count.setter
    def participated_conference_web_count(self, val):
        self._prop_dict["participatedConferenceWebCount"] = val

    @property
    def participated_conference_dial_in_out3rd_party_count(self):
        """
        Gets and sets the participatedConferenceDialInOut3rdPartyCount
        
        Returns:
            int:
                The participatedConferenceDialInOut3rdPartyCount
        """
        if "participatedConferenceDialInOut3rdPartyCount" in self._prop_dict:
            return self._prop_dict["participatedConferenceDialInOut3rdPartyCount"]
        else:
            return None

    @participated_conference_dial_in_out3rd_party_count.setter
    def participated_conference_dial_in_out3rd_party_count(self, val):
        self._prop_dict["participatedConferenceDialInOut3rdPartyCount"] = val

    @property
    def report_refresh_date(self):
        """
        Gets and sets the reportRefreshDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The reportRefreshDate
        """
        if "reportRefreshDate" in self._prop_dict:
            if isinstance(self._prop_dict["reportRefreshDate"], OneDriveObjectBase):
                return self._prop_dict["reportRefreshDate"]
            else :
                self._prop_dict["reportRefreshDate"] = Date(self._prop_dict["reportRefreshDate"])
                return self._prop_dict["reportRefreshDate"]

        return None

    @report_refresh_date.setter
    def report_refresh_date(self, val):
        self._prop_dict["reportRefreshDate"] = val

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
    def is_deleted(self):
        """
        Gets and sets the isDeleted
        
        Returns:
            bool:
                The isDeleted
        """
        if "isDeleted" in self._prop_dict:
            return self._prop_dict["isDeleted"]
        else:
            return None

    @is_deleted.setter
    def is_deleted(self, val):
        self._prop_dict["isDeleted"] = val

    @property
    def deleted_date(self):
        """
        Gets and sets the deletedDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The deletedDate
        """
        if "deletedDate" in self._prop_dict:
            if isinstance(self._prop_dict["deletedDate"], OneDriveObjectBase):
                return self._prop_dict["deletedDate"]
            else :
                self._prop_dict["deletedDate"] = Date(self._prop_dict["deletedDate"])
                return self._prop_dict["deletedDate"]

        return None

    @deleted_date.setter
    def deleted_date(self, val):
        self._prop_dict["deletedDate"] = val

    @property
    def last_activity_date(self):
        """
        Gets and sets the lastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The lastActivityDate
        """
        if "lastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["lastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["lastActivityDate"]
            else :
                self._prop_dict["lastActivityDate"] = Date(self._prop_dict["lastActivityDate"])
                return self._prop_dict["lastActivityDate"]

        return None

    @last_activity_date.setter
    def last_activity_date(self, val):
        self._prop_dict["lastActivityDate"] = val

    @property
    def assigned_products(self):
        """
        Gets and sets the assignedProducts
        
        Returns:
            str:
                The assignedProducts
        """
        if "assignedProducts" in self._prop_dict:
            return self._prop_dict["assignedProducts"]
        else:
            return None

    @assigned_products.setter
    def assigned_products(self, val):
        self._prop_dict["assignedProducts"] = val

    @property
    def report_period(self):
        """
        Gets and sets the reportPeriod
        
        Returns:
            str:
                The reportPeriod
        """
        if "reportPeriod" in self._prop_dict:
            return self._prop_dict["reportPeriod"]
        else:
            return None

    @report_period.setter
    def report_period(self, val):
        self._prop_dict["reportPeriod"] = val

