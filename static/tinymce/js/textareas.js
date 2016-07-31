tinyMCE.init({
    selector: "#id_tinymce_text",
    //selector: "textarea",
    //width: 800,
    height: 300,
    forced_root_block: false,
    plugins: [
        "advlist autolink lists link image charmap print preview anchor sh4tinymce",
        "searchreplace visualblocks code fullscreen",
        "insertdatetime table contextmenu paste addmore"
    ],
    toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter" +
    " alignright alignjustify | bullist numlist outdent indent | preview link image sh4tinymce",
    file_picker_callback: function(callback, value, meta) {
        if(meta.filetype=='image') {
            $('#my_form input').click();
        }
    }
});
//var editor = new EpicEditor({basePath: '/static/lib/epiceditor'}).load();
//console.log("{% static 'lib/epiceditor' %}");
//var editor = new EpicEditor({basePath: {% static 'lib/epiceditor' %}}).load();
