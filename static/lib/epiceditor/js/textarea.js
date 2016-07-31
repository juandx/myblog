//but invalid
$("#id_text").attr("id","my-edit-area");
var epicpath = "{% static 'lib/epiceditor' %}";
var editor = new EpicEditor({basePath: epicpath}).load();
//console.log(editor.getElement('editor').body.innerHTML);
$("#submit_btn").click(function(){
    $("#my-edit-area").val(editor.getElement('previewer').body.innerHTML);
});
