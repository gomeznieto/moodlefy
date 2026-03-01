
const themeToggle = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;

function updateThemeUI() {
    if (htmlElement.classList.contains('dark')) {
        themeToggle.textContent = '☀️';
    } else {
        themeToggle.textContent = '🌙';
    }
}

const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    if (savedTheme === 'light') {
        htmlElement.classList.remove('dark');
        editor.setOption("theme", "default");

    } else {
        htmlElement.classList.add('dark');
        editor.setOption("theme", "dracula");

    }
} else {
    htmlElement.classList.add('dark');
    editor.setOption("theme", "dracula");
}
updateThemeUI();

themeToggle.addEventListener('click', () => {
    htmlElement.classList.toggle('dark');
    const newTheme = htmlElement.classList.contains('dark') ? 'dark' : 'light';

    editor.setOption("theme", newTheme === 'dark' ? "dracula" : "default");

    localStorage.setItem('theme', newTheme);
    updateThemeUI();
});
