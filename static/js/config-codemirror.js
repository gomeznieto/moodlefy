// Language map
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
    'go': 'go',
    'css': 'css'
};

// Element
const languageSelect = document.getElementById("language");

// Configuration
var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,
    mode: modeMap[languageSelect.value] || 'cpp',
    indentUnit: 4,
    theme: "dracula",
    lineWrapping: true
});

// Language selector
languageSelect.addEventListener("change", function() {
    editor.setOption("mode", modeMap[this.value]);
});

// Indentación
document.getElementById("format-btn").addEventListener("click", function() {
    var totalLines = editor.lineCount();
    for (var i = 0; i < totalLines; i++) {
        editor.indentLine(i, "smart");
    }
});
