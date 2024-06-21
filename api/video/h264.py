import subprocess
import os
import random
import time

def compress_video_h264(input_video):

    # Input and output file paths
    # input_video = 'sample.mp4'
    # output_video_h264 = 'result_h264.mp4'

    extension   = "mp4"
    compressed_filename = "compress_"+str(int(time.time()))+str(int(random.random()))+"."+extension
    output_video_h264 = './uploads/'+compressed_filename

    # Perform H.264 compression using ffmpeg
    start_time_h264 = time.time()

    # ffmpeg command for H.264 compression
    ffmpeg_command_h264 = f"ffmpeg -i {input_video} -c:v libx264 -crf 30 -preset medium {output_video_h264}"

    # Execute ffmpeg command
    subprocess.call(ffmpeg_command_h264, shell=True)

    end_time_h264 = time.time()

    # Measure compression time
    compression_time_h264 = end_time_h264 - start_time_h264

    # Measure the compression ratio
    original_size_h264 = os.path.getsize(input_video)
    compressed_size_h264 = os.path.getsize(output_video_h264)
    compression_ratio_h264 = float(original_size_h264) / compressed_size_h264

    # print(f"H.264 Compression Time: {compression_time_h264:.4f} seconds")
    # print(f"Original Size: {original_size_h264} bytes")
    # print(f"Compressed Size: {compressed_size_h264} bytes")
    # print(f"Compression Ratio: {compression_ratio_h264:.2f}")

    return {
        'compression_time' : compression_time_h264,
        'original_size' : original_size_h264,
        'compressed_size' : compressed_size_h264,
        'url' : compressed_filename
    }
