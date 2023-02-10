"""SpotifyAPIから受け取ったjsonに対応するデータオブジェクト

Get Recommendationsが返すjsonに対応
https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
"""

from typing import List, Dict, Union
from pydantic import BaseModel

from pydantic import BaseModel


class Seed(BaseModel):
    afterFilteringSize: int
    afterRelinkingSize: int
    href: str
    id: str
    initialPoolSize: int
    type: str


class Images(BaseModel):
    url: str
    height: int
    width: int


class Album(BaseModel):
    album_type: str
    total_tracks: int
    available_markets: List[str]
    external_urls: Dict[str, str]
    href: str
    id: str
    images: List[Images]
    name: str
    release_date: str
    release_date_precision: str
    restrictions: Dict[str, str]
    type: str
    uri: str
    copyrights: List[Dict[str, str]]
    external_ids: Dict[str, str]
    genres: List[str]
    label: str
    popularity: int
    album_group: str
    artists: List[Dict[str, Union[str, Dict[str, str]]]]


class Followers(BaseModel):
    href: str
    total: int


class Artist(BaseModel):
    external_urls: Dict[str, str]
    followers: Followers
    genres: List[str]
    href: str
    id: str
    images: List[Images]
    name: str
    popularity: int
    type: str
    uri: str


class Track(BaseModel):
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: Dict[str, str]
    external_urls: Dict[str, str]
    href: str
    id: str
    is_playable: bool
    linked_from: Dict
    restrictions: Dict[str, str]
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str
    is_local: bool


class Recommendation(BaseModel):
    seeds: List[Seed]
    tracks: List[Track]
