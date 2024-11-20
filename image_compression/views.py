from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CompressImageForm
from PIL import Image
import io

# Create your views here.

def compress(request):
    user = request.user
    if request.method == 'POST':
        form = CompressImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_img = form.cleaned_data['original_img']
            quality = form.cleaned_data['quality']
            
            compressed_image = form.save(commit=False)
            compressed_image.user = user
            
            # Perform compression
            img = Image.open(original_img)
            output_format = img.format
            
            buffer = io.BytesIO()
            img.save(buffer, format=output_format, quality=quality)
            # save the compressed image in the model
            
            compressed_img_name = f'compressed_{original_img}'
            compressed_image.compressed_image.save(
                compressed_img_name,
                buffer
            )
            
            # Create the response for downloading the image
            response = HttpResponse(buffer, content_type=f'image/{output_format.lower()}')
            response['Content-Disposition'] = f'attachment; filename="{compressed_img_name}"'
            
          
            return response
             
    else:
        form = CompressImageForm()
        
        context = {
            'form': form,
        }
        return render(request, 'image_compression/compress.html', context=context)
