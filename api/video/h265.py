import subprocess
import os
import random
import time

def compress_video_h265(input_video):
# Input and output file paths
# input_video = 'sample.mp4'
# Output file path for H.265 compressed video
# output_video_h265 = 'result_h265.mp4'

    extension   = "mp4"
    compressed_filename = "compress_"+str(int(time.time()))+str(int(random.random()))+"."+extension
    output_video_h265 = './uploads/'+compressed_filename

    # Perform H.265 compression using ffmpeg
    start_time_h265 = time.time()

    # ffmpeg command for H.265 compression
    ffmpeg_command_h265 = f"ffmpeg -i {input_video} -c:v libx265 -crf 30 -preset medium {output_video_h265}"

    # Execute ffmpeg command
    subprocess.call(ffmpeg_command_h265, shell=True)

    end_time_h265 = time.time()

    # Measure compression time
    compression_time_h265 = end_time_h265 - start_time_h265

    # Measure the compression ratio
    original_size_h265 = os.path.getsize(input_video)
    compressed_size_h265 = os.path.getsize(output_video_h265)
    compression_ratio_h265 = float(original_size_h265) / compressed_size_h265

    """ print(f"H.265 Compression Time: {compression_time_h265:.4f} seconds")
    print(f"Original Size: {original_size_h265} bytes")
    print(f"Compressed Size: {compressed_size_h265} bytes")
    print(f"Compression Ratio: {compression_ratio_h265:.2f}") """

    return {
        'compression_time' : compression_time_h265,
        'original_size' : original_size_h265,
        'compressed_size' : compressed_size_h265,
        'url' : compressed_filename
    }
