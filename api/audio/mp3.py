from pydub import AudioSegment
import time
import random
import os

def compress_audio_mp3(input_audio):
    # Load the audio file
    #input_audio = './audio/sample.wav'
    #output_audio_mp3 = './audio/result.mp3'

    extension   = "mp3"
    compressed_filename = "compress_"+str(int(time.time()))+str(int(random.random()))+"."+extension
    output_audio_mp3 = './uploads/'+compressed_filename

    # Perform MP3 compression
    start_time_mp3 = time.time()

    audio = AudioSegment.from_wav(input_audio)
    audio.export(output_audio_mp3, format='mp3', bitrate='192k')  # Adjust bitrate as needed

    end_time_mp3 = time.time()

    # Measure compression time
    compression_time_mp3 = end_time_mp3 - start_time_mp3

    # Measure the compression ratio
    original_size_mp3 = os.path.getsize(input_audio)
    compressed_size_mp3 = os.path.getsize(output_audio_mp3)
    compression_ratio_mp3 = float(original_size_mp3) / compressed_size_mp3

    """ print(f"MP3 Compression Time: {compression_time_mp3:.4f} seconds")
    print(f"Original Size: {original_size_mp3} bytes")
    print(f"Compressed Size: {compressed_size_mp3} bytes")
    print(f"Compression Ratio: {compression_ratio_mp3:.2f}") """
    

    return {
        'compression_time' : compression_time_mp3,
        'original_size' : original_size_mp3,
        'compressed_size' : compressed_size_mp3,
        'url' : compressed_filename
    }
