# audioSite


Django Web API that simulates the behavior of an audio file
server while using a MongoDB / SQL database.

Audio file type can be one of the following:
- 1 Song
- 2  Podcast
- 3 Audiobook
# Database
## Song file fields:
- ID – (mandatory, integer, unique)
- Name of the song – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

## Podcast file fields:
- ID – (mandatory, integer, unique)
- Name of the podcast – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)
- Host – (mandatory, string, cannot be larger than 100 characters)
- Participants – (optional, list of strings, each string cannot be larger than
100 characters, maximum of 10 participants possible)

## Audiobook file fields:
- ID – (mandatory, integer, unique)
- Title of the audiobook – (mandatory, string, cannot be larger than 100
characters)
- Author of the title (mandatory, string, cannot be larger than 100
characters)
- Narrator - (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

![alt text](https://github.com/somesh3168/audioSite/blob/main/audioHome.JPG)
# 4 API Endpoints
## Get API
```sh
GET /api/get/<audioFileType>/ -- fetch list
GET /api/get/<audioFileType>/<audioFileID> -- fetch each item

/api/get/song/
/api/get/podcast/
/api/get/audiobook/

/api/get/song/1
/api/get/podcast/1
/api/get/audiobook/1
```

> The request will have the following fields:
> audioFileType – mandatory, one of the 3 audio types possible
> audioFileMetadata – mandatory, dictionary, contains the metadata for one
of the three audio files (song, podcast, audiobook)

![alt text](http://url/to/img.png)

## Delete API
```sh

DELETE /api/del/<audioFileType>/<audioFileID> -- delete item


/api/del/song/1
/api/del/podcast/1
/api/del/audiobook/1
```

> The route will be in the following format:
>“<audioFileType>/<audioFileID>”

![alt text](http://url/to/img.png)

## Update API

```sh
Update /api/update/<audioFileType>/<audioFileID> -- put request


/api/update/song/1
/api/update/podcast/1
/api/update/audiobook/1
```

> The route be in the following format: “<audioFileType>/<audioFileID>”
> The request body will be the same as the upload

![alt text](http://url/to/img.png)
## Create API
```sh
POST /api/create/<audioFileType>/ -- create item


/api/del/song/
/api/del/podcast/
/api/del/audiobook/
```

> audioFileMetadata – mandatory, dictionary, contains the metadata for one
> of the three audio files (song, podcast, audiobook)

![alt text](http://url/to/img.png)

### Resources

List of open source resources used to work properly:

* Python 3.6.6rc1
* Django==3.0.5
* djangorestframework==3.12.4
* pymongo==3.11.3
* pytz==2021.1
* typing-extensions==3.7.4.3

