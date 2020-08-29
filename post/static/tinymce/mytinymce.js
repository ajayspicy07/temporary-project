 



 var script = document.createElement('script')
 script.type = 'text/javaScript'

 script.src = "//cdn.tinymce.com/4/tinymce.min.js"

 //script.src = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'
 document.head.appendChild(script)

 tinymce.init({selector:'.tinymce',
      height : 500,
      max_height: 500,
      min_height: 500,
      
      themes: 'modern',
      images_upload_url: '/media',
     
      
  
      plugins: ' preview paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link  codesample table charmap hr pagebreak nonbreaking  toc advlist lists wordcount imagetools  noneditable  charmap anchor',
      
    
      toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | superscript subscript code | Blocks | outdent indent |  numlist bullist | forecolor backcolor table hr  removeformat | charmap | fullscreen  preview  |  image  link  anchor codesample |',


      
      codesample_dialog_height: 500,

      toolbar_sticky: true,
      menubar : false,

      
      statusbar: true,
  
      branding : false,
  
  });
