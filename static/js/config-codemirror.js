const modeMap = {
    'cpp': 'text/x-c++src',
    'cs': 'text/x-csharp',
    'java': 'text/x-java',
    'sql': 'text/x-sql',
    'javascript': 'javascript',
    'json': 'application/json',
    'python': 'python',
    'html': 'htmlmixed',
    'rust': 'rust',
    'go': 'go'
};

const languageSelect = document.getElementById("language");

var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,
    mode: modeMap[languageSelect.value] || 'javascript',
    indentUnit: 4,
    theme: "dracula",
    lineWrapping: true
});

languageSelect.addEventListener("change", function() {
    editor.setOption("mode", modeMap[this.value]);
});

document.getElementById("format-btn").addEventListener("click", function() {
    var totalLines = editor.lineCount();
    for (var i = 0; i < totalLines; i++) {
        editor.indentLine(i, "smart");
    }
});
