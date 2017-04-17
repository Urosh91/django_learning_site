function Editor(input, preview) {
    console.log(input);
    this.update = function() {
        preview.innerHTML = markdown.toHTML(input.value);
    };
    input.editor = this;
    this.update();
}
django.JQuery(document).ready(function() {
    new Editor(django.JQuery('#id_description')[0],
    django.JQuery('#preview')[0]);
});