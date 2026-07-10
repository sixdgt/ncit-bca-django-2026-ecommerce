window.onload = () => {
    const dateSpan = document.getElementById('today-date');
    dateSpan.style.fontWeight = '700';
    dateSpan.style.fontSize = '1.2rem';
    dateSpan.style.color = 'var(--primary-color)';

    // changing the time by second
    setInterval(() => {
        const now = new Date();
        dateSpan.textContent = `Today's Date: ${now.toDateString()} | Current Time: ${now.toLocaleTimeString()}`;
    });
}

