from PIL import Image
import os
import random
import time

def compress_gambar_webp(input_image):
    # Load the image
    #input_image = 'sample.jpg'
    #output_image_webp = 'result.webp'

    extension   = "webp"
    compressed_filename = "compress_"+str(int(time.time()))+str(int(random.random()))+"."+extension
    output_image_webp = './uploads/'+compressed_filename

    # Perform WebP compression
    start_time_webp = time.time()

    image = Image.open(input_image)
    image.save(output_image_webp, quality=70)  # WebP quality range: 0-100

    end_time_webp = time.time()

    # Measure compression time
    compression_time_webp = end_time_webp - start_time_webp

    # Measure the compression ratio
    original_size_webp = os.path.getsize(input_image)
    compressed_size_webp = os.path.getsize(output_image_webp)
    compression_ratio_webp = float(original_size_webp) / compressed_size_webp

    # print(f"WebP Compression Time: {compression_time_webp:.4f} seconds")
    # print(f"Original Size: {original_size_webp} bytes")
    # print(f"Compressed Size: {compressed_size_webp} bytes")
    # print(f"Compression Ratio: {compression_ratio_webp:.2f}")

    return {
        'compression_time' : compression_time_webp,
        'original_size' : original_size_webp,
        'compressed_size' : compressed_size_webp,
        'url' : compressed_filename
    }