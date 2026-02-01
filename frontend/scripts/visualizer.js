function typeTerminal(text, element, speed = 40) {
  return new Promise((resolve) => {
    element.textContent = "";
    let i = 0;

    const interval = setInterval(() => {
      element.textContent += text[i];
      i++;

      if (i >= text.length) {
        clearInterval(interval);
        resolve(); // 🔥 signal: typing finished
      }
    }, speed);
  });
}
