tinyMCE.init({
    selector: "textarea",
            //width: 800,
            height: 300,
            plugins: [
                "advlist autolink lists link image charmap print preview anchor sh4tinymce",
                "searchreplace visualblocks code fullscreen",
                "insertdatetime table contextmenu paste"
            ],
            toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter" +
            " alignright alignjustify | bullist numlist outdent indent | preview link image sh4tinymce",
            file_picker_callback: function(callback, value, meta) {
                if(meta.filetype=='image') {
                    console.log('ddd');
                    $('#my_form input').click();
                }
            }
});
