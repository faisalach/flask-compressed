from PIL import Image
import os
import random
import time

def compress_gambar_jpeg(input_image):
    # Load the image
    # input_image = 'sample.jpg'
    # output_image_jpeg = 'result.jpg'

    extension   = "jpg"
    compressed_filename = "compress_"+str(int(time.time()))+str(int(random.random()))+"."+extension
    output_image_jpeg = './uploads/'+compressed_filename

    # Perform JPEG compression
    start_time_jpeg = time.time()

    image = Image.open(input_image)
    image.save(output_image_jpeg, quality=70)  # JPEG quality range: 0-100

    end_time_jpeg = time.time()

    # Measure compression time
    compression_time_jpeg = end_time_jpeg - start_time_jpeg

    # Measure the compression ratio
    original_size_jpeg = os.path.getsize(input_image)
    compressed_size_jpeg = os.path.getsize(output_image_jpeg)
    compression_ratio_jpeg = float(original_size_jpeg) / compressed_size_jpeg

    # print(f"JPEG Compression Time: {compression_time_jpeg:.4f} seconds")
    # print(f"Original Size: {original_size_jpeg} bytes")
    # print(f"Compressed Size: {compressed_size_jpeg} bytes")
    # print(f"Compression Ratio: {compression_ratio_jpeg:.2f}")

    return {
        'compression_time' : compression_time_jpeg,
        'original_size' : original_size_jpeg,
        'compressed_size' : compressed_size_jpeg,
        'url' : compressed_filename
    }

