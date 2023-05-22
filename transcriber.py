from youtube_transcript_api import YouTubeTranscriptApi

# replace 'VIDEO_ID' with your YouTube video's ID
video_id = 'GizsSo-EevA'

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Write the transcript into a text file
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for entry in transcript:
        f.write(entry['text'] + '\n')
