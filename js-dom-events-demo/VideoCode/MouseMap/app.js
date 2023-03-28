

document.addEventListener('mousemove', function(e) {
    const r = Math.round(e.pageX * 255 / window.innerWidth);
    const b = Math.round(e.pageY * 255 / window.innerHeight);
    const color = `rgb(0, ${r}, ${b})`;
    document.body.style.backgroundColor = color;  
});