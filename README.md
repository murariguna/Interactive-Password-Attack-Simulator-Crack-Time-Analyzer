# Interactive-Password-Attack-Simulator-Crack-Time-Analyzer
# 🔐 Password Attack Simulator & Strength Analyzer

> An educational cybersecurity project that simulates real-world password attack techniques to analyze password strength and crack feasibility — without performing actual cracking.

---

## 📌 Overview

This project is a **full-stack cybersecurity simulation tool** designed to demonstrate how attackers evaluate weak passwords and how defensive mechanisms (strong passwords and secure hashing) improve security.

⚠️ **Important Notes**
- No real password cracking is performed  
- No passwords are stored, logged, or transmitted permanently  
- All results are **mathematical estimations and simulations**

This project is intended strictly for **educational and defensive security purposes**.

---

## 🧠 Features

- Cyber-themed interactive UI (HTML, CSS, JavaScript)
- Backend attack modeling using Python (Flask)
- Multiple real-world password attack techniques
- Hash-aware crack time estimation
- Attacker capability simulation (CPU / GPU / Botnet)
- Ethical and offline-safe implementation

---

## ⚔️ Password Attack Methods Used

This project models **industry-recognized password attack techniques** used by professional security tools such as Hashcat and John the Ripper.

---

### 1️ Brute Force Attack

**Description:**  
Attempts every possible combination of characters until the password is found.

**Why it matters:**  
- Guaranteed success over time  
- Time increases exponentially with password length and character variety

**Simulation logic:**  
- Calculates total combinations using detected character sets  
- Estimates crack time using attacker guess rates

**Key takeaway:**  
> Longer and more complex passwords dramatically resist brute force attacks.

---

### 2️ Dictionary Attack

**Description:**  
Attempts passwords from a predefined list of commonly used passwords.

**Examples:**
password
123456
admin
welcome
qwerty


**Why it works:**  
Users often reuse leaked, default, or simple passwords.

**Simulation logic:**  
- Compares input against curated common password lists  
- Immediate compromise if a match exists

**Key takeaway:**  
> Password popularity is more dangerous than password length.

---

### 3️ Hybrid Attack

**Description:**  
Combines dictionary words with predictable modifications.

**Examples:**
password → password123
admin → admin@2024
love → Love123!


**Why it’s effective:**  
Humans modify passwords in predictable ways.

**Simulation logic:**  
- Detects dictionary roots with numeric or symbolic suffixes  
- Flags vulnerability without brute forcing

**Key takeaway:**  
> Predictable creativity does not equal security.

---

### 4️ Rule-Based Attack

**Description:**  
Applies predefined transformation rules to known words.

**Common rules:**
- Capitalizing the first letter  
- Replacing letters (`a → @`, `o → 0`)  
- Appending symbols or numbers  

**Simulation logic:**  
- Applies known mutation rules  
- Estimates likelihood of early compromise

**Key takeaway:**  
> Attackers think in patterns, not guesses.

---

### 5️ Mask Attack

**Description:**  
Targets passwords with known structural patterns.

**Example mask:**
Uppercase + lowercase + digits + symbol


**Why it works:**  
Knowing the structure drastically reduces the search space.

**Simulation logic:**  
- Detects password structure  
- Reduces brute-force combinations mathematically

**Key takeaway:**  
> Predictable password formats weaken security.

---

### 6️ Hash-Aware Attack Modeling

**Description:**  
The same password behaves very differently depending on how it is stored.

| Hash Type | Relative Resistance |
|---------|---------------------|
| Plaintext | Instant compromise |
| MD5 | Very weak |
| SHA-1 | Weak |
| SHA-256 | Moderate |
| bcrypt | Strong |
| Argon2 | Very strong |

**Simulation logic:**  
- Applies hash slowdown multipliers  
- Demonstrates the defensive impact of secure hashing

**Key takeaway:**  
> Strong passwords are useless if stored insecurely.

---

### 7️ Attacker Capability Simulation

**Description:**  
Different attackers have different computational power.

| Attacker | Guess Rate |
|--------|-----------|
| CPU | 10⁶ guesses/sec |
| GPU | 10⁹ guesses/sec |
| Botnet | 10¹¹ guesses/sec |

**Why it matters:**  
Offline attacks are not limited by login restrictions.

**Key takeaway:**  
> Real attackers are faster than most users expect.

---

## 🛡️ Ethical & Security Considerations

- No real password cracking
- No credential storage
- No network-based attacks
- Uses trimmed public password datasets
- Designed for defensive cybersecurity education only

---

## 🎓 Educational Value

This project helps users understand:
- Why passwords fail
- How attackers prioritize guesses
- Why hashing and salting matter
- The difference between online and offline attacks

Suitable for:
- Cybersecurity students
- Academic demonstrations
- Portfolio projects
- Defensive security learning

---

## 🚀 Future Enhancements

- Online vs offline attack toggle
- Crack probability scoring
- Attack comparison charts
- Hash cost tuning (bcrypt / Argon2)
- Password improvement recommendations

---

## 📜 Disclaimer

This project is intended **solely for educational purposes**.  
It does **not** perform real password cracking and must not be used for unauthorized access or malicious activities.

---

⭐ If you like this project, give it a star — and always use strong passwords!
