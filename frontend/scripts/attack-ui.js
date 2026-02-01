const runBtn = document.getElementById("runBtn");
const terminal = document.getElementById("terminal");
const output = document.getElementById("terminalOutput");
const resultBox = document.getElementById("resultBox");
const passwordInput = document.getElementById("passwordInput");

runBtn.addEventListener("click", async () => {
  const password = passwordInput.value;

  if (!password) {
    alert("Enter a password first");
    return;
  }

  terminal.classList.remove("hidden");
  resultBox.classList.add("hidden");

  const fakeLog = `
Initializing attack engine...
Loading rulesets...
Trying....
Trying....
Trying....
Match Found!
`;

  // 1️⃣ Show fake attack log FIRST
  await typeTerminal(fakeLog, output);

  // 2️⃣ After typing finishes, show status
  output.textContent += "\nAttack simulation completed.\n";

  // 3️⃣ NOW call backend
  try {
    const res = await fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        password: password,
        attacker: "gpu",
        hash: "bcrypt"
      })
    });

    const data = await res.json();

    // 4️⃣ Display backend results AFTER fake log
    resultBox.classList.remove("hidden");
    resultBox.innerHTML = `
      <h2>Analysis Result</h2>
      <p><b>Entropy:</b> ${data.entropy}</p>
      <p><b>Brute Force Time:</b> ${data.brute_force_time}</p>
      ${data.dictionary ? `<p style="color:red">${data.dictionary}</p>` : ""}
      ${data.hybrid ? `<p>${data.hybrid}</p>` : ""}
    `;
  } catch (err) {
    output.textContent += "Error connecting to backend.\n";
    console.error(err);
  }
});
