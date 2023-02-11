"""SpotifyAPIから受け取ったjsonに対応するデータオブジェクト

Get Recommendationsが返すjsonに対応
https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
"""

from typing import List, Dict, Union, Optional
from pydantic import BaseModel

class Seed(BaseModel):
    afterFilteringSize: Optional[int]
    afterRelinkingSize: Optional[int]
    href: Optional[str]
    id: Optional[str]
    initialPoolSize: Optional[int]
    type: Optional[str]

class Images(BaseModel):
    url: Optional[str]
    height: Optional[int]
    width: Optional[int]

class Album(BaseModel):
    album_type: Optional[str]
    total_tracks: Optional[int]
    available_markets: Optional[List[str]]
    external_urls: Optional[Dict[str, str]]
    href: Optional[str]
    id: Optional[str]
    images: Optional[List[Images]]
    name: Optional[str]
    release_date: Optional[str]
    release_date_precision: Optional[str]
    restrictions: Optional[Dict[str, str]]
    type: Optional[str]
    uri: Optional[str]
    copyrights: Optional[List[Dict[str, str]]]
    external_ids: Optional[Dict[str, str]]
    genres: Optional[List[str]]
    label: Optional[str]
    popularity: Optional[int]
    album_group: Optional[str]
    artists: Optional[List[Dict[str, Union[str, Dict[str, str]]]]]

class Followers(BaseModel):
    href: Optional[str]
    total: Optional[int]

class Artist(BaseModel):
    external_urls: Optional[Dict[str, str]]
    followers: Optional[Followers]
    genres: Optional[List[str]]
    href: Optional[str]
    id: Optional[str]
    images: Optional[List[Images]]
    name: Optional[str]
    popularity: Optional[int]
    type: Optional[str]
    uri: Optional[str]

class Track(BaseModel):
    album: Optional[Album]
    artists: Optional[List[Artist]]
    available_markets: Optional[List[str]]
    disc_number: Optional[int]
    duration_ms: Optional[int]
    explicit: Optional[bool]
    external_ids: Optional[Dict[str, str]]
    external_urls: Optional[Dict[str, str]]
    href: Optional[str]
    id: Optional[str]
    is_playable: Optional[bool]
    linked_from: Optional[Dict]
    restrictions: Optional[Dict[str, str]]
    name: Optional[str]
    popularity: Optional[int]
    preview_url: Optional[str]
    track_number: Optional[int]
    type: Optional[str]
    uri: Optional[str]
    is_local: Optional[bool]

class Recommendation(BaseModel):
    seeds: Optional[List[Seed]]
    tracks: Optional[List[Track]]
