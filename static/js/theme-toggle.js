
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
    } else {
        htmlElement.classList.add('dark');
    }
} else {
    htmlElement.classList.add('dark');
}
updateThemeUI();

themeToggle.addEventListener('click', () => {
    htmlElement.classList.toggle('dark');
    const newTheme = htmlElement.classList.contains('dark') ? 'dark' : 'light';
    localStorage.setItem('theme', newTheme);
    updateThemeUI();
});
