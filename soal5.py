from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import ffmpeg_streaming

video = ffmpeg_streaming.input('sample-mp4-file.mp4')
hls = video.hls(Formats.h264())
hls.auto_generate_representations([360, 240])
hls.fragmented_mp4()
hls.output('hls.m3u8')
