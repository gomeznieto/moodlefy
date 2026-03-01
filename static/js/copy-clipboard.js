
function copyToClipboard() {
    const textarea = document.getElementById('html-result');
    const copyBtn = document.getElementById('copy-btn');

    navigator.clipboard.writeText(textarea.value).then(function() {
        const originalText = copyBtn.innerHTML;
        const originalBg = copyBtn.style.backgroundColor;
        copyBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <polyline points="20 6 9 17 4 12"></polyline></svg> <span>¡Copiado!</span>';
        copyBtn.style.backgroundColor = '#a6e3a1';
        copyBtn.style.color = '#1e1e2e';
        setTimeout(function() {
            copyBtn.innerHTML = originalText;
            copyBtn.style.backgroundColor = originalBg;
            copyBtn.style.color = '';
        }, 2000);
    }, function(err) {
            console.error('Error al copiar: ', err);
            alert('Error al copiar al portapapeles');
        });
}

const copyBtn = document.getElementById('copy-btn');
if (copyBtn) {
    copyBtn.addEventListener('click', copyToClipboard);
}
