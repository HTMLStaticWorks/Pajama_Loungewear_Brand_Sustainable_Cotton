(function () {
    const savedTheme = localStorage.getItem('theme') || 'light';
    const savedDir = localStorage.getItem('dir') || 'ltr';
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
