const input = document.getElementById("passwordInput");
const bar = document.getElementById("strengthBar");
const text = document.getElementById("strengthText");

input.addEventListener("input", () => {
  const score = analyzePassword(input.value);
  const percent = (score / 4) * 100;

  bar.style.width = percent + "%";
  bar.style.background =
    percent < 40 ? "red" : percent < 70 ? "orange" : "lime";

  text.textContent =
    percent < 40 ? "Weak" : percent < 70 ? "Moderate" : "Strong";
});