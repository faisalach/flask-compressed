from pydub import AudioSegment
import time
import random
import os

def compress_audio_ogg(input_audio):
    # Load the audio file
    #input_audio = 'sample.wav'
    #output_audio_ogg = 'result.ogg'
    extension   = "ogg"
    compressed_filename = "compress_"+str(int(time.time()))+str(int(random.random()))+"."+extension
    output_audio_ogg = './uploads/'+compressed_filename

    # Perform OGG Vorbis compression
    start_time_ogg = time.time()

    audio = AudioSegment.from_wav(input_audio)
    audio.export(output_audio_ogg, format='ogg', bitrate='192k')  # Adjust bitrate as needed

    end_time_ogg = time.time()

    # Measure compression time
    compression_time_ogg = end_time_ogg - start_time_ogg

    # Measure the compression ratio
    original_size_ogg = os.path.getsize(input_audio)
    compressed_size_ogg = os.path.getsize(output_audio_ogg)
    compression_ratio_ogg = float(original_size_ogg) / compressed_size_ogg

    """ print(f"OGG Vorbis Compression Time: {compression_time_ogg:.4f} seconds")
    print(f"Original Size: {original_size_ogg} bytes")
    print(f"Compressed Size: {compressed_size_ogg} bytes")
    print(f"Compression Ratio: {compression_ratio_ogg:.2f}") """

    return {
        'compression_time' : compression_time_ogg,
        'original_size' : original_size_ogg,
        'compressed_size' : compressed_size_ogg,
        'url' : compressed_filename
    }
