(function () {
    let savedTheme = 'light';
    let savedDir = 'ltr';
    try {
        savedTheme = localStorage.getItem('theme') || 'light';
        savedDir = localStorage.getItem('dir') || 'ltr';
    } catch (e) {
        console.warn('LocalStorage is not accessible:', e);
    }
    document.documentElement.setAttribute('dir', savedDir);
    document.documentElement.classList.add(savedTheme + '-mode');

    const observer = new MutationObserver(() => {
        if (document.body) {
            if (savedTheme === 'dark') {
                document.body.classList.add('dark-mode');
            } else {
                document.body.classList.remove('dark-mode');
            }
            observer.disconnect();
        }
    });
    observer.observe(document.documentElement, { childList: true });
})();
