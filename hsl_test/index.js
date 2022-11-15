const main = document.getElementsByTagName('main')[0];
for (let i = 0; i < 360; i += 0.5) {
    let div = document.createElement('div');
    div.style.backgroundColor = `hsl(${i}, 100%, 50%)`;
    main.appendChild(div);
};